#!/usr/bin/env python3
"""Match HW01 submissions to the NE 630 solution table."""

from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(os.environ.get("NE630_GRADING_ROOT", "/home/robertsj/Classes/ne630_local_grading")).expanduser()
NE630_ROOT = Path(os.environ.get("NE630_REPO_ROOT", "/home/robertsj/Classes/ne630")).expanduser()
TRANSCRIPTION_ROOT = Path(
    os.environ.get(
        "NE630_HW01_TRANSCRIPTION_ROOT",
        "/mnt/c/Users/Jeremy/Downloads/hw1_handwritten_scan_candidates_20260927",
    )
).expanduser()
HW_DIR = ROOT / "hw01"
TABLE_DIR = HW_DIR / "tables"
ARTIFACT_DIR = HW_DIR / "table_artifacts"
TRANSCRIPTION_ARTIFACT_DIR = ARTIFACT_DIR / "transcriptions"
PDF_TEXT_ARTIFACT_DIR = ARTIFACT_DIR / "pdf_text"

SCHEMA_VERSION = "ne630.solution_table.v0.1"
COURSE = "NE 630"
TERM = "Fall 2026"
HOMEWORK_ID = "hw01"
STATEMENT_PATH = str(NE630_ROOT / "homework/markdown/HW01.md")
SOLUTION_PATH = str(NE630_ROOT / "homework/solutions/hw01.tex")


EXPECTED = {
    ("p01", "a", "q_value"): {"value": -6.885, "unit": "MeV", "tol_abs": 0.02},
    ("p01", "b", "q_value"): {"value": 2.823, "unit": "MeV", "tol_abs": 0.02},
    ("p01", "c", "q_value"): {"value": 17.346, "unit": "MeV", "tol_abs": 0.03},
    ("p01", "d", "q_value"): {"value": 4.062, "unit": "MeV", "tol_abs": 0.02},
    ("p02", "", "percent_error"): {
        "value": -0.3184,
        "unit": "percent",
        "tol_abs": 0.05,
    },
    ("p03", "a", "mass_fraction"): {
        "value": 9.1e-4,
        "unit": "fraction",
        "tol_rel": 0.20,
    },
    ("p03", "b", "mass_fraction"): {
        "value": 9.76e-11,
        "unit": "fraction",
        "tol_rel": 0.20,
    },
}

EXPECTED_SHORT = {
    ("p03", "c", "sanity_check_claim"): {
        "text": (
            "The rough nuclear and coal fuel-use estimates are consistent at "
            "order-unity level when efficiency, enrichment, and fuel-composition "
            "assumptions are stated."
        ),
        "claims": [
            "nuclear estimate is checked against annual energy production",
            "coal estimate is checked against daily energy production",
            "assumptions about efficiency and composition are stated",
        ],
    }
}


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def read_manifest() -> dict[str, dict[str, str]]:
    manifest = HW_DIR / "reports/solution_manifest.csv"
    with manifest.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    return {f"{row['slug']}_{row['user_id']}": row for row in rows}


def student_group_from_candidate(filename: str) -> str | None:
    match = re.match(r"^\d+__([^_]+_\d+)_", filename)
    if not match:
        return None
    return match.group(1)


def candidate_id(filename: str) -> str:
    return filename.split("__", 1)[0]


def normalized_transcription_name(student_group: str) -> str:
    return f"{student_group}_transcription.md"


