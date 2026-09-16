#!/usr/bin/env python3
"""Rebuild the data figures used by the Fall 2026 solution manual.

The Homework 05 figures are recovered from the executed course notebook.  The
Homework 06 figures require the U-238 HDF5 file used by OpenMC and supplied via
``--u238-h5``.  This script is not invoked by ``make`` because the Beocat data
path is not portable; the generated figures are retained as source assets.
"""

from __future__ import annotations

import argparse
import base64
import json
from pathlib import Path

import h5py
import matplotlib.pyplot as plt
import numpy as np


RESONANCE_ENERGIES = np.array([6.67, 20.87, 36.68, 66.03, 80.75, 102.56])
NEUTRON_WIDTHS = np.array(
    [1.476e-3, 1.009e-2, 3.355e-2, 2.418e-2, 1.874e-3, 7.077e-2]
)
GAMMA_WIDTHS = np.array(
    [2.300e-2, 2.286e-2, 2.300e-2, 2.331e-2, 2.339e-2, 2.408e-2]
)


def extract_notebook_png(notebook: Path, cell: int, output: Path) -> None:
    """Extract the first PNG output from one executed notebook cell."""
    data = json.loads(notebook.read_text(encoding="utf-8"))
    for item in data["cells"][cell].get("outputs", []):
        encoded = item.get("data", {}).get("image/png")
        if encoded:
            if isinstance(encoded, list):
                encoded = "".join(encoded)
            output.write_bytes(base64.b64decode(encoded))
            return
    raise RuntimeError(f"no PNG output found in cell {cell} of {notebook}")


def read_openmc_xs(path: Path, nuclide: str, mt: int) -> tuple[np.ndarray, np.ndarray]:
    """Read one 294 K tabulated reaction directly from an OpenMC HDF5 file."""
    with h5py.File(path, "r") as data:
        energy = np.asarray(data[f"{nuclide}/energy/294K"])
        xs_data = data[f"{nuclide}/reactions/reaction_{mt:03d}/294K/xs"]
        xs = np.asarray(xs_data)
        threshold = int(xs_data.attrs["threshold_idx"])
    return energy[threshold : threshold + xs.size], xs


def slbw_capture(energy: np.ndarray) -> np.ndarray:
    """Return the six-resonance, zero-temperature SLBW approximation in barns."""
    sigma = np.zeros_like(energy, dtype=float)
    for resonance, neutron_width, gamma_width in zip(
        RESONANCE_ENERGIES, NEUTRON_WIDTHS, GAMMA_WIDTHS
    ):
        total_width = neutron_width + gamma_width
        wavelength = 4.55e-10 / np.sqrt(resonance)
        sigma_0 = (
            4.0
            * np.pi
            * wavelength**2
            * neutron_width
            / total_width
            * 1.0e24
        )
        sigma += (
            sigma_0
            * gamma_width
            / total_width
            * np.sqrt(resonance / energy)
            / (1.0 + 4.0 * (energy - resonance) ** 2 / total_width**2)
        )
    return sigma


def finish_plot(output: Path) -> None:
    plt.grid(which="both", color="0.88", linewidth=0.45)
    plt.tight_layout()
    plt.savefig(output, dpi=180)
    plt.close()


def build_hw06_figures(u238_h5: Path, output_dir: Path) -> None:
    energy, capture = read_openmc_xs(u238_h5, "U238", 102)

    plt.figure(figsize=(6.4, 3.5))
    plt.loglog(energy, capture, color="black", linewidth=0.7)
    plt.axvline(2.0e4, color="tab:red", linestyle=":", linewidth=1.0)
    plt.text(
        1.6e4,
        2.0e3,
        "resonances overlap\nnear $20$ keV",
        color="tab:red",
        horizontalalignment="right",
    )
    plt.xlim(1.0e-4, 1.0e7)
    plt.ylim(1.0e-4, 1.0e5)
    plt.xlabel(r"$E$ (eV)")
    plt.ylabel(r"$\sigma_\gamma(E)$ (b)")
    finish_plot(output_dir / "hw06_u238_capture_full.png")

    plt.figure(figsize=(6.4, 3.5))
    plt.semilogy(energy, capture, color="black", linewidth=0.8)
    plt.axvline(6.67, color="tab:red", linestyle=":", linewidth=1.0)
    plt.text(9.0, 2.0e-2, r"first large resonance near $6.67$ eV", color="tab:red")
    plt.xlim(1.0, 100.0)
    plt.ylim(1.0e-3, 2.0e4)
    plt.xlabel(r"$E$ (eV)")
    plt.ylabel(r"$\sigma_\gamma(E)$ (b)")
    finish_plot(output_dir / "hw06_u238_capture_1_100ev.png")

    fine_energy = np.linspace(1.0, 100.0, 1_980_001)
    plt.figure(figsize=(6.4, 3.5))
    plt.semilogy(
        fine_energy,
        slbw_capture(fine_energy),
        color="black",
        linewidth=0.8,
        label="six-resonance SLBW (0 K)",
    )
    plt.semilogy(
        energy,
        capture,
        color="tab:red",
        linestyle="--",
        linewidth=0.8,
        label="OpenMC (294 K)",
    )
    plt.xlim(1.0, 100.0)
    plt.ylim(1.0e-3, 1.0e5)
    plt.xlabel(r"$E$ (eV)")
    plt.ylabel(r"$\sigma_\gamma(E)$ (b)")
    plt.legend(loc="upper right", fontsize=8)
    finish_plot(output_dir / "hw06_slbw_comparison.png")


def main() -> None:
    default_notebook = Path(__file__).resolve().parents[2] / "notebooks/lesson_05.ipynb"
    parser = argparse.ArgumentParser()
    parser.add_argument("--u238-h5", type=Path, required=True)
    parser.add_argument("--notebook", type=Path, default=default_notebook)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).parent / "figures")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    extract_notebook_png(args.notebook, 8, args.output_dir / "hw05_h1_cross_sections.png")
    extract_notebook_png(args.notebook, 15, args.output_dir / "hw05_b10_cross_sections.png")
    build_hw06_figures(args.u238_h5, args.output_dir)


if __name__ == "__main__":
    main()
