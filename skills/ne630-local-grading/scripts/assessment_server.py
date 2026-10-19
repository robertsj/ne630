#!/usr/bin/env python3
"""Local browser interface for NE 630 assessment scoring."""

from __future__ import annotations

import argparse
import csv
import io
import json
import mimetypes
import os
import re
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, unquote, urlparse


ROOT = Path(os.environ.get("NE630_GRADING_ROOT", "/home/robertsj/Classes/ne630_local_grading")).expanduser().resolve()
NE630_ROOT = Path(os.environ.get("NE630_REPO_ROOT", "/home/robertsj/Classes/ne630")).expanduser().resolve()
WEB_ROOT = ROOT / "web" / "assessment"
SCORE_SCHEMA_VERSION = "ne630.assessment_scores.v0.1"
HW_RE = re.compile(r"^hw\d{2}$")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def homework_path(hw: str) -> Path:
    if not HW_RE.match(hw):
        raise ValueError(f"Invalid homework id: {hw}")
    return ROOT / hw


def score_path(hw: str) -> Path:
    return homework_path(hw) / "assessment" / "scores.json"


def key_for(row: dict) -> str:
    part = row.get("part_id", "")
    if part:
        return f"{row['homework_id']}.{row['problem_id']}.{part}.{row['answer_id']}"
    return f"{row['homework_id']}.{row['problem_id']}.{row['answer_id']}"


def canonical_student_group(group: str) -> str:
    return str(group or "").strip().lower()


def answer_label(row: dict) -> str:
    problem = row["problem_id"].replace("p", "P")
    part = row.get("part_id", "")
    answer = row["answer_id"].replace("_", " ")
    if part:
        return f"{problem}({part}) {answer}"
    return f"{problem} {answer}"


def sort_answer_key(item: dict) -> tuple:
    row = item["expected_row"]
    problem_num = int(row["problem_id"].replace("p", ""))
    part = row.get("part_id", "")
    part_order = {"": 0, "a": 1, "b": 2, "c": 3, "d": 4}
    return (problem_num, part_order.get(part, 99), row["answer_id"])


def display_value(row: dict | None) -> str:
    if not row:
        return ""
    value = row.get("value", {})
    if "display" in value:
        return str(value["display"])
    if value.get("kind") == "numerical":
        unit = f" {value.get('unit', '')}".rstrip()
        return f"{value.get('value')}{unit}"
    if "text" in value:
        return str(value["text"])
    return json.dumps(value, sort_keys=True)


def evidence_text(row: dict | None) -> str:
    if not row:
        return ""
    snippets = []
    for evidence in row.get("evidence", []):
        text = evidence.get("text")
        if text:
            snippets.append(text)
    return "\n\n".join(snippets)


def artifact_url(path: str) -> str:
    return f"/artifact?path={quote(path)}"


def default_scores(hw: str, answers: list[dict]) -> dict:
    return {
        "schema_version": SCORE_SCHEMA_VERSION,
        "homework_id": hw,
        "created_at": utc_now(),
        "updated_at": utc_now(),
        "rubric": {
            answer["key"]: {
                "label": answer["label"],
                "max_score": 1.0,
            }
            for answer in answers
        },
        "scores": {},
    }


def load_scores(hw: str, answers: list[dict]) -> dict:
    path = score_path(hw)
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
        data.setdefault("schema_version", SCORE_SCHEMA_VERSION)
        data.setdefault("homework_id", hw)
        data.setdefault("created_at", utc_now())
        data.setdefault("updated_at", utc_now())
        data.setdefault("rubric", {})
        data.setdefault("scores", {})
    else:
        data = default_scores(hw, answers)
    for answer in answers:
        data["rubric"].setdefault(answer["key"], {"label": answer["label"], "max_score": 1.0})
    return data


def save_scores(hw: str, data: dict) -> dict:
    path = score_path(hw)
    path.parent.mkdir(parents=True, exist_ok=True)
    data["schema_version"] = SCORE_SCHEMA_VERSION
    data["homework_id"] = hw
    data.setdefault("created_at", utc_now())
    data["updated_at"] = utc_now()
    data.setdefault("rubric", {})
    data.setdefault("scores", {})
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)
    return data


