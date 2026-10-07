"""
Relative interaction probabilities in a two-region (fuel/non-fuel) lattice cell.

Microscopic cross sections are read from the OpenMC HDF5 library named by the
OPENMC_CROSS_SECTIONS environment variable (as in lesson_09.ipynb) and combined
with simple models -- atom densities from openmc.Material, the Wigner rational
fuel escape probability, and reciprocity for the non-fuel region -- to show the
probability that a neutron colliding in the fuel (or outside it) undergoes each
kind of reaction.

The cell is described by a PinCell: a fuel material and its radius, the
material filling the rest of the cell (moderator, coolant and/or structure),
and the lattice pitch.  Every figure follows from that description, so another
spectrum is another PinCell in CELLS; its figures go to figures/<name>/.  A
cell marked homogeneous is instead treated as one volume-averaged material, as
suits a fast spectrum, and has no escape figures.

This replaces a 2014 script (kept as readdata_2014.py) that read tabulated
ENDF/B-VII.1 data from the *.txt files in this folder.  One deliberate change:
each nuclide's total cross section is split as

    capture = total absorption less fission (MT 101: (n,g), (n,p), (n,a), ...)
    fission = MT 18
    scatter = total - capture - fission (elastic, inelastic, (n,xn))

whereas the 2014 script used total - elastic - fission for "capture", which
put U-238 inelastic scattering above ~45 keV into the capture band.
"""
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import openmc
import openmc.data
from scipy.ndimage import uniform_filter1d

TEMPERATURE = "294K"
E_MIN, E_MAX = 1.0e-4, 1.0e7  # eV, widest range of the energy axes
E_THERMAL, E_FAST = 0.0253, 2.0e6  # eV
OUTDIR = Path(__file__).resolve().parent / "figures"

# ColorBrewer "Set1", in the order used by the original figures, and four more
# (navy, cyan, maroon, tan) for a cell with more bands than that
SET1 = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3",
        "#ff7f00", "#ffff33", "#a65628", "#f781bf"]
MORE = ["#1f2d7a", "#17becf", "#800000", "#e5c494"]
DARK = "#282828"  # escape band


# --------------------------------------------------------------------------- #
# Model
# --------------------------------------------------------------------------- #

@dataclass(frozen=True)
class PinCell:
    """A fuel rod and its share of whatever surrounds it in the lattice.

    `nonfuel` fills everything outside the rod (moderator, coolant and/or
    structure).  The figures stack each material's nuclides in the order they
    were added to it.
    """
    name: str                # subfolder of figures/ for this cell
    fuel: openmc.Material
    nonfuel: openmc.Material
    radius: float            # fuel radius [cm]
    pitch: float             # rod-to-rod spacing [cm]
    lattice: str = "square"  # or "hex"
    homogeneous: bool = False  # treat the cell as its volume-averaged mixture
    lumped: tuple = ()       # nuclides whose absorption shares one band
    smoothing: float = 0.0   # lethargy width averaged over in the stacked figures
    e_min: float = E_MIN     # lowest energy plotted [eV]
    # Energies [eV], or (low, high) ranges of them, compared in bar.png
    bar_energies: tuple = (E_THERMAL, E_FAST)

    @property
    def energy(self):
        """Energies [eV] at which everything is evaluated and plotted."""
        return np.logspace(np.log10(self.e_min), np.log10(E_MAX), 10_000)

    @property
    def fuel_area(self):
        return np.pi * self.radius**2

    @property
    def nonfuel_area(self):
        return cell_area(self.pitch, self.lattice) - self.fuel_area

    @property
    def chord(self):
        """Mean chord of the fuel, 4V/S."""
        return 2 * self.radius

    @property
    def mixture(self):
        """The fuel and non-fuel as one volume-averaged material."""
        areas = np.array([self.fuel_area, self.nonfuel_area])
        return openmc.Material.mix_materials(
            [self.fuel, self.nonfuel], areas / areas.sum(), "vo", name=self.name)


