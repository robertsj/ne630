"""NE 630: transparent, fixed-flux or fixed-power depletion using FNRP Table 3.2.

Only NumPy and SciPy are required. No OpenMC installation or data download is
needed. All arrays use group order FAST, INTERMEDIATE, THERMAL. Microscopic
cross sections are in barns; densities in atoms/cm3 of the nuclide's region;
time in seconds; the specified total flux is a fuel-reference flux in
n/cm2/s. See README.md for the flux convention and limits of the model.

Three chain levels:
    1 / 'constant_u238': instantaneous breeding, U238 held constant.
    2 / 'variable_u238': instantaneous breeding, U238 depleted.
    3 / 'full': all Table-3.2 actinides, delayed breeding, Pu capture chain,
                optional B10/Gd157 and I135/Xe135/Pm149/Sm149.
'full' means the table-supported teaching model, NOT a complete library chain.

Functions to start with: three_group_xs, condense, build_chain,
solve_depletion. Run the companion notebook for examples.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Sequence
import csv
import math
import re

import numpy as np
from scipy.integrate import solve_ivp

BARN = 1.0e-24
DAY = 86400.0
YEAR = 365.25 * DAY
AVOGADRO = 6.02214076e23
J_PER_MWD = 8.64e10
KAPPA_J = 200.0e6 * 1.602176634e-19  # common 200-MeV/fission approximation
GROUPS = ('fast', 'intermediate', 'thermal')
LETHARGY_WIDTH = math.log(1.0e5 / 1.0)
# Illustrative group-integrated fractions, NOT an OpenMC-derived PWR spectrum.
DEFAULT_PWR_SPECTRUM = (0.35, 0.55, 0.10)

# Columns: sigma_fT, sigma_aT, sigma_sT, I_f, I_a, sigma_fF, sigma_aF,
# sigma_sF. Thermal data are 293-K Maxwellian averages, NOT 2200-m/s values.
# I_f and I_a are infinite-dilution resonance integrals, not group averages.
# None means the original table does not supply that scattering datum.
TABLE32 = {
    'H1':    (0, .295, 47.7, 0, .149, 0, 3.92e-5, 3.93),
    'H2':    (0, 5.06e-4, 5.37, 0, 2.28e-4, 0, 5.34e-6, 2.55),
    'B10':   (0, 3409, 2.25, 0, 1722, 0, .491, 2.12),
    'C12':   (0, .003, 4.81, 0, .00153, 0, .00123, 2.36),
    'O16':   (0, 1.69e-4, 4.01, 0, 8.53e-5, 0, .012, 2.76),
    'Na23':  (0, .472, 3.09, 0, .310, 0, 2.34e-4, 3.13),
    'Fe56':  (0, 2.29, 11.3, 0, 1.32, 0, 9.22e-3, 3.20),
    'Zr91':  (0, .16, 6.45, 0, .746, 0, 3.35e-3, 5.89),
    'Xe135': (0, 2.64e6, None, 0, 7.65e3, 0, 7.43e-4, None),
    'Sm149': (0, 6.15e4, None, 0, 3.49e3, 0, .234, None),
    'Gd157': (0, 1.92e5, 1422, 0, 762, 0, .201, 6.51),
    'Th232': (0, 6.54, 11.8, 0, 84.9, .0713, .155, 7.08),
    'U233':  (464, 506, 14.2, 752, 886, 1.84, 1.89, 5.37),
    'U235':  (505, 591, 15.0, 272, 404, 1.22, 1.29, 6.33),
    'U238':  (1.05e-5, 2.42, 9.37, .002, 278, .304, .361, 7.42),
    'Pu239': (698, 973, 8.62, 289, 474, 1.81, 1.86, 7.42),
    'Pu240': (.0613, 263, 1.39, 3.74, 8452, 1.36, 1.42, 6.38),
    'Pu241': (946, 1273, 11.0, 571, 740, 1.62, 1.83, 6.24),
    'Pu242': (.0130, 16.6, 8.30, .94, 1117, 1.14, 1.22, 6.62),
}
ACTINIDES = ('Th232', 'U233', 'U235', 'U238', 'Pu239', 'Pu240', 'Pu241', 'Pu242')
# Explicit teaching parameters; Table 3.2 does NOT contain nu or kappa.
# The same approximate nu is used in all groups unless the caller replaces it.
# U235=2.43 and Pu239=2.90 match the Lesson 23 example. Other values are
# rounded illustrative assumptions, not a supplemental evaluated data library.
DEFAULT_NU = dict(Th232=2.50, U233=2.49, U235=2.43, U238=2.80,
                  Pu239=2.90, Pu240=3.00, Pu241=2.95, Pu242=3.00)

# Supplemental historical NuDat data served by KAERI (see README references).
# Ignored: long-lived actinide alpha decay, spontaneous fission, and the tiny
# Pu241 alpha branch. Precursors absent from Table 3.2 have zero neutron XS.
HALF_LIFE_S = {'U239': 23.45*60, 'Np239': 2.3565*DAY,
               'Th233': 22.3*60, 'Pa233': 26.967*DAY,
               'Pu241': 14.35*YEAR, 'I135': 6.57*3600,
               'Xe135': 9.14*3600, 'Pm149': 53.08*3600}

# Effective reduced-chain yields from IAEA WIMS Library Update, fpyield.htm.
# Order: I135, Xe135, Pm149. Pre-I and pre-Pm precursors are folded into
# the I and Pm sources; do not add cumulative Xe or Sm yields on top.
# These are fixed, parent-dependent yields, without incident-energy variation.
WIMS_YIELDS = {
    'Th232': (.055944, .00010204, .010885),
    'U233':  (.050304, .012268, .0077824),
    'U235':  (.062900, .0025761, .010816),
    'U238':  (.070147, .00026864, .016316),
    'Pu239': (.065354, .010763, .012175),
    'Pu240': (.068468, .0053067, .013552),
    'Pu241': (.069543, .0022690, .014765),
    'Pu242': (.069520, .0014391, .015796),
}


def _positive(x: float, name: str, allow_zero: bool = False) -> float:
    x = float(x)
    if not np.isfinite(x) or x < 0 or (x == 0 and not allow_zero):
        raise ValueError(f'{name} must be finite and {"nonnegative" if allow_zero else "positive"}.')
    return x


def spectrum_weights(values: Sequence[float] = DEFAULT_PWR_SPECTRUM) -> np.ndarray:
    """Normalize three nonnegative group-INTEGRATED fluxes in F,I,T order."""
    w = np.asarray(values, dtype=float)
    if w.shape != (3,) or not np.all(np.isfinite(w)) or np.any(w < 0) or w.sum() <= 0:
        raise ValueError('Spectrum must contain three finite nonnegative integrated fluxes, with positive sum.')
    return w / w.sum()


@dataclass(frozen=True)
class UO2Shielding:
    """FNRP Table 4.3, isolated-rod U238 empirical resonance integral.

    dancoff_diameter_increase is an OPTIONAL empirical effective-diameter
    increase (e.g. 0.10 for the Chapter 4 exercise), not a computed Dancoff C.
    This is a fixed, reference-condition fit; no temperature/burnup update.
    """
    density_g_cm3: float = 10.4
    diameter_cm: float = 0.82
    dancoff_diameter_increase: float = 0.0

    def integral_b(self) -> float:
        rho = _positive(self.density_g_cm3, 'UO2 density')
        d = _positive(self.diameter_cm, 'fuel diameter')
        c = _positive(self.dancoff_diameter_increase, 'effective diameter increase', True)
        deff = d * (1+c)
        if not (0.2 < d < 3.5) or not (0.2 < deff < 3.5):
            raise ValueError('Table 4.3 is restricted to 0.2 < diameter < 3.5 cm.')
        return 4.45 + 26.6 * np.sqrt(4.0 / (rho * deff))


@dataclass(frozen=True)
class GroupXS:
    absorption_b: np.ndarray
    fission_b: np.ndarray
    nu: np.ndarray = field(default_factory=lambda: np.zeros(3))
    provenance: str = ''

    def __post_init__(self):
        for key in ('absorption_b', 'fission_b', 'nu'):
            value = np.asarray(getattr(self, key), dtype=float).copy()
            if value.shape != (3,) or not np.all(np.isfinite(value)) or np.any(value < 0):
                raise ValueError(f'{key} must be a finite nonnegative three-vector.')
            value.flags.writeable = False
            object.__setattr__(self, key, value)
        if np.any(self.fission_b > self.absorption_b + 1.e-12):
            raise ValueError('Fission cannot exceed absorption.')

    @property
    def capture_b(self) -> np.ndarray:
        """Non-fission absorption; for B10 this is (n,alpha), not (n,gamma)."""
        return self.absorption_b - self.fission_b

    @property
    def nu_fission_b(self) -> np.ndarray:
        return self.nu * self.fission_b


@dataclass(frozen=True)
class OneGroupXS:
    absorption_b: float
    fission_b: float
    nu_fission_b: float

    @property
    def capture_b(self) -> float:
        return self.absorption_b - self.fission_b

    @property
    def nu(self) -> float:
        return self.nu_fission_b/self.fission_b if self.fission_b else 0.0


def three_group_xs(*, shielding: UO2Shielding | None = UO2Shielding(),
                   resonance_factors: Mapping[str, float] | None = None,
                   thermal_factors: Mapping[str, float] | None = None,
                   nu: Mapping[str, float | Sequence[float]] | None = None) -> dict[str, GroupXS]:
    """Convert Table 3.2 to F,I,T data, optionally correcting U238 resonances.

    sigma_I = I/log(1e5). The empirical UO2 correction is applied to U238
    ONLY. Additional per-nuclide factors must be supplied explicitly. A factor
    multiplies both absorption and fission in that group, preserving a >= f.
    These extra factors are sensitivity inputs, not Chapter-4 correlations.

    The effective U238 I includes phi_f/phi_m. Thus its epithermal weighting
    flux is the smooth moderator/inter-resonance reference, not an independently
    tallied depressed fuel spectrum. See README before using transport spectra.
    """
    rf, tf = dict(resonance_factors or {}), dict(thermal_factors or {})
    for mapping in (rf, tf):
        for name, val in mapping.items():
            if name not in TABLE32:
                raise KeyError(f'{name}: no Table 3.2 row.')
            _positive(val, f'factor for {name}', True)
    if shielding is not None and 'U238' in rf:
        raise ValueError('Specify empirical U238 shielding OR an explicit U238 resonance factor, not both.')
    if shielding is not None:
        rf['U238'] = shielding.integral_b() / TABLE32['U238'][4]
    nus = {**DEFAULT_NU, **dict(nu or {})}
    if set(nus) - set(TABLE32):
        raise KeyError('nu specified for an unknown Table 3.2 nuclide.')
    result = {}
    for name, row in TABLE32.items():
        ft, at, _, fi, ai, ff, af, _ = row
        a = np.array([af, ai/LETHARGY_WIDTH, at], dtype=float)
        f = np.array([ff, fi/LETHARGY_WIDTH, ft], dtype=float)
        a[1] *= rf.get(name, 1.0); f[1] *= rf.get(name, 1.0)
        a[2] *= tf.get(name, 1.0); f[2] *= tf.get(name, 1.0)
        n = np.asarray(nus.get(name, 0.0), dtype=float)
        n = np.full(3, float(n)) if n.ndim == 0 else n
        result[name] = GroupXS(a, f, n,
            f'FNRP Table 3.2; resonance multiplier={rf.get(name,1):.8g}; '
            f'thermal multiplier={tf.get(name,1):.8g}; nu is a teaching parameter')
    return result


def condense(xs3: Mapping[str, GroupXS], spectrum: Sequence[float] = DEFAULT_PWR_SPECTRUM
             ) -> dict[str, OneGroupXS]:
    """Return importable one-group data in barns. Condense nu*sigma_f together."""
    w = spectrum_weights(spectrum)
    return {n: OneGroupXS(float(x.absorption_b@w), float(x.fission_b@w),
                         float(x.nu_fission_b@w)) for n, x in xs3.items()}


def xs_rows(xs3: Mapping[str, GroupXS], spectrum=DEFAULT_PWR_SPECTRUM) -> list[dict]:
    """A notebook-friendly list of dicts, usable directly in pandas.DataFrame."""
    one = condense(xs3, spectrum)
    rows = []
    for name, x in xs3.items():
        row = {'nuclide': name}
        for g, i in zip(('F', 'I', 'T'), range(3)):
            row.update({f'sigma_a{g}_b': x.absorption_b[i], f'sigma_f{g}_b': x.fission_b[i]})
        row.update(sigma_a_b=one[name].absorption_b, sigma_f_b=one[name].fission_b,
                   sigma_c_b=one[name].capture_b, nu_sigma_f_b=one[name].nu_fission_b)
        rows.append(row)
    return rows


@dataclass(frozen=True)
class Cell:
    """Frozen geometry/backgrounds for reactivity and moderator B10 rates.

    Defaults are an illustrative PWR-like cell, not a validated operating state.
    Room-temperature Table-3.2 microscopic data are retained even when water
    density is changed. moderator_flux_ratios[g] = phi_m,g / phi_ref,g.
    Fuel oxygen is held fixed at its initial UO2 density.
    """
    moderator_to_fuel_volume: float = 2.0
    water_density_g_cm3: float = 0.7
    moderator_flux_ratios: tuple[float, float, float] = (1.0, 1.0, 1.16)
    boron_region: str = 'moderator'
    nonleakage: float = 1.0
    epsilon: float = 1.24  # FNRP Chapter 4 exercise; fixed in four-factor closure
    p_override: float | None = None
    # Table 3.1 H2O slowing-down power 1.28/cm at nominal density, scaled by rho.
    slowing_down_power_at_unit_density_cm1: float = 1.28
    extra_absorption_cm1: float = 0.0  # fuel-reference, one-group basis only

    def __post_init__(self):
        for key in ('moderator_to_fuel_volume', 'water_density_g_cm3',
                    'extra_absorption_cm1'):
            _positive(getattr(self,key), key, True)
        for key in ('epsilon', 'slowing_down_power_at_unit_density_cm1'):
            _positive(getattr(self,key), key)
        r = np.asarray(self.moderator_flux_ratios, dtype=float)
        if r.shape != (3,) or not np.all(np.isfinite(r)) or np.any(r < 0):
            raise ValueError('moderator_flux_ratios must be three nonnegative finite numbers.')
        if self.boron_region not in ('moderator', 'fuel'):
            raise ValueError('boron_region must be moderator or fuel.')
        if not 0 < self.nonleakage <= 1:
            raise ValueError('nonleakage must be in (0, 1].')
        if self.p_override is not None and not 0 < self.p_override <= 1:
            raise ValueError('p_override must be in (0, 1].')

    @property
    def water_densities(self) -> dict[str, float]:
        # Nominal mass-number molar mass; intentionally consistent with uo2_initial.
        n = self.water_density_g_cm3 * AVOGADRO / 18.0
        return {'H1': 2*n, 'O16': n}


def uo2_initial(enrichment: float = 0.04, density_g_cm3: float = 10.4, *,
                enrichment_basis: str = 'weight', b10_atoms_cm3: float = 0.0,
                gd157_atoms_cm3: float = 0.0) -> dict[str, float]:
    """Fresh UO2. Poison densities are additive trace loadings in their region.

    Enrichment is a FRACTION, e.g. 0.04, not percent. Integer molar masses
    235,238,16 are used. Adding Gd does not renormalize a Gd2O3/UO2 mixture.
    B10 is per moderator cm3 by default (or fuel cm3 with boron_region='fuel').
    """
    if not np.isfinite(enrichment) or not 0 <= enrichment <= 1:
        raise ValueError('enrichment must be a fraction in [0, 1].')
    rho = _positive(density_g_cm3, 'fuel density')
    if enrichment_basis == 'weight':
        e = (enrichment/235) / (enrichment/235 + (1-enrichment)/238)
    elif enrichment_basis == 'atom':
        e = enrichment
    else:
        raise ValueError('enrichment_basis must be weight or atom.')
    n = rho * AVOGADRO / (235*e + 238*(1-e) + 32)
    return {'U235': e*n, 'U238': (1-e)*n,
            'B10': _positive(b10_atoms_cm3, 'B10 density', True),
            'Gd157': _positive(gd157_atoms_cm3, 'Gd157 density', True)}


def b10_from_ppm(ppm: float, water_density_g_cm3: float = 0.7) -> float:
    """B10 ISOTOPE mass ppm in moderator -> atoms/cm3; not natural-boron ppm."""
    return (_positive(ppm, 'B10 ppm', True)*1e-6 *
            _positive(water_density_g_cm3, 'water density', True)*AVOGADRO/10)


@dataclass(frozen=True)
class Transition:
    """One loss event and its products; None of the matrix entries are hidden."""
    parent: str
    reaction: str  # capture, absorption, decay, fission
    products: tuple[tuple[str, float], ...]
    decay_constant_s: float = 0.0
    loss_fraction: float = 1.0
    note: str = ''


@dataclass(frozen=True)
class Chain:
    level: str
    nuclides: tuple[str, ...]
    transitions: tuple[Transition, ...]
    frozen: tuple[str, ...] = ()
    terminal: tuple[str, ...] = ()

    def describe(self) -> str:
        lines = [f'Model: {self.level}',
                 'Frozen external reservoirs: ' + (', '.join(self.frozen) or 'none')]
        for tr in self.transitions:
            products = ' + '.join(f'{v:g} {n}' if v != 1 else n for n,v in tr.products) or '(untracked)'
            note = f' [{tr.note}]' if tr.note else ''
            lines.append(f'{tr.parent:8s} --{tr.reaction:10s}--> {products}{note}')
        lines.append('Terminal/zero-XS bookkeeping sinks: ' + ', '.join(self.terminal))
        return '\n'.join(lines)


def build_chain(model: int | str = 3, *, include_poisons: bool | None = None,
                boron_mode: str = 'deplete',
                fission_yields: Mapping[str, Mapping[str, float]] | None = None,
                half_lives_s: Mapping[str, float] | None = None) -> Chain:
    """Build an inspectable reaction list, then derive the nuclide ordering.

    Models 1 and 2 differ ONLY in whether U238 is held fixed. Both lose Pu239
    capture products to an explicit sink. Model 3 retains Pu240--Pu242 and
    U239/Np239 delays. All Table-3.2 actinides are included; Th/U233 start at
    zero in a UO2 run. Precursor captures and terminal reactions are omitted
    because their cross sections are absent from Table 3.2.

    include_poisons defaults to True only for model 3. It can be switched on
    for models 1/2 or off for model 3 to isolate assumptions.
    """
    aliases = {1:'constant_u238', 2:'variable_u238', 3:'full',
               'constant_u238':'constant_u238', 'variable_u238':'variable_u238', 'full':'full'}
    if model not in aliases:
        raise ValueError('model must be 1, 2, 3, constant_u238, variable_u238, or full.')
    level = aliases[model]
    if include_poisons is None:
        include_poisons = level == 'full'
    if boron_mode not in ('deplete', 'fixed'):
        raise ValueError('boron_mode must be deplete or fixed (externally maintained).')
    if set(half_lives_s or {}) - set(HALF_LIFE_S):
        raise KeyError('Unknown precursor or decay parent in half_lives_s.')
    if fission_yields and not include_poisons:
        raise ValueError('Enable include_poisons to supply reduced-chain fission yields.')
    halflives = {**HALF_LIFE_S, **dict(half_lives_s or {})}
    for name, val in halflives.items():
        _positive(val, f'half-life of {name}')
    tr = []
    active = list(ACTINIDES if level == 'full' else ('U235','U238','Pu239'))
    if set(fission_yields or {}) - set(active):
        raise KeyError('Fission yield supplied for a parent outside the selected chain.')

    def capture(parent, daughter, reaction='capture', loss=1.0, note=''):
        tr.append(Transition(parent, reaction, ((daughter, loss),) if loss else (),
                             loss_fraction=loss, note=note))

    def decay(parent, daughter):
        tr.append(Transition(parent, 'decay', ((daughter, 1.0),),
                             np.log(2)/halflives[parent]))

    # --- Actinide chains: the three FNRP levels are explicit here. ---
    capture('U235', 'U236_sink')
    if level != 'full':
        capture('U238', 'Pu239', note='instantaneous U239/Np239 beta decays')
        capture('Pu239', 'Pu240_sink', note='no further Pu capture chain')
    else:
        capture('U238', 'U239')
        decay('U239', 'Np239')
        decay('Np239', 'Pu239')
        capture('Pu239', 'Pu240')
        capture('Pu240', 'Pu241')
        capture('Pu241', 'Pu242')
        decay('Pu241', 'Am241_sink')
        capture('Pu242', 'Pu243_sink')
        capture('Th232', 'Th233')
        decay('Th233', 'Pa233')
        decay('Pa233', 'U233')
        capture('U233', 'U234_sink')

    # --- Explicit burnable absorbers and the two reduced poison chains. ---
    if include_poisons:
        capture('B10', 'B10_products_sink', 'absorption', note='dominantly (n,alpha); Li/He untracked')
        capture('Gd157', 'Gd158_sink')
        decay('I135', 'Xe135')
        capture('Xe135', 'Xe136_sink')
        decay('Xe135', 'Cs135_sink')
        decay('Pm149', 'Sm149')
        capture('Sm149', 'Sm150_sink')

    # --- Fission: loss of ONE parent, plus parent-dependent products. ---
    for parent in active:
        products = {}
        if include_poisons:
            products = dict(zip(('I135', 'Xe135', 'Pm149'), WIMS_YIELDS[parent]))
            if fission_yields is not None and parent in fission_yields:
                products = dict(fission_yields[parent])
            if set(products) - {'I135', 'Xe135', 'Pm149', 'Sm149', 'Gd157'}:
                raise ValueError('Custom yields may feed I135, Xe135, Pm149, Sm149, or Gd157.')
            for daughter, y in products.items():
                _positive(y, f'{parent} -> {daughter} yield', True)
        if sum(products.values()) > 2:
            raise ValueError('The physical reduced-product yields cannot sum to more than 2.')
        products['FP_other_sink'] = 2.0 - sum(products.values())
        tr.append(Transition(parent, 'fission', tuple(products.items())))

    names = list(active)
    for t in tr:
        for name in (t.parent, *(n for n,v in t.products)):
            if name not in names:
                names.append(name)
    frozen = ['U238'] if level == 'constant_u238' else []
    if include_poisons and boron_mode == 'fixed':
        frozen.append('B10')
    terminal = tuple(n for n in names if n.endswith('_sink'))
    return Chain(level, tuple(names), tuple(tr), tuple(frozen), terminal)


def _rate_cross_sections(xs3, spectrum, cell, names):
    """Barns relative to the SPECIFIED fuel-reference total flux (no renorm)."""
    w = spectrum_weights(spectrum)
    result = {}
    zero = OneGroupXS(0., 0., 0.)
    for name in names:
        if name not in xs3:
            # Only explicitly listed decay-only nuclides or terminal sinks.
            if name not in HALF_LIFE_S and not name.endswith('_sink'):
                raise KeyError(f'No cross sections or explicit zero-XS convention for {name}.')
            result[name] = zero
            continue
        weights = w * np.asarray(cell.moderator_flux_ratios) if (
            name == 'B10' and cell.boron_region == 'moderator') else w
        x = xs3[name]
        result[name] = OneGroupXS(float(x.absorption_b@weights), float(x.fission_b@weights),
                                 float(x.nu_fission_b@weights))
    return result


def build_matrix(chain: Chain, xs3: Mapping[str, GroupXS], total_flux: float,
                 spectrum=DEFAULT_PWR_SPECTRUM, cell: Cell = Cell()) -> np.ndarray:
    """Build A for d[N; F]/dt = A[N; F], with F cumulative fissions/cm3.

    Each event subtracts its loss from the parent diagonal and adds each
    product to the appropriate daughter row. Frozen reservoirs retain their
    production channels but have ZERO parent loss. A[-1,:] counts fissions.
    """
    phi = _positive(total_flux, 'total flux', True)
    names = chain.nuclides
    index = {name:i for i,name in enumerate(names)}
    xs1 = _rate_cross_sections(xs3, spectrum, cell, names)
    A = np.zeros((len(names)+1, len(names)+1))
    for tr in chain.transitions:
        j = index[tr.parent]
        x = xs1[tr.parent]
        if tr.reaction == 'decay':
            rate = tr.decay_constant_s
        else:
            cross = {'capture':x.capture_b, 'absorption':x.absorption_b,
                     'fission':x.fission_b}[tr.reaction]
            rate = phi * BARN * cross
        if tr.parent not in chain.frozen:
            A[j,j] -= rate*tr.loss_fraction
        for name, multiplicity in tr.products:
            A[index[name],j] += multiplicity*rate
        if tr.reaction == 'fission':
            A[-1,j] += rate
    return A


def _hm_density(initial: Mapping[str,float]) -> float:
    """Initial heavy-metal mass in kg/cm3; integer molar-mass approximation."""
    mass = 0.
    for name, n in initial.items():
        if re.match(r'^(Th|Pa|U|Np|Pu|Am)\d+', name):
            a = int(re.search(r'\d+', name).group())
            mass += a*n/AVOGADRO/1000
    return _positive(mass, 'initial heavy-metal mass density')


@dataclass
class DepletionResult:
    time_s: np.ndarray
    densities: np.ndarray  # time-major: [time, nuclide]
    fissions_cm3: np.ndarray
    chain: Chain
    total_flux: float | np.ndarray  # scalar at fixed flux; time history at fixed power
    spectrum: np.ndarray
    xs3: dict[str, GroupXS]
    cell: Cell
    initial_hm_kg_cm3: float
    fuel_oxygen_atoms_cm3: float
    kappa_j: float
    matrix: np.ndarray
    solver_info: dict
    integrated_fluence_cm2: np.ndarray | None = None

    @property
    def nuclides(self):
        return self.chain.nuclides

    def density(self, name: str) -> np.ndarray:
        if name not in self.nuclides:
            raise KeyError(f'{name} is not in this chain; inspect result.nuclides.')
        return self.densities[:, self.nuclides.index(name)]

    @property
    def fluence_cm2(self):
        if self.integrated_fluence_cm2 is not None:
            return self.integrated_fluence_cm2
        return self.total_flux * self.time_s

    @property
    def burnup_mwd_kg(self):
        return self.kappa_j * self.fissions_cm3 / (J_PER_MWD*self.initial_hm_kg_cm3)

    @property
    def power_density_w_cm3(self):
        xs = self.one_group_xs
        sigma_f = np.array([xs[n].fission_b if n in xs else 0. for n in self.nuclides])
        return self.kappa_j * self.total_flux * BARN * (self.densities @ sigma_f)

    @property
    def one_group_xs(self):
        """Physical fuel-reference one-group data; moderator B10 rates differ."""
        return condense(self.xs3, self.spectrum)

    def axis(self, x: str = 'time', time_unit: str = 'days'):
        if x == 'time':
            units = {'s':1., 'hours':3600., 'days':DAY, 'years':YEAR}
            if time_unit not in units:
                raise ValueError(f'time_unit must be one of {tuple(units)}.')
            return self.time_s/units[time_unit], f'Time ({time_unit})'
        if x == 'fluence':
            return self.fluence_cm2, r'Fluence (n/cm$^2$)'
        if x == 'burnup':
            return self.burnup_mwd_kg, 'Burnup (MWd/kg initial HM)'
        raise ValueError('x must be time, fluence, or burnup.')

    def neutronics(self, closure: str = 'rate_ratio') -> dict[str, np.ndarray | dict]:
        """Return k_inf, k, rho, and absorption terms for a chosen closure.

        rate_ratio: total production / total absorption on the prescribed
        reference flux. This is a diagnostic, NOT a solved transport eigenvalue.
        four_factor: FNRP-style thermal numerator times epsilon*p, with p from
        U238 only (unless overridden). No extra p is applied to rate_ratio.
        Terminal sinks are intentionally neutronically inactive.
        """
        if closure not in ('rate_ratio', 'four_factor'):
            raise ValueError('closure must be rate_ratio or four_factor.')
        nt = len(self.time_s)
        fuel_abs, mod_abs, production = np.zeros(nt), np.zeros(nt), np.zeros(nt)
        contrib = {}
        w = self.spectrum
        r = np.asarray(self.cell.moderator_flux_ratios)
        if closure == 'four_factor':
            if w[2] == 0:
                raise ValueError('The thermal four-factor closure requires a nonzero thermal group.')
            fw = np.array([0.,0.,1.]); mw = np.array([0.,0.,r[2]])
            if self.cell.extra_absorption_cm1:
                raise ValueError('extra_absorption_cm1 is defined only for rate_ratio.')
        else:
            fw, mw = w, w*r
        for name in self.nuclides:
            if name not in self.xs3:
                continue
            dens, xs = self.density(name), self.xs3[name]
            ismod = name == 'B10' and self.cell.boron_region == 'moderator'
            if ismod:
                a = dens*BARN*(xs.absorption_b@mw)*self.cell.moderator_to_fuel_volume
                mod_abs += a
            else:
                a = dens*BARN*(xs.absorption_b@fw)
                fuel_abs += a
                production += dens*BARN*(xs.nu_fission_b@fw)
            contrib[name] = a
        oa = self.fuel_oxygen_atoms_cm3*BARN*(self.xs3['O16'].absorption_b@fw)
        fuel_abs += oa
        contrib['fuel_O16_fixed'] = np.full(nt, oa)
        for name,dens in self.cell.water_densities.items():
            a = dens*BARN*(self.xs3[name].absorption_b@mw)*self.cell.moderator_to_fuel_volume
            mod_abs += a
            contrib['moderator_'+name+'_fixed'] = np.full(nt,a)
        absorption = fuel_abs + mod_abs
        p = np.ones(nt)
        if closure == 'four_factor':
            if self.cell.p_override is not None:
                p[:] = self.cell.p_override
            else:
                power = (self.cell.slowing_down_power_at_unit_density_cm1 *
                         self.cell.water_density_g_cm3*self.cell.moderator_to_fuel_volume)
                if power <= 0:
                    raise ValueError('Empirical p requires a nonzero water moderator, or p_override.')
                n238 = self.density('U238') if 'U238' in self.nuclides else np.zeros(nt)
                ia = self.xs3['U238'].absorption_b[1]*LETHARGY_WIDTH
                p = np.exp(-n238*BARN*ia/power)
            production *= self.cell.epsilon*p
        else:
            absorption += self.cell.extra_absorption_cm1
        with np.errstate(divide='ignore', invalid='ignore'):
            k_inf = np.divide(production, absorption, out=np.zeros(nt), where=absorption>0)
            k = self.cell.nonleakage*k_inf
            rho = 1.0-1.0/k
        return dict(k_inf=k_inf, k=k, rho=rho, p=p,
                    production_cm1=production, absorption_cm1=absorption,
                    absorption_by_nuclide=contrib)

    def poison_worth(self, name: str, closure: str = 'rate_ratio') -> np.ndarray:
        """Exact frozen-state rho_with - rho_without for a nonfissioning absorber."""
        if name not in self.nuclides or name not in self.xs3:
            raise KeyError(name)
        if np.any(self.xs3[name].fission_b):
            raise ValueError('poison_worth applies only to nonfissioning absorbers.')
        n = self.neutronics(closure)
        with np.errstate(divide='ignore', invalid='ignore'):
            return -n['absorption_by_nuclide'][name]/(
                self.cell.nonleakage*n['production_cm1'])

    def fission_power_fraction(self, name: str) -> np.ndarray:
        xs = self.one_group_xs
        if name not in self.nuclides or name not in xs:
            raise KeyError(name)
        rate = self.total_flux*BARN*xs[name].fission_b*self.density(name)
        total = self.power_density_w_cm3/self.kappa_j
        return np.divide(rate, total, out=np.zeros_like(rate), where=total>0)

    def to_csv(self, path: str, closure: str = 'rate_ratio') -> None:
        n = self.neutronics(closure)
        columns = {'time_s':self.time_s, 'time_days':self.time_s/DAY,
                   'fluence_n_cm2':self.fluence_cm2, 'burnup_MWd_kgHM':self.burnup_mwd_kg,
                   'power_W_cm3_fuel':self.power_density_w_cm3, 'k':n['k'], 'rho':n['rho']}
        columns.update({name+'_atoms_cm3':self.density(name) for name in self.nuclides})
        with open(path,'w',newline='') as stream:
            writer=csv.writer(stream); writer.writerow(columns)
            writer.writerows(zip(*columns.values()))

    def plot(self, quantities: str | Sequence[str] = 'rho', *, x: str = 'time',
             time_unit: str = 'days', closure: str = 'rate_ratio', ax=None):
        """One plot per call; import Matplotlib only when plotting is requested."""
        import matplotlib.pyplot as plt
        qs = [quantities] if isinstance(quantities,str) else list(quantities)
        if not qs:
            raise ValueError('Specify at least one quantity.')
        classes = {('density' if q in self.nuclides else q) for q in qs}
        if len(classes)>1:
            raise ValueError('Plot different physical units in separate calls.')
        if ax is None:
            _,ax=plt.subplots(figsize=(6.5,4))
        xv,xlab=self.axis(x,time_unit)
        for q in qs:
            if q in self.nuclides:
                y=self.density(q); ylab=r'Number density (atoms/cm$^3$ of region)'
            elif q in ('rho','k','k_inf'):
                y=self.neutronics(closure)[q]
                ylab={'rho':r'Reactivity $\rho$ (dimensionless)', 'k':'Multiplication factor',
                      'k_inf':r'$k_\infty$'}[q]
            elif q=='power':
                y=self.power_density_w_cm3; ylab=r'Fission power (W/cm$^3$ fuel)'
            elif q=='burnup':
                y=self.burnup_mwd_kg; ylab='Burnup (MWd/kg initial HM)'
            else:
                raise KeyError(q)
            ax.plot(xv,y,label=q)
        ax.set(xlabel=xlab,ylabel=ylab); ax.legend(); ax.figure.tight_layout()
        return ax


def solve_depletion(time_s: Sequence[float], *, total_flux: float = 2.e14,
                    power_density_w_cm3: float | None = None,
                    initial: Mapping[str,float] | None = None, model: int | str = 3,
                    spectrum: Sequence[float] = DEFAULT_PWR_SPECTRUM,
                    xs3: Mapping[str,GroupXS] | None = None,
                    shielding: UO2Shielding | None = UO2Shielding(),
                    cell: Cell = Cell(), include_poisons: bool | None = None,
                    boron_mode: str = 'deplete',
                    chain: Chain | None = None,
                    fuel_oxygen_atoms_cm3: float | None = None,
                    initial_hm_kg_cm3: float | None = None, kappa_j: float = KAPPA_J,
                    method: str = 'BDF', rtol: float = 1.e-8, atol: float = 1.e-13,
                    max_step_s: float = np.inf) -> DepletionResult:
    """Solve depletion and integrated fissions using solve_ivp.

    By default total_flux is fixed. Supplying positive power_density_w_cm3
    (W per fuel cm3) instead determines flux at every RHS evaluation from
    P = kappa*phi*sum(N*sigma_f). total_flux is then ignored. The spectrum
    and microscopic cross sections remain fixed; decay rates are unchanged.
    The returned total_flux is a time history and fluence is integrated.
    At fixed power, matrix is the initial-state operator, not a constant
    operator for the full trajectory. Exhaustion of fissile inventory raises.

    time_s must begin at zero. To continue a new segment, supply the final
    inventory of the previous segment, but preserve the original HM mass for
    cumulative burnup accounting outside this function. This call returns
    segment-local time, fluence, and fission energy.

    atol applies to densities scaled by max(initial density), including the
    fission counter. Small negative roundoff values within 100*atol*scale are
    clipped and reported; larger negative values raise an error.

    Passing xs3 bypasses the Table-3.2 preparation (and shielding argument).
    Passing a custom chain bypasses model/include_poisons/boron options.
    """
    t = np.asarray(time_s,dtype=float)
    if t.ndim!=1 or len(t)<2 or not np.all(np.isfinite(t)) or t[0]!=0 or np.any(np.diff(t)<=0):
        raise ValueError('time_s must be a strictly increasing finite 1-D array starting at zero.')
    phi=_positive(total_flux,'total flux',True)
    power = (None if power_density_w_cm3 is None else
             _positive(power_density_w_cm3, 'power density'))
    _positive(rtol,'rtol'); _positive(atol,'atol'); _positive(kappa_j,'kappa_j')
    if not (max_step_s>0):
        raise ValueError('max_step_s must be positive.')
    if method not in ('BDF','Radau','LSODA','RK45','RK23','DOP853'):
        raise ValueError('Unsupported solve_ivp method.')
    inv=dict(uo2_initial() if initial is None else initial)
    for name,v in inv.items():
        _positive(v,f'initial density of {name}',True)
    w=spectrum_weights(spectrum)
    data=dict(three_group_xs(shielding=shielding) if xs3 is None else xs3)
    for required in ('H1','O16','U238'):
        if required not in data:
            raise KeyError(f'{required} is required in xs3 for the cell diagnostics.')
    ch=chain if chain is not None else build_chain(
        model,include_poisons=include_poisons,boron_mode=boron_mode)
    bad=[n for n,v in inv.items() if v and n not in ch.nuclides]
    if bad:
        raise ValueError(f'Nonzero initial nuclides excluded by this chain: {bad}. '
                         'Choose model=3 or enable the poison chains.')
    hm=_hm_density(inv) if initial_hm_kg_cm3 is None else _positive(initial_hm_kg_cm3,'HM density')
    oxygen=(2*sum(v for n,v in inv.items() if n in ACTINIDES)
            if fuel_oxygen_atoms_cm3 is None else _positive(fuel_oxygen_atoms_cm3,'oxygen density',True))
    n0=np.array([inv.get(n,0.) for n in ch.nuclides])
    scale=max(float(n0.max()),1.)
    y0=np.r_[n0/scale,0.]
    A=build_matrix(ch,data,phi,w,cell)
    options=dict(method=method,t_eval=t,rtol=rtol,atol=atol,max_step=max_step_s)
    if power is None:
        if method in ('BDF','Radau'):
            options['jac']=A
        elif method=='LSODA':
            options['jac']=lambda _t,_y:A
        rhs = lambda _t,y:A@y
    else:
        decay = build_matrix(ch,data,0.,w,cell)
        neutron_chain = Chain(ch.level, ch.nuclides,
                              tuple(tr for tr in ch.transitions if tr.reaction != 'decay'),
                              ch.frozen, ch.terminal)
        neutron = build_matrix(neutron_chain,data,1.,w,cell)
        fission_row = neutron[-1,:-1]

        def flux_for(inventory):
            rate_per_flux = scale * (inventory @ fission_row)
            if np.any(rate_per_flux <= 0) or not np.all(np.isfinite(rate_per_flux)):
                raise ValueError('Fixed power requires a positive fissionable inventory.')
            return power / (kappa_j * rate_per_flux)

        def rhs(_t, y):
            state = y[:-1]
            current_flux = flux_for(state[:-1])
            return np.r_[(decay + current_flux*neutron) @ state,
                         current_flux/1.e24]

        A = decay + flux_for(y0[:-1])*neutron
        y0 = np.r_[y0, 0.]  # fluence scaled by 1e24 n/cm2
    sol=solve_ivp(rhs,(0.,t[-1]),y0,**options)
    if not sol.success or sol.y.shape[1]!=len(t):
        raise RuntimeError('Depletion integration failed: '+sol.message)
    fluence = None if power is None else sol.y[-1]*1.e24
    y=(sol.y if power is None else sol.y[:-1]).T*scale
    minval=float(y.min())
    if minval < -100*atol*scale:
        raise RuntimeError(f'Materially negative density {minval:g}; tighten solver tolerances.')
    clipped=int(np.count_nonzero(y<0)); y=np.maximum(y,0.)
    if power is not None:
        phi = flux_for(y[:,:-1]/scale)
    info=dict(success=sol.success,message=sol.message,nfev=sol.nfev,njev=sol.njev,nlu=sol.nlu,
              method=method,rtol=rtol,scaled_atol=atol,scale_atoms_cm3=scale,
              clipped_negative_values=clipped,minimum_before_clipping=minval)
    info['normalization'] = 'fixed_flux' if power is None else 'fixed_power'
    return DepletionResult(t,y[:,:-1],y[:,-1],ch,phi,w,data,cell,hm,oxygen,kappa_j,A,info,fluence)


def read_reference_csv(path: str, *, axis: str = 'burnup') -> tuple[np.ndarray,np.ndarray,np.ndarray | None]:
    """Read time_s/burnup_MWd_kgHM/fluence_n_cm2 plus rho or k and optional sigma.

    k uncertainty is propagated as sigma_rho = sigma_k/k**2. Numerical units
    in CSV are explicit; percent/pcm inputs are not inferred automatically.
    """
    columns={'time':'time_s','burnup':'burnup_MWd_kgHM','fluence':'fluence_n_cm2'}
    if axis not in columns:
        raise ValueError('Invalid reference axis.')
    rows=np.genfromtxt(path,delimiter=',',names=True,dtype=float,encoding='utf-8')
    rows=np.atleast_1d(rows)
    names=rows.dtype.names or ()
    if columns[axis] not in names:
        raise ValueError(f'CSV needs {columns[axis]}.')
    if 'rho' in names:
        rho=rows['rho']; sigma=rows['sigma_rho'] if 'sigma_rho' in names else None
    elif 'k' in names:
        k=rows['k']
        if np.any(k<=0):
            raise ValueError('Reference k must be positive.')
        rho=1-1/k; sigma=rows['sigma_k']/k**2 if 'sigma_k' in names else None
    else:
        raise ValueError('CSV needs rho or k.')
    return rows[columns[axis]],rho,sigma


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model',choices=['constant_u238','variable_u238','full'],default='full')
    parser.add_argument('--years',type=float,default=5.)
    parser.add_argument('--flux',type=float,default=2e14)
    parser.add_argument('--output',default='depletion.csv')
    args=parser.parse_args()
    result=solve_depletion(np.linspace(0,args.years*YEAR,501),model=args.model,total_flux=args.flux)
    result.to_csv(args.output)
    print(result.chain.describe())
    print(f'Final burnup: {result.burnup_mwd_kg[-1]:.4f} MWd/kg initial HM')
    print(f'Final frozen-spectrum rho: {result.neutronics()["rho"][-1]:.6f}')
    print(f'Wrote {args.output}')
