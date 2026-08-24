#!/usr/bin/env python3
"""Print the NE 630 detailed schedule as a Canvas-safe HTML snippet."""

from __future__ import annotations

import argparse
import csv
import html
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SOURCE = ROOT / "administrivia" / "schedule-source.psv"
DEFAULT_OUTPUT = ROOT / "administrivia" / "generated" / "schedule-canvas.html"
FIELDNAMES = ["date", "kind", "meeting", "topic", "reading", "work"]
VALID_KINDS = {"class", "exam", "final", "no-class"}
EXPECTED_LESSONS = 41

REQUIRED_EVENTS = {
    date(2026, 9, 7): ("no-class", ("Labor Day",)),
    date(2026, 10, 2): ("exam", ("Exam 1",)),
    date(2026, 10, 9): ("no-class", ("Fall break", "Wildcat Pause")),
    date(2026, 11, 6): ("exam", ("Exam 2",)),
    date(2026, 11, 23): ("no-class", ("Fall break",)),
    date(2026, 11, 25): ("no-class", ("Fall break",)),
    date(2026, 11, 27): ("no-class", ("Fall break", "Thanksgiving")),
    date(2026, 12, 18): ("final", ("Final exam", "Exam 3")),
}


@dataclass(frozen=True)
class ScheduleRow:
    day: date
    kind: str
    meeting: str
    topic: str
    reading: str
    work: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build the NE 630 Canvas schedule snippet."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=DEFAULT_SOURCE,
        help="pipe-delimited schedule source",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="HTML snippet written for Canvas",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="print the Canvas snippet instead of writing it",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="validate the schedule source without writing HTML",
    )
    return parser.parse_args()


def parse_date(value: str, line_number: int) -> date:
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError as exc:
        raise ValueError(
            f"line {line_number}: date must be YYYY-MM-DD, got {value!r}"
        ) from exc


def read_schedule(path: Path) -> list[ScheduleRow]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="|")
        if reader.fieldnames != FIELDNAMES:
            raise ValueError(
                f"{path} header must be {'|'.join(FIELDNAMES)!r}; "
                f"got {reader.fieldnames!r}"
            )

        rows: list[ScheduleRow] = []
        for line_number, raw in enumerate(reader, start=2):
            if raw.get(None):
                raise ValueError(
                    f"line {line_number}: too many pipe-delimited fields"
                )
            row = {key: (raw[key] or "").strip() for key in FIELDNAMES}
            if not any(row.values()):
                continue
            rows.append(
                ScheduleRow(
                    day=parse_date(row["date"], line_number),
                    kind=row["kind"],
                    meeting=row["meeting"],
                    topic=row["topic"],
                    reading=row["reading"],
                    work=row["work"],
                )
            )
    return rows


def validate(rows: list[ScheduleRow]) -> None:
    errors: list[str] = []
    by_date: dict[date, ScheduleRow] = {}

    previous_day: date | None = None
    lesson_numbers: list[int] = []
    lesson_pattern = re.compile(r"Lesson\s+(\d+)$")

    for row in rows:
        if row.kind not in VALID_KINDS:
            errors.append(f"{row.day}: unknown kind {row.kind!r}")
        if not row.topic:
            errors.append(f"{row.day}: topic is required")
        if previous_day and row.day <= previous_day:
            errors.append(f"{row.day}: schedule dates must be strictly increasing")
        if row.day in by_date:
            errors.append(f"{row.day}: duplicate schedule date")
        by_date[row.day] = row
        previous_day = row.day

        if row.kind == "class":
            match = lesson_pattern.fullmatch(row.meeting)
            if not match:
                errors.append(f"{row.day}: class meeting must be 'Lesson N'")
            else:
                lesson_numbers.append(int(match.group(1)))

    expected_lessons = list(range(1, EXPECTED_LESSONS + 1))
    if lesson_numbers != expected_lessons:
        errors.append(
            "class lessons must be numbered consecutively "
            f"1-{EXPECTED_LESSONS}; got {lesson_numbers!r}"
        )

    for required_day, (required_kind, required_texts) in REQUIRED_EVENTS.items():
        row = by_date.get(required_day)
        if not row:
            errors.append(f"{required_day}: required schedule event is missing")
            continue
        if row.kind != required_kind:
            errors.append(
                f"{required_day}: expected kind {required_kind!r}, got {row.kind!r}"
            )
        combined = " ".join([row.meeting, row.topic, row.reading, row.work]).lower()
        if not any(text.lower() in combined for text in required_texts):
            errors.append(
                f"{required_day}: expected one of "
                f"{', '.join(required_texts)!r} in the row"
            )

    if errors:
        joined = "\n  - ".join(errors)
        raise ValueError(f"schedule validation failed:\n  - {joined}")


def format_day(day: date) -> str:
    return f"{day.strftime('%a')}, {day.strftime('%b')} {day.day}"


def cell(value: str, *, strong: bool = False) -> str:
    escaped = html.escape(value, quote=True)
    if strong and escaped:
        escaped = f"<strong>{escaped}</strong>"
    return f"<td>{escaped}</td>"


def build_snippet(rows: list[ScheduleRow]) -> str:
    parts = [
        "<!-- NE 630 Canvas schedule -->",
        '<div class="ne630-schedule">',
        "  <h2>NE 630 Fall 2026 Schedule</h2>",
        (
            "  <p>This schedule is the working plan for the course. "
            "Routine pacing updates will be announced in Canvas.</p>"
        ),
        "  <table>",
        "    <caption>NE 630 Fall 2026 schedule</caption>",
        "    <thead>",
        "      <tr>",
        '        <th scope="col">Date</th>',
        '        <th scope="col">Meeting</th>',
        '        <th scope="col">Topic</th>',
        '        <th scope="col">Reading</th>',
        '        <th scope="col">Work</th>',
        "      </tr>",
        "    </thead>",
        "    <tbody>",
    ]

    for row in rows:
        emphasize = row.kind in {"exam", "final", "no-class"}
        parts.extend(
            [
                "      <tr>",
                f"        {cell(format_day(row.day))}",
                f"        {cell(row.meeting, strong=emphasize)}",
                f"        {cell(row.topic, strong=emphasize)}",
                f"        {cell(row.reading)}",
                f"        {cell(row.work)}",
                "      </tr>",
            ]
        )

    parts.extend(
        [
            "    </tbody>",
            "  </table>",
            "</div>",
        ]
    )
    return "\n".join(parts)


def main() -> int:
    args = parse_args()
    rows = read_schedule(args.source)
    validate(rows)

    if args.check_only:
        print(f"OK: {len(rows)} schedule rows validated")
        return 0

    snippet = build_snippet(rows)
    if args.stdout:
        print(snippet)
        return 0

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(snippet + "\n", encoding="utf-8")
    try:
        display_path = args.output.relative_to(ROOT)
    except ValueError:
        display_path = args.output
    print(f"Wrote {display_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