def cell_area(pitch, lattice):
    """Area of one rod's cell in a "square" or "hex" (triangular-pitch) lattice."""
    return {"square": 1.0, "hex": np.sqrt(3) / 2}[lattice] * pitch**2


def uo2(enrichment=0.04, density=10.0):
    """UO2 with U-235 enrichment given as a weight fraction of uranium."""
    moles = {"U238": (1.0 - enrichment) / openmc.data.atomic_mass("U238"),
             "U235": enrichment / openmc.data.atomic_mass("U235")}
    fuel = openmc.Material(name="uo2")
    for name, n in moles.items():
        fuel.add_nuclide(name, n / sum(moles.values()))
    fuel.add_nuclide("O16", 2.0)
    fuel.set_density("g/cm3", density)
    return fuel


def u_pu_zr(plutonium=0.20, zirconium=0.10, density=15.8, smear=0.75):
    """U-Pu-Zr metallic fuel, by weight fraction, as smeared within its cladding.

    A metallic slug is cast to fill only about 75% of the area inside the
    cladding, leaving room to swell, so its `density` is reduced by `smear`
    to fill the whole fuel radius.  Uranium is taken as U-238, plutonium as
    Pu-239 and zirconium as Zr-90.
    """
    fuel = openmc.Material(name="u-pu-zr")
    fuel.add_nuclide("U238", 1.0 - plutonium - zirconium, "wo")
    fuel.add_nuclide("Pu239", plutonium, "wo")
    fuel.add_nuclide("Zr90", zirconium, "wo")
    fuel.set_density("g/cm3", smear * density)
    return fuel


def h2o(density=1.0):
    water = openmc.Material(name="h2o")
    water.add_nuclide("H1", 2.0)
    water.add_nuclide("O16", 1.0)
    water.set_density("g/cm3", density)
    return water


def sodium(density=0.837):
    coolant = openmc.Material(name="sodium")
    coolant.add_nuclide("Na23", 1.0)
    coolant.set_density("g/cm3", density)
    return coolant


def ods_steel(density=7.13):
    """The ODS steel cladding of lesson_16.ipynb, reduced to its main elements.

    Iron, chromium and aluminum are 97% of that steel's atoms.  They are kept
    in the lesson's proportions (given there as atoms/b-cm), each as its most
    abundant isotope.
    """
    steel = openmc.Material(name="ods steel")
    steel.add_nuclide("Fe56", 5.3872e-2)
    steel.add_nuclide("Cr52", 1.7753e-2)
    steel.add_nuclide("Al27", 9.1482e-3)
    steel.set_density("g/cm3", density)
    return steel


def pwr():
    """UO2 rods in water on a square pitch of 1.4 fuel diameters."""
    radius = 0.45
    return PinCell("pwr", uo2(), h2o(), radius, pitch=1.4 * 2 * radius)


def sfr():
    """A sodium-cooled, metallic-fuel pin with the dimensions of lesson_16.ipynb.

    The fuel is U-Pu-Zr in place of that lesson's UO2.  The non-fuel is the
    lesson's sodium and its cladding (the gap ignored, as there) mixed by
    volume.

    A fast neutron's mean free path is much longer than the cell is wide, so
    as in the lesson the whole cell is treated as one volume-averaged
    material.  Little of a fast spectrum lies below 1 keV, so the figures
    start there.  The mixture's resonances leave no single energy between
    there and 1 MeV representative, so bar.png averages over a decade instead
    and the stacked figure is smoothed.  Absorption outside the heavy metal
    is too small to show nuclide by nuclide, so it shares one band.
    """
    radius, clad_radius, pitch = 0.4742, 0.5419, 1.1897  # cm
    clad = np.pi * (clad_radius**2 - radius**2)
    coolant = cell_area(pitch, "hex") - np.pi * clad_radius**2
    nonfuel = openmc.Material.mix_materials(
        [sodium(), ods_steel()], np.array([coolant, clad]) / (coolant + clad),
        "vo", name="sodium and cladding")
    return PinCell("sfr", u_pu_zr(), nonfuel, radius, pitch, lattice="hex",
                   homogeneous=True, e_min=1.0e3,
                   bar_energies=((1.0e5, 1.0e6), E_FAST),
                   lumped=("Zr90", "Na23", "Fe56", "Cr52", "Al27"), smoothing=0.05)


