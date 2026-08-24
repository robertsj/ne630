#!/usr/bin/env python3
"""Build and validate the NE 630 CourseDog syllabus artifact.

The source stays in Markdown. This script strips source-maintenance comments,
checks that the source still covers K-State's Fall 2026 syllabus-policy
anchors, and emits:

- generated/syllabus-coursedog.md
- generated/coursedog-fields.tsv
- generated/coursedog-copy.html
- generated/coursedog-copy-fields.tsv
- generated/sections/*.md
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "syllabus.md"
DEFAULT_MARKDOWN = ROOT / "generated" / "syllabus-coursedog.md"
DEFAULT_FIELDS = ROOT / "generated" / "coursedog-fields.tsv"
DEFAULT_SECTIONS_DIR = ROOT / "generated" / "sections"
DEFAULT_COPY_PAGE = ROOT / "generated" / "coursedog-copy.html"
DEFAULT_COPY_FIELDS = ROOT / "generated" / "coursedog-copy-fields.tsv"

FIELD_RE = re.compile(r"<!--\s*coursedog-field:\s*(.*?)\s*-->", re.IGNORECASE)
FRONT_MATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n+", re.DOTALL)
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
MULTI_BLANK_RE = re.compile(r"\n{3,}")
PLACEHOLDER_RE = re.compile(r"\b(TBD|TODO|FIXME|INSERT)\b|\[[^\]]*(insert|tbd|update)[^\]]*\]", re.IGNORECASE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
LIST_ITEM_RE = re.compile(r"\s*(?:[-+*]|\d+[.)])\s+")
TABLE_RE = re.compile(r"\s*\|.*")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
URL_RE = re.compile(r"(?<![\"'>])(https?://[^\s<]+)")

REQUIRED_FIELDS = [
    "Course Information",
    "Instructor Information",
    "Course Description",
    "Required Materials",
    "Canvas and Communications",
    "Student Resources",
    "Learning Outcomes",
    "Assessment and Grading",
    "Course Policies",
    "Course Roadmap",
    "University Statements",
]

REQUIRED_PHRASES = {
    "CourseDog official repository": "coursedog",
    "Canvas LMS": "canvas",
    "student learning outcomes": "student learning outcomes",
    "grading scale": "grading scale",
    "attendance policy": "attendance",
    "late or make-up policy": "late",
    "AI policy": "generative ai",
    "Honor Pledge": "on my honor",
    "Student Access Center": "student access center",
    "campus safety statement category": "campus safety",
    "student resources": "student support",
}


def read_source(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"source file not found: {path}")
    return path.read_text(encoding="utf-8")


def strip_front_matter(text: str) -> str:
    return FRONT_MATTER_RE.sub("", text, count=1)


def clean_markdown(text: str) -> str:
    text = strip_front_matter(text)
    text = COMMENT_RE.sub("", text)
    text = MULTI_BLANK_RE.sub("\n\n", text)
    return unwrap_soft_line_breaks(text)


def unwrap_soft_line_breaks(text: str) -> str:
    """Remove source-editor hard wraps while preserving Markdown block structure."""
    output: list[str] = []
    paragraph: list[str] = []
    in_code_fence = False

    def flush_paragraph() -> None:
        if paragraph:
            output.append(" ".join(line.strip() for line in paragraph))
            paragraph.clear()

    def append_blank() -> None:
        if output and output[-1] != "":
            output.append("")

    for line in text.strip().splitlines():
        stripped = line.strip()

        if in_code_fence:
            output.append(line.rstrip())
            if stripped.startswith("```") or stripped.startswith("~~~"):
                in_code_fence = False
            continue

        if not stripped:
            flush_paragraph()
            append_blank()
            continue

        if stripped.startswith("```") or stripped.startswith("~~~"):
            flush_paragraph()
            output.append(line.rstrip())
            in_code_fence = True
            continue

        if stripped.startswith(">"):
            flush_paragraph()
            output.append(line.rstrip())
            continue

        if HEADING_RE.fullmatch(stripped) or TABLE_RE.fullmatch(line) or re.fullmatch(r"[-*_]{3,}", stripped):
            flush_paragraph()
            output.append(line.rstrip())
            continue

        if LIST_ITEM_RE.match(line):
            flush_paragraph()

        paragraph.append(line)

    flush_paragraph()
    return "\n".join(output).strip() + "\n"


def split_fields(text: str) -> list[tuple[str, str]]:
    text = strip_front_matter(text)
    matches = list(FIELD_RE.finditer(text))
    fields: list[tuple[str, str]] = []

    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        name = match.group(1).strip()
        body = COMMENT_RE.sub("", text[start:end]).strip()
        fields.append((name, unwrap_soft_line_breaks(MULTI_BLANK_RE.sub("\n\n", body)).strip()))

    return fields


def block_after_heading(text: str, title: str, level: int) -> str:
    """Return one Markdown heading block, including the heading line."""
    lines = text.splitlines()
    start: int | None = None

    for index, line in enumerate(lines):
        match = HEADING_RE.match(line.strip())
        if match and len(match.group(1)) == level and match.group(2).strip() == title:
            start = index
            break

    if start is None:
        return ""

    end = len(lines)
    for index in range(start + 1, len(lines)):
        match = HEADING_RE.match(lines[index].strip())
        if match and len(match.group(1)) <= level:
            end = index
            break

    return "\n".join(lines[start:end]).strip()


def strip_first_heading(text: str) -> str:
    lines = text.strip().splitlines()
    if lines and HEADING_RE.match(lines[0].strip()):
        lines = lines[1:]
    return "\n".join(lines).strip()


def normalize_section(text: str) -> str:
    return text.strip() + "\n" if text.strip() else ""


def slice_from(text: str, start: str, end: str | None = None) -> str:
    start_index = text.find(start)
    if start_index == -1:
        return ""
    end_index = text.find(end, start_index) if end else len(text)
    if end_index == -1:
        end_index = len(text)
    return text[start_index:end_index].strip()


def combine_sections(*sections: str) -> str:
    return "\n\n".join(section.strip() for section in sections if section.strip())


def render_inline(markdown: str) -> str:
    escaped = html.escape(markdown, quote=False)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", escaped)
    escaped = re.sub(r"_(.+?)_", r"<em>\1</em>", escaped)
    escaped = LINK_RE.sub(
        lambda match: (
            f'<a href="{html.escape(match.group(2), quote=True)}">'
            f"{html.escape(match.group(1))}</a>"
        ),
        escaped,
    )
    escaped = URL_RE.sub(
        lambda match: f'<a href="{html.escape(match.group(1), quote=True)}">{html.escape(match.group(1))}</a>',
        escaped,
    )
    return escaped


def render_table(lines: list[str]) -> str:
    rows: list[list[str]] = []
    for line in lines:
        stripped = line.strip().strip("|")
        cells = [cell.strip() for cell in stripped.split("|")]
        rows.append(cells)

    if len(rows) < 2:
        return "".join(f"<p>{render_inline(line)}</p>" for line in lines)

    header = rows[0]
    body = rows[2:]
    parts = ["<table>", "<thead>", "<tr>"]
    parts.extend(f"<th>{render_inline(cell)}</th>" for cell in header)
    parts.extend(["</tr>", "</thead>", "<tbody>"])
    for row in body:
        parts.append("<tr>")
        parts.extend(f"<td>{render_inline(cell)}</td>" for cell in row)
        parts.append("</tr>")
    parts.extend(["</tbody>", "</table>"])
    return "\n".join(parts)


def basic_markdown_to_html(markdown: str) -> str:
    """Small fallback renderer for CourseDog copy snippets if pandoc is absent."""
    lines = markdown.strip().splitlines()
    output: list[str] = []
    index = 0

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()

        if not stripped:
            index += 1
            continue

        if stripped.startswith("|"):
            table_lines: list[str] = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                table_lines.append(lines[index])
                index += 1
            output.append(render_table(table_lines))
            continue

        if re.match(r"[-+*]\s+", stripped):
            items: list[str] = []
            while index < len(lines):
                match = re.match(r"[-+*]\s+(.*)", lines[index].strip())
                if not match:
                    break
                items.append(match.group(1))
                index += 1
            output.append("<ul>")
            output.extend(f"<li>{render_inline(item)}</li>" for item in items)
            output.append("</ul>")
            continue

        if re.match(r"\d+[.)]\s+", stripped):
            items = []
            while index < len(lines):
                match = re.match(r"\d+[.)]\s+(.*)", lines[index].strip())
                if not match:
                    break
                items.append(match.group(1))
                index += 1
            output.append("<ol>")
            output.extend(f"<li>{render_inline(item)}</li>" for item in items)
            output.append("</ol>")
            continue

        paragraph: list[str] = []
        while index < len(lines):
            candidate = lines[index].strip()
            if not candidate:
                break
            if candidate.startswith("|") or re.match(r"[-+*]\s+", candidate) or re.match(r"\d+[.)]\s+", candidate):
                break
            paragraph.append(candidate)
            index += 1
        output.append(f"<p>{render_inline(' '.join(paragraph))}</p>")

    return "\n".join(output).strip()


def find_pandoc() -> str | None:
    found = shutil.which("pandoc")
    if found:
        return found

    sibling = Path(sys.executable).with_name("pandoc")
    if sibling.exists():
        return str(sibling)

    return None


def markdown_to_html(markdown: str) -> str:
    pandoc = find_pandoc()
    if pandoc:
        try:
            completed = subprocess.run(
                [pandoc, "--from", "gfm", "--to", "html"],
                input=markdown,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True,
            )
            return completed.stdout.strip()
        except (OSError, subprocess.CalledProcessError):
            pass

    return basic_markdown_to_html(markdown)


def course_description_sections(course_description: str) -> tuple[str, str]:
    match = re.search(r"Catalog description:\s*(.*?)(?:\n\n|$)", course_description, re.DOTALL)
    catalog_description = match.group(1).replace("\n", " ").strip() if match else course_description
    additional = course_description
    if match:
        additional = (course_description[: match.start()] + course_description[match.end() :]).strip()
    return catalog_description, additional


def build_standalone_sections(cleaned: str) -> list[tuple[str, str, str]]:
    course_info = strip_first_heading(block_after_heading(cleaned, "Course Information", 2))
    instructor_info = strip_first_heading(block_after_heading(cleaned, "Instructor Information", 2))
    course_description = strip_first_heading(block_after_heading(cleaned, "Course Description", 2))
    catalog_description, additional_course_info = course_description_sections(course_description)
    required_materials = strip_first_heading(block_after_heading(cleaned, "Required Materials", 2))
    canvas = strip_first_heading(block_after_heading(cleaned, "Canvas and Communications", 2))
    student_resources = strip_first_heading(block_after_heading(cleaned, "Student Resources", 2))
    outcomes = strip_first_heading(block_after_heading(cleaned, "Student Learning Outcomes", 2))
    assessment = strip_first_heading(block_after_heading(cleaned, "Assessment and Grading", 2))
    attendance = strip_first_heading(block_after_heading(cleaned, "Attendance", 3))
    late_work = strip_first_heading(block_after_heading(cleaned, "Late Work and Make-Up Work", 3))
    collaboration = strip_first_heading(block_after_heading(cleaned, "Collaboration", 3))
    ai_policy = strip_first_heading(block_after_heading(cleaned, "Artificial Intelligence and Technology Use", 3))
    course_materials = strip_first_heading(block_after_heading(cleaned, "Course Materials", 3))
    syllabus_changes = strip_first_heading(block_after_heading(cleaned, "Syllabus Changes", 3))
    roadmap = strip_first_heading(block_after_heading(cleaned, "Course Roadmap", 2))
    university_statements = strip_first_heading(block_after_heading(cleaned, "Mandatory University Statements", 2))

    assessment_methods_start = "### Homework" if "### Homework" in assessment else "Homework is assigned regularly."
    grading_weights = slice_from(assessment, "Final grades are based on:", "The default grading scale is:")
    grading_scale = slice_from(assessment, "The default grading scale is:", "I may lower grade thresholds")
    threshold_policy = slice_from(assessment, "I may lower grade thresholds", assessment_methods_start)
    assessment_methods = slice_from(assessment, assessment_methods_start)

    return [
        ("course-information.md", "Course Information", course_info),
        ("course-instructor-information.md", "Course Instructor Information", instructor_info),
        ("course-description.md", "Course Description", catalog_description),
        ("additional-course-information.md", "Additional Course Information", additional_course_info),
        ("required-course-materials.md", "Required Course Materials", required_materials),
        ("canvas-course-link.md", "Canvas Course Link", canvas),
        ("student-learning-outcomes.md", "Student Learning Outcomes", outcomes),
        ("grading-scale.md", "Grading Scale", grading_scale),
        (
            "course-specific-grading-policies-and-procedures.md",
            "Course Specific Grading Policies and Procedures",
            combine_sections(grading_weights, threshold_policy),
        ),
        ("assessments-and-evaluation-methods.md", "Assessments and Evaluation Methods", assessment_methods),
        ("ai-policy.md", "AI Policy", ai_policy),
        ("course-attendance-policies-and-procedures.md", "Course Attendance Policies and Procedures", attendance),
        ("late-submission-policy-make-up-class-policy.md", "Late Submission Policy / Make-up class policy", late_work),
        ("course-specific-policy-regarding-academic-honesty.md", "Course Specific Policy Regarding Academic Honesty", collaboration),
        (
            "additional-course-specific-policies.md",
            "Additional Course Specific Policies",
            combine_sections(course_materials, syllabus_changes),
        ),
        ("student-resources-available.md", "Student Resources Available", student_resources),
        (
            "course-schedule-of-activities.md",
            "Anticipated Course Schedule and Outline (Subject to change to best fit needs of students and course learning outcomes)",
            roadmap,
        ),
        ("course-specific-language.md", "Course Specific Language", university_statements),
    ]


def validate(cleaned: str, fields: list[tuple[str, str]]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    field_names = {name for name, _body in fields}
    missing_fields = [name for name in REQUIRED_FIELDS if name not in field_names]
    for name in missing_fields:
        errors.append(f"missing CourseDog field marker: {name}")

    lowered = cleaned.lower()
    for label, phrase in REQUIRED_PHRASES.items():
        if phrase.lower() not in lowered:
            errors.append(f"missing required policy/content anchor: {label}")

    placeholders = sorted({match.group(0) for match in PLACEHOLDER_RE.finditer(cleaned)})
    for placeholder in placeholders:
        warnings.append(f"possible unresolved placeholder: {placeholder}")

    return errors, warnings


def write_markdown(path: Path, cleaned: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(cleaned, encoding="utf-8")


def write_fields(path: Path, fields: list[tuple[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["coursedog_field", "markdown"])
        for name, body in fields:
            writer.writerow([name, body])


def write_standalone_sections(sections_dir: Path, sections: list[tuple[str, str, str]]) -> None:
    sections_dir.mkdir(parents=True, exist_ok=True)
    for filename, _label, body in sections:
        if not body.strip():
            continue
        (sections_dir / filename).write_text(normalize_section(body), encoding="utf-8")


def write_sections_index(path: Path, sections: list[tuple[str, str, str]], sections_dir: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["coursedog_field", "markdown_file"])
        for filename, label, body in sections:
            if body.strip():
                writer.writerow([label, str((sections_dir / filename).relative_to(ROOT))])


def write_copy_page(path: Path, sections: list[tuple[str, str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    cards: list[str] = []

    for filename, label, body in sections:
        if not body.strip():
            continue

        slug = Path(filename).stem
        cards.append(
            f"""
