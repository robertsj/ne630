"""Rebuild slide figures whose generating code survives in NE 630 notebooks.

This intentionally excludes figures that require unavailable OpenMC data or
whose provenance is uncertain.  Run with the course's scientific Python
environment; NumPy, SciPy, Matplotlib, and Pillow are required.
"""

from __future__ import annotations

import argparse
import base64
import json
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy.integrate import odeint, solve_ivp


OUTPUT_DIR = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = OUTPUT_DIR / "generated"
REPO_ROOT = OUTPUT_DIR.parents[1]
SLIDES_DIR = REPO_ROOT / "slides"
NOTEBOOK_DIR = REPO_ROOT / "notebooks"

PURPLE = "#512888"
ORANGE = "#CA7C1B"

plt.rcParams.update(
    {
        "font.family": "serif",
        "pgf.rcfonts": False,
        "pgf.texsystem": "xelatex",
        "savefig.bbox": "tight",
    }
)


def save_figure(
    fig: plt.Figure,
    filename: str,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / filename
    fig.savefig(destination)
    plt.close(fig)
    print(f"generated {destination.name}")


def build_realistic_rho(output_dir: Path = DEFAULT_OUTPUT_DIR) -> None:
    """Source: notebooks/lesson_24.ipynb, cells 18--19."""

    atan2 = np.arctan2

    def rho_base(B, T_F=1200, T_C=600, C_B=0):
        del C_B
        return (
            0.265701782943972
            + 0.0173604082545277 * atan2(0.0173604082545277, abs(B) ** 0.5)
            - 2.64479010825198e-5 * T_F
            - 0.00319948157566795 * B
            - 5.72926698137041e-6 * B * T_C
        )

    B_values = np.linspace(0, 62, 1_000_000)
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(B_values, rho_base(B_values))
    ax.grid(True)
    ax.set_xlabel(r"$B$ [MWd/kg]")
    ax.set_ylabel(r"$\rho$")
    save_figure(fig, "realistic_rho.pdf", output_dir)


def build_subcritical_multiplication(output_dir: Path = DEFAULT_OUTPUT_DIR) -> None:
    """Source: notebooks/lesson_26.ipynb, cells 24--26."""

    def population(t, k_infinity):
        lifetime = 1e-2
        source = 1.0
        return (lifetime * source / (k_infinity - 1)) * (
            np.exp((k_infinity - 1) / lifetime * t) - 1
        )

    t = np.linspace(0, 10, 10_000)
    fig, ax = plt.subplots(figsize=(8, 6))
    for k_infinity in (0.5, 0.9, 0.99):
        ax.plot(t, population(t, k_infinity), label=f"{k_infinity:g}")
    ax.set_xlabel(r"$t$ [s]")
    ax.set_ylabel(r"$n(t)/S_0$")
    ax.legend()
    save_figure(fig, "subcrit_mult.pgf", output_dir)


def build_example_kinetics(output_dir: Path = DEFAULT_OUTPUT_DIR) -> None:
    """Source: notebooks/lesson_27.ipynb, cells 39 and 49--60."""

    betas = np.array([0.00021, 0.00142, 0.00128, 0.00257, 0.00075, 0.00027])
    half_lives = np.array([56, 23, 6.2, 2.3, 0.61, 0.23])
    lambdas = np.log(2) / half_lives
    generation_time = 5e-5

    def reactivity(t):
        return 0.001 if 1 <= t <= 2 else 0.0

    def derivatives(y, t, rho, beta_i, lambda_i, Lambda):
        n = y[0]
        precursors = y[1:]
        beta = beta_i.sum()
        result = np.zeros(7)
        result[0] = ((rho(t) - beta) / Lambda) * n + np.sum(precursors * lambda_i)
        result[1:] = -precursors * lambda_i + beta_i * n / Lambda
        return result

    initial = np.zeros(7)
    initial[0] = 1e8
    initial[1:] = betas * initial[0] / (lambdas * generation_time)
    times = np.linspace(0, 10, 10_000)
    solution = odeint(
        derivatives,
        initial,
        times,
        args=(reactivity, betas, lambdas, generation_time),
    )

    fig, ax = plt.subplots()
    ax.plot(times, solution[:, 0], label=r"$n(t)$")
    for index in range(6):
        ax.plot(times, solution[:, index + 1], label=rf"$C_{{{index + 1}}}(t)$")
    ax.set_xlabel(r"$t$ [s]")
    ax.set_yscale("log")
    ax.legend()
    save_figure(fig, "example_kinetics.pgf", output_dir)


def solve_one_group(reactivity, beta=0.0065, Lambda=5e-5, decay=0.0766, n0=1.0):
    """One-delayed-group step solution from lesson_28.ipynb, cell 14."""

    c0 = beta * n0 / (decay * Lambda)
    coefficient_b = decay * (1 - (reactivity - beta) / (decay * Lambda))
    coefficient_c = -(decay * (reactivity - beta) / Lambda + decay * beta / Lambda)
    discriminant = np.sqrt(coefficient_b**2 - 4 * coefficient_c)
    omega_1 = (-coefficient_b + discriminant) / 2
    omega_2 = (-coefficient_b - discriminant) / 2
    a1 = (reactivity * n0 / Lambda - n0 * omega_2) / (omega_1 - omega_2)
    a2 = n0 - a1
    b1 = (-beta * n0 * omega_2 / (decay * Lambda)) / (omega_1 - omega_2)
    b2 = c0 - b1
    population = lambda t: a1 * np.exp(omega_1 * t) + a2 * np.exp(omega_2 * t)
    precursor = lambda t: b1 * np.exp(omega_1 * t) + b2 * np.exp(omega_2 * t)
    return population, precursor, omega_1, omega_2


def build_traces(output_dir: Path = DEFAULT_OUTPUT_DIR) -> None:
    """Source: notebooks/lesson_28.ipynb, cell 15."""

    beta = 0.0065
    fig, axes = plt.subplots(2, 2, figsize=(7, 7))
    short_time = np.linspace(0, 0.1, 1_000)

    positive = (
        (0.05, "k", "-", r"$\rho=0.05\beta$"),
        (0.10, "k", "--", r"$\rho=0.1\beta$"),
        (0.15, PURPLE, (5, (10, 3)), r"$\rho=\rho_A$"),
        (0.20, "k", "-.", r"$\rho=0.2\beta$"),
    )
    negative = (
        (-0.05, "k", "-", r"$\rho=-0.05\beta$"),
        (-0.10, "k", "--", r"$\rho=-0.1\beta$"),
        (-0.15, PURPLE, (5, (10, 3)), r"$\rho=\rho_B$"),
        (-0.20, "k", "-.", r"$\rho=-0.2\beta$"),
    )

    for fraction, color, line_style, label in positive:
        population, _, omega_1, omega_2 = solve_one_group(fraction * beta)
        axes[0, 0].plot(short_time, population(short_time), color=color, ls=line_style, lw=1)
        if abs(fraction) != 0.15:
            y = 1.035 + 0.065 * positive.index((fraction, color, line_style, label))
            axes[0, 0].text(0.05, y, label, color=color)
            axes[0, 0].text(0.05, y - 0.015, rf"$\omega_1={omega_1:.4f}$", color=color)
            axes[0, 0].text(0.05, y - 0.030, rf"$\omega_2={omega_2:.1f}$", color=color)
        else:
            axes[0, 0].text(0.05, 1.16, label, color=color)

    negative_text_y = (0.98, 0.935, 0.875, 0.856)
    for index, (fraction, color, line_style, label) in enumerate(negative):
        population, _, omega_1, omega_2 = solve_one_group(fraction * beta)
        axes[0, 1].plot(short_time, population(short_time), color=color, ls=line_style, lw=1)
        y = negative_text_y[index]
        axes[0, 1].text(0.05, y, label, color=color)
        if abs(fraction) != 0.15:
            axes[0, 1].text(0.05, y - 0.010, rf"$\omega_1={omega_1:.4f}$", color=color)
            axes[0, 1].text(0.05, y - 0.020, rf"$\omega_2={omega_2:.1f}$", color=color)

    long_time = np.linspace(0, 10, 1_000)
    for fraction, color, line_style, _ in positive:
        population, _, _, _ = solve_one_group(fraction * beta)
        axes[1, 0].plot(long_time, population(long_time), color=color, ls=line_style, lw=1)
    for fraction, color, line_style, _ in negative:
        population, _, _, _ = solve_one_group(fraction * beta)
        axes[1, 1].plot(long_time, population(long_time), color=color, ls=line_style, lw=1)

    axes[0, 0].set_ylabel(r"$n(t)/n_0$")
    axes[0, 0].set_xlabel(r"$t$ (s)")
    axes[0, 0].set_title(r"$\rho > 0$ (step insertion)")
    axes[0, 1].set_xlabel(r"$t$ (s)")
    axes[0, 1].set_title(r"$\rho < 0$ (step removal)")
    axes[1, 0].set_ylabel(r"$n(t)/n_0$")
    axes[1, 0].set_xlabel(r"$t$ (s)")
    axes[1, 1].set_xlabel(r"$t$ (s)")
    fig.tight_layout()
    save_figure(fig, "traces.pgf", output_dir)


def build_slab_boundary_conditions(output_dir: Path = DEFAULT_OUTPUT_DIR) -> None:
    """Reconstruct the scenario stated in lectures 33 and 34."""

    slab_width = 10.0
    diffusion = 1.0
    absorption = 0.1
    source = 1.0
    diffusion_length = np.sqrt(diffusion / absorption)
    x = np.linspace(0, slab_width, 1_000)
    particular = source / absorption
    scaled_width = slab_width / diffusion_length

    zero_flux = particular * (
        1 - np.cosh(x / diffusion_length) / np.cosh(scaled_width)
    )
    partial_current_denominator = np.cosh(scaled_width) + (
        2 * diffusion / diffusion_length
    ) * np.sinh(scaled_width)
    zero_partial_current = particular * (
        1 - np.cosh(x / diffusion_length) / partial_current_denominator
    )

    fig, ax = plt.subplots(figsize=(9, 3))
    ax.plot(x, zero_flux, label="zero flux")
    ax.plot(x, zero_partial_current, label="zero partial current")
    ax.set_ylabel(r"$\phi(x)$")
    ax.set_xlabel(r"$x$")
    ax.legend()
    save_figure(fig, "slab_bc.pgf", output_dir)


def blend_colors(color1: str, color2: str, ratio: float) -> str:
    rgb1 = tuple(int(color1.lstrip("#")[i : i + 2], 16) for i in (0, 2, 4))
    rgb2 = tuple(int(color2.lstrip("#")[i : i + 2], 16) for i in (0, 2, 4))
    blended = tuple(int((1 - ratio) * first + ratio * second) for first, second in zip(rgb1, rgb2))
    return "#" + "".join(f"{component:02x}" for component in blended)


def build_multiplying_slab(output_dir: Path = DEFAULT_OUTPUT_DIR) -> None:
    """Source: notebooks/Lesson_33_and_34_examples.ipynb, cells 45--48."""

    slab_width = 10.0
    diffusion = 0.5
    absorption = 0.2
    source = 1.0
    diffusion_length = np.sqrt(diffusion / absorption)

    def flux(x, k_infinity):
        if k_infinity <= 1:
            alpha = np.sqrt((1 - k_infinity) / diffusion_length**2)
            return source / (diffusion * alpha**2) * (
                1 - np.cosh(alpha * x) / np.cosh(0.5 * alpha * slab_width)
            )
        alpha = np.sqrt((k_infinity - 1) / diffusion_length**2)
        return source / (diffusion * alpha**2) * (
            np.cos(alpha * x) / np.cos(0.5 * alpha * slab_width) - 1
        )

    x = np.linspace(-slab_width / 2, slab_width / 2, 1_000)
    values = [0.0, 0.25, 0.50, 0.75, 0.9, 0.99, 1.05, 1.1, 1.15, 1.2, 1.25]
    fig, ax = plt.subplots(figsize=(8, 3))
    for k_infinity in values:
        ax.plot(
            x,
            flux(x, k_infinity),
            color=blend_colors("#000000", "#512fff", k_infinity / max(values)),
            label=rf"$k_{{\infty}}={k_infinity:.2f}$",
        )
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$\phi(x)$")
    ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    save_figure(fig, "multiplying_slab.pgf", output_dir)


def build_xenon_transient(output_dir: Path = DEFAULT_OUTPUT_DIR) -> None:
    """Correct the variable-name typos in the generator shown in lecture 22."""

    def derivatives(t, concentrations, flux, sigma_a_xe, sigma_f):
        gamma_i, gamma_xe = 0.0639, 0.00237
        lambda_i = 0.693 / (6.7 * 3600)
        lambda_xe = 0.693 / (9.2 * 3600)
        sigma_a_xe *= 1e-24
        iodine, xenon = concentrations
        phi = flux(t)
        d_iodine = -lambda_i * iodine + gamma_i * sigma_f * phi
        d_xenon = (
            -lambda_xe * xenon
            + lambda_i * iodine
            + (gamma_xe * sigma_f - sigma_a_xe * xenon) * phi
        )
        return d_iodine, d_xenon

    hour = 3600
    day = 24 * hour
    flux = lambda t: 2e14 if t < 3 * day else 0.0
    result = solve_ivp(
        fun=derivatives,
        t_span=(0.0, 5 * day),
        y0=(0, 0),
        args=(flux, 2.3e6, 0.16),
        max_step=hour,
    )
    time_hours = result.t / hour
    iodine, xenon = result.y

    fig, ax = plt.subplots()
    ax.plot(time_hours, iodine, color=ORANGE, lw=1, label="I")
    ax.plot(time_hours, xenon, color=PURPLE, lw=1, ls="-.", label="Xe")
    ax.set_xlabel(r"$t$ (h)")
    ax.set_ylabel(r"$N(t)$ (cm$^{-3}$)")
    ax.legend()
    save_figure(fig, "Xe_transient.pdf", output_dir)


def extract_notebook_png(notebook: str, cell_index: int) -> Image.Image:
    notebook_data = json.loads((NOTEBOOK_DIR / notebook).read_text(encoding="utf-8"))
    for output in notebook_data["cells"][cell_index].get("outputs", []):
        encoded = output.get("data", {}).get("image/png")
        if encoded:
            from io import BytesIO

            return Image.open(BytesIO(base64.b64decode(encoded))).convert("RGB")
    raise RuntimeError(f"No embedded PNG found in {notebook}, cell {cell_index}")


def extract_xenon_comparison(output_dir: Path = DEFAULT_OUTPUT_DIR) -> None:
    """Source: embedded output in notebooks/lesson_22.ipynb, cell 2."""

    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "xe135_comparison.pdf"
    extract_notebook_png("lesson_22.ipynb", 2).save(destination)
    print(f"extracted {destination.name}")


def _tex_asset_path(path: Path) -> str:
    """Return a portable path suitable for inclusion from the slides directory."""

    try:
        return path.resolve().relative_to(SLIDES_DIR.resolve()).as_posix()
    except ValueError:
        # Outputs outside the repository are useful for tests and previews.  Keep
        # those wrappers relocatable by referring to the sibling asset by name.
        return path.name


def extract_prompt_drop_illustration(output_dir: Path = DEFAULT_OUTPUT_DIR) -> None:
    """Source: attachment in notebooks/lesson_28.ipynb, cell 22."""

    notebook_data = json.loads((NOTEBOOK_DIR / "lesson_28.ipynb").read_text(encoding="utf-8"))
    attachments = notebook_data["cells"][22].get("attachments", {})
    encoded = attachments["image.png"]["image/png"]
    output_dir.mkdir(parents=True, exist_ok=True)
    image_path = output_dir / "prompt_drop_illustration.png"
    image_path.write_bytes(base64.b64decode(encoded))
    wrapper_path = output_dir / "prompt_drop_illustration.pgf"
    wrapper_path.write_text(
        f"\\includegraphics{{{_tex_asset_path(image_path)}}}\n",
        encoding="utf-8",
    )
    print(f"extracted {image_path.name} and generated {wrapper_path.name}")


@dataclass(frozen=True)
class FigureTarget:
    builder: Callable[[Path], None]
    outputs: tuple[str, ...]
    description: str


TARGETS = {
    "realistic_rho": FigureTarget(
        build_realistic_rho,
        ("realistic_rho.pdf",),
        "burnup-dependent reactivity plot",
    ),
    "subcrit_mult": FigureTarget(
        build_subcritical_multiplication,
        ("subcrit_mult.pgf",),
        "subcritical multiplication plot",
    ),
    "example_kinetics": FigureTarget(
        build_example_kinetics,
        ("example_kinetics.pgf",),
        "six-group point-kinetics example",
    ),
    "traces": FigureTarget(
        build_traces,
        ("traces.pgf",),
        "one-group kinetics traces",
    ),
    "slab_bc": FigureTarget(
        build_slab_boundary_conditions,
        ("slab_bc.pgf",),
        "slab boundary-condition comparison",
    ),
    "multiplying_slab": FigureTarget(
        build_multiplying_slab,
        ("multiplying_slab.pgf",),
        "multiplying-slab flux profiles",
    ),
    "xenon_transient": FigureTarget(
        build_xenon_transient,
        ("Xe_transient.pdf",),
        "iodine/xenon transient",
    ),
    "xe135_comparison": FigureTarget(
        extract_xenon_comparison,
        ("xe135_comparison.pdf",),
        "xenon comparison embedded in lesson 22",
    ),
    "prompt_drop_illustration": FigureTarget(
        extract_prompt_drop_illustration,
        ("prompt_drop_illustration.png", "prompt_drop_illustration.pgf"),
        "prompt-drop notebook attachment and PGF wrapper",
    ),
}

GROUPS = {
    "all": tuple(TARGETS),
    "plots": tuple(TARGETS)[:7],
    "notebook-assets": tuple(TARGETS)[7:],
    "pdf": ("realistic_rho", "xenon_transient", "xe135_comparison"),
    "pgf": (
        "subcrit_mult",
        "example_kinetics",
        "traces",
        "slab_bc",
        "multiplying_slab",
        "prompt_drop_illustration",
    ),
}


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"write figures here (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--target",
        action="append",
        choices=tuple(TARGETS),
        help="build one target; may be supplied more than once",
    )
    parser.add_argument(
        "--group",
        action="append",
        choices=tuple(GROUPS),
        help="build a target group; may be supplied more than once",
    )
    parser.add_argument(
        "--list-targets",
        action="store_true",
        help="list available targets and groups, then exit",
    )
    return parser.parse_args(argv)


def selected_targets(
    targets: Sequence[str] | None,
    groups: Sequence[str] | None,
) -> list[str]:
    """Return selected target names once, in reproducible build order."""

    requested = set(targets or ())
    for group in groups or ():
        requested.update(GROUPS[group])
    if not requested:
        requested.update(GROUPS["all"])
    return [name for name in TARGETS if name in requested]


def print_targets() -> None:
    print("Targets:")
    for name, target in TARGETS.items():
        print(f"  {name:<26} {target.description}")
    print("Groups:")
    for name, members in GROUPS.items():
        print(f"  {name:<26} {' '.join(members)}")


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    if args.list_targets:
        print_targets()
        return 0

    args.output_dir.mkdir(parents=True, exist_ok=True)
    for name in selected_targets(args.target, args.group):
        TARGETS[name].builder(args.output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