CELLS = [pwr, sfr]


# --------------------------------------------------------------------------- #
# Data
# --------------------------------------------------------------------------- #

@lru_cache(maxsize=None)
def load_nuclide(name):
    """Read a nuclide's IncidentNeutron data from the OpenMC library."""
    library = openmc.data.DataLibrary.from_xml()
    return openmc.data.IncidentNeutron.from_hdf5(
        library.get_by_material(name)["path"])


def nubar(nuc, energy):
    """Total neutrons per fission, summing prompt and delayed yields."""
    if 18 not in nuc:
        return np.zeros_like(energy)
    neutrons = [p for p in nuc[18].products if p.particle == "neutron"]
    total = [p for p in neutrons if p.emission_mode == "total"]
    return sum(p.yield_(energy) for p in (total or neutrons))


def micro_xs(nuc, energy, temperature=TEMPERATURE):
    """Microscopic cross sections [b] (and nubar) of `nuc` at `energy` [eV].

    MT 1 and MT 101 are not stored in the HDF5 files; indexing the
    IncidentNeutron object builds them by summing their component reactions
    (so `mt in nuc` is False for them, but `nuc[mt]` works).
    """
    def xs(mt):
        try:
            return nuc[mt].xs[temperature](energy)
        except KeyError:
            return np.zeros_like(energy)

    total, capture, fission = xs(1), xs(101), xs(18)
    return {"total": total,
            "elastic": xs(2),
            "capture": capture,
            "fission": fission,
            "scatter": total - capture - fission,
            "nubar": nubar(nuc, energy)}


def macro_xs(material, micro):
    """Macroscopic cross sections [1/cm] of `material`, by nuclide and reaction."""
    densities = material.get_nuclide_atom_densities()  # atoms/b-cm
    return {name: {rxn: N * micro[name][rxn]
                   for rxn in ("total", "capture", "fission", "scatter")}
            for name, N in densities.items()}


def symbol_and_mass(name):
    Z, A, _ = openmc.data.zam(name)
    return openmc.data.ATOMIC_SYMBOL[Z], A


def by_mass(names):
    """Unique nuclide names, lightest first."""
    return sorted(set(names), key=openmc.data.zam)


def is_fissionable(name):
    return 18 in load_nuclide(name)


def is_fissile(name):
    """Actinides with an odd number of neutrons fission at any neutron energy."""
    Z, A, _ = openmc.data.zam(name)
    return Z >= 90 and (A - Z) % 2 == 1


def collision_bands(material, lumped=()):
    """(label, [(nuclide, reaction), ...]) for each band of collisions in `material`.

    A nuclide has a band for each of its reactions.  Capture is labelled
    "gamma" for fissionable nuclides, where it is all but entirely (n,gamma).
    For the others it is the only absorption, and not always radiative -- for
    O-16 it is mostly (n,alpha) above a few MeV -- hence "a".

    The nuclides in `lumped` instead share one "other a" band, placed where
    the first of them would have had its own.
    """
    bands, other = [], []
    for name in material.get_nuclides():
        symbol, A = symbol_and_mass(name)
        tags = {"capture": "a", "scatter": "s"}
        if is_fissionable(name):
            tags = {"capture": r"$\gamma$", "scatter": "s", "fission": "f"}
        for rxn, tag in tags.items():
            if rxn == "capture" and name in lumped:
                if not other:
                    bands.append(("other a", other))
                other.append((name, rxn))
            else:
                bands.append((rf"${{}}^{{{A}}}${symbol} {tag}", [(name, rxn)]))
    return bands


def fractions(sigma, bands):
    """Each band's macroscopic cross section divided by the material total."""
    total = sum(s["total"] for s in sigma.values())
    return [sum(sigma[name][rxn] for name, rxn in members) / total
            for _, members in bands]


