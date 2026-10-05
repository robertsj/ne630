"""Generate slide figures backed by OpenMC evaluated nuclear data.

The four cross-section targets only read the HDF5 data library.  The
``mc_vs_nr_u238_h1`` target also runs a deterministic fixed-source OpenMC
calculation; all XML, HDF5, and log files from that run are written beneath
``--work-dir`` (or a temporary directory when no work directory is supplied).
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Callable, Sequence
from contextlib import ExitStack
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


OUTPUT_DIR = Path(__file__).resolve().parent / "generated"
TEMPERATURE = "294K"
PURPLE = "#512888"
ORANGE = "#CA7C1B"

plt.rcParams.update(
    {
        "font.family": "serif",
        "pgf.rcfonts": False,
        "pgf.texsystem": "xelatex",
    }
)


class GenerationError(RuntimeError):
    """A user-actionable figure-generation failure."""


def import_openmc() -> Any:
    try:
        import openmc
    except (ImportError, OSError) as error:
        raise GenerationError(
            "OpenMC's Python package is unavailable. Activate an OpenMC "
            "environment (for example, `conda activate openmc`) and retry."
        ) from error
    return openmc


@dataclass
class NuclearData:
    """Lazy access to nuclides in one OpenMC cross_sections.xml library."""

    openmc: Any
    cross_sections: Path
    library: Any = field(init=False)
    _nuclides: dict[str, Any] = field(default_factory=dict, init=False)

    def __post_init__(self) -> None:
        try:
            self.library = self.openmc.data.DataLibrary.from_xml(
                self.cross_sections
            )
        except Exception as error:
            raise GenerationError(
                f"Could not read OpenMC data library {self.cross_sections}: {error}"
            ) from error

    def nuclide(self, name: str) -> Any:
        if name not in self._nuclides:
            record = self.library.get_by_material(name)
            if record is None or record.get("type") != "neutron":
                raise GenerationError(
                    f"Neutron data for {name} is absent from {self.cross_sections}"
                )
            path = Path(record["path"])
            if not path.is_file():
                raise GenerationError(
                    f"OpenMC data file for {name} does not exist: {path}"
                )
            try:
                self._nuclides[name] = (
                    self.openmc.data.IncidentNeutron.from_hdf5(path)
                )
            except Exception as error:
                raise GenerationError(
                    f"Could not load OpenMC data for {name} from {path}: {error}"
                ) from error
        return self._nuclides[name]

    def cross_section(self, name: str, mt: int) -> Callable[[np.ndarray], np.ndarray]:
        nuclide = self.nuclide(name)
        try:
            reaction = nuclide[mt]
        except KeyError as error:
            raise GenerationError(
                f"OpenMC data for {name} has no MT={mt} reaction"
            ) from error
        if TEMPERATURE not in reaction.xs:
            available = ", ".join(reaction.xs)
            raise GenerationError(
                f"OpenMC data for {name} MT={mt} lacks {TEMPERATURE}; "
                f"available temperatures: {available}"
            )
        return reaction.xs[TEMPERATURE]


def save_figure(fig: plt.Figure, output_dir: Path, filename: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / filename
    fig.savefig(destination)
    plt.close(fig)
    print(f"generated {destination}")


def build_h1_xsec(data: NuclearData, output_dir: Path) -> None:
    energy = np.logspace(-2, 7, 10_000)
    elastic = data.cross_section("H1", 2)
    capture = data.cross_section("H1", 102)

    fig, axes = plt.subplots(1, 2, figsize=(8, 3))
    axes[0].loglog(energy, elastic(energy), color=PURPLE, lw=1)
    axes[0].set_xlabel(r"$E$ (eV)")
    axes[0].set_ylabel(r"$\sigma_s(E)$ (b)")
    axes[0].set_title("(a) Elastic scattering")

    capture_values = capture(energy)
    one_over_v = energy**-0.5
    axes[1].loglog(energy, capture_values, color=ORANGE, lw=1)
    axes[1].loglog(
        energy,
        one_over_v,
        color="k",
        ls=":",
        lw=1,
        label=r"$1/\sqrt{E}$",
    )
    axes[1].set_xlabel(r"$E$ (eV)")
    axes[1].set_ylabel(r"$\sigma_a(E)$ (b)")
    axes[1].set_title("(b) Absorption")
    axes[1].legend(frameon=False)
    fig.tight_layout()
    save_figure(fig, output_dir, "h1_xsec.pgf")


def build_u235_fission(data: NuclearData, output_dir: Path) -> None:
    energy = np.logspace(-2, 7, 10_000)
    fission = data.cross_section("U235", 18)

    fig, ax = plt.subplots(figsize=(8, 3))
    ax.loglog(energy, fission(energy), color=PURPLE, lw=1)
    ax.set_xlabel(r"$E$ (eV)")
    ax.set_ylabel(r"$\sigma_f(E)$ (b)")
    ax.set_title(r"${}^{235}$U")
    fig.tight_layout()
    save_figure(fig, output_dir, "u235_fission.pgf")


def build_u238_inelastic(data: NuclearData, output_dir: Path) -> None:
    energy = np.logspace(4, 7.4, 20_000)
    # MT=4 is reconstructed by OpenMC from the available MT=51--91 levels
    # when the evaluated HDF5 library does not store a redundant sum directly.
    inelastic = data.cross_section("U238", 4)
    fission = data.cross_section("U238", 18)

    fig, ax = plt.subplots(figsize=(8, 3))
    ax.loglog(energy, inelastic(energy), color=PURPLE, lw=1, label="inelastic")
    ax.loglog(energy, fission(energy), color=ORANGE, lw=1, label="fission")
    ax.set_xlabel(r"$E$ (eV)")
    ax.set_ylabel(r"$\sigma(E)$ (b)")
    ax.set_title(r"${}^{238}$U threshold reactions")
    ax.legend(frameon=False)
    fig.tight_layout()
    save_figure(fig, output_dir, "U238_inelastic.pgf")


def prompt_neutron_yield(nuclide: Any) -> Callable[[np.ndarray], np.ndarray]:
    for product in nuclide[18].products:
        if product.particle == "neutron" and product.emission_mode == "prompt":
            return product.yield_
    raise GenerationError(
        f"OpenMC fission data for {nuclide.name} has no prompt-neutron yield"
    )


def uranium_eta(data: NuclearData, energy: np.ndarray, enrichment: float) -> np.ndarray:
    u235 = data.nuclide("U235")
    u238 = data.nuclide("U238")
    u235_fission = data.cross_section("U235", 18)(energy)
    u238_fission = data.cross_section("U238", 18)(energy)
    u235_capture = data.cross_section("U235", 102)(energy)
    u238_capture = data.cross_section("U238", 102)(energy)
    u235_nubar = prompt_neutron_yield(u235)(energy)
    u238_nubar = prompt_neutron_yield(u238)(energy)

    production = (
        enrichment * u235_fission * u235_nubar
        + (1.0 - enrichment) * u238_fission * u238_nubar
    )
    absorption = (
        enrichment * (u235_fission + u235_capture)
        + (1.0 - enrichment) * (u238_fission + u238_capture)
    )
    return np.divide(
        production,
        absorption,
        out=np.zeros_like(production),
        where=absorption > 0.0,
    )


def build_eta_nat_20(data: NuclearData, output_dir: Path) -> None:
    energy = np.logspace(-4, 7, 10_000)

    fig, ax = plt.subplots(figsize=(8, 3))
    ax.semilogx(
        energy,
        uranium_eta(data, energy, 0.007),
        color="k",
        lw=0.9,
        label="natural uranium",
    )
    ax.semilogx(
        energy,
        uranium_eta(data, energy, 0.20),
        color="b",
        lw=0.9,
        label="20% enrichment",
    )
    ax.set_xlabel("Energy (eV)")
    ax.set_ylabel(r"$\eta(E)$")
    ax.legend(frameon=False)
    fig.tight_layout()
    save_figure(fig, output_dir, "eta_nat_20.pgf")


def find_openmc_executable() -> Path:
    candidates = [Path(sys.executable).with_name("openmc")]
    on_path = shutil.which("openmc")
    if on_path:
        candidates.append(Path(on_path))
    for candidate in candidates:
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return candidate.resolve()
    raise GenerationError(
        "The OpenMC executable is unavailable. Activate an OpenMC environment "
        "whose `openmc` executable accompanies its Python package."
    )


def build_mc_vs_nr(
    data: NuclearData,
    output_dir: Path,
    work_dir: Path,
) -> None:
    """Compare direct transport with the narrow-resonance approximation.

    This follows the Lecture 11 specification: a 2 MeV fixed source in a
    reflective sphere containing a 10:1 H-1/U-238 atom mixture, plotted from
    1 eV through 0.1 MeV.  The NR curve is normalized to the simulation in the
    highest-energy bin.  A fixed seed makes the transport result repeatable.
    """

    openmc = data.openmc
    openmc_exec = find_openmc_executable()
    work_dir.mkdir(parents=True, exist_ok=True)

    material = openmc.Material(name="10:1 H-1/U-238 mixture")
    material.add_nuclide("H1", 10.0)
    material.add_nuclide("U238", 1.0)
    material.set_density("atom/b-cm", 0.066)
    material.temperature = 294.0
    materials = openmc.Materials([material])
    materials.cross_sections = str(data.cross_sections)

    sphere = openmc.Sphere(r=1.0, boundary_type="reflective")
    cell = openmc.Cell(fill=material, region=-sphere)
    geometry = openmc.Geometry([cell])

    settings = openmc.Settings()
    settings.run_mode = "fixed source"
    settings.source = openmc.IndependentSource(
        space=openmc.stats.Point((0.0, 0.0, 0.0)),
        energy=openmc.stats.Discrete([2.0e6], [1.0]),
    )
    settings.batches = 100
    settings.particles = 2_000
    settings.seed = 63011
    settings.cutoff = {"energy_neutron": 1.0}

    energy_edges = np.geomspace(1.0, 1.0e5, 501)
    tally = openmc.Tally(name="spectrum")
    tally.filters = [openmc.CellFilter(cell), openmc.EnergyFilter(energy_edges)]
    tally.scores = ["flux"]
    tally.estimator = "tracklength"

    model = openmc.Model(
        geometry=geometry,
        materials=materials,
        settings=settings,
        tallies=openmc.Tallies([tally]),
    )

    try:
        statepoint_path = model.run(
            cwd=work_dir.resolve(),
            openmc_exec=openmc_exec,
            output=False,
            threads=1,
        )
    except (OSError, RuntimeError, subprocess.CalledProcessError) as error:
        raise GenerationError(
            f"OpenMC transport failed in {work_dir}: {error}"
        ) from error

    statepoint_path = Path(statepoint_path)
    if not statepoint_path.is_file():
        raise GenerationError(
            f"OpenMC finished without producing its statepoint: {statepoint_path}"
        )

    with openmc.StatePoint(statepoint_path) as statepoint:
        spectrum = statepoint.get_tally(name="spectrum")
        bin_flux = spectrum.get_values(scores=["flux"], value="mean").ravel()

    energy = np.sqrt(energy_edges[:-1] * energy_edges[1:])
    sphere_volume = 4.0 * np.pi / 3.0
    phi_openmc = bin_flux / (sphere_volume * np.diff(energy_edges))
    number_densities = material.get_nuclide_atom_densities()
    sigma_total = sum(
        float(number_densities[name]) * data.cross_section(name, 1)(energy)
        for name in ("H1", "U238")
    )
    phi_nr_unscaled = 1.0 / (sigma_total * energy)
    if not np.isfinite(phi_openmc[-1]) or phi_openmc[-1] <= 0.0:
        raise GenerationError(
            "The highest-energy OpenMC tally bin is empty; cannot normalize "
            "the NR curve at 0.1 MeV."
        )
    phi_nr = phi_nr_unscaled * (phi_openmc[-1] / phi_nr_unscaled[-1])

    fig, ax = plt.subplots(figsize=(8, 3))
    ax.step(energy_edges[:-1], phi_openmc, where="post", color="k", lw=1, label="OpenMC")
    ax.plot(energy, phi_nr, color=PURPLE, lw=1, label="NR")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1.0, 1.0e5)
    ax.set_xlabel(r"$E$ [eV]")
    ax.set_ylabel(r"$\phi(E)$ [n/cm$^2$-s-eV]")
    ax.legend(frameon=False)
    fig.tight_layout()
    save_figure(fig, output_dir, "mc_vs_nr_u238_h1.pdf")


TARGETS: dict[str, Callable[[NuclearData, Path], None]] = {
    "h1_xsec": build_h1_xsec,
    "u235_fission": build_u235_fission,
    "U238_inelastic": build_u238_inelastic,
    "eta_nat_20": build_eta_nat_20,
}
TRANSPORT_TARGET = "mc_vs_nr_u238_h1"


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUTPUT_DIR,
        help=f"write generated figures here (default: {OUTPUT_DIR})",
    )
    parser.add_argument(
        "--target",
        action="append",
        choices=(*TARGETS, TRANSPORT_TARGET),
        help="generate one target; may be supplied more than once (default: all)",
    )
    parser.add_argument(
        "--cross-sections",
        type=Path,
        default=os.environ.get("OPENMC_CROSS_SECTIONS"),
        help="OpenMC cross_sections.xml (default: OPENMC_CROSS_SECTIONS)",
    )
    parser.add_argument(
        "--work-dir",
        type=Path,
        help="directory for OpenMC run files (default: temporary directory)",
    )
    return parser.parse_args(argv)


def selected_targets(requested: Sequence[str] | None) -> list[str]:
    if not requested:
        return [*TARGETS, TRANSPORT_TARGET]
    selected = set(requested)
    return [
        name
        for name in (*TARGETS, TRANSPORT_TARGET)
        if name in selected
    ]


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    if args.cross_sections is None:
        raise GenerationError(
            "No OpenMC data library was specified. Pass --cross-sections "
            "or set OPENMC_CROSS_SECTIONS."
        )
    cross_sections = args.cross_sections.expanduser().resolve()
    if not cross_sections.is_file():
        raise GenerationError(
            f"OpenMC cross_sections.xml does not exist: {cross_sections}"
        )

    openmc = import_openmc()
    data = NuclearData(openmc, cross_sections)
    targets = selected_targets(args.target)
    output_dir = args.output_dir.expanduser()

    with ExitStack() as stack:
        work_dir: Path | None = None
        if TRANSPORT_TARGET in targets:
            if args.work_dir is None:
                temporary = stack.enter_context(
                    tempfile.TemporaryDirectory(prefix="ne630-openmc-")
                )
                work_dir = Path(temporary)
            else:
                work_dir = args.work_dir.expanduser()

        for name in targets:
            if name == TRANSPORT_TARGET:
                assert work_dir is not None
                build_mc_vs_nr(data, output_dir, work_dir)
            else:
                TARGETS[name](data, output_dir)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except GenerationError as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(2) from error
