#!/usr/bin/env python3
"""Build Canvas-ready student feedback from NE 630 assessment payloads."""

from __future__ import annotations

import csv
import io
import json
import re
from datetime import datetime, timezone
from typing import Any


SCHEMA_VERSION = "ne630.canvas_feedback.v0.1"

FEEDBACK_KEY_TEXT = {
    "missing": "I could not identify a final answer for this item; please make final answers explicit.",
    "review_uncertain": "I could not verify this item cleanly from the extracted submission; please make the final answer and supporting work explicit.",
    "p01_unit_kev": "The value appears to be on the keV scale but was reported as MeV; convert by 1000 before reporting.",
    "p01_sign": "The magnitude is close, but the Q-value sign convention is reversed; use reactant masses minus product masses.",
    "p01_beta_atomic": "For beta-minus Q-values with neutral atomic masses, do not subtract an extra electron mass; the electron masses are already accounted for.",
    "p01_reaction_accounting": "The completed reaction or mass accounting is not close to the reference; recheck A/Z conservation and the mass inputs.",
    "p02_sign": "The magnitude is close, but the percent-error sign is reversed; use 100(Kapprox - Ktrue)/Ktrue.",
    "p02_close": "The percent-error calculation is close but outside tolerance; recheck the relativistic speed and avoid premature rounding.",
    "p02_formula": "The percent-error result is not close to the reference; recheck the relativistic velocity and the Kapprox - Ktrue definition.",
    "p03_percent_fraction": "The result appears to be on a percent-like scale; convert it to the requested mass fraction.",
    "p03_scale": "The mass-fraction scale is not close; recheck the rest-mass denominator and eV/MeV conversion.",
    "p03c_review": "The consistency check needs clearer assumptions and a comparison of the fuel estimate to plant energy demand.",
}

P03C_COMPACT_REFERENCE = (
    "This was a relatively open-ended question. My own compact answer is: from parts (a) and (b), "
    "nuclear fuel releases about 9×10⁶ times more energy per unit mass than carbon combustion. "
    "A quoted nuclear-fuel use of 20 tons/year is therefore plausible only after assumptions about "
    "enrichment, burnup, efficiency, capacity factor, and what counts as 'fuel' are made explicit. "
    "For example, by assuming the coal number means pure carbon and the nuclear number means fully "
    "fissioned ²³⁵U, 10,000 tons/day × 365 days/year = 3.65×10⁶ tons/year of coal; dividing by "
    "9×10⁶ gives about 0.4 tons/year of fully fissioned ²³⁵U for the same energy scale, so the "
    "quoted 20 tons/year is a reasonable order-of-magnitude fuel-use figure once the real reactor "
    "(e.g., power, efficiency) and fuel-cycle (e.g., enrichment) assumptions are included."
)


SUPERSCRIPT = {
    "0": "⁰",
    "1": "¹",
    "2": "²",
    "3": "³",
    "4": "⁴",
    "5": "⁵",
    "6": "⁶",
    "7": "⁷",
    "8": "⁸",
    "9": "⁹",
    "+": "⁺",
    "-": "⁻",
    "=": "⁼",
    "(": "⁽",
    ")": "⁾",
    "a": "ᵃ",
    "b": "ᵇ",
    "c": "ᶜ",
    "d": "ᵈ",
    "e": "ᵉ",
    "f": "ᶠ",
    "g": "ᵍ",
    "h": "ʰ",
    "i": "ⁱ",
    "j": "ʲ",
    "k": "ᵏ",
    "l": "ˡ",
    "m": "ᵐ",
    "n": "ⁿ",
    "o": "ᵒ",
    "p": "ᵖ",
    "r": "ʳ",
    "s": "ˢ",
    "t": "ᵗ",
    "u": "ᵘ",
    "v": "ᵛ",
    "w": "ʷ",
    "x": "ˣ",
    "y": "ʸ",
    "z": "ᶻ",
}