def smooth(y, energy, width):
    """Moving average of `y` over `width` in lethargy on the log-spaced `energy`.

    This is meant for collision fractions, not cross sections.  Across a
    narrow resonance the collision density stays nearly flat in lethargy while
    the flux dips, so an even average of the fractions is the average over
    collisions.  Averaging the cross sections first would weight them by a
    flat flux instead and exaggerate every resonance peak.
    """
    points = int(round(width / np.log(energy[1] / energy[0])))
    if points < 2:
        return y
    return uniform_filter1d(y, size=points, mode="nearest")


def bar_fractions(material, bands, nuclides, where, grid):
    """Each band's share of the collisions in `material` at the energy `where`.

    `where` may instead be a (low, high) range, for the shares averaged over
    the points of the log-spaced `grid` within it, that is, evenly in lethargy
    (see `smooth`).
    """
    if np.isscalar(where):
        energies = np.array([where])
    else:
        energies = grid[(grid >= where[0]) & (grid <= where[1])]
    micro = {name: micro_xs(nuclides[name], energies)
             for name in material.get_nuclides()}
    return [y.mean() for y in fractions(macro_xs(material, micro), bands)]


def escape_probabilities(cell, sigma_fuel, sigma_nonfuel):
    """First-flight escape probabilities from the fuel and from the non-fuel.

    The fuel uses the Wigner rational approximation with mean chord 4V/S; the
    rest of the cell uses reciprocity, V_f Sigma_f P_fn = V_n Sigma_n P_nf.
    That takes every neutron leaving a rod to collide before it reaches
    another, so where the non-fuel is optically thin P_nf comes out above 1.
    It is capped there; a cell that thin throughout is better treated as
    homogeneous.
    """
    P_f = 1 / (1 + sigma_fuel * cell.chord)
    P_n = np.minimum(cell.fuel_area * sigma_fuel * P_f
                     / (cell.nonfuel_area * sigma_nonfuel), 1.0)
    return P_f, P_n


# --------------------------------------------------------------------------- #
# Figures
# --------------------------------------------------------------------------- #

def set_style():
    # The "classic" style reproduces the matplotlib 1.x defaults of the
    # original figures (Computer Modern math text, outlined patches, etc.).
    # Constrained layout is what makes room for the legends beside the axes.
    plt.style.use("classic")
    plt.rcParams.update({"font.family": "serif",
                         "xtick.direction": "out",
                         "ytick.direction": "out",
                         "figure.constrained_layout.use": True})


def palette(n, base):
    """`n` colors: from `base` if it has enough, otherwise matplotlib's tab20."""
    colors = base if n <= len(base) else plt.get_cmap("tab20").colors
    return [colors[i % len(colors)] for i in range(n)]


def legend_outside(ax, size=20, **kwargs):
    """Put the legend in the margin to the right of the axes.

    A figure legend with an "outside" location gets its own strip of the
    figure under constrained layout: the axes shrink to make room, so the
    legend can neither cover the data nor be clipped when saved.
    """
    ax.figure.legend(*ax.get_legend_handles_labels(),
                     loc="outside center right", prop={"size": size}, **kwargs)


def energy_label(energy):
    """An energy [eV] in the unit that keeps the number short, e.g. "2 MeV".

    A (low, high) range gives both ends, e.g. "100 keV\u20131 MeV".
    """
    if not np.isscalar(energy):
        return "\u2013".join(energy_label(e) for e in energy)
    for scale, unit in ((1e6, "MeV"), (1e3, "keV")):
        if energy >= scale:
            return f"{energy / scale:g} {unit}"
    return f"{energy:g} eV"


def finish(ax, xlabel, ylabel, path):
    ax.tick_params(labelsize=18)
    ax.set_xlabel(xlabel, fontsize=20)
    ax.set_ylabel(ylabel, fontsize=20)
    ax.figure.savefig(path)
    plt.close(ax.figure)


