"""Regenerate the one-species Br-87 graphical exercise.

Run from any directory; the PDF is written next to this file in handouts/figures/.
The unknown reactivities are deliberately omitted from the plot labels.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FixedLocator, FixedFormatter
import numpy as np
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parent
GAMMA, FN, NU = 0.01274, 0.0260, 2.43
BETA = FN * GAMMA / NU
LAM = np.log(2.0) / 55.65
GEN_TIME = 5e-5
PURPLE, ORANGE = "#512888", "#CA7C1B"


def modes(dollars):
    """Exact two-mode solution for n(0)=1 and critical precursor equilibrium."""
    rho = dollars * BETA
    A = np.array([[(rho-BETA)/GEN_TIME, LAM],
                  [BETA/GEN_TIME, -LAM]])
    fast, slow = np.sort(np.linalg.eigvals(A).real)
    amplitude = (rho/GEN_TIME-fast)/(slow-fast)
    return slow, fast, amplitude, 1-amplitude


def density(t, dollars):
    t = np.asarray(t, dtype=float)
    slow, fast, a, b = modes(dollars)
    out = np.ones_like(t)
    mask = t >= 0
    out[mask] = a*np.exp(slow*t[mask]) + b*np.exp(fast*t[mask])
    return out


def verify():
    """Check modal formulas against an independent matrix exponential."""
    for d in [.2, .5, -.2, -.5]:
        A = np.array([[(d*BETA-BETA)/GEN_TIME, LAM],
                      [BETA/GEN_TIME, -LAM]])
        y0 = np.array([1., BETA/(LAM*GEN_TIME)])
        times = np.array([0., .01, 1., 5., 100.])
        reference = np.array([(expm(A*t)@y0)[0] for t in times])
        np.testing.assert_allclose(density(times, d), reference, rtol=2e-11)
        slow, fast, a, b = modes(d)
        rho_recovered = GEN_TIME*slow + BETA*slow/(slow+LAM)
        np.testing.assert_allclose(rho_recovered, d*BETA, rtol=2e-12)
        print(f"rho/beta={d:+.1f}: T={1/slow:.6f} s; "
              f"slow intercept={a:.6f}; prompt J={1/(1-d):.6f}")


def main():
    verify()
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 9,
        "axes.titlesize": 10, "axes.labelsize": 9,
        "xtick.labelsize": 8, "ytick.labelsize": 8,
        "legend.fontsize": 8.3, "axes.linewidth": .65,
        "pdf.fonttype": 42, "ps.fonttype": 42,
        "mathtext.fontset": "dejavusans",
    })
    fig, axes = plt.subplots(2, 2, figsize=(7.54, 5.62))
    fig.subplots_adjust(left=.083, right=.987, top=.953, bottom=.085,
                        wspace=.24, hspace=.43)
    early = np.r_[np.linspace(-1, 0, 60, endpoint=False),
                  np.linspace(0, 5, 650)]
    positive = np.r_[np.linspace(0, 5, 250), np.linspace(5.1, 250, 650)]
    negative = np.r_[np.linspace(0, 5, 250), np.linspace(5.1, 600, 900)]
    cases = [(axes[0, 0], early, [.2, .5], ["+0.2\\beta", "\\rho_A"],
              "(a) Positive step: early response"),
             (axes[0, 1], early, [-.2, -.5], ["-0.2\\beta", "\\rho_B"],
              "(b) Negative step: early response"),
             (axes[1, 0], positive, [.2, .5], ["+0.2\\beta", "\\rho_A"],
              "(c) Positive step: late response"),
             (axes[1, 1], negative, [-.2, -.5], ["-0.2\\beta", "\\rho_B"],
              "(d) Negative step: late response")]
    for ax, t, ds, labels, title in cases:
        for d, label, color, style in zip(ds, labels, [PURPLE, ORANGE], ["--", "-"]):
            ax.plot(t, density(t, d), color=color, ls=style, lw=1.9,
                    label="$"+label+"$")
        ax.set_title(title, loc="left", pad=9, fontweight="bold")
        ax.set_xlabel("Time, $t$ (s)", labelpad=3)
        ax.set_ylabel("$n(t)/n_0$", labelpad=3)
        ax.grid(which="major", color=".75", linewidth=.50)
        ax.grid(which="minor", color=".88", linewidth=.40)
        ax.set_axisbelow(True)
        ax.tick_params(direction="out", length=3, width=.6, which="major")
        ax.tick_params(direction="out", length=2, width=.4, which="minor")
        ax.legend(loc="best", frameon=True, facecolor="white",
                  framealpha=1, edgecolor=".8", handlelength=2.8)
    for ax in axes[0]:
        ax.set_xlim(-1, 5)
        ax.axvline(0, color=".35", lw=.7, zorder=1)
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.xaxis.set_minor_locator(MultipleLocator(.5))
        ax.yaxis.set_minor_locator(MultipleLocator(.05))
    axes[0, 0].set_ylim(.95, 2.2)
    axes[0, 0].yaxis.set_major_locator(MultipleLocator(.2))
    axes[0, 1].set_ylim(.60, 1.02)
    axes[0, 1].yaxis.set_major_locator(MultipleLocator(.1))
    for ax in axes[1]:
        ax.set_yscale("log")
    axes[1, 0].set_xlim(0, 250)
    axes[1, 0].set_ylim(1, 50)
    axes[1, 0].xaxis.set_major_locator(MultipleLocator(50))
    axes[1, 0].xaxis.set_minor_locator(MultipleLocator(10))
    axes[1, 0].yaxis.set_major_locator(FixedLocator([1, 2, 5, 10, 20, 50]))
    axes[1, 0].yaxis.set_major_formatter(FixedFormatter(["1", "2", "5", "10", "20", "50"]))
    axes[1, 0].yaxis.set_minor_locator(FixedLocator([3, 4, 6, 7, 8, 9, 30, 40]))
    axes[1, 0].yaxis.set_minor_formatter(FixedFormatter([""]*8))
    axes[1, 1].set_xlim(0, 600)
    axes[1, 1].set_ylim(.05, 1.05)
    axes[1, 1].xaxis.set_major_locator(MultipleLocator(100))
    axes[1, 1].xaxis.set_minor_locator(MultipleLocator(20))
    axes[1, 1].yaxis.set_major_locator(FixedLocator([.05, .1, .2, .5, 1]))
    axes[1, 1].yaxis.set_major_formatter(FixedFormatter(["0.05", "0.1", "0.2", "0.5", "1"]))
    axes[1, 1].yaxis.set_minor_locator(FixedLocator([.06, .07, .08, .09, .3, .4, .6, .7, .8, .9]))
    axes[1, 1].yaxis.set_minor_formatter(FixedFormatter([""]*10))
    fig.savefig(ROOT/"lesson_27_traces.pdf",
                metadata={"Title": "NE 630 Lesson 27: one-species Br-87 traces",
                          "Author": "Jeremy Roberts"})
    plt.close(fig)


if __name__ == "__main__":
    main()