SUBSCRIPT = {
    "0": "₀",
    "1": "₁",
    "2": "₂",
    "3": "₃",
    "4": "₄",
    "5": "₅",
    "6": "₆",
    "7": "₇",
    "8": "₈",
    "9": "₉",
    "+": "₊",
    "-": "₋",
    "=": "₌",
    "(": "₍",
    ")": "₎",
    "a": "ₐ",
    "e": "ₑ",
    "h": "ₕ",
    "i": "ᵢ",
    "j": "ⱼ",
    "k": "ₖ",
    "l": "ₗ",
    "m": "ₘ",
    "n": "ₙ",
    "o": "ₒ",
    "p": "ₚ",
    "r": "ᵣ",
    "s": "ₛ",
    "t": "ₜ",
    "u": "ᵤ",
    "v": "ᵥ",
    "x": "ₓ",
}

LATEX_SYMBOLS = {
    "\\approx": "≈",
    "\\cdot": "×",
    "\\times": "×",
    "\\%": "%",
    "\\mega\\electronvolt": "MeV",
    "\\electronvolt": "eV",
    "\\rightarrow": "→",
    "\\to": "→",
    "\\leq": "≤",
    "\\geq": "≥",
    "\\neq": "≠",
    "\\propto": "∝",
    "\\infty": "∞",
    "\\alpha": "α",
    "\\beta": "β",
    "\\gamma": "γ",
    "\\delta": "δ",
    "\\Delta": "Δ",
    "\\eta": "η",
    "\\lambda": "λ",
    "\\nu": "ν",
    "\\sigma": "σ",
    "\\Sigma": "Σ",
    "\\phi": "φ",
    "\\chi": "χ",
    "\\xi": "ξ",
    "\\pi": "π",
    "\\ell": "ℓ",
    "\\prime": "′",
    "\\ln": "ln",
    "\\lim": "lim",
    "\\int": "∫",
    "\\exp": "exp",
    "\\rm": "",
    "\\quad": " ",
    "\\,": " ",
    "\\;": " ",
}

