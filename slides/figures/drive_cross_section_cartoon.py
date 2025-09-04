import os
import shutil
import subprocess
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

# Filenames relative to this script's directory
TEMPLATE_NAME = "cross_section_cartoon_shared_template.tex"
SHARED_NAME   = "cross_section_cartoon_shared.tex"
TEX_3D_NAME   = "cross_section_cartoon_3D.tex"
TEX_2D_NAME   = "cross_section_cartoon_2D.tex"


def _here() -> Path:
    """Directory containing this script."""
    return Path(__file__).resolve().parent


def _fmt_centers(centers: Iterable[Sequence[float]]) -> str:
    """
    Format centers as TikZ-friendly lines inside \\def\\nuclei{...}:
        0.15/0.60/0.70,
        0.35/1.40/2.50,
        ...
    The last line omits the trailing comma.
    """
    lines: List[str] = []
    for triplet in centers:
        if len(triplet) != 3:
            raise ValueError(f"Each center must have three components (x,y,z). Got: {triplet!r}")
        x, y, z = triplet
        lines.append(f"  {x:.6g}/{y:.6g}/{z:.6g},")
    if lines:
        lines[-1] = lines[-1].rstrip(',')
    return "\n".join(lines)


def _ensure_xelatex() -> str:
    """
    Return the path to xelatex if available, otherwise raise a helpful error.
    """
    exe = shutil.which("xelatex")
    if exe is None:
        raise RuntimeError(
            "xelatex not found on PATH. Please install a TeX distribution (TeX Live/MacTeX/MiKTeX) "
            "and ensure 'xelatex' is available on your PATH."
        )
    return exe


def _run_xelatex(texfile: Path, jobname: str) -> None:
    """
    Compile the provided TeX file with xelatex, using a unique jobname so outputs don't overwrite.
    Runs twice to stabilize references if needed.
    """
    exe = _ensure_xelatex()
    cmd = [exe, "-interaction=nonstopmode", "-halt-on-error", f"-jobname={jobname}", texfile.name]
    for _ in range(2):
        # Use cwd so TeX can find relative \input files
        proc = subprocess.run(cmd, cwd=texfile.parent)
        if proc.returncode != 0:
            raise RuntimeError(f"xelatex failed while compiling {texfile} (jobname={jobname}).")


def render(centers: Iterable[Sequence[float]], xcut: float, radius: float) -> Tuple[Path, Path]:
    """
    Creates 'cross_section_cartoon_shared.tex' from the template with the supplied centers, xcut,
    and radius, then generates both the 3D and 2D PDFs using xelatex.

    Parameters
    ----------
    centers : iterable of (x, y, z)
        The nucleus centers in slab coordinates (units consistent with your TikZ).
    xcut : float
        The x-plane at which the yz cross section is taken.
    radius : float
        Sphere radius used in both the 3D and 2D renderings.

    Returns
    -------
    (pdf3d, pdf2d) : Tuple[Path, Path]
        Paths to the generated 3D and 2D PDF files.
    """
    base = _here()
    template_path = base / TEMPLATE_NAME
    shared_path   = base / SHARED_NAME
    tex3d_path    = base / TEX_3D_NAME
    tex2d_path    = base / TEX_2D_NAME

    # Load template and substitute placeholders
    template = template_path.read_text(encoding="utf-8")
    rendered = (
        template
        .replace("%%%CENTERS%%%", _fmt_centers(centers))
        .replace("%%%CUT%%%", f"{xcut:.6g}")
        .replace("%%%RADIUS%%%", f"{radius:.6g}")
    )
    shared_path.write_text(rendered, encoding="utf-8")

    # Build unique suffix based on xcut to avoid overwriting outputs
    suffix = f"x{xcut:.2f}".replace('.', 'p')
    job3d = f"cross_section_cartoon_3D_{suffix}"
    job2d = f"cross_section_cartoon_2D_{suffix}"

    # Compile 3D and 2D
    _run_xelatex(tex3d_path, job3d)
    _run_xelatex(tex2d_path, job2d)

    pdf3d = tex3d_path.with_name(job3d + ".pdf")
    pdf2d = tex2d_path.with_name(job2d + ".pdf")
    return pdf3d, pdf2d


if __name__ == "__main__":
    nuclei_centers = [
        [0.15, 0.60, 0.70],
        [0.35, 1.40, 2.50],
        [0.75, 2.10, 1.10],
        [0.60, 0.90, 2.20],
        [0.20, 2.60, 0.50],
        [0.90, 1.80, 1.70],
    ]

    xcuts = [0.0, 0.25, 0.5, 0.75, 1.0]
    radius = 0.25

    outputs: List[Tuple[Path, Path]] = []
    for x in xcuts:
        out3d, out2d = render(nuclei_centers, x, radius)
        outputs.append((out3d, out2d))

    # Friendly summary
    print("Generated PDFs:")
    for (p3d, p2d) in outputs:
        print(f"  3D: {p3d.name}   |   2D: {p2d.name}")