def select_transcriptions(index_rows: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in index_rows:
        group = student_group_from_candidate(row["pdf"])
        row["student_group"] = group or ""
        if group:
            grouped.setdefault(group, []).append(row)

    selected: list[dict[str, str]] = []
    report_rows: list[dict[str, str]] = []
    for group, rows in sorted(grouped.items()):
        selected_row = sorted(
            rows,
            key=lambda row: (
                "source" in row["pdf"].lower(),
                "solution_source" in row["pdf"].lower(),
                int(candidate_id(row["pdf"])),
            ),
        )[0]
        for row in rows:
            is_selected = row is selected_row
            reason = "selected"
            if not is_selected:
                reason = "duplicate_or_source_pdf_for_same_student_group"
            report_rows.append(
                {
                    "student_group": group,
                    "candidate_pdf": row["pdf"],
                    "transcription": row["transcription"],
                    "selected_for_table": "yes" if is_selected else "no",
                    "selection_reason": reason,
                    "problem1": row.get("problem1", ""),
                    "problem2": row.get("problem2", ""),
                    "problem3": row.get("problem3", ""),
                    "uncertain_markers": row.get("uncertain_markers", ""),
                    "illegible_markers": row.get("illegible_markers", ""),
                    "not_present_markers": row.get("not_present_markers", ""),
                    "unassigned_section": row.get("unassigned_section", ""),
                }
            )
        selected.append(selected_row)
    return selected, report_rows


def section(text: str, problem_number: int) -> str:
    pattern = re.compile(rf"^## Problem {problem_number}\s*$", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        return ""
    next_match = re.search(r"^## Problem \d+\s*$", text[match.end() :], re.MULTILINE)
    end = match.end() + next_match.start() if next_match else len(text)
    return text[match.end() : end].strip()


def problem_section_text(text: str, problem_number: int) -> str:
    markdown = section(text, problem_number)
    if markdown:
        return markdown

    def markers(number: int) -> list[re.Match[str]]:
        found = []
        pattern = re.compile(
            rf"(?im)^.*(?:\b{number}\s+Question\s+{number}\b|(?:Question|Problem)\s+{number}\b).*$"
        )
        for match in pattern.finditer(text):
            line = match.group(0)
            lowered = line.lower()
            if "homework" in lowered and ":" not in line:
                continue
            found.append(match)
        return found

    starts = markers(problem_number)
    if not starts:
        if problem_number in {1, 2}:
            later = markers(3)
            if later:
                return text[: later[-1].start()].strip()
        return ""
    start_match = starts[-1]
    next_markers = [match for match in markers(problem_number + 1) if match.start() > start_match.end()]
    end = next_markers[0].start() if next_markers else len(text)
    return text[start_match.end() : end].strip()


def strip_notes(problem_text: str) -> str:
    return problem_text.split("### Notes", 1)[0].strip()


def balanced_boxed_contents(text: str) -> list[str]:
    results: list[str] = []
    needle = r"\boxed{"
    start = 0
    while True:
        index = text.find(needle, start)
        if index == -1:
            return results
        i = index + len(needle)
        depth = 1
        while i < len(text) and depth:
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
            i += 1
        if depth == 0:
            results.append(text[index + len(needle) : i - 1])
            start = i
        else:
            start = index + len(needle)


NUMBER = r"[-+]?(?:\d*\.\d+|\d+(?:,\d{3})*|\d+)(?:\s*(?:\\times|\\cdot|×|x)\s*10(?:\^\{?[-+]?\d+\}?|[-+]\d+|\d+)|[eE]\{?[-+]?\d+\}?)?"


def normalize_number(raw: str) -> float | None:
    raw = raw.strip().replace(",", "")
    raw = raw.replace("−", "-")
    raw = raw.replace(r"\,", "")
    sci = re.search(
        r"([-+]?(?:\d*\.\d+|\d+))\s*(?:\\times|\\cdot|×|x)\s*10(?:\^\{?([-+]?\d+)\}?|([-+]\d+)|(\d+))",
        raw,
    )
    if sci:
        exponent = sci.group(2) or sci.group(3) or sci.group(4)
        return float(sci.group(1)) * (10 ** int(exponent))
    e_notation = re.search(r"([-+]?(?:\d*\.\d+|\d+))[eE]\{?([-+]?\d+)\}?", raw)
    if e_notation:
        return float(e_notation.group(1)) * (10 ** int(e_notation.group(2)))
    try:
        return float(raw)
    except ValueError:
        return None


def display_text(raw: str) -> str:
    return re.sub(r"\s+", " ", raw).strip()


def normalize_pdf_text(text: str) -> str:
    text = text.replace("−", "-")
    text = text.replace("M eV", "MeV")
    text = text.replace("m eV", "meV")
    return text


def latex_group(text: str, start: int) -> tuple[str, int] | None:
    if start >= len(text) or text[start] != "{":
        return None
    depth = 1
    i = start + 1
    while i < len(text) and depth:
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
        i += 1
    if depth:
        return None
    return text[start + 1 : i - 1], i


def numeric_expression_value(text: str) -> float | None:
    text = text.strip()
    if not text:
        return None
    text = text.replace("−", "-")
    sci = re.search(
        r"([-+]?(?:\d*\.\d+|\d+(?:,\d{3})*|\d+))\s*(?:\\times|\\cdot|×|x)\s*10(?:\^\{?([-+]?\d+)\}?|([-+]\d+)|(\d+))",
        text,
    )
    if sci:
        return normalize_number(sci.group(0))
    e_notation = re.search(r"([-+]?(?:\d*\.\d+|\d+(?:,\d{3})*|\d+))[eE]\{?([-+]?\d+)\}?", text)
    if e_notation:
        return normalize_number(e_notation.group(0))
    plain = re.search(r"[-+]?(?:\d*\.\d+|\d+(?:,\d{3})*|\d+)", text)
    if plain:
        return normalize_number(plain.group(0))
    return None


def latex_fraction_candidates(text: str) -> list[tuple[float, str]]:
    candidates: list[tuple[float, str]] = []
    start = 0
    while True:
        index = text.find(r"\frac", start)
        if index == -1:
            return candidates
        numerator_start = text.find("{", index + len(r"\frac"))
        if numerator_start == -1:
            start = index + len(r"\frac")
            continue
        numerator_group = latex_group(text, numerator_start)
        if numerator_group is None:
            start = numerator_start + 1
            continue
        numerator, denominator_start = numerator_group
        denominator_group = latex_group(text, denominator_start)
        if denominator_group is None:
            start = denominator_start
            continue
        denominator, end = denominator_group
        numerator_value = numeric_expression_value(numerator)
        denominator_value = numeric_expression_value(denominator)
        if numerator_value is not None and denominator_value not in {None, 0.0}:
            candidates.append((numerator_value / denominator_value, text[index:end]))
        start = end


def fraction_value_from_text(text: str) -> tuple[float, str, bool] | None:
    review = marker_needs_review(text)
    fraction_candidates = latex_fraction_candidates(text)
    if fraction_candidates:
        value, display = fraction_candidates[-1]
        return value, display_text(display), review

    search_text = text.rsplit("=", 1)[-1] if "=" in text else text
    number_matches = list(re.finditer(NUMBER, search_text))
    for match in reversed(number_matches):
        value = normalize_number(match.group(0))
        if value is None:
            continue
        display = display_text(match.group(0))
        unit_window = search_text[match.end() : match.end() + 12]
        if "%" in unit_window or r"\%" in unit_window:
            value = value / 100.0
            percent_match = re.search(r"(?:\\%|%)", unit_window)
            if percent_match:
                display = display_text(search_text[match.start() : match.end() + percent_match.end()])
        return value, display, review
    return None


def labeled_answer_blocks(text: str) -> list[str]:
    """Return display-math blocks immediately following handwritten answer labels."""
    blocks: list[str] = []
    label = r"(?:Boxed|Red box|Box)"
    for match in re.finditer(
        rf"(?is){label}:\s*(?:\$\$(.*?)\$\$|\\\[(.*?)\\\])",
        text,
    ):
        block = match.group(1) or match.group(2) or ""
        if block.strip():
            blocks.append(block.strip())
    return blocks


def answer_blocks(text: str) -> list[str]:
    return balanced_boxed_contents(text) + labeled_answer_blocks(text)


def numeric_from_box(box: str, desired_unit: str | None = None) -> tuple[float, str] | None:
    plain = display_text(box)
    pairs: list[tuple[float, str, str]] = []
    for match in re.finditer(rf"({NUMBER})\s*(?:\\,|\\\s*|\s)*(?:\\mathrm\{{)?([A-Za-z%]+)(?:\}})?", box):
        value = normalize_number(match.group(1))
        if value is None:
            continue
        unit = match.group(2)
        pairs.append((value, unit, match.group(0)))
    if desired_unit:
        for value, unit, raw in reversed(pairs):
            if unit.lower() == desired_unit.lower():
                return value, plain
    if pairs:
        value, unit, raw = pairs[-1]
        return value, plain
    numbers = [normalize_number(match.group(0)) for match in re.finditer(NUMBER, box)]
    numbers = [value for value in numbers if value is not None]
    if numbers:
        return numbers[-1], plain
    return None


def extract_p1_q_values(p1: str) -> list[tuple[float, str, bool]]:
    work = strip_notes(p1)
    values: list[tuple[float, str, bool]] = []
    for box in answer_blocks(work):
        if "Q" not in box and "MeV" not in box and "keV" not in box:
            continue
        parsed = numeric_from_box(box, "MeV")
        if parsed is None:
            parsed = numeric_from_box(box, "keV")
            if parsed is not None:
                parsed = (parsed[0] / 1000.0, parsed[1])
        if parsed is not None:
            values.append((parsed[0], parsed[1], marker_needs_review(box)))

    if len(values) < 4:
        keyed: dict[str, tuple[float, str, bool]] = {}
        for match in re.finditer(
            rf"(?ims)\b([abcd])\)\s*(?:&\s*)?(?:Q\s*=\s*)?({NUMBER})\s*(?:\\,|\\\s*|\s)*(?:\\mathrm\{{)?MeV(?:\}})?",
            work,
        ):
            value = normalize_number(match.group(2))
            if value is None:
                continue
            keyed.setdefault(
                match.group(1).lower(),
                (value, display_text(match.group(0)), marker_needs_review(match.group(0))),
            )
        if keyed:
            table_values = [keyed[key] for key in ["a", "b", "c", "d"] if key in keyed]
            if len(table_values) > len(values):
                values = table_values
    if len(values) < 4:
        section_values: list[tuple[float, str, bool]] = []
        for part in ["a", "b", "c", "d"]:
            part_text = split_part(work, part)
            matches = list(
                re.finditer(
                    rf"({NUMBER})\s*(?:\\,|\\\s*|\s)*(?:\\mathrm\{{)?MeV(?:\}})?",
                    part_text,
                )
            )
            if not matches:
                continue
            match = matches[-1]
            value = normalize_number(match.group(1))
            if value is None:
                continue
            section_values.append(
                (
                    value,
                    display_text(match.group(0)),
                    marker_needs_review(part_text[max(0, match.start() - 80) : match.end() + 80]),
                )
            )
        if len(section_values) > len(values):
            values = section_values
    return values[:4]


def extract_p2_percent_error(p2: str) -> tuple[float, str, bool] | None:
    work = strip_notes(p2)
    boxes = balanced_boxed_contents(work)
    for box in reversed(boxes):
        if "%" in box or "err" in box.lower() or "error" in box.lower():
            parsed = numeric_from_box(box, "%")
            if parsed is not None:
                return parsed[0], parsed[1], marker_needs_review(box)
    matches = list(re.finditer(rf"({NUMBER})\s*\\?%", work))
    if matches:
        value = normalize_number(matches[-1].group(1))
        if value is not None:
            return value, display_text(matches[-1].group(0)), False
    if "error" in work.lower() or "err" in work.lower():
        for box in reversed(answer_blocks(work)):
            parsed = numeric_from_box(box)
            if parsed is None:
                continue
            value, display = parsed
            if abs(value) <= 100:
                return value, display, marker_needs_review(box)
    return None


def split_part(text: str, part: str) -> str:
    marker_pattern = re.compile(
        rf"(?im)^\s*(?:P\d+\)\s*)?(?:\(?{re.escape(part)}\)|{re.escape(part)}[.)])(?:\s+.*)?$"
    )
    markers = list(marker_pattern.finditer(text))
    if not markers:
        marker_pattern = re.compile(
            rf"(?im)^\s*(?:P\d+\)\s*)?(?:\(?{re.escape(part)}\)|{re.escape(part)}[.)])"
        )
        markers = list(marker_pattern.finditer(text))
    if not markers:
        return ""
    marker = markers[-1]
    next_marker = re.search(r"(?im)^\s*(?:\(?[abcd]\)|[abcd][.)])(?:\s+.*)?$", text[marker.end() :])
    end = marker.end() + next_marker.start() if next_marker else len(text)
    return text[marker.end() : end].strip()


def extract_fraction(part_text: str) -> tuple[float, str, bool] | None:
    boxes = answer_blocks(part_text)
    for box in reversed(boxes):
        parsed = fraction_value_from_text(box)
        if parsed is None:
            continue
        value, display, local_review = parsed
        if not (0.0 < abs(value) < 1.0):
            continue
        return value, display, local_review
    return None


def pdf_part_text(text: str, part: str) -> str:
    marker_pattern = re.compile(
        rf"(?im)^\s*(?:Part\s*)?\(?{re.escape(part)}\)(?:\s*[:.)-].*|\s+.*)?$"
    )
    markers = list(marker_pattern.finditer(text))
    if not markers:
        return ""
    marker = markers[-1]
    next_marker = re.search(r"(?im)^\s*(?:Part\s*)?\(?[abc]\)(?:\s*[:.)-].*|\s+.*)?$", text[marker.end() :])
    end = marker.end() + next_marker.start() if next_marker else len(text)
    return text[marker.end() : end].strip()


def nearby_text(text: str, start: int, end: int, radius: int = 240) -> str:
    return display_text(text[max(0, start - radius) : min(len(text), end + radius)])


def extract_mev_values(text: str) -> list[tuple[float, str, int, int]]:
    values: list[tuple[float, str, int, int]] = []
    for match in re.finditer(rf"({NUMBER})\s*(?:M\s*eV|MeV)", normalize_pdf_text(text)):
        value = normalize_number(match.group(1))
        if value is None:
            continue
        if abs(value) >= 100:
            continue
        values.append((value, display_text(match.group(0)), match.start(), match.end()))
    return values


def extract_pdf_p1_q_values(text: str) -> list[tuple[float, str, str]]:
    p1 = problem_section_text(normalize_pdf_text(text), 1)
    line_values: list[tuple[float, str, int, int]] = []
    offset = 0
    for line in p1.splitlines(keepends=True):
        if "Q" in line and ("MeV" in line or "M eV" in line):
            for value, display, start, end in extract_mev_values(line):
                line_values.append((value, display, offset + start, offset + end))
        offset += len(line)
    values = line_values if len(line_values) >= 4 else extract_mev_values(p1)
    if len(values) > 4:
        values = values[-4:]
    return [(value, display, nearby_text(p1, start, end)) for value, display, start, end in values[:4]]


def extract_pdf_p2_percent_error(text: str) -> tuple[float, str, str] | None:
    p2 = problem_section_text(normalize_pdf_text(text), 2)
    matches = []
    for match in re.finditer(rf"({NUMBER})\s*%", p2):
        value = normalize_number(match.group(1))
        if value is None or abs(value) > 20:
            continue
        matches.append((value, display_text(match.group(0)), match.start(), match.end()))
    if not matches:
        return None
    negative_matches = [match for match in matches if match[0] < 0]
    value, display, start, end = (negative_matches[-1] if negative_matches else matches[-1])
    return value, display, nearby_text(p2, start, end)


def extract_pdf_fraction(part_text: str) -> tuple[float, str, str] | None:
    text = normalize_pdf_text(part_text)
    matches = []
    for match in re.finditer(NUMBER, text):
        value = normalize_number(match.group(0))
        if value is None:
            continue
        display = display_text(match.group(0))
        unit_window = text[match.end() : match.end() + 8]
        if "%" in unit_window:
            value = value / 100.0
            display = display_text(text[match.start() : match.end() + unit_window.index("%") + 1])
        if 0 < abs(value) < 1:
            matches.append((value, display, match.start(), match.end()))
    if not matches:
        return None
    value, display, start, end = matches[-1]
    return value, display, nearby_text(text, start, end)


def extract_pdf_p3_fractions(text: str) -> dict[str, tuple[float, str, str]]:
    p3 = problem_section_text(text, 3)
    candidates: list[tuple[float, str, int, int]] = []
    normalized = normalize_pdf_text(p3)
    for match in re.finditer(NUMBER, normalized):
        value = normalize_number(match.group(0))
        if value is None:
            continue
        display = display_text(match.group(0))
        unit_window = normalized[match.end() : match.end() + 8]
        if "%" in unit_window:
            value = value / 100.0
            display = display_text(normalized[match.start() : match.end() + unit_window.index("%") + 1])
        if 0 < abs(value) < 1:
            candidates.append((value, display, match.start(), match.end()))

    results: dict[str, tuple[float, str, str]] = {}
    for value, display, start, end in candidates:
        magnitude = abs(value)
        if "a" not in results and 1e-5 <= magnitude <= 1e-2:
            results["a"] = (value, display, nearby_text(normalized, start, end))
        if "b" not in results and 1e-13 <= magnitude <= 1e-8:
            results["b"] = (value, display, nearby_text(normalized, start, end))
    return results


def pdftotext_artifact(manifest_row: dict[str, str], student_group: str) -> Path | None:
    source_pdf = Path(manifest_row["output_file"])
    if not source_pdf.exists():
        return None
    PDF_TEXT_ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    output = PDF_TEXT_ARTIFACT_DIR / f"{student_group}_pdftotext.txt"
    result = subprocess.run(
        ["pdftotext", "-layout", str(source_pdf), "-"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    output.write_text(result.stdout, encoding="utf-8")
    return output


def extract_pdf_rows_for_student(
    student_group: str,
    manifest_row: dict[str, str],
    extracted_at: str,
) -> tuple[list[dict], list[dict]]:
    rows: list[dict] = []
    errors: list[dict] = []
    local_path = pdftotext_artifact(manifest_row, student_group)
    if local_path is None:
        return rows, [{"student_group": student_group, "answer": "*", "reason": "pdftotext failed or normalized PDF missing"}]
    text = local_path.read_text(encoding="utf-8", errors="replace")
    part_labels = ["a", "b", "c", "d"]

    p1_values = extract_pdf_p1_q_values(text)
    for index, (value, display, evidence) in enumerate(p1_values):
        rows.append(
            student_numeric_row(
                manifest_row,
                student_group,
                local_path,
                extracted_at,
                "p01",
                part_labels[index],
                "q_value",
                value,
                display,
                evidence,
                False,
                0.90,
                "regex_from_pdf_text",
                "pdf text fallback extraction",
            )
        )
    for missing_index in range(len(p1_values), 4):
        errors.append(
            {
                "student_group": student_group,
                "answer": f"p01.{part_labels[missing_index]}.q_value",
                "reason": "not extracted from PDF text",
            }
        )

    p2_value = extract_pdf_p2_percent_error(text)
    if p2_value:
        value, display, evidence = p2_value
        rows.append(
            student_numeric_row(
                manifest_row,
                student_group,
                local_path,
                extracted_at,
                "p02",
                "",
                "percent_error",
                value,
                display,
                evidence,
                False,
                0.88,
                "regex_from_pdf_text",
                "pdf text fallback extraction",
            )
        )
    else:
        errors.append({"student_group": student_group, "answer": "p02.percent_error", "reason": "not extracted from PDF text"})

    p3 = problem_section_text(text, 3)
    p3_fractions = extract_pdf_p3_fractions(text)
    for part in ["a", "b"]:
        extracted = p3_fractions.get(part) or extract_pdf_fraction(pdf_part_text(p3, part))
        if extracted:
            value, display, evidence = extracted
            rows.append(
                student_numeric_row(
                    manifest_row,
                    student_group,
                    local_path,
                    extracted_at,
                    "p03",
                    part,
                    "mass_fraction",
                    value,
                    display,
                    evidence,
                    False,
                    0.86,
                    "regex_from_pdf_text",
                    "pdf text fallback extraction",
                )
            )
        else:
            errors.append({"student_group": student_group, "answer": f"p03.{part}.mass_fraction", "reason": "not extracted from PDF text"})

    part_c = pdf_part_text(p3, "c")
    if part_c:
        rows.append(
            student_short_row(
                manifest_row,
                student_group,
                local_path,
                extracted_at,
                part_c,
                False,
                "section_from_pdf_text",
                0.78,
            )
        )
    else:
        errors.append({"student_group": student_group, "answer": "p03.c.sanity_check_claim", "reason": "not present in PDF text"})

    return rows, errors


def extract_pdf_fallback_rows(
    manifest: dict[str, dict[str, str]],
    already_processed: set[str],
    extracted_at: str,
) -> tuple[list[dict], list[dict]]:
    rows: list[dict] = []
    errors: list[dict] = []
    for student_group, manifest_row in sorted(manifest.items()):
        if student_group in already_processed:
            continue
        student_rows, student_errors = extract_pdf_rows_for_student(student_group, manifest_row, extracted_at)
        rows.extend(student_rows)
        errors.extend(student_errors)
    return rows, errors


def marker_needs_review(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in ["[uncertain", "[illegible", "[not present]"])


def compare_numeric(value: float, expected: dict[str, float]) -> tuple[str, str]:
    expected_value = expected["value"]
    if "tol_abs" in expected:
        diff = abs(value - expected_value)
        if diff <= expected["tol_abs"]:
            return "match", f"abs diff {diff:.4g} <= {expected['tol_abs']}"
        return "mismatch", f"abs diff {diff:.4g} > {expected['tol_abs']}"
    tol_rel = expected.get("tol_rel", 0.05)
    denom = max(abs(expected_value), 1e-300)
    rel = abs(value - expected_value) / denom
    if rel <= tol_rel:
        return "match", f"rel diff {rel:.3g} <= {tol_rel}"
    return "mismatch", f"rel diff {rel:.3g} > {tol_rel}"


def prompt_for(problem_id: str, part_id: str = "") -> dict[str, str]:
    label = problem_id.replace("p", "Problem ")
    if part_id:
        label = f"{label}({part_id})"
    return {
        "statement_path": STATEMENT_PATH,
        "statement_locator": label,
    }


def reference_for(problem_id: str, part_id: str, answer_id: str) -> dict[str, str]:
    label = problem_id.replace("p", "Problem ")
    if part_id:
        label = f"{label}({part_id})"
    return {
        "solution_path": SOLUTION_PATH,
        "solution_locator": f"{label} {answer_id}",
        "expected_answer_id": f"{HOMEWORK_ID}.{problem_id}.{part_id + '.' if part_id else ''}{answer_id}",
    }


def expected_rows(extracted_at: str) -> list[dict]:
    rows: list[dict] = []
    evidence = {
        ("p01", "a", "q_value"): r"Q_1 \approx -6.885~\mega\electronvolt",
        ("p01", "b", "q_value"): r"Q_2 \approx 2.823~\mega\electronvolt",
        ("p01", "c", "q_value"): r"Q_3 \approx 17.346~\mega\electronvolt",
        ("p01", "d", "q_value"): r"Q_4 \approx 4.062~\mega\electronvolt",
        ("p02", "", "percent_error"): r"\%\text{err}=\boxed{-0.3184\%}",
        ("p03", "a", "mass_fraction"): r"\Delta m_0 / m_0 \approx 200/219834 \approx \boxed{0.00091}",
        ("p03", "b", "mass_fraction"): r"\Delta m_0/m_0 \approx \boxed{9.76\cdot10^{-11}}",
    }
    for (problem_id, part_id, answer_id), spec in EXPECTED.items():
        row = base_row(problem_id, part_id, answer_id, "expected", extracted_at)
        row["source"] = {"role": "expected", "path": SOLUTION_PATH, "locator": answer_id}
        row["answer_kind"] = "numerical"
        row["value"] = {
            "kind": "numerical",
            "value": spec["value"],
            "unit": spec["unit"],
            "display": f"{spec['value']} {spec['unit']}",
        }
        if "tol_abs" in spec:
            row["value"]["tolerance_abs"] = spec["tol_abs"]
        if "tol_rel" in spec:
            row["value"]["tolerance_rel"] = spec["tol_rel"]
        row["comparison"] = {"method": "numeric_tolerance", "status": "not_compared"}
        row["evidence"] = [{"kind": "latex", "text": evidence[(problem_id, part_id, answer_id)]}]
        row["extraction"] = {
            "method": "manual_seed_from_instructor_solution",
            "tool": "match_hw01_transcriptions.py",
            "extracted_at": extracted_at,
            "confidence": 1.0,
            "needs_review": False,
        }
        rows.append(row)

    for (problem_id, part_id, answer_id), spec in EXPECTED_SHORT.items():
        row = base_row(problem_id, part_id, answer_id, "expected", extracted_at)
        row["source"] = {"role": "expected", "path": SOLUTION_PATH, "locator": answer_id}
        row["answer_kind"] = "short_answer"
        row["value"] = {"kind": "short_answer", "text": spec["text"], "claims": spec["claims"]}
        row["comparison"] = {"method": "rubric", "status": "not_compared"}
        row["evidence"] = [
            {
                "kind": "text",
                "text": (
                    "That's within a factor of 2 of the first number, so ``sanity'' prevails. "
                    "Again, this is close, so we've passed the ``sanity'' check."
                ),
            }
        ]
        row["extraction"] = {
            "method": "manual_seed_from_instructor_solution",
            "tool": "match_hw01_transcriptions.py",
            "extracted_at": extracted_at,
            "confidence": 1.0,
            "needs_review": False,
        }
        rows.append(row)
    return rows


def base_row(problem_id: str, part_id: str, answer_id: str, role: str, extracted_at: str) -> dict:
    row = {
        "schema_version": SCHEMA_VERSION,
        "course": COURSE,
        "term": TERM,
        "homework_id": HOMEWORK_ID,
        "problem_id": problem_id,
        "answer_id": answer_id,
        "prompt": prompt_for(problem_id, part_id),
        "reference": reference_for(problem_id, part_id, answer_id),
    }
    if part_id:
        row["part_id"] = part_id
    return row


def student_source(manifest_row: dict[str, str], student_group: str, transcription_path: Path) -> dict[str, str]:
    source = {
        "role": "student",
        "student_group": student_group,
        "path": manifest_row["output_file"],
        "locator": str(transcription_path),
        "route_guess": manifest_row.get("route_guess", ""),
    }
    if manifest_row.get("sha256"):
        source["sha256"] = manifest_row["sha256"]
    return source


def student_numeric_row(
    manifest_row: dict[str, str],
    student_group: str,
    transcription_path: Path,
    extracted_at: str,
    problem_id: str,
    part_id: str,
    answer_id: str,
    value: float,
    display: str,
    evidence_text: str,
    needs_review: bool,
    confidence: float,
    extraction_method: str = "regex_from_handwritten_transcription",
    review_reason: str = "transcription marker or heuristic extraction",
) -> dict:
    spec = EXPECTED[(problem_id, part_id, answer_id)]
    status, notes = compare_numeric(value, spec)
    row = base_row(problem_id, part_id, answer_id, "student", extracted_at)
    row["source"] = student_source(manifest_row, student_group, transcription_path)
    row["answer_kind"] = "numerical"
    row["value"] = {
        "kind": "numerical",
        "value": value,
        "unit": spec["unit"],
        "display": display,
    }
    row["comparison"] = {
        "compare_to_answer_id": row["reference"]["expected_answer_id"],
        "method": "numeric_tolerance",
        "status": status,
        "notes": notes,
    }
    row["evidence"] = [
        {
            "kind": "text",
            "text": evidence_text[:1000],
            "path": str(transcription_path),
            "sha256": sha256_path(transcription_path),
        }
    ]
    row["extraction"] = {
        "method": extraction_method,
        "tool": "match_hw01_transcriptions.py",
        "extracted_at": extracted_at,
        "confidence": confidence,
        "needs_review": needs_review,
    }
    if needs_review:
        row["extraction"]["review_reason"] = review_reason
    return row


def student_short_row(
    manifest_row: dict[str, str],
    student_group: str,
    transcription_path: Path,
    extracted_at: str,
    text: str,
    needs_review: bool,
    extraction_method: str = "section_from_handwritten_transcription",
    confidence: float | None = None,
) -> dict:
    problem_id, part_id, answer_id = "p03", "c", "sanity_check_claim"
    row = base_row(problem_id, part_id, answer_id, "student", extracted_at)
    row["source"] = student_source(manifest_row, student_group, transcription_path)
    row["answer_kind"] = "short_answer"
    cleaned = display_text(text)
    row["value"] = {"kind": "short_answer", "text": cleaned[:3000]}
    row["comparison"] = {
        "compare_to_answer_id": row["reference"]["expected_answer_id"],
        "method": "rubric",
        "status": "manual_review",
        "notes": "Short-answer comparison intentionally deferred to rubric/manual review.",
    }
    row["evidence"] = [
        {
            "kind": "text",
            "text": cleaned[:1000],
            "path": str(transcription_path),
            "sha256": sha256_path(transcription_path),
        }
    ]
    row["extraction"] = {
        "method": extraction_method,
        "tool": "match_hw01_transcriptions.py",
        "extracted_at": extracted_at,
        "confidence": (0.72 if cleaned else 0.0) if confidence is None else confidence,
        "needs_review": True if needs_review or not cleaned else False,
    }
    if row["extraction"]["needs_review"]:
        row["extraction"]["review_reason"] = "short answer requires rubric review or was not clearly present"
    return row


def extract_student_rows(
    selected_rows: list[dict[str, str]],
    manifest: dict[str, dict[str, str]],
    extracted_at: str,
) -> tuple[list[dict], list[dict]]:
    rows: list[dict] = []
    errors: list[dict] = []
    TRANSCRIPTION_ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    part_labels = ["a", "b", "c", "d"]

    for item in selected_rows:
        student_group = item["student_group"]
        manifest_row = manifest.get(student_group)
        source_path = TRANSCRIPTION_ROOT / item["transcription"]
        local_path = TRANSCRIPTION_ARTIFACT_DIR / normalized_transcription_name(student_group)
        shutil.copy2(source_path, local_path)
        text = local_path.read_text(encoding="utf-8", errors="replace")

        if manifest_row is None:
            errors.append({"student_group": student_group, "answer": "*", "reason": "no matching solution_manifest row"})
            continue

        file_review = any(
            item.get(field, "0") not in {"", "0", "no"}
            for field in ["uncertain_markers", "illegible_markers"]
        )

        p1_values = extract_p1_q_values(section(text, 1))
        for index, (value, display, local_review) in enumerate(p1_values):
            part = part_labels[index]
            rows.append(
                student_numeric_row(
                    manifest_row,
                    student_group,
                    local_path,
                    extracted_at,
                    "p01",
                    part,
                    "q_value",
                    value,
                    display,
                    display,
                    file_review or local_review,
                    0.82 if not (file_review or local_review) else 0.65,
                )
            )
        for missing_index in range(len(p1_values), 4):
            errors.append(
                {
                    "student_group": student_group,
                    "answer": f"p01.{part_labels[missing_index]}.q_value",
                    "reason": "not extracted from transcription",
                }
            )

        p2_value = extract_p2_percent_error(section(text, 2))
        if p2_value:
            value, display, local_review = p2_value
            rows.append(
                student_numeric_row(
                    manifest_row,
                    student_group,
                    local_path,
                    extracted_at,
                    "p02",
                    "",
                    "percent_error",
                    value,
                    display,
                    display,
                    file_review or local_review,
                    0.80 if not (file_review or local_review) else 0.62,
                )
            )
        else:
            errors.append({"student_group": student_group, "answer": "p02.percent_error", "reason": "not extracted from transcription"})

        p3 = section(text, 3)
        for part in ["a", "b"]:
            extracted = extract_fraction(split_part(p3, part))
            if extracted:
                value, display, local_review = extracted
                rows.append(
                    student_numeric_row(
                        manifest_row,
                        student_group,
                        local_path,
                        extracted_at,
                        "p03",
                        part,
                        "mass_fraction",
                        value,
                        display,
                        display,
                        file_review or local_review,
                        0.78 if not (file_review or local_review) else 0.60,
                    )
                )
            else:
                errors.append({"student_group": student_group, "answer": f"p03.{part}.mass_fraction", "reason": "not extracted from transcription"})

        part_c = split_part(p3, "c")
        if part_c and "[not present]" not in part_c.lower():
            rows.append(
                student_short_row(
                    manifest_row,
                    student_group,
                    local_path,
                    extracted_at,
                    part_c,
                    file_review or marker_needs_review(part_c),
                )
            )
        else:
            errors.append({"student_group": student_group, "answer": "p03.c.sanity_check_claim", "reason": "not present in transcription"})

    return rows, errors


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def validate_rows(rows: list[dict]) -> None:
    from jsonschema import Draft202012Validator

    schema = json.loads((ROOT / "schema/solution_table.schema.json").read_text())
    validator = Draft202012Validator(schema)
    failures = []
    for index, row in enumerate(rows, 1):
        for error in validator.iter_errors(row):
            failures.append((index, error.json_path, error.message))
    if failures:
        for failure in failures[:20]:
            print(failure)
        raise SystemExit(f"{len(failures)} schema validation failures")


def write_match_report(path: Path, report_rows: list[dict[str, str]], manifest: dict[str, dict[str, str]]) -> None:
    fields = [
        "student_group",
        "candidate_pdf",
        "transcription",
        "matched_manifest",
        "normalized_solution_pdf",
        "route_guess",
        "selected_for_table",
        "selection_reason",
        "problem1",
        "problem2",
        "problem3",
        "uncertain_markers",
        "illegible_markers",
        "not_present_markers",
        "unassigned_section",
    ]
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for row in report_rows:
            manifest_row = manifest.get(row["student_group"])
            output = ""
            route = ""
            if manifest_row:
                output = manifest_row.get("output_file", "")
                route = manifest_row.get("route_guess", "")
            writer.writerow(
                {
                    **row,
                    "matched_manifest": "yes" if manifest_row else "no",
                    "normalized_solution_pdf": output,
                    "route_guess": route,
                }
            )


def write_errors(path: Path, errors: list[dict], extracted_at: str) -> None:
    with path.open("w", encoding="utf-8") as stream:
        for error in errors:
            stream.write(json.dumps({**error, "extracted_at": extracted_at}, sort_keys=True) + "\n")


def main() -> None:
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    extracted_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    index_rows = read_tsv(TRANSCRIPTION_ROOT / "HW01_TRANSCRIPTION_INDEX.tsv")
    selected_rows, match_report_rows = select_transcriptions(index_rows)
    manifest = read_manifest()

    rows = expected_rows(extracted_at)
    student_rows, errors = extract_student_rows(selected_rows, manifest, extracted_at)
    selected_groups = {row["student_group"] for row in selected_rows}
    pdf_rows, pdf_errors = extract_pdf_fallback_rows(manifest, selected_groups, extracted_at)
    rows.extend(student_rows)
    rows.extend(pdf_rows)
    errors.extend(pdf_errors)
    validate_rows(rows)

    table_path = TABLE_DIR / "solution_table.jsonl"
    errors_path = TABLE_DIR / "solution_table.errors.jsonl"
    report_path = HW_DIR / "reports/transcription_match_report.csv"
    summary_path = HW_DIR / "reports/solution_table_summary.json"
    write_jsonl(table_path, rows)
    write_errors(errors_path, errors, extracted_at)
    write_match_report(report_path, match_report_rows, manifest)

    summary = {
        "extracted_at": extracted_at,
        "table_path": str(table_path),
        "errors_path": str(errors_path),
        "match_report_path": str(report_path),
        "transcription_folder": str(TRANSCRIPTION_ROOT),
        "candidate_transcriptions": len(index_rows),
        "selected_transcriptions": len(selected_rows),
        "pdf_fallback_students": len(set(manifest) - selected_groups),
        "pdf_fallback_rows": len(pdf_rows),
        "rows": len(rows),
        "expected_rows": sum(1 for row in rows if row["source"]["role"] == "expected"),
        "student_rows": sum(1 for row in rows if row["source"]["role"] == "student"),
        "needs_review_rows": sum(1 for row in rows if row["extraction"].get("needs_review")),
        "errors": len(errors),
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