def build_payload(hw: str) -> dict:
    hw_dir = homework_path(hw)
    table_rows = read_jsonl(hw_dir / "tables" / "solution_table.jsonl")
    error_rows = read_jsonl(hw_dir / "tables" / "solution_table.errors.jsonl")
    manifest_rows = read_csv(hw_dir / "reports" / "solution_manifest.csv")

    expected_rows = [row for row in table_rows if row.get("source", {}).get("role") == "expected"]
    student_rows = [row for row in table_rows if row.get("source", {}).get("role") == "student"]
    expected_by_key = {key_for(row): row for row in expected_rows}
    answers = [
        {
            "key": key,
            "label": answer_label(row),
            "problem_id": row["problem_id"],
            "part_id": row.get("part_id", ""),
            "answer_id": row["answer_id"],
            "answer_kind": row["answer_kind"],
            "expected_display": display_value(row),
            "expected_evidence": evidence_text(row),
            "expected_row": row,
        }
        for key, row in expected_by_key.items()
    ]
    answers.sort(key=sort_answer_key)

    students: dict[str, dict] = {}
    for manifest in manifest_rows:
        group = canonical_student_group(f"{manifest.get('slug', '')}_{manifest.get('user_id', '')}".strip("_"))
        if not group:
            continue
        students[group] = {
            "student_group": group,
            "solution_pdf": manifest.get("output_file", ""),
            "solution_pdf_url": artifact_url(manifest.get("output_file", "")) if manifest.get("output_file") else "",
            "route_guess": manifest.get("route_guess", ""),
            "manifest_status": manifest.get("status", ""),
            "answers": {},
            "errors": [],
            "row_count": 0,
            "needs_review_count": 0,
            "comparison_counts": {},
        }

    for row in student_rows:
        source = row.get("source", {})
        group = canonical_student_group(source.get("student_group", ""))
        if not group:
            continue
        students.setdefault(
            group,
            {
                "student_group": group,
                "solution_pdf": source.get("path", ""),
                "solution_pdf_url": artifact_url(source.get("path", "")) if source.get("path") else "",
                "route_guess": source.get("route_guess", ""),
                "manifest_status": "",
                "answers": {},
                "errors": [],
                "row_count": 0,
                "needs_review_count": 0,
                "comparison_counts": {},
            },
        )
        expected_key = row.get("comparison", {}).get("compare_to_answer_id") or key_for(row)
        students[group]["answers"][expected_key] = {
            "display": display_value(row),
            "evidence": evidence_text(row),
            "answer_kind": row.get("answer_kind", ""),
            "comparison": row.get("comparison", {}),
            "extraction": row.get("extraction", {}),
            "source_path": source.get("path", ""),
            "source_url": artifact_url(source.get("path", "")) if source.get("path") else "",
            "locator": source.get("locator", ""),
            "locator_url": artifact_url(source.get("locator", "")) if source.get("locator", "") else "",
            "row": row,
        }
        students[group]["row_count"] += 1
        if row.get("extraction", {}).get("needs_review"):
            students[group]["needs_review_count"] += 1
        status = row.get("comparison", {}).get("status", "unknown")
        counts = students[group]["comparison_counts"]
        counts[status] = counts.get(status, 0) + 1

    for error in error_rows:
        group = canonical_student_group(error.get("student_group", ""))
        if not group:
            continue
        students.setdefault(
            group,
            {
                "student_group": group,
                "solution_pdf": "",
                "solution_pdf_url": "",
                "route_guess": "",
                "manifest_status": "",
                "answers": {},
                "errors": [],
                "row_count": 0,
                "needs_review_count": 0,
                "comparison_counts": {},
            },
        )
        students[group]["errors"].append(error)

    score_data = load_scores(hw, answers)
    return {
        "homework_id": hw,
        "generated_at": utc_now(),
        "paths": {
            "root": str(ROOT),
            "table": str(hw_dir / "tables" / "solution_table.jsonl"),
            "errors": str(hw_dir / "tables" / "solution_table.errors.jsonl"),
            "scores": str(score_path(hw)),
        },
        "answers": [{k: v for k, v in answer.items() if k != "expected_row"} for answer in answers],
        "students": sorted(students.values(), key=lambda item: item["student_group"]),
        "scores": score_data,
    }


def safe_artifact(path_text: str) -> Path:
    path = Path(unquote(path_text)).expanduser().resolve()
    roots = [ROOT, NE630_ROOT]
    if not any(path == root or root in path.parents for root in roots):
        raise ValueError("artifact path is outside allowed local roots")
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(path)
    return path


