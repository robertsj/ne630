#!/usr/bin/env python3
"""Compile public source bundles and compare them with published PDFs."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[2]
PUBLIC_DIRECTORY = REPOSITORY / "site" / "_static" / "handouts"
LESSONS = (1, 2, 3, 4, 5)
REQUIRED_TOOLS = ("latexmk", "pdftoppm")


class BuildCheckError(RuntimeError):
    """Raised when a public handout bundle does not reproduce its PDF."""


def _run(command: list[str], *, directory: Path | None = None) -> subprocess.CompletedProcess[bytes]:
    try:
        return subprocess.run(
            command,
            cwd=directory,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError as error:
        output = error.stdout.decode("utf-8", errors="replace")
        tail = "\n".join(output.splitlines()[-30:])
        raise BuildCheckError(f"command failed: {' '.join(command)}\n{tail}") from error


def _extract_bundle(bundle: Path, destination: Path) -> None:
    with zipfile.ZipFile(bundle) as archive:
        for member in archive.infolist():
            relative = Path(member.filename)
            if relative.is_absolute() or ".." in relative.parts or member.is_dir():
                raise BuildCheckError(f"unsafe or unexpected ZIP member: {member.filename}")
            output = destination / relative
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(archive.read(member))


def _render(pdf: Path, prefix: Path) -> list[Path]:
    _run(["pdftoppm", "-r", "144", "-png", str(pdf), str(prefix)])
    return sorted(prefix.parent.glob(f"{prefix.name}-*.png"))


def _check_lesson(lesson: int, temporary_root: Path) -> None:
    basename = f"lesson_{lesson:02d}_handout"
    public_lesson = PUBLIC_DIRECTORY / f"lesson-{lesson:02d}"
    bundle = public_lesson / f"{basename}_source.zip"
    published_pdf = public_lesson / f"{basename}.pdf"
    if not bundle.is_file() or not published_pdf.is_file():
        raise BuildCheckError(f"Lesson {lesson:02d} is missing its source bundle or PDF")

    build_directory = temporary_root / f"lesson-{lesson:02d}"
    build_directory.mkdir()
    _extract_bundle(bundle, build_directory)
    _run(
        [
            "latexmk",
            "-g",
            "-xelatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            f"{basename}.tex",
        ],
        directory=build_directory,
    )

    rebuilt_pdf = build_directory / f"{basename}.pdf"
    if not rebuilt_pdf.is_file():
        raise BuildCheckError(f"Lesson {lesson:02d} source bundle did not produce a PDF")

    published_pages = _render(published_pdf, build_directory / "published")
    rebuilt_pages = _render(rebuilt_pdf, build_directory / "rebuilt")
    if len(published_pages) != 2 or len(rebuilt_pages) != 2:
        raise BuildCheckError(
            f"Lesson {lesson:02d} must render as two pages "
            f"(published={len(published_pages)}, rebuilt={len(rebuilt_pages)})"
        )
    for page_number, (published, rebuilt) in enumerate(
        zip(published_pages, rebuilt_pages, strict=True), start=1
    ):
        if published.read_bytes() != rebuilt.read_bytes():
            raise BuildCheckError(
                f"Lesson {lesson:02d} page {page_number} differs between the "
                "published PDF and public source bundle"
            )


def check_builds() -> None:
    missing_tools = [tool for tool in REQUIRED_TOOLS if shutil.which(tool) is None]
    if missing_tools:
        raise BuildCheckError(f"required command(s) not found: {', '.join(missing_tools)}")

    with tempfile.TemporaryDirectory(prefix="ne630-handout-check-") as temporary:
        temporary_root = Path(temporary)
        for lesson in LESSONS:
            _check_lesson(lesson, temporary_root)


def main() -> int:
    argparse.ArgumentParser(description=__doc__).parse_args()
    try:
        check_builds()
    except (BuildCheckError, zipfile.BadZipFile) as error:
        print(f"handout build check failed: {error}", file=sys.stderr)
        return 1
    print(
        f"Verified {len(LESSONS)} public source bundles against their two-page PDFs."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