PLAIN_MATH_PATTERNS = [
    (r"\boverline\{?Delta\s*u\}?", "Δū"),
    (r"\boverlineΔ\s*u\b", "Δū"),
    (r"\boverlineDelta\s*u\b", "Δū"),
    (r"\bbar\s+v\b", "v̄"),
    (r"\buprime\b", "u′"),
    (r"\bSigma(?=_)", "Σ"),
    (r"\bSigma\b", "Σ"),
    (r"\bsigma(?=_)", "σ"),
    (r"\bsigma\b", "σ"),
    (r"\bphi(?=[_(])", "φ"),
    (r"\bphi\b", "φ"),
    (r"\beta\b", "η"),
    (r"\blambda\b", "λ"),
    (r"\balpha(?=_)", "α"),
    (r"\balpha\b", "α"),
    (r"_gamma\b", "_γ"),
    (r"_alpha\b", "_α"),
    (r"\bgamma\b", "γ"),
    (r"\bDelta\b", "Δ"),
    (r"\bxi\b", "ξ"),
    (r"\bpi\b", "π"),
    (r"\bsqrt\s*\(", "√("),
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def script_text(text: str, table: dict[str, str], marker: str) -> str:
    if not text:
        return ""
    chars = []
    for char in text:
        if char in table:
            chars.append(table[char])
        else:
            return f"{marker}({text})" if len(text) > 1 else marker + text
    return "".join(chars)


def compact_fraction(numerator: str, denominator: str) -> str:
    def wrap(part: str) -> str:
        part = part.strip()
        if re.fullmatch(r"[A-Za-z0-9.⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉₊₋₍₎ᵃ-ᶻₐ-ₓα-ωΑ-Ων̄φΣσλℓ′]+", part):
            return part
        return f"({part})"

    return f"{wrap(numerator)}/{wrap(denominator)}"


def latex_math_to_unicode(text: str) -> str:
    text = re.sub(r"\\(?:Aboxed|boxed|mathrm|text|rm)\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\isoA\{([^}]+)\}\{([^}]+)\}", r"^\2\1", text)
    text = re.sub(r"\\sqrt\{([^{}]+)\}", r"√(\1)", text)
    text = re.sub(r"\\overline\{([^{}]+)\}", lambda m: m.group(1) + "\u0304", text)
    text = re.sub(r"\\widetilde\{([^{}]+)\}", lambda m: m.group(1) + "\u0303", text)
    text = text.replace("\\bar\\nu", "ν̄")
    text = re.sub(r"\\bar\{?\\?nu\}?", "ν̄", text)
    for old, new in LATEX_SYMBOLS.items():
        text = text.replace(old, new)
    text = text.replace("\\left", "").replace("\\right", "")
    text = re.sub(r"\\\s+", " ", text)
    for pattern, replacement in PLAIN_MATH_PATTERNS:
        text = re.sub(pattern, replacement, text)
    text = re.sub(r"\^\{([^{}]+)\}", lambda m: script_text(m.group(1), SUPERSCRIPT, "^"), text)
    text = re.sub(r"_\{([^{}]+)\}", lambda m: script_text(m.group(1), SUBSCRIPT, "_"), text)
    text = re.sub(r"\^([+-]?\d+)", lambda m: script_text(m.group(1), SUPERSCRIPT, "^"), text)
    text = re.sub(r"_([+-]?\d+)", lambda m: script_text(m.group(1), SUBSCRIPT, "_"), text)
    text = re.sub(r"\^([a-z])\b", lambda m: script_text(m.group(1), SUPERSCRIPT, "^"), text)
    text = re.sub(r"_([a-z])\b", lambda m: script_text(m.group(1), SUBSCRIPT, "_"), text)
    previous = None
    while previous != text:
        previous = text
        text = re.sub(
            r"\\frac\{([^{}]+)\}\{([^{}]+)\}",
            lambda m: compact_fraction(m.group(1), m.group(2)),
            text,
        )
    text = re.sub(r"\\frac([A-Za-z0-9.]+)([A-Za-z0-9.]+)", r"\1/\2", text)
    return text


def collapse(value: Any) -> str:
    text = str(value or "")
    text = latex_math_to_unicode(text)
    text = text.replace("\\mathrm", "")
    text = text.replace("\\text", "")
    text = text.replace("\\boxed", "")
    text = text.replace("\\Aboxed", "")
    text = text.replace("~", " ")
    text = re.sub(r"[{}]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def truncate(text: str, limit: int = 140) -> str:
    text = collapse(text)
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def finish_sentence(text: str) -> str:
    text = collapse(text).rstrip(" .")
    return f"{text}." if text else ""


def display_score(value: Any) -> str:
    if value in (None, ""):
        return "?"
    number = float(value)
    return str(int(number)) if number.is_integer() else f"{number:g}"


def problem_title(problem_id: str) -> str:
    match = re.search(r"(\d+)", problem_id or "")
    if not match:
        return "Problem"
    return f"Problem {int(match.group(1))}"


def short_answer_label(answer: dict) -> str:
    problem = (answer.get("problem_id") or "").upper()
    part = answer.get("part_id") or ""
    prefix = problem
    if part:
        prefix = f"{problem}({part})"
    desc = str(answer.get("answer_id") or "").replace("_", " ")
    desc = re.sub(r"\bq value\b", "Q-value", desc, flags=re.IGNORECASE)
    desc = re.sub(r"\bn to z\b", "N/Z", desc, flags=re.IGNORECASE)
    desc = re.sub(r"\b(\d+)(day|month|year|yr)\b", r"\1 \2", desc)
    desc = re.sub(r"\byr\b", "year", desc)
    desc = re.sub(r"\bapprox\b", "approximate", desc)
    desc = re.sub(r"\s+", " ", desc).strip()
    if not desc:
        return prefix
    return f"{prefix}, {desc}"


def score_item(scores: dict, student_group: str, answer_key: str) -> dict:
    return scores.get("scores", {}).get(student_group, {}).get(answer_key, {})


def is_full_credit(item: dict) -> bool:
    score = item.get("score")
    if score in (None, ""):
        return False
    max_score = float(item.get("max_score", 1) or 1)
    return float(score) >= max_score - 1e-9


def clean_saved_note(note: str) -> str:
    note = collapse(note)
    if not note:
        return ""
    if note.startswith("Draft review needed"):
        return ""
    if note.startswith("Draft placeholder"):
        return ""
    if note.startswith("Draft: extracted answer matches"):
        return ""
    note = re.sub(r"\bcomparison status is [a-z_]+;?\s*", "", note, flags=re.IGNORECASE)
    note = re.sub(r"\bComparison intentionally deferred to manual/rubric review\.?\.?", "", note)
    note = note.replace("extraction is marked needs_review", "the final answer was not clearly extractable")
    note = re.sub(r"\s*;\s*;", "; ", note)
    return note.strip(" ;.")


def expected_value(answer: dict, limit: int = 150) -> str:
    raw_expected = collapse(answer.get("expected_display", ""))
    caption_match = re.search(r'"caption":\s*"([^"]+)"', raw_expected)
    if caption_match:
        raw_expected = caption_match.group(1)
    return truncate(raw_expected, limit)


def submitted_value(extracted: dict | None, limit: int = 120) -> str:
    if not extracted:
        return ""
    return truncate(extracted.get("display", ""), limit)


def anchored_submitted_value(extracted: dict | None, limit: int = 90) -> str:
    if not extracted:
        return ""
    raw = collapse(extracted.get("display", ""))
    if not raw:
        return ""
    lower = raw.lower()
    if len(raw) > limit * 2:
        return ""
    if lower.startswith(("ne 630", "problem statement", "final answer: see figure", "### student work")):
        return ""
    return truncate(raw, limit)


def compare_key(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", collapse(text).lower())


def reference_basis(answer: dict, limit: int = 140) -> str:
    evidence = collapse(answer.get("expected_evidence", ""))
    expected = collapse(answer.get("expected_display", ""))
    if not evidence:
        return ""
    if expected and compare_key(evidence) == compare_key(expected):
        return ""
    return truncate(evidence, limit)


def comparison_phrase(
    answer: dict,
    extracted: dict | None,
    expected_limit: int = 150,
    submitted_limit: int = 120,
) -> str:
    expected = expected_value(answer, expected_limit)
    submitted = submitted_value(extracted, submitted_limit)
    basis = reference_basis(answer)
    if expected and submitted:
        if basis:
            return f"I get {expected} from {basis}, but it looks like you got {submitted}"
        return f"I expected {expected}, but it looks like you got {submitted}"
    if expected:
        if basis:
            return f"I get {expected} from {basis}"
        return f"I expected {expected}"
    if submitted:
        return f"It looks like you got {submitted}"
    return "check against the reference solution"


def manual_review_sentence(answer: dict, extracted: dict | None) -> str:
    label = short_answer_label(answer)
    submitted = submitted_value(extracted)
    expected = expected_value(answer, 170)
    comparison = comparison_phrase(answer, extracted, expected_limit=170)
    basis = reference_basis(answer, 170)
    if expected and len(expected) < 170:
        target = f" The target idea/result is {expected}."
    elif basis:
        target = f" My reference solution uses {basis}."
    else:
        target = " Compare your final claim and reasoning against the reference solution."
    if expected and submitted:
        return f"{label}: {comparison}. This written response still needs rubric review."
    if submitted:
        return f"{label}: It looks like you got {submitted}, but this written response still needs rubric review.{target}"
    return f"{label}: this written response needs a clearer final claim and supporting reasoning.{target}"


def p03c_review_sentence(label: str, score_text: str, extracted: dict | None) -> str:
    submitted = collapse((extracted or {}).get("display", "")).lower()
    same_path_markers = [
        "1000",
        "mw",
        "mwe",
        "thermal",
        "efficiency",
        "coal",
        "tons/day",
        "tons/year",
        "365",
        "pure carbon",
        "power",
        "plant",
    ]
    same_path_count = sum(1 for marker in same_path_markers if marker in submitted)

    if same_path_count >= 4:
        student_path = (
            "It looks like you were doing roughly the same kind of plant-scale comparison, "
            "but the assumptions, units, and final comparison to the 1000 MWe scale need to be clearer."
        )
    elif submitted:
        student_path = (
            "It looks like you took an alternative path or left some assumptions implicit. "
            "That can be reasonable, but it is up to you to decide whether those assumptions are true "
            "and to state them explicitly."
        )
    else:
        student_path = (
            "I could not identify a clear final comparison in the extracted work; make the assumptions "
            "and sanity-check conclusion explicit."
        )

    return f"{label}{score_text}: {P03C_COMPACT_REFERENCE} {student_path}"


def issue_sentence(answer: dict, item: dict, extracted: dict | None) -> str | None:
    if is_full_credit(item):
        return None

    label = short_answer_label(answer)
    status = (
        (extracted or {}).get("comparison", {}).get("status")
        or item.get("comparison_status")
        or "unscored"
    )
    feedback_key = item.get("feedback_key") or ""
    saved_note = clean_saved_note(item.get("notes", ""))
    comparison = comparison_phrase(answer, extracted)
    score = display_score(item.get("score"))
    score_text = "" if score == "?" else f" [{score}/{display_score(item.get('max_score', 1))}]"

    if feedback_key == "p03c_review":
        return p03c_review_sentence(label, score_text, extracted)

    if feedback_key in FEEDBACK_KEY_TEXT and feedback_key != "pass":
        parts = [f"{label}{score_text}: {comparison}"]
        parts.append(FEEDBACK_KEY_TEXT[feedback_key])
        return finish_sentence("; ".join(parts))

    if saved_note:
        parts = [f"{label}{score_text}: {comparison}"]
        parts.append(saved_note)
        return finish_sentence("; ".join(parts))

    if not extracted or status == "missing":
        return f"{label}{score_text}: {comparison}, but I could not identify a final submitted answer. Please make final answers explicit."

    if status == "near_match":
        tail = "Recheck units, rounding, setup, and whether the final value is clearly identified."
        parts = [f"{label}{score_text}: {comparison}"]
        parts.append(tail)
        return finish_sentence("; ".join(parts))

    if status == "mismatch":
        tail = "Recheck the setup, signs, units, and final arithmetic."
        parts = [f"{label}{score_text}: {comparison}"]
        parts.append(tail)
        return finish_sentence("; ".join(parts))

    if status == "manual_review":
        return manual_review_sentence(answer, extracted)

    if status == "match":
        return f"{label}: {comparison}. The final answer was not clear enough to score automatically. Please make the final result easy to verify."

    parts = [f"{label}: {comparison}"]
    parts.append("I could not verify this item cleanly; please make the final answer and supporting work explicit")
    return finish_sentence("; ".join(parts))


def compact_label(answer: dict) -> str:
    return short_answer_label(answer).replace(", ", " ")


def record_expected(record: dict, limit: int = 70) -> str:
    return truncate(record["answer"].get("expected_display", ""), limit)


def record_submitted(record: dict, limit: int = 70) -> str:
    return truncate((record.get("extracted") or {}).get("display", ""), limit)


def record_list(records: list[dict], limit: int = 4) -> str:
    labels = [compact_label(record["answer"]) for record in records[:limit]]
    if len(records) > limit:
        labels.append(f"{len(records) - limit} more")
    if not labels:
        return ""
    if len(labels) == 1:
        return labels[0]
    return ", ".join(labels[:-1]) + f", and {labels[-1]}"


def numeric_issue_list(records: list[dict], verb: str, limit: int = 4) -> str:
    snippets = []
    for record in records[:limit]:
        label = compact_label(record["answer"])
        comparison = comparison_phrase(
            record["answer"],
            record.get("extracted"),
            expected_limit=70,
            submitted_limit=70,
        )
        snippets.append(f"{label}: {comparison}")
    if len(records) > limit:
        snippets.append(f"{len(records) - limit} more item(s)")
    return f"{verb}: " + "; ".join(snippets) + "."


def anchored_issue_list(records: list[dict], intro: str, limit: int = 3) -> str:
    snippets = []
    for record in records[:limit]:
        label = compact_label(record["answer"])
        answer = record["answer"]
        extracted = record.get("extracted")
        expected = expected_value(answer, 90)
        submitted = anchored_submitted_value(extracted, 90)
        basis = reference_basis(answer, 90)
        if expected and submitted and basis:
            comparison = f"I get {expected} from {basis}, while your extracted answer reads {submitted}"
        elif expected and submitted:
            comparison = f"I expected {expected}, while your extracted answer reads {submitted}"
        elif expected and basis:
            comparison = f"I get {expected} from {basis}"
        elif expected:
            comparison = f"I expected {expected}"
        elif basis:
            comparison = f"My reference solution uses {basis}"
        elif submitted:
            comparison = f"Your extracted answer reads {submitted}"
        else:
            comparison = "compare your final claim against the reference solution"
        snippets.append(f"{label}: {comparison}")
    if len(records) > limit:
        snippets.append(f"{len(records) - limit} more item(s) need the same kind of explicit comparison")
    return f"{intro} Concrete anchors: " + "; ".join(snippets) + "."


def problem_feedback(problem: str, records: list[dict]) -> str:
    issues = [record for record in records if record["issue"]]
    checked = sum(1 for record in records if record["has_student_answer"])
    problem_name = problem_title(problem)

    if not issues:
        if checked:
            return f"{problem_name}: good work; the checked answers for this problem match the expected results."
        return f"{problem_name}: I could not identify clear final answers for this problem; please make the final results explicit."

    tailored = [
        record
        for record in issues
        if record["item"].get("feedback_key") in FEEDBACK_KEY_TEXT
        and record["item"].get("feedback_key") not in {"missing", "review_uncertain"}
    ]
    manual = [record for record in issues if record["status"] == "manual_review" and record not in tailored]
    near = [record for record in issues if record["status"] == "near_match" and record not in tailored]
    mismatch = [record for record in issues if record["status"] == "mismatch" and record not in tailored]
    missing = [
        record
        for record in issues
        if (record["status"] == "missing" or not record["has_student_answer"])
        and record not in tailored
    ]
    unclear_match = [record for record in issues if record["status"] == "match" and record not in tailored]
    other = [
        record
        for record in issues
        if record not in tailored + manual + near + mismatch + missing + unclear_match
    ]

    parts: list[str] = []
    if tailored:
        parts.extend(record["issue"] for record in tailored[:4])
        if len(tailored) > 4:
            parts.append(f"{len(tailored) - 4} additional item(s) have similar targeted feedback.")
    if manual:
        parts.append(
            anchored_issue_list(
                manual,
                f"For {record_list(manual)}, make the final claim, assumptions, and supporting reasoning explicit.",
            )
        )
    if mismatch:
        parts.append(numeric_issue_list(mismatch, "Recheck these answers against the reference"))
    if near:
        parts.append(numeric_issue_list(near, "These answers are close but outside the nominal tolerance"))
    if missing:
        parts.append(
            anchored_issue_list(
                missing,
                f"I could not identify final answers for {record_list(missing)}; make final answers explicit.",
            )
        )
    if other:
        parts.append(
            anchored_issue_list(
                other,
                f"Review {record_list(other)} against the reference solution; the extracted evidence was not clean enough to summarize confidently.",
            )
        )
    if unclear_match and not (tailored or manual or near or mismatch or missing or other):
        parts.append(
            anchored_issue_list(
                unclear_match,
                f"For {record_list(unclear_match)}, state the final answer explicitly enough to grade.",
            )
        )

    text = f"{problem_name}: " + " ".join(parts)
    return text


def student_feedback(payload: dict, student: dict) -> dict:
    scores = payload["scores"]
    records_by_problem: dict[str, list[dict]] = {}
    total = 0.0
    total_max = 0.0
    scored_items = 0
    unscored_items = 0

    for answer in payload["answers"]:
        key = answer["key"]
        item = score_item(scores, student["student_group"], key)
        extracted = student.get("answers", {}).get(key)
        raw_score = item.get("score")
        if raw_score not in (None, ""):
            total += float(raw_score)
            total_max += float(item.get("max_score", 1) or 1)
            scored_items += 1
        else:
            unscored_items += 1
        status = (
            (extracted or {}).get("comparison", {}).get("status")
            or item.get("comparison_status")
            or "unscored"
        )
        record = {
            "answer": answer,
            "item": item,
            "extracted": extracted,
            "status": status,
            "issue": issue_sentence(answer, item, extracted),
            "full_credit": is_full_credit(item),
            "has_student_answer": extracted is not None,
        }
        records_by_problem.setdefault(answer.get("problem_id", ""), []).append(record)

    lines = [f"{payload['homework_id'].upper()} feedback:"]
    for problem, records in records_by_problem.items():
        lines.append(problem_feedback(problem, records))

    text = "\n\n".join(lines).strip()
    percent = round(100 * total / total_max, 1) if total_max else None
    return {
        "student_group": student["student_group"],
        "feedback_text": text,
        "total_score": round(total, 4),
        "total_max": round(total_max, 4),
        "percent": percent,
        "scored_items": scored_items,
        "unscored_items": unscored_items,
        "line_count": len(lines),
    }


def build_feedback(payload: dict) -> dict:
    students = [student_feedback(payload, student) for student in payload["students"]]
    return {
        "schema_version": SCHEMA_VERSION,
        "homework_id": payload["homework_id"],
        "generated_at": utc_now(),
        "source_paths": payload.get("paths", {}),
        "student_count": len(students),
        "students": students,
    }


def feedback_markdown(feedback: dict) -> str:
    lines = [
        f"# {feedback['homework_id'].upper()} Canvas Feedback",
        "",
        f"Generated: {feedback['generated_at']}",
        "",
        "Each block is intended as one pasteable Canvas SpeedGrader comment for that student/homework.",
        "",
    ]
    for student in feedback["students"]:
        score = f"{student['total_score']:g}/{student['total_max']:g}" if student["total_max"] else "unscored"
        lines.extend(
            [
                f"## {student['student_group']}",
                "",
                f"Current explicit score total: {score}; unscored items: {student['unscored_items']}.",
                "",
                "```text",
                student["feedback_text"],
                "```",
                "",
            ]
        )
    return "\n".join(lines)


def feedback_csv(feedback: dict) -> str:
    output = io.StringIO()
    fields = [
        "homework_id",
        "student_group",
        "total_score",
        "total_max",
        "percent",
        "scored_items",
        "unscored_items",
        "feedback_text",
    ]
    writer = csv.DictWriter(output, fieldnames=fields)
    writer.writeheader()
    for student in feedback["students"]:
        row = {field: student.get(field, "") for field in fields}
        row["homework_id"] = feedback["homework_id"]
        writer.writerow(row)
    return output.getvalue()


def feedback_json(feedback: dict) -> str:
    return json.dumps(feedback, indent=2, sort_keys=True) + "\n"
