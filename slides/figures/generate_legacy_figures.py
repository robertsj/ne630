#!/usr/bin/env python3
"""Recreate data-free slide figures whose original sources are unavailable.

These are deterministic reconstructions from the definitions in the lecture
notes, not byte-for-byte reproductions of the missing legacy artwork.  The
script deliberately excludes figures that depend on OpenMC or evaluated
nuclear data.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable, Sequence
from math import erf
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle


DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parent / "generated"
PURPLE = "#512888"
ORANGE = "#CA7C1B"

# Do not embed a path to Matplotlib's private font directory in PGF output.
# The including slide document supplies its own fonts instead.
plt.rcParams.update(
    {
        "font.family": "serif",
        "pgf.rcfonts": False,
        "pgf.texsystem": "xelatex",
        "savefig.bbox": "tight",
    }
)


def save_figure(fig: plt.Figure, destination: Path) -> None:
    """Save *fig* with stable PDF metadata, then close it."""

    destination.parent.mkdir(parents=True, exist_ok=True)
    options: dict[str, object] = {"bbox_inches": "tight", "pad_inches": 0.02}
    if destination.suffix == ".pdf":
        options["metadata"] = {
            "Creator": "NE 630 generate_legacy_figures.py",
            "CreationDate": None,
            "ModDate": None,
        }
    fig.savefig(destination, **options)
    plt.close(fig)
    print(f"generated {destination}")


def _draw_target(ax: plt.Axes, samples: np.ndarray, title: str) -> None:
    """Draw one accuracy/precision target with fixed sample locations."""

    for radius in (0.25, 0.50, 0.75, 1.00):
        ax.add_patch(
            Circle(
                (0.0, 0.0),
                radius,
                facecolor="none",
                edgecolor="#777777",
                linewidth=0.8,
            )
        )
    ax.axhline(0.0, color="#bbbbbb", linewidth=0.55, zorder=0)
    ax.axvline(0.0, color="#bbbbbb", linewidth=0.55, zorder=0)
    ax.scatter(
        samples[:, 0],
        samples[:, 1],
        s=34,
        marker="x",
        linewidths=1.7,
        color=PURPLE,
        zorder=3,
    )
    ax.scatter([0.0], [0.0], s=24, marker="+", linewidths=1.3, color=ORANGE, zorder=4)
    ax.set(xlim=(-1.22, 1.22), ylim=(-1.22, 1.22), aspect="equal", title=title)
    ax.set_axis_off()


def build_accuracy_vs_precision(output_dir: Path) -> None:
    """Visualize the definitions in ``slides/lecture_01.tex``.

    The samples are paired about their intended mean.  Thus the two accurate
    panels have a mean exactly at the accepted value, while the two inaccurate
    panels have the same explicit systematic offset.
    """

    precise = np.array(
        [
            (0.12, 0.04),
            (-0.12, -0.04),
            (0.04, -0.12),
            (-0.04, 0.12),
            (0.10, -0.08),
            (-0.10, 0.08),
            (0.02, 0.06),
            (-0.02, -0.06),
        ]
    )
    imprecise = np.array(
        [
            (0.72, 0.12),
            (-0.72, -0.12),
            (0.14, 0.68),
            (-0.14, -0.68),
            (0.55, -0.50),
            (-0.55, 0.50),
            (0.34, 0.42),
            (-0.34, -0.42),
            (0.68, -0.22),
            (-0.68, 0.22),
        ]
    )
    systematic_offset = np.array((0.42, 0.35))

    # The lecture includes this PGF at full text width and still needs room for
    # a sentence below it.  A single row keeps the complete figure inside the
    # Beamer frame instead of clipping the lower two targets.
    fig, axes = plt.subplots(1, 4, figsize=(10.4, 2.55))
    panels = (
        (precise, "Accurate,\nprecise"),
        (imprecise, "Accurate,\nnot precise"),
        (precise + systematic_offset, "Precise,\nnot accurate"),
        (imprecise + systematic_offset, "Neither accurate\nnor precise"),
    )
    for ax, (samples, title) in zip(axes.flat, panels, strict=True):
        _draw_target(ax, samples, title)
    fig.subplots_adjust(left=0.01, right=0.99, bottom=0.02, top=0.82, wspace=0.08)
    save_figure(fig, output_dir / "accuracy_vs_precision.pgf")


def hydrogen_free_gas_kernel(
    outgoing_energy: np.ndarray,
    incident_energy: float,
    thermal_energy: float,
) -> np.ndarray:
    """Evaluate the H-1 free-gas kernel quoted as D&H 9-23 in Lecture 11."""

    if incident_energy <= 0.0 or thermal_energy <= 0.0:
        raise ValueError("incident_energy and thermal_energy must be positive")
    if np.any(outgoing_energy < 0.0):
        raise ValueError("outgoing_energy must be nonnegative")

    result = np.empty_like(outgoing_energy, dtype=float)
    downscatter = outgoing_energy <= incident_energy
    result[downscatter] = np.fromiter(
        (
            erf(float(np.sqrt(energy / thermal_energy)))
            for energy in outgoing_energy[downscatter]
        ),
        dtype=float,
        count=np.count_nonzero(downscatter),
    ) / incident_energy

    incident_erf = erf(np.sqrt(incident_energy / thermal_energy))
    result[~downscatter] = (
        np.exp((incident_energy - outgoing_energy[~downscatter]) / thermal_energy)
        * incident_erf
        / incident_energy
    )
    return result


def build_thermal_scattering_hydrogen(output_dir: Path) -> None:
    """Plot the dimensionless H-1 free-gas kernel from ``lecture_11.tex``."""

    # Expressing both energies in units of kT makes the figure independent of
    # a chosen temperature while retaining the exact kernel in the lecture.
    thermal_energy = 1.0
    outgoing = np.geomspace(1.0e-3, 20.0, 1_500)
    incident_ratios = (0.25, 1.0, 4.0)
    colors = (ORANGE, PURPLE, "#333333")

    # This plot shares its Beamer frame with the full piecewise kernel above.
    # Keep it deliberately wide and shallow so the x-axis remains visible.
    fig, ax = plt.subplots(figsize=(7.2, 2.35))
    for ratio, color in zip(incident_ratios, colors, strict=True):
        incident = ratio * thermal_energy
        kernel = hydrogen_free_gas_kernel(outgoing, incident, thermal_energy)
        dimensionless_kernel = incident * kernel
        ax.plot(
            outgoing / thermal_energy,
            dimensionless_kernel,
            color=color,
            linewidth=1.8,
            label=rf"$E'/kT={ratio:g}$",
        )
        transition = erf(np.sqrt(ratio))
        ax.plot([ratio], [transition], marker="o", markersize=4.0, color=color)

    ax.set_xscale("log")
    ax.set_xlim(1.0e-3, 20.0)
    ax.set_ylim(0.0, 1.05)
    ax.set_xlabel(r"outgoing energy, $E/kT$")
    ax.set_ylabel(r"dimensionless kernel, $E' p(E'\to E)$")
    ax.grid(which="both", color="#dddddd", linewidth=0.55)
    ax.legend(frameon=False, ncols=3, loc="upper center")
    fig.tight_layout()
    save_figure(fig, output_dir / "thermal_scattering_hydrogen.pdf")


GENERATORS: dict[str, Callable[[Path], None]] = {
    "accuracy_vs_precision": build_accuracy_vs_precision,
    "thermal_scattering_hydrogen": build_thermal_scattering_hydrogen,
}


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "targets",
        nargs="*",
        choices=tuple(GENERATORS),
        default=tuple(GENERATORS),
        help="figures to generate (default: all)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="destination directory (default: figures/generated)",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    for target in args.targets:
        GENERATORS[target](args.output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