def plot_stack(energy, bands, labels, colors, path, escape=None, smoothing=0.0):
    """Stack `bands` (fractions of all collisions) from 0 to 1 versus energy.

    With `escape`, the bands are scaled by the probability of colliding at
    all and the escape probability fills the rest.  With `smoothing`, each
    band is averaged over that width in lethargy.
    """
    if escape is not None:
        bands = [y * (1 - escape) for y in bands] + [escape]
        labels = labels + ["escape"]
        colors = colors + [DARK]
    bands = [smooth(y, energy, smoothing) for y in bands]
    _, ax = plt.subplots(figsize=(12, 8))
    ax.stackplot(energy, *bands, colors=colors, labels=labels,
                 edgecolor="k", linewidth=0.25)
    ax.set_xscale("log")
    ax.axis([energy[0], energy[-1], 0.0, 1.0])
    legend_outside(ax, reverse=True)  # listed as stacked, top band first
    finish(ax, "energy [eV]", "relative probability", path)


def plot_bar(energies, bands, labels, colors, path):
    """Stack `bands`, evaluated at just the few `energies`, one bar for each."""
    x = np.arange(len(energies))
    _, ax = plt.subplots(figsize=(12, 8))
    bottom = np.zeros(len(energies))
    for y, color, label in zip(bands, colors, labels):
        ax.bar(x, y, 0.5, bottom=bottom, color=color, label=label)
        bottom += y
    ax.set_xticks(x, [energy_label(e) for e in energies])
    ax.set_xlim(-0.5, len(energies) - 0.5)
    legend_outside(ax, reverse=True)
    finish(ax, "", "relative probability", path)


def plot_sigma(energy, micro, path, hue=None):
    """Elastic cross section of each nuclide; total and fission too if it has one.

    `hue` gives each nuclide's color for when there are too many curves to
    color one by one.
    """
    curves = []
    for name in by_mass(micro):
        symbol, A = symbol_and_mass(name)
        reactions = [("elastic", "el")]
        if is_fissionable(name):
            reactions = [("total", "t"), ("elastic", "el"), ("fission", "f")]
        curves += [(name, rxn, r"$\sigma^{{}^{%d}\mathrm{%s}}_{%s}$" % (A, symbol, tag))
                   for rxn, tag in reactions]
    colors = SET1[:4] + [DARK] + SET1[5:]
    if len(curves) <= len(colors):
        # A color for every curve, as in the original figure
        styles = [(color, "-") for color in colors]
    else:
        # Too many for that: a color for each nuclide, a dash for each reaction
        hue = hue or dict(zip(by_mass(micro), palette(len(micro), colors)))
        dash = {"elastic": "-", "total": "--", "fission": ":"}
        styles = [(hue[name], dash[rxn]) for name, rxn, _ in curves]
    _, ax = plt.subplots(figsize=(12, 8))
    for (name, rxn, label), (color, linestyle) in zip(curves, styles):
        ax.loglog(energy, micro[name][rxn], color=color, ls=linestyle, lw=2,
                  label=label)
    largest = max(micro[name][rxn].max() for name, rxn, _ in curves)
    ax.axis([energy[0], energy[-1], 1e-2, 10 ** np.ceil(np.log10(largest))])
    legend_outside(ax)
    finish(ax, "energy [eV]", r"$\sigma$ [b]", path)


def plot_nubar(energy, micro, names, path):
    _, ax = plt.subplots(figsize=(12, 8))
    for name, color in zip(names, palette(len(names), ["k", "b", "r", "g"])):
        ax.semilogx(energy, micro[name]["nubar"], color=color, lw=2,
                    label="{}-{}".format(*symbol_and_mass(name)))
    legend_outside(ax)
    finish(ax, "incident neutron energy [eV]", r"$\bar{\nu}$", path)


