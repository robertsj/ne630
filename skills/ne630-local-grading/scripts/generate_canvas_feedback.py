#!/usr/bin/env python3
"""Generate Canvas-ready feedback artifacts for NE 630 local grading."""

from __future__ import annotations

import argparse
from pathlib import Path

from assessment_server import ROOT, build_payload, homework_path
from feedback_summaries import build_feedback, feedback_csv, feedback_json, feedback_markdown


def available_homeworks() -> list[str]:
    return sorted(item.name for item in ROOT.iterdir() if item.is_dir() and item.name.startswith("hw"))


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)


def generate(hw: str) -> dict:
    payload = build_payload(hw)
    feedback = build_feedback(payload)
    out_dir = homework_path(hw) / "assessment"
    write_text(out_dir / "canvas_feedback.json", feedback_json(feedback))
    write_text(out_dir / "canvas_feedback.md", feedback_markdown(feedback))
    write_text(out_dir / "canvas_feedback.csv", feedback_csv(feedback))
    return feedback


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("homeworks", nargs="*", help="Homework ids such as hw01. Defaults to every hwNN directory.")
    parser.add_argument("--index", action="store_true", help="Also write reports/canvas_feedback_index.md.")
    args = parser.parse_args()

    homeworks = args.homeworks or available_homeworks()
    generated = [generate(hw) for hw in homeworks]

    if args.index:
        lines = ["# Canvas Feedback Index", ""]
        for feedback in generated:
            hw = feedback["homework_id"]
            lines.append(
                f"- {hw.upper()}: {feedback['student_count']} students -> "
                f"`{homework_path(hw) / 'assessment' / 'canvas_feedback.md'}`"
            )
        lines.append("")
        write_text(ROOT / "reports" / "canvas_feedback_index.md", "\n".join(lines))

    for feedback in generated:
        print(f"{feedback['homework_id']}: {feedback['student_count']} feedback boxes")


if __name__ == "__main__":
    main()