def csv_export(hw: str) -> str:
    payload = build_payload(hw)
    scores = payload["scores"]
    answers = payload["answers"]
    output = io.StringIO()
    fields = ["student_group", "total_score", "total_max", "percent", "scored_items", "row_count", "needs_review_rows", "extraction_errors"]
    for answer in answers:
        fields.extend([f"{answer['key']}.score", f"{answer['key']}.max", f"{answer['key']}.notes"])
    writer = csv.DictWriter(output, fieldnames=fields)
    writer.writeheader()
    for student in payload["students"]:
        student_scores = scores.get("scores", {}).get(student["student_group"], {})
        row = {
            "student_group": student["student_group"],
            "row_count": student["row_count"],
            "needs_review_rows": student["needs_review_count"],
            "extraction_errors": len(student["errors"]),
        }
        total = 0.0
        total_max = 0.0
        scored = 0
        for answer in answers:
            key = answer["key"]
            rubric_max = float(scores.get("rubric", {}).get(key, {}).get("max_score", 1.0) or 0.0)
            item = student_scores.get(key, {})
            raw_score = item.get("score")
            row[f"{key}.score"] = raw_score if raw_score is not None else ""
            row[f"{key}.max"] = item.get("max_score", rubric_max)
            row[f"{key}.notes"] = item.get("notes", "")
            if raw_score not in (None, ""):
                total += float(raw_score)
                total_max += float(item.get("max_score", rubric_max) or 0.0)
                scored += 1
        row["total_score"] = f"{total:.4g}"
        row["total_max"] = f"{total_max:.4g}"
        row["percent"] = f"{100 * total / total_max:.4g}" if total_max else ""
        row["scored_items"] = scored
        writer.writerow(row)
    return output.getvalue()


class AssessmentHandler(BaseHTTPRequestHandler):
    server_version = "NE630Assessment/0.1"

    def log_message(self, fmt: str, *args) -> None:
        print(f"{self.address_string()} - {fmt % args}")

    def send_json(self, data: dict, status: HTTPStatus = HTTPStatus.OK) -> None:
        body = json.dumps(data, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_text(self, text: str, content_type: str, filename: str | None = None) -> None:
        body = text.encode("utf-8")
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        if filename:
            self.send_header("Content-Disposition", f'attachment; filename="{filename}"')
        self.end_headers()
        self.wfile.write(body)

    def send_file(self, path: Path) -> None:
        ctype = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        body = path.read_bytes()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def not_found(self, message: str = "not found") -> None:
        self.send_json({"error": message}, HTTPStatus.NOT_FOUND)

    def bad_request(self, message: str) -> None:
        self.send_json({"error": message}, HTTPStatus.BAD_REQUEST)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        path = parsed.path
        try:
            if path in {"/", "/assessment", "/assessment/"}:
                self.send_file(WEB_ROOT / "index.html")
                return
            if path.startswith("/assessment/"):
                requested = (WEB_ROOT / path.removeprefix("/assessment/")).resolve()
                if WEB_ROOT not in requested.parents and requested != WEB_ROOT:
                    self.bad_request("invalid static path")
                    return
                if requested.exists() and requested.is_file():
                    self.send_file(requested)
                    return
                self.not_found()
                return
            if path == "/api/homeworks":
                homeworks = sorted(item.name for item in ROOT.iterdir() if item.is_dir() and HW_RE.match(item.name))
                self.send_json({"homeworks": homeworks})
                return
            match = re.match(r"^/api/hw/(hw\d{2})/data$", path)
            if match:
                self.send_json(build_payload(match.group(1)))
                return
            match = re.match(r"^/api/hw/(hw\d{2})/scores$", path)
            if match:
                payload = build_payload(match.group(1))
                self.send_json(payload["scores"])
                return
            match = re.match(r"^/api/hw/(hw\d{2})/export.csv$", path)
            if match:
                self.send_text(csv_export(match.group(1)), "text/csv; charset=utf-8", f"{match.group(1)}_assessment_scores.csv")
                return
            if path == "/artifact":
                query = parse_qs(parsed.query)
                requested = query.get("path", [""])[0]
                if not requested:
                    self.bad_request("missing path")
                    return
                self.send_file(safe_artifact(requested))
                return
            self.not_found()
        except FileNotFoundError as exc:
            self.not_found(str(exc))
        except ValueError as exc:
            self.bad_request(str(exc))
        except Exception as exc:  # noqa: BLE001 - local tool should surface errors in browser.
            self.send_json({"error": str(exc)}, HTTPStatus.INTERNAL_SERVER_ERROR)

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        match = re.match(r"^/api/hw/(hw\d{2})/scores$", parsed.path)
        if not match:
            self.not_found()
            return
        length = int(self.headers.get("Content-Length", "0"))
        try:
            data = json.loads(self.rfile.read(length).decode("utf-8"))
            saved = save_scores(match.group(1), data)
            self.send_json(saved)
        except json.JSONDecodeError as exc:
            self.bad_request(f"invalid JSON: {exc}")
        except ValueError as exc:
            self.bad_request(str(exc))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    if not (WEB_ROOT / "index.html").exists():
        raise SystemExit(f"Missing web assets at {WEB_ROOT}")
    server = ThreadingHTTPServer((args.host, args.port), AssessmentHandler)
    print(f"Serving NE 630 assessment UI at http://{args.host}:{args.port}/assessment/?hw=hw01")
    server.serve_forever()


if __name__ == "__main__":
    main()
