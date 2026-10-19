#!/usr/bin/env python3
"""Build a roster-ordered SpeedGrader queue from Canvas grades and feedback CSVs."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from assessment_server import ROOT, homework_path


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as stream:
        return list(csv.DictReader(stream))


def canvas_user_id(student_group: str) -> str:
    if "_" not in student_group:
        return ""
    return student_group.rsplit("_", 1)[-1]


def assignment_column(headers: list[str], hw: str) -> str:
    prefix = hw.upper()
    matches = [header for header in headers if header.startswith(f"{prefix} ")]
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one {prefix} assignment column, found {matches}")
    return matches[0]


def real_roster_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return [row for row in rows if row.get("ID", "").strip().isdigit()]


def build_queue(hw: str, grades_csv: Path) -> list[dict[str, str]]:
    grades_rows = read_csv(grades_csv)
    if not grades_rows:
        raise ValueError(f"No rows found in grades CSV: {grades_csv}")

    headers = list(grades_rows[0])
    hw_column = assignment_column(headers, hw)
    roster_rows = real_roster_rows(grades_rows)

    feedback_csv = homework_path(hw) / "assessment" / "canvas_feedback.csv"
    feedback_rows = read_csv(feedback_csv)
    feedback_by_id = {canvas_user_id(row.get("student_group", "")): row for row in feedback_rows}

    queue: list[dict[str, str]] = []
    for roster in roster_rows:
        user_id = roster["ID"].strip()
        feedback = feedback_by_id.get(user_id)
        if feedback:
            queue.append(
                {
                    "homework_id": hw,
                    "student_group": feedback["student_group"],
                    "canvas_user_id": user_id,
                    "canvas_student": roster.get("Student", ""),
                    "canvas_score": "1",
                    "submission_status": "submitted",
                    "canvas_gradebook_value": roster.get(hw_column, ""),
                    "internal_total_score": feedback.get("total_score", ""),
                    "internal_total_max": feedback.get("total_max", ""),
                    "feedback_text": feedback.get("feedback_text", ""),
                }
            )
        else:
            queue.append(
                {
                    "homework_id": hw,
                    "student_group": roster.get("Student", "") or f"canvas_user_{user_id}",
                    "canvas_user_id": user_id,
                    "canvas_student": roster.get("Student", ""),
                    "canvas_score": "0",
                    "submission_status": "no_submission",
                    "canvas_gradebook_value": roster.get(hw_column, ""),
                    "internal_total_score": "0",
                    "internal_total_max": "",
                    "feedback_text": "Not submitted.",
                }
            )

    return queue


def write_queue(hw: str, rows: list[dict[str, str]], output: Path | None = None) -> Path:
    output = output or homework_path(hw) / "assessment" / "speedgrader_queue.csv"
    output.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "homework_id",
        "student_group",
        "canvas_user_id",
        "canvas_student",
        "canvas_score",
        "submission_status",
        "canvas_gradebook_value",
        "internal_total_score",
        "internal_total_max",
        "feedback_text",
    ]
    tmp = output.with_suffix(output.suffix + ".tmp")
    with tmp.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    tmp.replace(output)
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("homework_id", help="Homework id such as hw01.")
    parser.add_argument("grades_csv", type=Path, help="Canvas grades CSV exported from the gradebook.")
    parser.add_argument("--output", type=Path, help="Output CSV path. Defaults to hwNN/assessment/speedgrader_queue.csv.")
    args = parser.parse_args()

    hw = args.homework_id.lower()
    rows = build_queue(hw, args.grades_csv.expanduser().resolve())
    output = write_queue(hw, rows, args.output)
    missing = sum(1 for row in rows if row["submission_status"] == "no_submission")
    submitted = sum(1 for row in rows if row["submission_status"] == "submitted")
    print(f"{hw}: wrote {len(rows)} SpeedGrader rows to {output}")
    print(f"{hw}: submitted={submitted}, no_submission={missing}")


if __name__ == "__main__":
    main()
