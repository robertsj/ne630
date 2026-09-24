#!/usr/bin/env python3
"""Create public handout artifacts for the Sphinx site."""

from __future__ import annotations

import argparse
import hashlib
import io
import re
import sys
import zipfile
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[2]
SOURCE_DIRECTORY = REPOSITORY / "handouts"
OUTPUT_DIRECTORY = REPOSITORY / "site" / "_static" / "handouts"
LESSONS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14)
LESSON_SUPPORT_FILES = {
    5: ("spectra.pdf",),
    6: (
        "figures/h1_xsec.pgf",
        "figures/u235_fission.pgf",
        "figures/u238_threshold.ipynb",
        "figures/u238_threshold.pdf",
    ),
    7: (
        "figures/u238_threshold.ipynb",
        "figures/u238_threshold.pdf",
    ),
    10: (
        "figures/nr.pdf",
        "figures/wr.pdf",
    ),
}


class ExportError(RuntimeError):
    """Raised when a handout cannot be exported safely."""


def _read_required(path: Path) -> bytes:
    if not path.is_file():
        raise ExportError(f"required handout artifact is missing: {path.relative_to(REPOSITORY)}")
    return path.read_bytes()


def _validate_public_wrapper(path: Path, text: str) -> None:
    if not re.search(r"\\documentclass\s*\{ne630boardhandout\}", text):
        raise ExportError(f"{path.name} must use the shared ne630boardhandout class directly")
    if "\\handoutsolutionsfalse" not in text:
        raise ExportError(f"{path.name} must set \\handoutsolutionsfalse for public export")
    if "\\handoutsolutionstrue" in text:
        raise ExportError(f"{path.name} enables solution output")


def _source_readme(lesson: int, support_files: tuple[str, ...]) -> bytes:
    basename = f"lesson_{lesson:02d}_handout"
    file_lines = [
        f"  {basename}.tex       document wrapper; set \\handoutsolutionstrue for a solution copy",
        f"  {basename}_body.tex  handout body with blanks and solution payloads",
        "  ne630boardhandout.cls     shared document class",
    ]
    file_lines.extend(
        f"  {name:<24} "
        + ("OpenMC plot-source notebook" if name.endswith(".ipynb") else "supporting figure")
        for name in support_files
    )
    files = "\n".join(file_lines)
    content = f"""NE 630 Lesson {lesson:02d} handout source

Files:
{files}

Compile the public, non-solution handout with XeLaTeX:

  latexmk -xelatex -interaction=nonstopmode -halt-on-error {basename}.tex

The committed wrapper sets \\handoutsolutionsfalse and therefore reproduces the
published PDF. To make a private solution copy, change that one line to
\\handoutsolutionstrue before compiling. Do not publish generated source with
solutions enabled.

Myriad Pro is used when it is installed in one of the paths recognized by the
class; otherwise the class falls back to TeX Gyre Heros. Libertinus Math and
the standard packages named by the class are also required.
"""
    return content.encode("utf-8")


def _zip_bytes(files: dict[str, bytes]) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(files):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, files[name])
    return buffer.getvalue()


def expected_exports() -> dict[Path, bytes]:
    class_bytes = _read_required(SOURCE_DIRECTORY / "ne630boardhandout.cls")
    exports: dict[Path, bytes] = {Path("ne630boardhandout.cls"): class_bytes}

    for lesson in LESSONS:
        basename = f"lesson_{lesson:02d}_handout"
        directory = Path(f"lesson-{lesson:02d}")
        wrapper_path = SOURCE_DIRECTORY / f"{basename}.tex"
        body_path = SOURCE_DIRECTORY / f"{basename}_body.tex"
        pdf_path = SOURCE_DIRECTORY / f"{basename}.pdf"

        wrapper = _read_required(wrapper_path)
        _validate_public_wrapper(wrapper_path, wrapper.decode("utf-8"))
        body = _read_required(body_path)
        pdf = _read_required(pdf_path)
        if not pdf.startswith(b"%PDF-"):
            raise ExportError(f"{pdf_path.name} is not a PDF file")

        support_files = LESSON_SUPPORT_FILES.get(lesson, ())
        support_contents = {
            name: _read_required(SOURCE_DIRECTORY / name) for name in support_files
        }
        readme = _source_readme(lesson, support_files)
        bundle_files = {
            "README.txt": readme,
            f"{basename}.tex": wrapper,
            f"{basename}_body.tex": body,
            "ne630boardhandout.cls": class_bytes,
            **support_contents,
        }

        exports[directory / f"{basename}.pdf"] = pdf
        exports[directory / f"{basename}.tex"] = wrapper
        exports[directory / f"{basename}_body.tex"] = body
        for name, content in support_contents.items():
            exports[directory / name] = content
        exports[directory / f"{basename}_source.zip"] = _zip_bytes(bundle_files)

    return exports


def _digest(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def check_exports(exports: dict[Path, bytes]) -> list[str]:
    errors: list[str] = []
    expected_paths = {OUTPUT_DIRECTORY / relative for relative in exports}
    actual_paths = {path for path in OUTPUT_DIRECTORY.rglob("*") if path.is_file()}

    for relative, expected in exports.items():
        destination = OUTPUT_DIRECTORY / relative
        if not destination.is_file():
            errors.append(f"missing generated file: {destination.relative_to(REPOSITORY)}")
        elif destination.read_bytes() != expected:
            errors.append(
                f"stale generated file: {destination.relative_to(REPOSITORY)} "
                f"(expected sha256 {_digest(expected)[:12]})"
            )

    for unexpected in sorted(actual_paths - expected_paths):
        errors.append(f"unexpected public handout file: {unexpected.relative_to(REPOSITORY)}")
    return errors


def write_exports(exports: dict[Path, bytes]) -> None:
    errors = [error for error in check_exports(exports) if error.startswith("unexpected")]
    if errors:
        raise ExportError("\n".join(errors) + "\nRefusing to delete an unrecognized public file.")

    for relative, content in exports.items():
        destination = OUTPUT_DIRECTORY / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.is_file() or destination.read_bytes() != content:
            destination.write_bytes(content)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify generated exports without modifying them",
    )
    arguments = parser.parse_args()

    try:
        exports = expected_exports()
        if arguments.check:
            errors = check_exports(exports)
            if errors:
                raise ExportError("\n".join(errors))
            print(f"Verified {len(exports)} public handout files.")
        else:
            write_exports(exports)
            print(f"Exported {len(exports)} public handout files.")
    except (ExportError, UnicodeDecodeError) as error:
        print(f"handout export failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
