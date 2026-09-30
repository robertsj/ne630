#!/usr/bin/env python3
"""Initialize the HW04 NE 630 solution table from typeset submissions.

Handwritten/scan submissions are intentionally deferred until OCR or
transcriptions are available. This script seeds the expected rows and extracts
student final-answer atoms from the route-B/LaTeX-style normalized PDFs.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(os.environ.get("NE630_GRADING_ROOT", "/home/robertsj/Classes/ne630_local_grading")).expanduser()
NE630_ROOT = Path(os.environ.get("NE630_REPO_ROOT", "/home/robertsj/Classes/ne630")).expanduser()
HW_DIR = ROOT / "hw04"
TABLE_DIR = HW_DIR / "tables"
ARTIFACT_DIR = HW_DIR / "table_artifacts"
PDF_TEXT_DIR = ARTIFACT_DIR / "pdf_text"

SCHEMA_VERSION = "ne630.solution_table.v0.1"
COURSE = "NE 630"
TERM = "Fall 2026"
HOMEWORK_ID = "hw04"
STATEMENT_PATH = str(NE630_ROOT / "homework/markdown/HW04.md")
SOLUTION_PATH = str(NE630_ROOT / "homework/solutions/hw04.tex")


@dataclass(frozen=True)
class AnswerSpec:
    problem_id: str
    part_id: str
    answer_id: str
    label: str
    value: float
    unit: str
    display: str
    tolerance_abs: float
    evidence: str
    markers: tuple[str, ...]
    fallback_tokens: tuple[str, ...]
    min_value: float
    max_value: float

    @property
    def key(self) -> tuple[str, str, str]:
        return (self.problem_id, self.part_id, self.answer_id)

    @property
    def expected_answer_id(self) -> str:
        part = f"{self.part_id}." if self.part_id else ""
        return f"{HOMEWORK_ID}.{self.problem_id}.{part}{self.answer_id}"


@dataclass(frozen=True)
class TextSpec:
    problem_id: str
    part_id: str
    answer_id: str
    label: str
    answer_kind: str
    expected_text: str
    evidence: str
    claims: tuple[str, ...] = ()

    @property
    def expected_answer_id(self) -> str:
        part = f"{self.part_id}." if self.part_id else ""
        return f"{HOMEWORK_ID}.{self.problem_id}.{part}{self.answer_id}"


SPECS: tuple[AnswerSpec, ...] = (
    AnswerSpec(
        "p01",
        "a",
        "flux",
        "Problem 1(a) neutron flux",
        2.94e5,
        "n cm^-2 s^-1",
        "2.94e5 n cm^-2 s^-1",
        8.0e3,
        r"\phi_u \approx \boxed{2.94 \cdot 10^{5}~\mathrm{n\,cm^{-2}\,s^{-1}}}",
        (
            r"Final\s+(?:answer|Result)\s*\(a\)",
            r"Answer:\s*[^\n]{0,30}(?:ϕ|phi|flux)",
            r"ϕ\s*(?:=|≈)\s*[0-9][^\n]{0,80}n\s*cm",
            r"phi\s*(?:=|≈)\s*[0-9][^\n]{0,80}n\s*cm",
        ),
        ("ϕ", "phi", "flux", "n cm"),
        1.0e4,
        1.0e6,
    ),
    AnswerSpec(
        "p01",
        "b",
        "absorption_cross_section",
        "Problem 1(b) absorption cross section",
        0.02303,
        "cm^-1",
        "0.02303 cm^-1",
        0.001,
        r"\Sigma_a = -\ln(0.1)/100 \approx \boxed{0.023~\mathrm{cm^{-1}}}",
        (
            r"Final\s+(?:answer|Result)\s*\(b\)",
            r"Answer:\s*Σ",
            r"Σa?\s*(?:=|≈)\s*[0-9][^\n]{0,60}cm",
        ),
        ("Σ", "Sigma", "cross", "cm"),
        0.005,
        0.08,
    ),
    AnswerSpec(
        "p01",
        "c",
        "distance",
        "Problem 1(c) distance from source",
        178.0,
        "cm",
        "178 cm",
        4.0,
        r"r \approx \boxed{178~\mathrm{cm}}",
        (
            r"Final\s+(?:answer|Result)\s*\(c\)",
            r"Answer:\s*(?:R|r)",
            r"(?:must|located|distance)[^\n]{0,80}(?:177|178|1\.78)",
            r"r\s*(?:=|≈)\s*(?:177|178|1\.77|1\.78)",
        ),
        ("r", "distance", "cm", "m"),
        120.0,
        230.0,
    ),
    AnswerSpec(
        "p02",
        "a",
        "water_macroscopic_cross_section",
        "Problem 2(a) water macroscopic cross section",
        1.17,
        "cm^-1",
        "1.17 cm^-1",
        0.03,
        r"\Sigma_w \approx \boxed{1.17~\mathrm{cm^{-1}}}",
        (
            r"Final\s+(?:answer|Result)\s*\(a\)",
            r"Answer:\s*Σwater",
            r"Σ(?:water|t,w|w)\s*(?:=|≈)\s*[0-9][^\n]{0,40}cm",
        ),
        ("water", "Σ", "cm"),
        0.8,
        1.5,
    ),
    AnswerSpec(
        "p02",
        "b",
        "steam_macroscopic_cross_section",
        "Problem 2(b) steam macroscopic cross section",
        0.057,
        "cm^-1",
        "0.057 cm^-1",
        0.005,
        r"\Sigma_s \approx \boxed{0.057~\mathrm{cm^{-1}}}",
        (
            r"Final\s+(?:answer|Result)\s*\(b\)",
            r"Answer:\s*Σsteam",
            r"Σ(?:steam|t,s|s)\s*(?:=|≈)\s*[0-9][^\n]{0,50}cm",
        ),
        ("steam", "Σ", "cm"),
        0.02,
        0.12,
    ),
    AnswerSpec(
        "p02",
        "c",
        "mixture_macroscopic_cross_section",
        "Problem 2(c) mixture macroscopic cross section",
        0.72,
        "cm^-1",
        "0.72 cm^-1",
        0.04,
        r"\Sigma_{\mathrm{mix}} \approx \boxed{0.72~\mathrm{cm^{-1}}}",
        (
            r"Final\s+(?:answer|Result)\s*\(c\)",
            r"Answer:\s*Σmix",
            r"Σmix\s*(?:=|≈)\s*[0-9][^\n]{0,50}cm",
        ),
        ("mix", "mixture", "Σ", "cm"),
        0.5,
        0.95,
    ),
    AnswerSpec(
        "p02",
        "d",
        "room_water_macroscopic_cross_section",
        "Problem 2(d) room-temperature water macroscopic cross section",
        1.58,
        "cm^-1",
        "1.58 cm^-1",
        0.05,
        r"\Sigma_{w'} \approx \boxed{1.58~\mathrm{cm^{-1}}}",
        (
            r"Final\s+(?:answer|Result)\s*\(d\)",
            r"Answer:\s*Σ(?:water,?1\.0|room)",
            r"Σ(?:room|water,RT|t,RT|water,1\.0)\s*(?:=|≈)\s*[0-9][^\n]{0,50}cm",
        ),
        ("room", "RT", "1.0", "Σ", "cm"),
        1.2,
        1.9,
    ),
    AnswerSpec(
        "p03",
        "",
        "uo2_macroscopic_cross_section",
        "Problem 3 UO2 macroscopic thermal cross section",
        1.01,
        "cm^-1",
        "1.01 cm^-1",
        0.04,
        r"\Sigma_t^{\mathrm{UO}_2} \approx \boxed{1.01~\mathrm{cm^{-1}}}",
        (
            r"Final\s+(?:answer|Result)",
            r"Answer:\s*ΣUO2",
            r"Σ(?:total|t|UO2)\s*(?:=|≈)\s*[0-9][^\n]{0,50}cm",
        ),
        ("Σ", "UO2", "total", "cm"),
        0.8,
        1.3,
    ),
)
TEXT_SPECS: tuple[TextSpec, ...] = ()


SCI_RE = re.compile(
    r"(?P<mant>[-+]?(?:\d{1,3}(?:,\s?\d{3})+|\d*\.\d+|\d+))"
    r"\s*(?:×|x|X|\\times|\\cdot|·)\s*10\s*(?P<exp>[-+]?\d+)"
)
NUMBER_RE = re.compile(r"[-+]?(?:\d{1,3}(?:,\s?\d{3})+|\d*\.\d+|\d+)")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_manifest() -> list[dict[str, str]]:
    with (HW_DIR / "reports/solution_manifest.csv").open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def student_group(row: dict[str, str]) -> str:
    output = row.get("output_file") or ""
    if output.endswith("_solution.pdf"):
        return Path(output).stem.removesuffix("_solution")
    return f"{row['slug']}_{row['user_id']}".lower()


def prompt_for(problem_id: str, part_id: str) -> dict[str, str]:
    problem_number = int(problem_id.replace("p", ""))
    locator = f"Problem {problem_number}"
    if part_id:
        locator = f"{locator}({part_id})"
    return {"statement_path": STATEMENT_PATH, "statement_locator": locator}


def reference_for(spec: AnswerSpec | TextSpec) -> dict[str, str]:
    locator = spec.label
    return {
        "solution_path": SOLUTION_PATH,
        "solution_locator": locator,
        "expected_answer_id": spec.expected_answer_id,
    }


def base_row(spec: AnswerSpec | TextSpec) -> dict:
    row = {
        "schema_version": SCHEMA_VERSION,
        "course": COURSE,
        "term": TERM,
        "homework_id": HOMEWORK_ID,
        "problem_id": spec.problem_id,
        "answer_id": spec.answer_id,
        "prompt": prompt_for(spec.problem_id, spec.part_id),
        "reference": reference_for(spec),
    }
    if spec.part_id:
        row["part_id"] = spec.part_id
    return row


def expected_rows(extracted_at: str) -> list[dict]:
    rows: list[dict] = []
    for spec in SPECS:
        row = base_row(spec)
        row["source"] = {"role": "expected", "path": SOLUTION_PATH, "locator": spec.label}
        row["answer_kind"] = "numerical"
        row["value"] = {
            "kind": "numerical",
            "value": spec.value,
            "unit": spec.unit,
            "display": spec.display,
            "tolerance_abs": spec.tolerance_abs,
        }
        row["comparison"] = {"method": "numeric_tolerance", "status": "not_compared"}
        row["evidence"] = [{"kind": "latex", "text": spec.evidence}]
        row["extraction"] = {
            "method": "manual_seed_from_instructor_solution",
            "tool": "match_hw04_latex.py",
            "extracted_at": extracted_at,
            "confidence": 1.0,
            "needs_review": False,
        }
        rows.append(row)
    return rows


def expected_text_rows(extracted_at: str) -> list[dict]:
    rows: list[dict] = []
    for spec in TEXT_SPECS:
        row = base_row(spec)
        row["source"] = {"role": "expected", "path": SOLUTION_PATH, "locator": spec.label}
        row["answer_kind"] = spec.answer_kind
        if spec.answer_kind == "algebraic":
            row["value"] = {
                "kind": "algebraic",
                "latex": spec.expected_text,
                "display": spec.expected_text,
            }
            method = "symbolic_equivalence"
        else:
            row["value"] = {
                "kind": "short_answer",
                "text": spec.expected_text,
                "claims": list(spec.claims),
            }
            method = "rubric"
        row["comparison"] = {"method": method, "status": "not_compared"}
        row["evidence"] = [{"kind": "latex" if spec.answer_kind == "algebraic" else "text", "text": spec.evidence}]
        row["extraction"] = {
            "method": "manual_seed_from_instructor_solution",
            "tool": "match_hw04_latex.py",
            "extracted_at": extracted_at,
            "confidence": 1.0,
            "needs_review": False,
        }
        rows.append(row)
    return rows


def normalize_text(text: str) -> str:
    return (
        text.replace("\u2212", "-")
        .replace("\u2013", "-")
        .replace("\u2014", "-")
        .replace("\xa0", " ")
        .replace("Σt,mix", "Σmix")
        .replace("Σt,water", "Σwater")
        .replace("Σt,steam", "Σsteam")
    )


def problem_section(text: str, problem_id: str) -> str:
    number = int(problem_id.replace("p", ""))
    matches = list(re.finditer(r"(?im)^Problem\s+([123])\b", text))
    starts: list[tuple[int, int]] = []
    for match in matches:
        starts.append((int(match.group(1)), match.start()))
    if not starts:
        return text
    for index, (found_number, start) in enumerate(starts):
        if found_number != number:
            continue
        end = len(text)
        for next_number, next_start in starts[index + 1 :]:
            if next_number > found_number:
                end = next_start
                break
        return text[start:end]
    return text


def part_section(section: str, part_id: str) -> str:
    if not part_id:
        return section
    markers = list(re.finditer(rf"(?im)^\s*(?:\(?{re.escape(part_id)}\)|Part\s+\(?{re.escape(part_id)}\)?)\b", section))
    if not markers:
        return section
    start = markers[-1].start()
    next_match = re.search(r"(?im)^\s*(?:\([a-z]\)|Part\s+\(?[a-z]\)?)\b", section[markers[-1].end() :])
    end = markers[-1].end() + next_match.start() if next_match else len(section)
    return section[start:end]


def cleaned_section_excerpt(text: str, spec: TextSpec) -> str:
    section = part_section(problem_section(normalize_text(text), spec.problem_id), spec.part_id)
    return re.sub(r"\s+", " ", section).strip()[:3000]


def numeric_candidates(snippet: str) -> list[tuple[float, str, int, int]]:
    results: list[tuple[float, str, int, int]] = []
    occupied: list[tuple[int, int]] = []
    for match in SCI_RE.finditer(snippet):
        mantissa = match.group("mant").replace(",", "").replace(" ", "")
        exponent = int(match.group("exp"))
        value = float(mantissa) * 10**exponent
        results.append((value, match.group(0), match.start(), match.end()))
        occupied.append((match.start(), match.end()))

    def covered(start: int, end: int) -> bool:
        return any(start >= a and end <= b for a, b in occupied)

    for match in NUMBER_RE.finditer(snippet):
        if covered(match.start(), match.end()):
            continue
        raw = match.group(0)
        try:
            value = float(raw.replace(",", "").replace(" ", ""))
        except ValueError:
            continue
        results.append((value, raw, match.start(), match.end()))
    return results


def convert_candidate(spec: AnswerSpec, value: float, raw: str, snippet: str, start: int, end: int) -> float | None:
    before = snippet[max(0, start - 20) : start].lower()
    after = snippet[end : min(len(snippet), end + 40)].lower()
    raw_clean = raw.replace(",", "").replace(" ", "")
    if spec.key == ("p01", "c", "distance"):
        if "cm2" in after or "cm^2" in after:
            return None
        converted = value
        if (" m" in after or "m " in after or "m." in after) and "cm" not in after and value < 10:
            converted = value * 100.0
        if value < 10 and "cm" not in after and ("distance" in snippet.lower() or "from the point source" in snippet.lower()):
            converted = value * 100.0
        return converted if spec.min_value <= converted <= spec.max_value else None

    if spec.key == ("p01", "a", "flux"):
        if value < 10 and re.fullmatch(r"10\d+", raw_clean):
            return None
        return value if spec.min_value <= value <= spec.max_value else None

    # Reject common constants in derivations unless the value is in the answer range.
    if spec.min_value <= value <= spec.max_value:
        return value
    return None


def candidate_windows(section: str, spec: AnswerSpec) -> list[tuple[str, bool]]:
    windows: list[tuple[str, bool]] = []
    for pattern in spec.markers:
        for match in re.finditer(pattern, section, re.IGNORECASE | re.DOTALL):
            start = max(0, match.start() - 120)
            end = min(len(section), match.end() + 420)
            windows.append((section[start:end], True))
    lines = section.splitlines()
    for index, line in enumerate(lines):
        lowered = line.lower()
        token_hits = sum(1 for token in spec.fallback_tokens if token.lower() in lowered)
        if token_hits >= 2:
            start = max(0, index - 1)
            end = min(len(lines), index + 3)
            windows.append(("\n".join(lines[start:end]), False))
    return windows


def extract_value(text: str, spec: AnswerSpec) -> tuple[float, str, str, bool, float, str] | None:
    section = normalize_text(problem_section(text, spec.problem_id))
    best: tuple[float, str, str, bool, float, str] | None = None
    best_score = math.inf
    for window, direct_marker in candidate_windows(section, spec):
        for value, raw, start, end in numeric_candidates(window):
            converted = convert_candidate(spec, value, raw, window, start, end)
            if converted is None:
                continue
            scale = max(abs(spec.value), 1e-12)
            closeness = abs(converted - spec.value) / scale
            marker_bonus = -0.10 if direct_marker else 0.0
            label_bonus = -0.05 if re.search(r"Final|Answer|Result", window, re.IGNORECASE) else 0.0
            score = closeness + marker_bonus + label_bonus
            if score < best_score:
                confidence = 0.90 if direct_marker else 0.72
                needs_review = not direct_marker
                reason = "" if direct_marker else "value found by section fallback rather than explicit final-answer marker"
                evidence = re.sub(r"\s+", " ", window).strip()
                display = f"{converted:g} {spec.unit}"
                best = (converted, display, evidence[:1200], needs_review, confidence, reason)
                best_score = score
    return best


def compare_numeric(value: float, spec: AnswerSpec) -> tuple[str, str]:
    difference = abs(value - spec.value)
    if difference <= spec.tolerance_abs:
        return "match", f"within absolute tolerance {spec.tolerance_abs:g}"
    if difference <= max(2 * spec.tolerance_abs, 0.05 * abs(spec.value)):
        return "near_match", f"outside tolerance; absolute difference {difference:g}"
    return "mismatch", f"outside tolerance; absolute difference {difference:g}"


def pdf_text_path(group: str) -> Path:
    return PDF_TEXT_DIR / f"{group}_pdftotext.txt"


def ensure_pdf_text(row: dict[str, str], group: str) -> Path:
    PDF_TEXT_DIR.mkdir(parents=True, exist_ok=True)
    output = pdf_text_path(group)
    subprocess.run(["pdftotext", "-layout", row["output_file"], str(output)], check=False)
    return output


def student_row(
    spec: AnswerSpec,
    manifest_row: dict[str, str],
    group: str,
    text_path: Path,
    extracted: tuple[float, str, str, bool, float, str],
    extracted_at: str,
) -> dict:
    value, display, evidence, needs_review, confidence, review_reason = extracted
    status, notes = compare_numeric(value, spec)
    row = base_row(spec)
    row["source"] = {
        "role": "student",
        "student_group": group,
        "path": manifest_row["output_file"],
        "locator": str(text_path),
        "route_guess": manifest_row.get("route_guess", ""),
    }
    if manifest_row.get("sha256"):
        row["source"]["sha256"] = manifest_row["sha256"]
    row["answer_kind"] = "numerical"
    row["value"] = {"kind": "numerical", "value": value, "unit": spec.unit, "display": display}
    row["comparison"] = {
        "compare_to_answer_id": spec.expected_answer_id,
        "method": "numeric_tolerance",
        "status": status,
        "notes": notes,
    }
    row["evidence"] = [
        {
            "kind": "text",
            "text": evidence,
            "path": str(text_path),
            "sha256": sha256_path(text_path),
        }
    ]
    row["extraction"] = {
        "method": "regex_from_pdftotext_latex_submission",
        "tool": "match_hw04_latex.py",
        "extracted_at": extracted_at,
        "confidence": confidence,
        "needs_review": needs_review,
    }
    if needs_review:
        row["extraction"]["review_reason"] = review_reason
    return row


def student_text_row(
    spec: TextSpec,
    manifest_row: dict[str, str],
    group: str,
    text_path: Path,
    text: str,
    extracted_at: str,
) -> dict:
    excerpt = cleaned_section_excerpt(text, spec)
    row = base_row(spec)
    row["source"] = {
        "role": "student",
        "student_group": group,
        "path": manifest_row["output_file"],
        "locator": str(text_path),
        "route_guess": manifest_row.get("route_guess", ""),
    }
    if manifest_row.get("sha256"):
        row["source"]["sha256"] = manifest_row["sha256"]
    row["answer_kind"] = spec.answer_kind
    if spec.answer_kind == "algebraic":
        row["value"] = {"kind": "algebraic", "latex": excerpt or "", "display": excerpt or ""}
        method = "symbolic_equivalence"
    else:
        row["value"] = {"kind": "short_answer", "text": excerpt or ""}
        method = "rubric"
    row["comparison"] = {
        "compare_to_answer_id": spec.expected_answer_id,
        "method": method,
        "status": "manual_review",
        "notes": "Comparison intentionally deferred to manual/rubric review.",
    }
    row["evidence"] = [
        {
            "kind": "text",
            "text": excerpt[:1000],
            "path": str(text_path),
            "sha256": sha256_path(text_path),
        }
    ]
    row["extraction"] = {
        "method": "section_from_pdftotext_latex_submission",
        "tool": "match_hw04_latex.py",
        "extracted_at": extracted_at,
        "confidence": 0.65 if excerpt else 0.0,
        "needs_review": True,
        "review_reason": "algebraic or short-answer item requires rubric/manual comparison",
    }
    if not excerpt:
        row["extraction"]["review_reason"] = "problem section not found in PDF text"
    return row


def extract_student_rows(manifest_rows: list[dict[str, str]], extracted_at: str) -> tuple[list[dict], list[dict], list[dict[str, str]]]:
    rows: list[dict] = []
    errors: list[dict] = []
    report_rows: list[dict[str, str]] = []
    for manifest_row in manifest_rows:
        group = student_group(manifest_row)
        route = manifest_row.get("route_guess", "")
        if not route.startswith("route_b"):
            errors.append(
                {
                    "student_group": group,
                    "answer": "all",
                    "reason": "deferred_pending_handwritten_or_pdf_transcription",
                    "source_path": manifest_row.get("output_file", ""),
                    "route_guess": route,
                }
            )
            continue
        text_path = ensure_pdf_text(manifest_row, group)
        text = text_path.read_text(encoding="utf-8", errors="replace")
        extracted_count = 0
        review_count = 0
        for spec in SPECS:
            extracted = extract_value(text, spec)
            if extracted is None:
                errors.append(
                    {
                        "student_group": group,
                        "answer": spec.expected_answer_id,
                        "reason": "not extracted from typeset PDF text",
                        "pdf_text": str(text_path),
                        "source_path": manifest_row.get("output_file", ""),
                        "route_guess": route,
                    }
                )
                continue
            rows.append(student_row(spec, manifest_row, group, text_path, extracted, extracted_at))
            extracted_count += 1
            if extracted[3]:
                review_count += 1
        for spec in TEXT_SPECS:
            rows.append(student_text_row(spec, manifest_row, group, text_path, text, extracted_at))
            extracted_count += 1
            review_count += 1
        report_rows.append(
            {
                "student_group": group,
                "route_guess": route,
                "normalized_solution_pdf": manifest_row.get("output_file", ""),
                "pdf_text": str(text_path),
                "student_rows": str(extracted_count),
                "needs_review_rows": str(review_count),
                "missing_rows": str(len(SPECS) + len(TEXT_SPECS) - extracted_count),
                "selection_rule": manifest_row.get("rule", ""),
            }
        )
    return rows, errors, report_rows


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_errors(path: Path, errors: list[dict], extracted_at: str) -> None:
    with path.open("w", encoding="utf-8") as stream:
        for error in errors:
            stream.write(json.dumps({**error, "extracted_at": extracted_at}, ensure_ascii=False, sort_keys=True) + "\n")


def write_report(path: Path, rows: list[dict[str, str]]) -> None:
    fields = [
        "student_group",
        "route_guess",
        "normalized_solution_pdf",
        "pdf_text",
        "student_rows",
        "needs_review_rows",
        "missing_rows",
        "selection_rule",
    ]
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def validate_rows(rows: list[dict]) -> None:
    from jsonschema import Draft202012Validator

    schema = json.loads((ROOT / "schema/solution_table.schema.json").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    failures = []
    for index, row in enumerate(rows, 1):
        for error in validator.iter_errors(row):
            failures.append((index, error.json_path, error.message))
    if failures:
        for failure in failures[:20]:
            print(failure)
        raise SystemExit(f"{len(failures)} schema validation failures")


def main() -> None:
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    extracted_at = utc_now()
    manifest_rows = read_manifest()
    rows = expected_rows(extracted_at)
    rows.extend(expected_text_rows(extracted_at))
    student_rows, errors, report_rows = extract_student_rows(manifest_rows, extracted_at)
    rows.extend(student_rows)
    validate_rows(rows)

    table_path = TABLE_DIR / "solution_table.jsonl"
    errors_path = TABLE_DIR / "solution_table.errors.jsonl"
    report_path = HW_DIR / "reports/latex_solution_table_report.csv"
    summary_path = HW_DIR / "reports/solution_table_summary.json"
    write_jsonl(table_path, rows)
    write_errors(errors_path, errors, extracted_at)
    write_report(report_path, report_rows)

    summary = {
        "extracted_at": extracted_at,
        "homework_id": HOMEWORK_ID,
        "table_path": str(table_path),
        "errors_path": str(errors_path),
        "latex_report_path": str(report_path),
        "rows": len(rows),
        "expected_rows": sum(1 for row in rows if row["source"]["role"] == "expected"),
        "student_rows": sum(1 for row in rows if row["source"]["role"] == "student"),
        "latex_students": len(report_rows),
        "manifest_students": len(manifest_rows),
        "deferred_students": sum(1 for error in errors if error.get("answer") == "all"),
        "needs_review_rows": sum(1 for row in rows if row["extraction"].get("needs_review")),
        "errors": len(errors),
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