<article class="field" id="{html.escape(slug, quote=True)}">
  <header class="field-header">
    <div>
      <p class="kicker">CourseDog field</p>
      <h2>{html.escape(label)}</h2>
      <p class="filename">{html.escape(filename)}</p>
    </div>
    <div class="actions">
      <button type="button" data-action="copy-rich">Copy rich text</button>
      <button type="button" data-action="copy-markdown">Copy Markdown</button>
    </div>
  </header>
  <p class="status" aria-live="polite"></p>
  <div class="field-body">
{markdown_to_html(body)}
  </div>
  <details>
    <summary>Markdown source</summary>
    <textarea readonly>{html.escape(body)}</textarea>
  </details>
</article>"""
        )

    page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>NE 630 CourseDog Copy Board</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f6f7f9;
      --panel: #ffffff;
      --ink: #1b1f24;
      --muted: #5d6773;
      --line: #d7dde5;
      --accent: #2451a6;
      --accent-dark: #17356d;
      --ok: #1c6b45;
      --warn: #8a4d00;
    }}
    * {{
      box-sizing: border-box;
    }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--ink);
      font: 16px/1.5 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}
    main {{
      width: min(1120px, calc(100% - 32px));
      margin: 0 auto;
      padding: 32px 0 56px;
    }}
    .page-header {{
      margin-bottom: 24px;
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: clamp(1.8rem, 2.7vw, 2.6rem);
      line-height: 1.1;
      letter-spacing: 0;
    }}
    h2 {{
      margin: 0;
      font-size: 1.1rem;
      line-height: 1.25;
      letter-spacing: 0;
    }}
    p {{
      margin: 0 0 1rem;
    }}
    .note {{
      max-width: 78ch;
      color: var(--muted);
    }}
    .field {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      margin: 16px 0;
      overflow: hidden;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
    }}
    .field-header {{
      display: flex;
      align-items: start;
      justify-content: space-between;
      gap: 16px;
      padding: 16px 18px;
      border-bottom: 1px solid var(--line);
      background: #fbfcfe;
    }}
    .kicker {{
      margin: 0 0 2px;
      color: var(--muted);
      font-size: 0.76rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }}
    .filename {{
      margin: 4px 0 0;
      color: var(--muted);
      font-size: 0.88rem;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    }}
    .actions {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      justify-content: flex-end;
    }}
    button {{
      appearance: none;
      border: 1px solid var(--accent);
      border-radius: 6px;
      background: var(--accent);
      color: #fff;
      cursor: pointer;
      font: inherit;
      font-weight: 650;
      min-height: 36px;
      padding: 7px 11px;
    }}
    button + button {{
      background: #fff;
      color: var(--accent);
    }}
    button:hover,
    button:focus {{
      border-color: var(--accent-dark);
      outline: 2px solid rgba(36, 81, 166, 0.18);
      outline-offset: 1px;
    }}
    .status {{
      min-height: 1.4rem;
      margin: 0;
      padding: 8px 18px 0;
      color: var(--ok);
      font-size: 0.92rem;
    }}
    .status.warn {{
      color: var(--warn);
    }}
    .field-body {{
      padding: 12px 18px 18px;
    }}
    .field-body > :first-child {{
      margin-top: 0;
    }}
    .field-body > :last-child {{
      margin-bottom: 0;
    }}
    ul,
    ol {{
      padding-left: 1.35rem;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 0.75rem 0 1rem;
    }}
    th,
    td {{
      border: 1px solid var(--line);
      padding: 6px 8px;
      text-align: left;
      vertical-align: top;
    }}
    th {{
      background: #eef2f7;
      font-weight: 700;
    }}
    a {{
      color: var(--accent);
    }}
    details {{
      border-top: 1px solid var(--line);
      padding: 10px 18px 14px;
      background: #fbfcfe;
    }}
    summary {{
      cursor: pointer;
      color: var(--muted);
      font-weight: 650;
    }}
    textarea {{
      width: 100%;
      min-height: 140px;
      margin-top: 10px;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 10px;
      font: 0.9rem/1.45 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      resize: vertical;
    }}
    @media (max-width: 720px) {{
      main {{
        width: min(100% - 20px, 1120px);
        padding-top: 18px;
      }}
      .field-header {{
        display: block;
      }}
      .actions {{
        justify-content: flex-start;
        margin-top: 12px;
      }}
    }}
  </style>
</head>
<body>
  <main>
    <header class="page-header">
      <h1>NE 630 CourseDog Copy Board</h1>
      <p class="note">Generated from <code>administrivia/syllabus.md</code>. Click <strong>Copy rich text</strong>, then paste into the matching CourseDog WYSIWYG box. If the browser blocks clipboard access, the rendered field will be selected so Ctrl+C can copy it.</p>
    </header>
{''.join(cards)}
  </main>
  <script>
    function setStatus(field, message, warn) {{
      const status = field.querySelector(".status");
      status.textContent = message;
      status.classList.toggle("warn", Boolean(warn));
    }}

    function selectElementContents(element) {{
      const range = document.createRange();
      range.selectNodeContents(element);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
    }}

    function copySelection(element) {{
      selectElementContents(element);
      try {{
        const copied = document.execCommand("copy");
        if (copied) {{
          window.getSelection().removeAllRanges();
        }}
        return copied;
      }} catch (error) {{
        return false;
      }}
    }}

    async function copyRich(button) {{
      const field = button.closest(".field");
      const body = field.querySelector(".field-body");
      const htmlText = body.innerHTML.trim();
      const plainText = body.innerText.trim();

      try {{
        if (navigator.clipboard && window.ClipboardItem) {{
          await navigator.clipboard.write([
            new ClipboardItem({{
              "text/html": new Blob([htmlText], {{ type: "text/html" }}),
              "text/plain": new Blob([plainText], {{ type: "text/plain" }})
            }})
          ]);
          setStatus(field, "Copied rich text.");
          return;
        }}
      }} catch (error) {{
      }}

      if (copySelection(body)) {{
        setStatus(field, "Copied rich text.");
      }} else {{
        selectElementContents(body);
        setStatus(field, "Selected rendered content. Press Ctrl+C, then paste into CourseDog.", true);
      }}
    }}

    async function copyMarkdown(button) {{
      const field = button.closest(".field");
      const textarea = field.querySelector("textarea");

      try {{
        if (navigator.clipboard) {{
          await navigator.clipboard.writeText(textarea.value.trim());
          setStatus(field, "Copied Markdown.");
          return;
        }}
      }} catch (error) {{
      }}

      textarea.focus();
      textarea.select();
      if (document.execCommand("copy")) {{
        setStatus(field, "Copied Markdown.");
      }} else {{
        setStatus(field, "Selected Markdown. Press Ctrl+C.", true);
      }}
    }}

    document.addEventListener("click", function (event) {{
      const button = event.target.closest("button[data-action]");
      if (!button) {{
        return;
      }}
      if (button.dataset.action === "copy-rich") {{
        copyRich(button);
      }}
      if (button.dataset.action === "copy-markdown") {{
        copyMarkdown(button);
      }}
    }});
  </script>
</body>
</html>
"""
    path.write_text(page, encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    parser.add_argument("--fields-out", type=Path, default=DEFAULT_FIELDS)
    parser.add_argument("--sections-dir", type=Path, default=DEFAULT_SECTIONS_DIR)
    parser.add_argument("--copy-page-out", type=Path, default=DEFAULT_COPY_PAGE)
    parser.add_argument("--copy-fields-out", "--sections-index", dest="copy_fields_out", type=Path, default=DEFAULT_COPY_FIELDS)
    parser.add_argument("--check-only", action="store_true", help="validate without writing generated files")
    parser.add_argument("--fail-on-warning", action="store_true", help="treat placeholder warnings as failures")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    source = args.source.resolve()
    raw = read_source(source)
    cleaned = clean_markdown(raw)
    fields = split_fields(raw)
    standalone_sections = build_standalone_sections(cleaned)
    errors, warnings = validate(cleaned, fields)

    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 2

    if warnings and args.fail_on_warning:
        return 3

    if not args.check_only:
        write_markdown(args.markdown_out.resolve(), cleaned)
        write_fields(args.fields_out.resolve(), fields)
        sections_dir = args.sections_dir.resolve()
        write_standalone_sections(sections_dir, standalone_sections)
        write_sections_index(args.copy_fields_out.resolve(), standalone_sections, sections_dir)
        write_copy_page(args.copy_page_out.resolve(), standalone_sections)

    stamp = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    print(f"validated {source}")
    if not args.check_only:
        print(f"wrote {args.markdown_out.resolve()}")
        print(f"wrote {args.fields_out.resolve()}")
        print(f"wrote {args.copy_page_out.resolve()}")
        print(f"wrote {args.copy_fields_out.resolve()}")
        print(f"wrote raw field Markdown in {args.sections_dir.resolve()}")
    print(f"completed {stamp}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
