#!/usr/bin/env python3
"""Verify source provenance and substantive payloads in seeded Lessons 25--39.

Checks ordered, per-frame display/inline math, tags, complete tabular bodies,
verbatim code, and figure targets; expands zero-argument lesson notation aliases.
Notebook cell, stored-output, and embedded-image checks are delegated to
check_notebook_handouts.py.
Allows whitespace/font changes, frame-to-section conversion, minted-to-verbatim,
and the original prompt-drop PGF's single-image wrapper. This is intentionally
not a general TeX interpreter, an exhaustive prose comparison, a figure-data
validation, a PDF/rendering check, or a verification of inherited physics.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

from check_math_layout import math_layout_tokens

ROOT = Path(__file__).resolve().parent
CODE = re.compile(
    r"\\begin\{(?P<env>minted|lstlisting|NEunicodecode|verbatim|Verbatim)\}"
    r"(?:\[[^\]]*\])?(?:\{[^{}]*\})?(?P<body>.*?)\\end\{(?P=env)\}", re.S)
MATH_ENVS = r"equation\*?|align\*?|alignat\*?|gather\*?|multline\*?|flalign\*?|displaymath"
TOKEN = re.compile(r"\\[A-Za-z@]+|\\.|[A-Za-z0-9]+|[^\s]", re.S)
FONTS = re.compile(r"\\(?:tiny|scriptsize|footnotesize|small|normalsize|large|Large|"
                   r"LARGE|huge|Huge|displaystyle|textstyle|scriptstyle|scriptscriptstyle)\b")


def uncomment_plain(text: str) -> str:
    lines = []
    for line in text.splitlines():
        for i, char in enumerate(line):
            if char == "%":
                j = i
                while j and line[j - 1] == "\\":
                    j -= 1
                if (i - j) % 2 == 0:
                    line = line[:i]
                    break
        lines.append(line)
    return "\n".join(lines)


def uncomment(text: str) -> str:
    """Keep literal percent signs and other TeX-looking content inside code."""
    parts, end = [], 0
    for match in CODE.finditer(text):
        parts.extend((uncomment_plain(text[end:match.start()]), match[0]))
        end = match.end()
    return "".join(parts) + uncomment_plain(text[end:])


def group(text: str, pos: int, left: str = "{", right: str = "}") -> tuple[str, int]:
    while pos < len(text) and text[pos].isspace():
        pos += 1
    if pos >= len(text) or text[pos] != left:
        raise ValueError(f"Expected {left!r} near {text[pos:pos+40]!r}")
    start, depth, pos = pos + 1, 1, pos + 1
    while pos < len(text):
        if text[pos] == "\\":
            match = re.match(r"\\(?:[A-Za-z@]+|.)", text[pos:], re.S)
            pos += len(match[0]) if match else 1
            continue
        if text[pos] == left:
            depth += 1
        elif text[pos] == right:
            depth -= 1
            if depth == 0:
                return text[start:pos], pos + 1
        pos += 1
    raise ValueError("Unbalanced TeX group")


def calls(text: str, name: str, count: int):
    for match in re.finditer(r"\\(?:" + name + r")\b\*?", text):
        pos, values = match.end(), []
        while pos < len(text) and text[pos].isspace():
            pos += 1
        if pos < len(text) and text[pos] == "[":
            _, pos = group(text, pos, "[", "]")
        for _ in range(count):
            value, pos = group(text, pos)
            values.append(value)
        yield match.start(), pos, values


def aliases(text: str) -> dict[str, str]:
    result = {}
    preamble = text.split(r"\begin{document}", 1)[0]
    for match in re.finditer(r"\\(?:newcommand|renewcommand|providecommand)\*?\s*\{(\\[A-Za-z@]+)\}", preamble):
        pos = match.end()
        while pos < len(preamble) and preamble[pos].isspace():
            pos += 1
        if pos < len(preamble) and preamble[pos] == "{":
            result[match[1][1:]], _ = group(preamble, pos)
    return result


def normalized(text: str, macros: dict[str, str] | None = None) -> tuple[str, ...]:
    text = uncomment_plain(text)
    for _ in range(12):
        expanded = re.sub(r"\\([A-Za-z@]+)", lambda m: (macros or {}).get(m[1], m[0]), text)
        if expanded == text:
            break
        text = expanded
    else:
        raise ValueError("Recursive notation aliases")
    return tuple(TOKEN.findall(FONTS.sub("", text)))


def normalized_math(text, macros=None):
    return math_layout_tokens(normalized(text, macros))


def environments(text: str, names: str):
    for match in re.finditer(r"\\begin\{(" + names + r")\}", text):
        end = text.find(r"\end{" + match[1] + "}", match.end())
        if end < 0:
            raise ValueError(f"Unclosed {match[1]} environment")
        yield match.start(), end + len(match[1]) + 6, match[1], text[match.end():end]


def frames(text: str):
    result = []
    for match in re.finditer(r"\\begin\{frame\}(?:\[[^\]]*\])?", text):
        pos = match.end()
        while text[pos].isspace():
            pos += 1
        title = ""
        if text[pos] == "{":
            title, pos = group(text, pos)
        end = text.index(r"\end{frame}", pos)
        result.append((title, text[pos:end]))
    return result


def sections(text: str):
    headings = list(calls(text, "Sec", 2))
    end_document = text.index(r"\end{document}")
    return [(values[0], values[1], text[end:headings[i + 1][0] if i + 1 < len(headings) else end_document])
            for i, (_, end, values) in enumerate(headings)]


def figure_target(name: str, cwd: Path, seen: tuple[Path, ...] = ()) -> str:
    from check_figure_assets import figure_target as local_figure_target
    path = local_figure_target(cwd / name, ROOT)
    if not path.suffix:
        path = next((path.with_suffix(s) for s in (".pdf", ".png", ".pgf")
                     if path.with_suffix(s).is_file()), path)
    if not path.is_file() or not path.stat().st_size:
        raise ValueError(f"Missing or empty figure: {path}")
    if path in seen:
        raise ValueError(f"Recursive figure wrapper: {path}")
    if path.suffix == ".pgf":
        wrapper = uncomment(path.read_text()).strip()
        images = list(calls(wrapper, "includegraphics", 1))
        # One existing PGF is solely an includegraphics wrapper around its PNG.
        if len(images) == 1 and not wrapper[:images[0][0]].strip() and not wrapper[images[0][1]:].strip():
            return figure_target(images[0][2][0], cwd, seen + (path,))
    return str(path)


def payloads(text: str, macros: dict[str, str], cwd: Path) -> dict[str, list]:
    result = {"code": [tuple(line.rstrip() for line in m["body"].strip("\n").splitlines())
                       for m in CODE.finditer(text)]}
    text = CODE.sub("", text)
    displays = list(environments(text, MATH_ENVS))
    result["display math"] = [(kind, normalized_math(body, macros)) for _, _, kind, body in displays]
    result["tags"] = [normalized(values[0], macros) for _, _, values in calls(text, "tag", 1)]
    result["tables"] = [(kind, normalized(body, macros)) for _, _, kind, body in
                        environments(text, r"tabular\*?|tabularx|longtable")]
    from check_figure_assets import catalog
    figure_records = {(ROOT / r['path']).resolve(): r for r in catalog(ROOT)['figures'].values()}
    result['figures'] = []
    for start, end, values in calls(text, 'input|includegraphics', 1):
        target = Path(figure_target(values[0], cwd))
        pages = figure_records.get(target, {}).get('pages', 1)
        selected = re.search(r'\bpage\s*=\s*(\d+)', text[start:end])
        requested = [int(selected[1])] if selected else range(1, pages + 1)
        if any(page < 1 or page > pages for page in requested):
            raise ValueError('invalid handout figure page')
        result['figures'].extend(str(target) + (f'#page={page}' if pages > 1 else '') for page in requested)
    # Remove complete display environments before collecting inline dollar math.
    for start, end, _, _ in reversed(displays):
        text = text[:start] + text[end:]
    result["inline math"] = []
    for match in re.finditer(r"\\\[(.*?)\\\]|\\\((.*?)\\\)", text, re.S):
        result["inline math"].append(normalized_math(match[1] or match[2], macros))
    text = re.sub(r"\\\[.*?\\\]|\\\(.*?\\\)", "", text, flags=re.S)
    opening = None
    for match in re.finditer(r"\\.|(?P<dollar>\$\$?)", text, re.S):
        if not match["dollar"]:
            continue
        if opening is None:
            opening = match
        else:
            if opening["dollar"] != match["dollar"]:
                raise ValueError("Mixed dollar-math delimiters")
            result["inline math"].append(normalized_math(text[opening.end():match.start()], macros))
            opening = None
    if opening is not None:
        raise ValueError("Unclosed dollar math")
    return result


def compare_frame(source: tuple[str, str], handout: tuple[str, str, str],
                  source_macros: dict[str, str], handout_macros: dict[str, str],
                  source_dir: Path, handout_dir: Path) -> tuple[list[str], Counter]:
    number, title, body = handout
    issues = []
    if normalized(source[0], source_macros) != normalized(title, handout_macros):
        issues.append(f"section {number}: frame title differs")
    expected = payloads(source[1], source_macros, source_dir)
    actual = payloads(body, handout_macros, handout_dir)
    for kind, values in expected.items():
        if values != actual[kind]:
            first = next((i + 1 for i, pair in enumerate(zip(values, actual[kind]))
                          if pair[0] != pair[1]), min(len(values), len(actual[kind])) + 1)
            issues.append(f"section {number}: {kind} differ at item {first} "
                          f"(source {len(values)}, handout {len(actual[kind])})")
    return issues, Counter({kind: len(values) for kind, values in expected.items()})


def audit(record: dict, root: Path) -> tuple[list[str], Counter]:
    if record.get("source_kind") == "notebook":
        from check_notebook_handouts import audit_notebook
        return audit_notebook(record, root)
    source_path, handout_path = root / record["source"], root / record["handout"]
    raw = source_path.read_bytes()
    issues, counts = [], Counter()
    if hashlib.sha256(raw).hexdigest() != record["source_sha256"]:
        issues.append("source SHA-256 differs; reconcile the slide, handout, and manifest")
    source, handout = uncomment(raw.decode()), uncomment(handout_path.read_text())
    source_macros, handout_macros = aliases(source), aliases(handout)
    all_frames, all_sections = frames(source), sections(handout)
    title_count = sum(r"\titlepage" in body for _, body in all_frames)
    objective_count = sum(title == "Primary Objective" for title, _ in all_frames)
    substantive = [(title, body) for title, body in all_frames
                   if title != "Primary Objective" and r"\titlepage" not in body]
    observed = {"total": len(all_frames), "title": title_count,
                "primary_objective": objective_count, "substantive": len(substantive),
                "handout_sections": len(all_sections)}
    if observed != record["frame_counts"]:
        issues.append(f"frame/section counts differ from manifest: {observed}")
    if len(substantive) != len(all_sections):
        issues.append("substantive frame count differs from section count")
    metadata = list(calls(handout, "Lesson", 4))
    if len(metadata) != 1:
        issues.append("expected exactly one Lesson metadata command")
    else:
        number, title, _, focus = metadata[0][2]
        if number != str(record["lesson"]) or " ".join(title.split()) != record["title"]:
            issues.append("handout lesson/title metadata differs from manifest")
        objective = next(body for title, body in all_frames if title == "Primary Objective")
        quoted = objective.split(r"\begin{quote}", 1)[1].split(r"\end{quote}", 1)[0]
        quoted = next(calls(quoted, "textcolor", 2))[2][1]
        if normalized("Students will be able to " + quoted, source_macros) != normalized(focus, handout_macros):
            issues.append("primary objective differs from handout metadata")
    raw_title = next(calls(source, "title", 1))[2][0]
    internal = re.search(r"Lecture\s+(\d+)", raw_title)
    if (int(internal[1]) if internal else None) != record["source_internal_lesson"]:
        issues.append("source internal lesson label differs from manifest")
    source_title = re.sub(r"\\\\\s*\{\\small\\it NE 630 - Lecture \d+\}", "", raw_title)
    source_title = " ".join(source_title.replace(r"\\", " ").split())
    if source_title != record["title"]:
        issues.append("source title differs from manifest")
    duplicates = sorted((path for path in source_path.parent.glob("lecture_*.tex")
                         if int(path.stem.split("_")[-1]) < record["lesson"]
                         and path.read_bytes() == raw),
                        key=lambda p: int(p.stem.split("_")[-1]))
    duplicate = (root / record["duplicate_of"]).resolve() if record.get("duplicate_of") else None
    if duplicate != (duplicates[0].resolve() if duplicates else None):
        issues.append("duplicate-source relationship differs from manifest")
    if duplicate and not record.get("warnings"):
        issues.append("duplicate-source warning is missing")
    for index, (frame, section) in enumerate(zip(substantive, all_sections), 1):
        if section[0] != str(index):
            issues.append(f"section {index}: numbering differs")
        found, category_counts = compare_frame(frame, section, source_macros, handout_macros,
                                               source_path.parent, handout_path.parent)
        issues.extend(found)
        counts.update(category_counts)
    counts["sections"] = len(all_sections)
    return issues, counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="handouts directory")
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = json.loads((root / "seeded_lessons.json").read_text())
    records = manifest["lessons"]
    if [record["lesson"] for record in records] != list(range(25, 40)):
        parser.error("manifest must contain Lessons 25--39 exactly once, in order")
    slide_records = [r for r in records if r.get("source_kind") != "notebook"]
    notebook_records = [r for r in records if r.get("source_kind") == "notebook"]
    expected_totals = {
        "lessons": len(records),
        "slide_lessons": len(slide_records),
        "notebook_lessons": len(notebook_records),
        "source_frames": sum(r["frame_counts"]["total"] for r in slide_records),
        "substantive_frames": sum(r["frame_counts"]["substantive"] for r in slide_records),
        "notebook_cells": sum(r["cell_counts"]["total"] for r in notebook_records),
        "handout_sections": sum(r["frame_counts"]["handout_sections"] for r in slide_records)
        + sum(r["cell_counts"]["handout_sections"] for r in notebook_records),
    }
    if manifest["totals"] != expected_totals:
        parser.error("manifest totals are inconsistent")
    from check_figure_assets import catalog, check_layout_and_paths
    catalog(root)
    check_layout_and_paths(root)
    passed, counts = 0, Counter()
    for record in records:
        try:
            issues, category_counts = audit(record, root)
        except (OSError, ValueError, KeyError, StopIteration) as error:
            issues, category_counts = [str(error)], Counter()
        counts.update(category_counts)
        print(f"{'FAIL' if issues else 'PASS'} L{record['lesson']}")
        for issue in issues:
            print(f"  {issue}")
        passed += not issues
    print(f"{passed}/{len(records)} seeded lessons verified: " +
          ", ".join(f"{count} {kind}" for kind, count in sorted(counts.items())) + ".")
    print("Scope: provenance and ordered payload preservation; exhaustive prose, physics, figure data, "
          "and PDF appearance require separate review.")
    return passed != len(records)


if __name__ == "__main__":
    sys.exit(main())
