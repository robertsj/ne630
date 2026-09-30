#!/usr/bin/env python3
"""Collect normalized final-solution PDFs from a Canvas submission export.

The script is deliberately conservative. It preserves the raw Canvas archive,
copies only the selected final-solution PDF for each student group, and writes
CSV reports for every automatic decision and every case needing review.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from zipfile import BadZipFile, ZipFile


CANVAS_NAME_RE = re.compile(
    r"^(?P<slug>.+?)_(?P<user_id>\d+)_(?P<submission_id>\d+)_(?P<original>.+)$"
)

POSITIVE_TERMS = {
    "solution": 120,
    "solutions": 110,
    "answer": 90,
    "answers": 90,
    "final": 35,
    "hw1": 35,
    "hw01": 35,
    "homework": 30,
    "hmwk": 25,
    "hwrk": 25,
    "reactor": 10,
    "theory": 5,
    "ne630": 15,
    "ne": 3,
    "630": 3,
}

NEGATIVE_TERMS = {
    "discourse": -180,
    "transcript": -160,
    "chat": -150,
    "conversation": -150,
    "prompt": -120,
    "prompts": -120,
    "dialogue": -120,
    "dialog": -120,
    "ai": -90,
    "gpt": -80,
    "claude": -80,
    "gemini": -80,
}

IMAGE_EXTENSIONS = {"jpg", "jpeg"}


@dataclass(frozen=True)
class OuterEntry:
    zip_path: str
    basename: str
    slug: str
    user_id: str
    submission_id: str
    original_name: str
    extension: str


@dataclass(frozen=True)
class Candidate:
    source_kind: str
    source_entry: str
    original_name: str
    nested_archive: str
    internal_path: str
    display_name: str
    score: int
    rule: str
    is_pdf: bool
    signature: str
    content: bytes

    @property
    def size_bytes(self) -> int:
        return len(self.content)


@dataclass
class GroupResult:
    slug: str
    user_id: str
    status: str
    route_guess: str
    output_file: str
    source_entry: str
    nested_archive: str
    internal_path: str
    original_name: str
    rule: str
    confidence: str
    sha256: str
    size_bytes: str
    candidate_count: int
    review_reason: str
    candidates: str


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Collect final-solution PDFs from a Canvas homework ZIP export."
    )
    parser.add_argument(
        "archive",
        type=Path,
        help="Canvas submissions ZIP, e.g. hw01/raw/hw1_subs.zip",
    )
    parser.add_argument(
        "--homework-dir",
        type=Path,
        default=None,
        help=(
            "Homework working directory. Defaults to the parent of raw/ when "
            "the archive lives under a raw directory."
        ),
    )
    parser.add_argument(
        "--solutions-dir",
        type=Path,
        default=None,
        help="Destination for normalized solution PDFs. Defaults to homework-dir/solutions.",
    )
    parser.add_argument(
        "--reports-dir",
        type=Path,
        default=None,
        help="Destination for CSV reports. Defaults to homework-dir/reports.",
    )
    parser.add_argument(
        "--work-dir",
        type=Path,
        default=None,
        help="Working directory for derived builds. Defaults to homework-dir/work.",
    )
    parser.add_argument(
        "--overwrite",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Overwrite normalized outputs and reports when they already exist.",
    )
    parser.add_argument(
        "--clean-output",
        action="store_true",
        help=(
            "Remove previously generated *_solution.pdf and "
            "*_solution.source.txt files before collecting."
        ),
    )
    return parser.parse_args(argv)


def infer_homework_dir(archive: Path, explicit: Path | None) -> Path:
    if explicit is not None:
        return explicit
    if archive.parent.name == "raw":
        return archive.parent.parent
    return Path.cwd()


def parse_outer_entry(zip_path: str) -> OuterEntry | None:
    basename = os.path.basename(zip_path)
    if not basename or basename.startswith(".") or "__MACOSX/" in zip_path:
        return None
    match = CANVAS_NAME_RE.match(basename)
    if match:
        slug = match.group("slug")
        user_id = match.group("user_id")
        submission_id = match.group("submission_id")
        original_name = match.group("original")
    else:
        stem = Path(basename).stem
        slug = sanitize_stem(stem)
        user_id = "unknown"
        submission_id = "unknown"
        original_name = basename
    extension = Path(basename).suffix.lower().lstrip(".")
    return OuterEntry(
        zip_path=zip_path,
        basename=basename,
        slug=slug,
        user_id=user_id,
        submission_id=submission_id,
        original_name=original_name,
        extension=extension,
    )


def sanitize_stem(value: str) -> str:
    stem = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").lower()
    return stem or "unknown"


def token_set(name: str) -> set[str]:
    stem = Path(name).stem.lower()
    spaced = re.sub(r"[^a-z0-9]+", " ", stem)
    tokens = set(spaced.split())
    compact = re.sub(r"[^a-z0-9]+", "", stem)
    if compact:
        tokens.add(compact)
    return tokens


def has_homework_marker(path: str) -> bool:
    """Return True for common homework filename markers such as hw4 or hw04."""
    lower = path.lower()
    return re.search(r"(?:^|[^a-z0-9])hw0?\d+(?:[^a-z0-9]|$)", lower) is not None


def score_pdf_name(path: str) -> tuple[int, str]:
    basename = os.path.basename(path).lower()
    tokens = token_set(basename)
    if basename == "solution.pdf":
        return 1000, "exact solution.pdf"

    score = 0
    notes: list[str] = []
    for term, weight in POSITIVE_TERMS.items():
        if term in tokens:
            score += weight
            notes.append(f"+{term}")
    for term, weight in NEGATIVE_TERMS.items():
        if term in tokens:
            score += weight
            notes.append(f"{term}")

    if has_homework_marker(path) and not ({"hw1", "hw01"} & tokens):
        score += 35
        notes.append("+homework marker")

    # These long labels are reliable even when tokenization splits punctuation.
    lower_path = path.lower()
    for term in ("discourse", "transcript", "conversation"):
        if term in lower_path and term not in tokens:
            score -= 130
            notes.append(term)
    for term in ("solution", "answers", "answer", "homework"):
        if term in lower_path and term not in tokens:
            score += 45
            notes.append(f"+{term}")

    if not notes:
        notes.append("filename heuristic")
    return score, ", ".join(notes)


def score_tex_name(path: str, content: str) -> tuple[int, str]:
    lower_path = path.lower()
    basename = os.path.basename(lower_path)
    stem = Path(basename).stem
    notes: list[str] = []

    if any(term in lower_path for term in ("discourse", "transcript", "template")):
        return -1000, "not a final-solution TeX target"

    score = 0
    if basename == "__collector_solution_wrapper.tex":
        score += 950
        notes.append("generated solution-only wrapper")
    elif basename == "solution.tex":
        score += 1000
        notes.append("exact solution.tex")
    elif basename in {"answers.tex", "answer.tex"}:
        score += 800
        notes.append("answer TeX")
    elif basename == "main.tex":
        score += 650
        notes.append("main TeX")
    elif stem in {"hw1", "hw01"} or "hw01" in stem or "hw1" in stem or has_homework_marker(lower_path):
        score += 520
        notes.append("homework TeX")

    if "\\documentclass" in content:
        score += 120
        notes.append("standalone document")
    if "\\begin{document}" in content:
        score += 60
        notes.append("document body")
    if "solution" in lower_path or "answer" in lower_path:
        score += 75
        notes.append("solution-like name")

    if not notes:
        notes.append("TeX filename heuristic")
    return score, ", ".join(notes)


def jpeg_metadata(content: bytes) -> tuple[int, int, int, int]:
    """Return width, height, color components, and precision for a JPEG image."""
    if not content.startswith(b"\xff\xd8"):
        raise ValueError("not a JPEG image")
    i = 2
    sof_markers = {
        0xC0,
        0xC1,
        0xC2,
        0xC3,
        0xC5,
        0xC6,
        0xC7,
        0xC9,
        0xCA,
        0xCB,
        0xCD,
        0xCE,
        0xCF,
    }
    while i < len(content) - 1:
        if content[i] != 0xFF:
            i += 1
            continue
        while i < len(content) and content[i] == 0xFF:
            i += 1
        if i >= len(content):
            break
        marker = content[i]
        i += 1
        if marker in {0x01, *range(0xD0, 0xD8), 0xD8, 0xD9}:
            continue
        if i + 2 > len(content):
            break
        segment_length = int.from_bytes(content[i : i + 2], "big")
        if segment_length < 2 or i + segment_length > len(content):
            break
        if marker in sof_markers:
            precision = content[i + 2]
            height = int.from_bytes(content[i + 3 : i + 5], "big")
            width = int.from_bytes(content[i + 5 : i + 7], "big")
            components = content[i + 7]
            return width, height, components, precision
        i += segment_length
    raise ValueError("could not find JPEG dimensions")


def make_pdf(objects: list[bytes]) -> bytes:
    output = io.BytesIO()
    output.write(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for index, obj in enumerate(objects, start=1):
        offsets.append(output.tell())
        output.write(f"{index} 0 obj\n".encode("ascii"))
        output.write(obj)
        if not obj.endswith(b"\n"):
            output.write(b"\n")
        output.write(b"endobj\n")
    xref_at = output.tell()
    output.write(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    output.write(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        output.write(f"{offset:010d} 00000 n \n".encode("ascii"))
    output.write(
        (
            f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
            f"startxref\n{xref_at}\n%%EOF\n"
        ).encode("ascii")
    )
    return output.getvalue()


def jpeg_to_pdf(content: bytes) -> bytes:
    width_px, height_px, components, precision = jpeg_metadata(content)
    color_space = {
        1: "/DeviceGray",
        3: "/DeviceRGB",
        4: "/DeviceCMYK",
    }.get(components)
    if color_space is None:
        raise ValueError(f"unsupported JPEG color component count: {components}")

    page_width = 612.0
    page_height = 792.0
    margin = 36.0
    scale = min((page_width - 2 * margin) / width_px, (page_height - 2 * margin) / height_px)
    display_width = width_px * scale
    display_height = height_px * scale
    x_offset = (page_width - display_width) / 2
    y_offset = (page_height - display_height) / 2
    content_stream = (
        "q\n"
        f"{display_width:.4f} 0 0 {display_height:.4f} {x_offset:.4f} {y_offset:.4f} cm\n"
        "/Im0 Do\n"
        "Q\n"
    ).encode("ascii")

    image_extra = ""
    if components == 4:
        image_extra = " /Decode [1 0 1 0 1 0 1 0]"

    image_object = (
        (
            f"<< /Type /XObject /Subtype /Image /Width {width_px} /Height {height_px} "
            f"/ColorSpace {color_space} /BitsPerComponent {precision} "
            f"/Filter /DCTDecode /Length {len(content)}{image_extra} >>\n"
            "stream\n"
        ).encode("ascii")
        + content
        + b"\nendstream\n"
    )
    content_object = (
        f"<< /Length {len(content_stream)} >>\nstream\n".encode("ascii")
        + content_stream
        + b"endstream\n"
    )
    return make_pdf(
        [
            b"<< /Type /Catalog /Pages 2 0 R >>\n",
            b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>\n",
            (
                b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
                b"/Resources << /XObject << /Im0 4 0 R >> >> "
                b"/Contents 5 0 R >>\n"
            ),
            image_object,
            content_object,
        ]
    )


def converted_jpeg_candidate(
    entry: OuterEntry,
    source_kind: str,
    content: bytes,
    nested_archive: str = "",
    internal_path: str = "",
    display_name: str | None = None,
) -> Candidate | None:
    try:
        pdf_content = jpeg_to_pdf(content)
    except ValueError:
        return None
    name_for_score = internal_path or entry.original_name
    score, notes = score_pdf_name(name_for_score)
    if score <= 0 and source_kind.startswith("nested"):
        return None
    return Candidate(
        source_kind=source_kind,
        source_entry=entry.zip_path,
        original_name=entry.original_name,
        nested_archive=nested_archive,
        internal_path=internal_path,
        display_name=display_name or entry.original_name,
        score=max(score, 40 if source_kind.startswith("top_level") else score),
        rule=f"converted JPEG image to archival PDF; {notes}",
        is_pdf=True,
        signature="generated_pdf_from_jpeg",
        content=pdf_content,
    )


def summarize_candidate(candidate: Candidate) -> str:
    nested = f" in {candidate.nested_archive}" if candidate.nested_archive else ""
    return (
        f"{candidate.display_name}{nested}"
        f" [score={candidate.score}, rule={candidate.rule}, "
        f"valid_pdf={candidate.is_pdf}, signature={candidate.signature}]"
    )


def choose_candidate(candidates: list[Candidate]) -> tuple[Candidate | None, str, str]:
    if not candidates:
        return None, "no PDF candidate found", "0.00"

    valid_candidates = [candidate for candidate in candidates if candidate.is_pdf]
    if not valid_candidates:
        return None, "PDF-extension candidates are not valid PDFs by header", "0.00"

    exact = [c for c in valid_candidates if c.rule == "exact solution.pdf"]
    if len(exact) == 1:
        return exact[0], "selected exact solution.pdf", "1.00"
    if len(exact) > 1:
        return None, "multiple exact solution.pdf candidates", "0.00"

    sorted_candidates = sorted(valid_candidates, key=lambda c: c.score, reverse=True)
    best = sorted_candidates[0]
    runner_up = sorted_candidates[1] if len(sorted_candidates) > 1 else None

    if best.score < 0:
        return None, "only negative-scoring PDF candidates found", "0.00"

    if runner_up is None:
        if best.source_kind == "top_level_pdf":
            return best, "single standalone PDF candidate", "0.88"
        if best.source_kind == "top_level_image_pdf":
            return best, "converted standalone image upload to PDF", "0.82"
        if best.source_kind == "built_tex_pdf":
            return best, best.rule, "0.72"
        if best.source_kind == "nested_image_pdf":
            return best, "converted nested image candidate to PDF", "0.70"
        return best, "single nested PDF candidate", "0.78"

    score_gap = best.score - runner_up.score
    if score_gap >= 90:
        return best, "unique best PDF by filename heuristic", "0.78"
    if score_gap >= 35 and best.score >= 35 and runner_up.score < 0:
        return best, "only plausible non-discourse PDF candidate", "0.74"

    return None, "ambiguous PDF candidates", "0.00"


def route_guess(entries: list[OuterEntry], selected: Candidate | None) -> str:
    has_zip = any(entry.extension == "zip" for entry in entries)
    pdf_count = sum(entry.extension == "pdf" for entry in entries)
    if selected and selected.source_kind == "top_level_image_pdf":
        return "route_a_image_upload_converted"
    if selected and selected.source_kind == "nested_image_pdf":
        return "route_b_zip_image_converted"
    if selected and selected.source_kind == "built_tex_pdf":
        return "route_b_zip_built_from_tex"
    if has_zip and selected and selected.source_kind == "nested_pdf":
        if selected.rule == "exact solution.pdf":
            return "route_b_zip"
        return "route_b_zip_nonstandard_solution_name"
    if has_zip:
        return "route_b_zip_needs_review"
    if pdf_count == 1:
        return "route_a_pdf"
    if pdf_count > 1:
        return "top_level_multi_pdf"
    return "unknown"


def iter_nested_pdf_candidates(outer_zip: ZipFile, entry: OuterEntry) -> Iterable[Candidate]:
    try:
        nested_bytes = outer_zip.read(entry.zip_path)
        with ZipFile(io.BytesIO(nested_bytes)) as nested_zip:
            for name in nested_zip.namelist():
                if name.endswith("/") or "__MACOSX/" in name:
                    continue
                extension = Path(name).suffix.lower().lstrip(".")
                if extension != "pdf" and extension not in IMAGE_EXTENSIONS:
                    continue
                try:
                    content = nested_zip.read(name)
                except KeyError:
                    continue
                score, rule = score_pdf_name(name)
                is_pdf, signature = classify_content(content)
                if is_pdf:
                    yield Candidate(
                        source_kind="nested_pdf",
                        source_entry=entry.zip_path,
                        original_name=entry.original_name,
                        nested_archive=entry.basename,
                        internal_path=name,
                        display_name=os.path.basename(name),
                        score=score,
                        rule=rule,
                        is_pdf=is_pdf,
                        signature=signature,
                        content=content,
                    )
                elif signature == "jpeg" or extension in IMAGE_EXTENSIONS:
                    converted = converted_jpeg_candidate(
                        entry,
                        "nested_image_pdf",
                        content,
                        nested_archive=entry.basename,
                        internal_path=name,
                        display_name=os.path.basename(name),
                    )
                    if converted is not None:
                        yield converted
    except BadZipFile:
        return


def iter_group_candidates(outer_zip: ZipFile, entries: list[OuterEntry]) -> list[Candidate]:
    candidates: list[Candidate] = []
    for entry in entries:
        if entry.extension == "pdf":
            content = outer_zip.read(entry.zip_path)
            score, rule = score_pdf_name(entry.original_name)
            is_pdf, signature = classify_content(content)
            if is_pdf:
                candidates.append(
                    Candidate(
                        source_kind="top_level_pdf",
                        source_entry=entry.zip_path,
                        original_name=entry.original_name,
                        nested_archive="",
                        internal_path="",
                        display_name=entry.original_name,
                        score=score,
                        rule=rule,
                        is_pdf=is_pdf,
                        signature=signature,
                        content=content,
                    )
                )
            elif signature == "jpeg":
                converted = converted_jpeg_candidate(entry, "top_level_image_pdf", content)
                if converted is not None:
                    candidates.append(converted)
        elif entry.extension in IMAGE_EXTENSIONS:
            content = outer_zip.read(entry.zip_path)
            converted = converted_jpeg_candidate(entry, "top_level_image_pdf", content)
            if converted is not None:
                candidates.append(converted)
        elif entry.extension == "zip":
            candidates.extend(iter_nested_pdf_candidates(outer_zip, entry))
    return candidates


def write_sidecar(
    sidecar_path: Path,
    archive: Path,
    output_path: Path,
    group_label: str,
    result: GroupResult,
) -> None:
    text = "\n".join(
        [
            "NE 630 normalized homework solution artifact",
            f"student_group: {group_label}",
            f"source_archive: {archive}",
            f"normalized_file: {output_path}",
            f"route_guess: {result.route_guess}",
            f"selection_rule: {result.rule}",
            f"confidence: {result.confidence}",
            f"source_entry: {result.source_entry}",
            f"nested_archive: {result.nested_archive}",
            f"internal_path: {result.internal_path}",
            f"original_name: {result.original_name}",
            f"sha256: {result.sha256}",
            f"size_bytes: {result.size_bytes}",
            "",
        ]
    )
    sidecar_path.write_text(text, encoding="utf-8")


def write_csv(path: Path, rows: list[GroupResult], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: getattr(row, field) for field in fieldnames})


def classify_content(content: bytes) -> tuple[bool, str]:
    header = content[:1024]
    if b"%PDF-" in header:
        return True, "pdf"
    if content.startswith(b"\xff\xd8\xff"):
        return False, "jpeg"
    if content.startswith(b"PK\x03\x04"):
        return False, "zip"
    if len(content) == 0:
        return False, "empty"
    return False, content[:8].hex()


def clean_generated_outputs(solutions_dir: Path) -> None:
    for pattern in ("*_solution.pdf", "*_solution.source.txt"):
        for path in solutions_dir.glob(pattern):
            if path.is_file():
                path.unlink()


def safe_extract_zip_bytes(data: bytes, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    destination_resolved = destination.resolve()
    with ZipFile(io.BytesIO(data)) as nested_zip:
        for info in nested_zip.infolist():
            if info.is_dir() or "__MACOSX/" in info.filename:
                continue
            parts = [part for part in Path(info.filename).parts if part not in {"", "."}]
            if not parts or any(part == ".." for part in parts):
                raise ValueError(f"unsafe archive path: {info.filename}")
            target = destination.joinpath(*parts).resolve()
            if destination_resolved not in {target, *target.parents}:
                raise ValueError(f"unsafe archive path: {info.filename}")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(nested_zip.read(info))


def choose_tex_target(source_dir: Path) -> tuple[Path | None, int, str]:
    best_path: Path | None = None
    best_score = -10_000
    best_rule = ""
    for tex_path in source_dir.rglob("*.tex"):
        rel = tex_path.relative_to(source_dir).as_posix()
        try:
            content = tex_path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        score, rule = score_tex_name(rel, content)
        if score > best_score:
            best_path = tex_path
            best_score = score
            best_rule = rule
    if best_score < 0:
        return None, best_score, best_rule
    return best_path, best_score, best_rule


def maybe_write_solution_wrapper(source_dir: Path) -> Path | None:
    """Create a solution-only wrapper when main.tex also inputs discourse files."""
    main_tex = source_dir / "main.tex"
    if not main_tex.exists():
        return None
    content = main_tex.read_text(encoding="utf-8", errors="replace")
    if "\\begin{document}" not in content or "\\end{document}" not in content:
        return None
    preamble, remainder = content.split("\\begin{document}", 1)
    body, _end = remainder.split("\\end{document}", 1)
    kept_lines: list[str] = []
    dropped_discourse_like = False
    for line in body.splitlines():
        lowered = line.lower()
        if "\\input" not in lowered and "\\include" not in lowered:
            continue
        if any(term in lowered for term in ("transcript", "discourse", "dialogue", "chat")):
            dropped_discourse_like = True
            continue
        kept_lines.append(line)
    if not kept_lines or not dropped_discourse_like:
        return None
    wrapper = source_dir / "__collector_solution_wrapper.tex"
    wrapper.write_text(
        "\n".join(
            [
                "% Auto-generated by collect_solutions.py.",
                "% Builds the submitted solution input without discourse/transcript inputs.",
                preamble.rstrip(),
                "\\begin{document}",
                *kept_lines,
                "\\end{document}",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return wrapper


def tex_engine_for(target: Path) -> str | None:
    content = target.read_text(encoding="utf-8", errors="replace")[:5000].lower()
    if "xelatex" in content or "\\usepackage{fontspec}" in content:
        return shutil.which("xelatex")
    return shutil.which("pdflatex")


def build_tex_pdf(source_dir: Path, target: Path, build_log: Path) -> tuple[bytes | None, str]:
    engine = tex_engine_for(target)
    if engine is None:
        return None, "no usable TeX engine found"
    target_rel = target.relative_to(source_dir).as_posix()
    command = [
        engine,
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        "-no-shell-escape",
        target_rel,
    ]
    log_parts: list[str] = []
    for run_number in (1, 2):
        completed = subprocess.run(
            command,
            cwd=source_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=120,
            check=False,
        )
        log_parts.append(f"===== pass {run_number}: {' '.join(command)} =====\n")
        log_parts.append(completed.stdout)
        log_parts.append("\n")
        if completed.returncode != 0:
            build_log.write_text("".join(log_parts), encoding="utf-8", errors="replace")
            return None, f"TeX build failed on pass {run_number}; see {build_log}"

    build_log.write_text("".join(log_parts), encoding="utf-8", errors="replace")
    pdf_path = target.with_suffix(".pdf")
    if not pdf_path.exists():
        return None, f"TeX build did not produce {pdf_path.name}; see {build_log}"
    pdf_content = pdf_path.read_bytes()
    is_pdf, signature = classify_content(pdf_content)
    if not is_pdf:
        return None, f"TeX output is not a valid PDF by header ({signature}); see {build_log}"
    return pdf_content, f"built PDF from {target_rel}; build log: {build_log}"


def attempt_tex_builds(
    outer_zip: ZipFile,
    entries: list[OuterEntry],
    work_dir: Path,
    group_label: str,
) -> tuple[list[Candidate], list[str]]:
    candidates: list[Candidate] = []
    notes: list[str] = []
    for entry in entries:
        if entry.extension != "zip":
            continue
        nested_label = sanitize_stem(Path(entry.basename).stem)
        build_root = work_dir / "builds" / group_label / nested_label
        source_dir = build_root / "source"
        build_log = build_root / "build.log"
        if build_root.exists():
            shutil.rmtree(build_root)
        try:
            safe_extract_zip_bytes(outer_zip.read(entry.zip_path), source_dir)
            maybe_write_solution_wrapper(source_dir)
            target, tex_score, tex_rule = choose_tex_target(source_dir)
            if target is None:
                notes.append(f"{entry.basename}: no plausible final-solution TeX target")
                continue
            pdf_content, build_note = build_tex_pdf(source_dir, target, build_log)
            if pdf_content is None:
                notes.append(f"{entry.basename}: {build_note}")
                continue
            target_rel = target.relative_to(source_dir).as_posix()
            candidates.append(
                Candidate(
                    source_kind="built_tex_pdf",
                    source_entry=entry.zip_path,
                    original_name=entry.original_name,
                    nested_archive=entry.basename,
                    internal_path=target_rel,
                    display_name=Path(target_rel).name,
                    score=tex_score,
                    rule=f"{build_note}; {tex_rule}",
                    is_pdf=True,
                    signature="built_pdf_from_tex",
                    content=pdf_content,
                )
            )
        except (BadZipFile, OSError, subprocess.TimeoutExpired, ValueError) as exc:
            notes.append(f"{entry.basename}: source build error: {exc}")
    return candidates, notes


def collect(
    archive: Path,
    homework_dir: Path,
    solutions_dir: Path,
    reports_dir: Path,
    work_dir: Path,
    overwrite: bool,
    clean_output: bool,
) -> int:
    archive = archive.resolve()
    homework_dir = homework_dir.resolve()
    solutions_dir = solutions_dir.resolve()
    reports_dir = reports_dir.resolve()
    work_dir = work_dir.resolve()
    solutions_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)
    work_dir.mkdir(parents=True, exist_ok=True)
    if clean_output:
        clean_generated_outputs(solutions_dir)

    with ZipFile(archive) as outer_zip:
        entries = [
            parsed
            for info in outer_zip.infolist()
            if not info.is_dir()
            for parsed in [parse_outer_entry(info.filename)]
            if parsed is not None
        ]
        groups: dict[tuple[str, str], list[OuterEntry]] = {}
        for entry in entries:
            groups.setdefault((entry.slug, entry.user_id), []).append(entry)

        results: list[GroupResult] = []
        for (slug, user_id), group_entries in sorted(groups.items()):
            group_label = f"{sanitize_stem(slug)}_{user_id}"
            candidates = iter_group_candidates(outer_zip, group_entries)
            selected, reason, confidence = choose_candidate(candidates)
            build_notes: list[str] = []
            if selected is None and any(entry.extension == "zip" for entry in group_entries):
                build_candidates, build_notes = attempt_tex_builds(
                    outer_zip, group_entries, work_dir, group_label
                )
                candidates.extend(build_candidates)
                selected, reason, confidence = choose_candidate(candidates)
            route = route_guess(group_entries, selected)
            candidate_summary = " | ".join(summarize_candidate(c) for c in candidates)
            if build_notes:
                build_summary = " | ".join(f"BUILD_NOTE: {note}" for note in build_notes)
                candidate_summary = (
                    f"{candidate_summary} | {build_summary}"
                    if candidate_summary
                    else build_summary
                )

            if selected is None:
                results.append(
                    GroupResult(
                        slug=slug,
                        user_id=user_id,
                        status="needs_review",
                        route_guess=route,
                        output_file="",
                        source_entry="",
                        nested_archive="",
                        internal_path="",
                        original_name="",
                        rule="",
                        confidence=confidence,
                        sha256="",
                        size_bytes="",
                        candidate_count=len(candidates),
                        review_reason=reason,
                        candidates=candidate_summary,
                    )
                )
                continue

            output_name = f"{group_label}_solution.pdf"
            output_path = solutions_dir / output_name
            if output_path.exists() and not overwrite:
                raise FileExistsError(f"{output_path} exists; rerun with --overwrite")
            output_path.write_bytes(selected.content)
            digest = hashlib.sha256(selected.content).hexdigest()

            result = GroupResult(
                slug=slug,
                user_id=user_id,
                status="copied",
                route_guess=route,
                output_file=str(output_path),
                source_entry=selected.source_entry,
                nested_archive=selected.nested_archive,
                internal_path=selected.internal_path,
                original_name=selected.original_name,
                rule=reason,
                confidence=confidence,
                sha256=digest,
                size_bytes=str(selected.size_bytes),
                candidate_count=len(candidates),
                review_reason="",
                candidates=candidate_summary,
            )
            sidecar_path = output_path.with_suffix(".source.txt")
            write_sidecar(sidecar_path, archive, output_path, group_label, result)
            results.append(result)

    manifest_fields = [
        "slug",
        "user_id",
        "status",
        "route_guess",
        "output_file",
        "source_entry",
        "nested_archive",
        "internal_path",
        "original_name",
        "rule",
        "confidence",
        "sha256",
        "size_bytes",
        "candidate_count",
        "review_reason",
        "candidates",
    ]
    review_fields = [
        "slug",
        "user_id",
        "route_guess",
        "candidate_count",
        "review_reason",
        "candidates",
    ]
    write_csv(reports_dir / "solution_manifest.csv", results, manifest_fields)
    write_csv(
        reports_dir / "needs_review.csv",
        [row for row in results if row.status == "needs_review"],
        review_fields,
    )

    copied = sum(row.status == "copied" for row in results)
    review = sum(row.status == "needs_review" for row in results)
    print(f"archive: {archive}")
    print(f"homework_dir: {homework_dir}")
    print(f"solutions_dir: {solutions_dir}")
    print(f"reports_dir: {reports_dir}")
    print(f"work_dir: {work_dir}")
    print(f"student_groups: {len(results)}")
    print(f"copied: {copied}")
    print(f"needs_review: {review}")
    return 1 if review else 0


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    archive = args.archive
    homework_dir = infer_homework_dir(archive, args.homework_dir)
    solutions_dir = args.solutions_dir or homework_dir / "solutions"
    reports_dir = args.reports_dir or homework_dir / "reports"
    work_dir = args.work_dir or homework_dir / "work"
    try:
        return collect(
            archive,
            homework_dir,
            solutions_dir,
            reports_dir,
            work_dir,
            args.overwrite,
            args.clean_output,
        )
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    except BadZipFile as exc:
        print(f"error: not a readable ZIP archive: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
