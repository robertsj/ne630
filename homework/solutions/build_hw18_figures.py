#!/usr/bin/env python3
"""Rebuild the Homework 18 solution figures from the retained source data."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "hw18_p_over_d.csv"
OUTPUT = ROOT / "figures"


def finish(path: Path) -> None:
    plt.grid(color="0.88", linewidth=0.6)
    plt.tight_layout()
    plt.savefig(path, dpi=180)
    plt.close()


def main() -> None:
    values = np.genfromtxt(DATA, delimiter=",", names=True)
    pd = values["P_over_D"]
    OUTPUT.mkdir(exist_ok=True)

    plt.figure(figsize=(6.4, 3.7))
    plt.plot(pd, values["k_inf"], "o-", color="#512888", markersize=3)
    plt.xlabel(r"$P/D$")
    plt.ylabel(r"$k_\infty$")
    finish(OUTPUT / "hw18_koo.png")

    plt.figure(figsize=(7.2, 4.0))
    for field, label in (
        ("eta", r"$\ln\eta$"),
        ("f", r"$\ln f$"),
        ("p", r"$\ln p$"),
        ("epsilon", r"$\ln\epsilon$"),
    ):
        plt.plot(pd, np.log(values[field]), "o-", markersize=2.5, label=label)
    plt.xlabel(r"$P/D$")
    plt.ylabel("logarithm of factor")
    plt.legend(ncol=2)
    finish(OUTPUT / "hw18_log_four_factors.png")


if __name__ == "__main__":
    main()