def plot_eta(energy, micro, sigma_fuel, path):
    """Neutrons produced per absorption in each fissile nuclide and in the fuel."""
    nu_fission = sum(micro[n]["nubar"] * s["fission"] for n, s in sigma_fuel.items())
    absorption = sum(s["fission"] + s["capture"] for s in sigma_fuel.values())
    _, ax = plt.subplots(figsize=(12, 8))
    for name in by_mass(n for n in sigma_fuel if is_fissile(n)):
        xs = micro[name]
        ax.semilogx(energy,
                    xs["nubar"] * xs["fission"] / (xs["fission"] + xs["capture"]),
                    label="{}-{}".format(*symbol_and_mass(name)))
    ax.semilogx(energy, nu_fission / absorption, label="fuel")
    legend_outside(ax)
    finish(ax, "energy [eV]", r"$\eta$", path)


def plot_escape(energy, P_esc, path):
    _, ax = plt.subplots(figsize=(12, 8))
    ax.semilogx(energy, P_esc)
    ax.set_xlim(energy[0], energy[-1])
    finish(ax, "energy [eV]", "escape probability", path)


# --------------------------------------------------------------------------- #

def make_figures(cell):
    outdir = OUTDIR / cell.name
    outdir.mkdir(parents=True, exist_ok=True)

    fuel_names, nonfuel_names = cell.fuel.get_nuclides(), cell.nonfuel.get_nuclides()
    nuclides = {name: load_nuclide(name) for name in fuel_names + nonfuel_names}
    energy = cell.energy
    micro = {name: micro_xs(nuc, energy) for name, nuc in nuclides.items()}
    sigma_fuel = macro_xs(cell.fuel, micro)

    # Collisions in an infinite medium of fuel, or of the whole cell smeared
    material = cell.mixture if cell.homogeneous else cell.fuel
    bands = collision_bands(material, cell.lumped)
    labels = [label for label, _ in bands]
    colors = palette(len(bands), SET1 + MORE)
    split = fractions(macro_xs(material, micro), bands)
    plot_stack(energy, split, labels, colors, outdir / "prob.png",
               smoothing=cell.smoothing)

    # The same at a couple of representative energies
    bar_split = np.transpose([bar_fractions(material, bands, nuclides, where, energy)
                              for where in cell.bar_energies])
    plot_bar(cell.bar_energies, bar_split, labels, colors, outdir / "bar.png")
    print(f"{cell.name:<13}"
          + "".join(f"{energy_label(e):>16}" for e in cell.bar_energies))
    for (_, members), y in zip(bands, bar_split):
        name, rxn = members[0] if len(members) == 1 else ("other", members[0][1])
        print(f"{name:>5} {rxn:>7}" + "".join(f"{v:16.4f}" for v in y))

    if not cell.homogeneous:
        # Neutrons born in the fuel (non-fuel) either escape it or collide there
        sigma_nonfuel = macro_xs(cell.nonfuel, micro)
        nonfuel_bands = collision_bands(cell.nonfuel, cell.lumped)
        P_fuel, P_nonfuel = escape_probabilities(
            cell,
            sum(s["total"] for s in sigma_fuel.values()),
            sum(s["total"] for s in sigma_nonfuel.values()))
        plot_escape(energy, P_fuel, outdir / "escape.png")
        plot_stack(energy, split, labels, colors, outdir / "prob2.png",
                   escape=P_fuel, smoothing=cell.smoothing)
        plot_stack(energy, fractions(sigma_nonfuel, nonfuel_bands),
                   [label for label, _ in nonfuel_bands],
                   palette(len(nonfuel_bands), SET1 + MORE), outdir / "prob3.png",
                   escape=P_nonfuel, smoothing=cell.smoothing)

    # In a mixture each nuclide has one scatter band, whose color can stand
    # for the nuclide in the cross-section figure too
    hue = None
    if cell.homogeneous:
        hue = {members[0][0]: color for (_, members), color in zip(bands, colors)
               if members[0][1] == "scatter"}
    plot_sigma(energy, micro, outdir / "sigma.png", hue)
    plot_nubar(energy, micro, by_mass(n for n in fuel_names if is_fissionable(n)),
               outdir / "nubar.png")
    plot_eta(energy, micro, sigma_fuel, outdir / "eta.png")


def main():
    set_style()
    for cell in CELLS:
        make_figures(cell())


if __name__ == "__main__":
    main()
