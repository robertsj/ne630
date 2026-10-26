#!/usr/bin/env python3
"""Audit notebook-derived handouts against pinned notebook cells and stored outputs.

Checks source hashes, ordered cell provenance, code, ordered math, selected stored
output representations, and exact embedded image bytes. Math whitespace, font-size
commands, and equivalent dollar/bracket delimiters may differ. A stored rich result
may use its exact text/plain alternative. This is not an exhaustive prose comparison,
a notebook execution, a rendering check, or a verification of inherited physics.
"""
from __future__ import annotations

import argparse
import base64
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

from check_math_layout import math_layout_tokens

ROOT = Path(__file__).resolve().parent
CODE = re.compile(r"\\begin\{NEunicodecode\}(?:\[[^\]]*\])?\n?(.*?)\\end\{NEunicodecode\}", re.S)
FONT = re.compile(r"\\(?:tiny|scriptsize|footnotesize|small|normalsize|large|Large|LARGE|huge|Huge|"
                  r"displaystyle|textstyle|scriptstyle|scriptscriptstyle)\b")
TOKEN = re.compile(r"\\[A-Za-z@]+|\\.|[A-Za-z0-9]+|[^\s]", re.S)
MATH_START = re.compile(r"\\begin\{(?P<env>equation\*?|align\*?|alignat\*?|gather\*?|multline\*?|"
                        r"flalign\*?|displaymath)\}|\\(?P<bracket>[\[(])|(?P<dollar>\$\$?)|\\.", re.S)
FIGURE = re.compile(r"\\includegraphics\*?(?:\s*\[[^\]]*\])?\s*\{([^{}]+)\}")
MARKER = re.compile(r"^% Notebook source:\s*(?P<source>.*?)\s*$|"
                    r"^% Notebook cell (?P<cell>\d+) \((?P<kind>[^)]+)\)\s*$|"
                    r"^% End notebook cell (?P<end>\d+)\s*$", re.M)


def _text(value) -> str:
    return value if isinstance(value, str) else "".join(value)


def _uncomment(text: str) -> str:
    # Replace comments with spaces so all event offsets still refer to the input.
    return "\n".join(
        _uncomment_line(line) for line in text.split("\n"))


def _uncomment_line(line: str) -> str:
    for match in re.finditer("%", line):
        preceding = len(line[:match.start()]) - len(line[:match.start()].rstrip("\\"))
        if preceding % 2 == 0:
            return line[:match.start()] + " " * (len(line) - match.start())
    return line


def _tokens(text: str) -> tuple[str, ...]:
    return tuple(TOKEN.findall(FONT.sub("", _uncomment(text))))


def _code(text: str) -> tuple[str, ...]:
    return tuple(line.rstrip() for line in text.strip("\n").splitlines())


def _math(text: str, *, tex_comments: bool = True):
    """Return ordered (start, end, inline/display, tokens), skipping verbatim."""
    text = CODE.sub(lambda m: " " * len(m[0]), text)
    if tex_comments:
        text = _uncomment(text)
    result, pos = [], 0
    while match := MATH_START.search(text, pos):
        begin = match.end()
        if match["env"]:
            closing = r"\end{" + match["env"] + "}"
            end = text.find(closing, begin)
            kind = "display"
        elif match["bracket"]:
            closing = r"\]" if match["bracket"] == "[" else r"\)"
            end = text.find(closing, begin)
            kind = "display" if match["bracket"] == "[" else "inline"
        elif match["dollar"]:
            closing = match["dollar"]
            closing_matches = re.finditer(r"\\.|(?P<dollar>\$\$?)", text[begin:], re.S)
            candidate = next((m for m in closing_matches if m["dollar"]), None)
            if candidate is None or candidate["dollar"] != closing:
                raise ValueError("unclosed or mixed dollar-math delimiters")
            end = begin + candidate.start()
            kind = "display" if closing == "$$" else "inline"
        else:
            pos = begin
            continue
        if end < 0:
            raise ValueError(f"unclosed {closing} math delimiter")
        pos = end + len(closing)
        result.append((match.start(), pos, kind, math_layout_tokens(_tokens(text[begin:end]))))
    return result


def _group(text: str, pos: int):
    while pos < len(text) and text[pos].isspace():
        pos += 1
    if pos >= len(text) or text[pos] != "{":
        raise ValueError("expected braced metadata argument")
    begin, depth, pos = pos + 1, 1, pos + 1
    while pos < len(text):
        if text[pos] == "\\":
            token = re.match(r"\\(?:[A-Za-z@]+|.)", text[pos:], re.S)
            pos += len(token[0])
            continue
        if text[pos] == "{":
            depth += 1
        elif text[pos] == "}":
            depth -= 1
            if not depth:
                return text[begin:pos], pos + 1
        pos += 1
    raise ValueError("unbalanced metadata argument")


def _metadata(text: str):
    values = []
    for match in re.finditer(r"\\Lesson\b", _uncomment(text)):
        pos, args = match.end(), []
        for _ in range(4):
            value, pos = _group(text, pos)
            args.append(value)
        values.append(args)
    return values


def _blocks(text: str, source_paths: list[Path], root: Path):
    issues, blocks, opened = [], [], None
    active = source_paths[0] if len(source_paths) == 1 else None
    for marker in MARKER.finditer(text):
        if marker["source"] is not None:
            if opened:
                issues.append("notebook source marker appears inside a cell")
            active = (root / marker["source"]).resolve()
            if active not in source_paths:
                issues.append(f"unknown notebook source marker: {marker['source']}")
        elif marker["cell"] is not None:
            if opened:
                issues.append(f"notebook cell {opened[1]} is missing its end marker")
            if active is None:
                issues.append("cell marker lacks a notebook source")
            opened = (active, int(marker["cell"]), marker["kind"], marker.end())
        else:
            if opened is None:
                issues.append(f"unmatched end marker for notebook cell {marker['end']}")
                continue
            path, index, kind, begin = opened
            if index != int(marker["end"]):
                issues.append(f"notebook cell {index} has a mismatched end marker")
            blocks.append((path, index, kind, text[begin:marker.start()]))
            opened = None
    if opened:
        issues.append(f"notebook cell {opened[1]} is missing its end marker")
    return issues, blocks


def _events(block: str, root: Path):
    events = [(m.start(), "text", _code(m[1])) for m in CODE.finditer(block)]
    events.extend((start, "math", tokens) for start, _, _, tokens in _math(block))
    outside_code = CODE.sub(lambda m: " " * len(m[0]), _uncomment(block))
    events.extend((m.start(), "image", (root / m[1]).resolve()) for m in FIGURE.finditer(outside_code))
    return [(kind, payload) for _, kind, payload in sorted(events)]


def _asset_key(asset: dict, root: Path):
    kind = "attachment" if "attachment" in asset else "output"
    return ((root / asset["source"]).resolve(), asset["cell"], kind, asset[kind], asset.get("mime", "image/png"))


def audit_notebook(record: dict, root: Path) -> tuple[list[str], Counter]:
    """Return provenance/payload issues and counts for one notebook seed record."""
    root = root.resolve()
    issues, counts, notebooks, expected = [], Counter(), {}, []
    for source in record.get("notebook_sources", []):
        path = (root / source["source"]).resolve()
        try:
            raw = path.read_bytes()
            if hashlib.sha256(raw).hexdigest() != source["source_sha256"]:
                issues.append(f"notebook source SHA-256 differs: {source['source']}")
            notebook = json.loads(raw)
            notebooks[path] = notebook
            selected = source["cells"]
            if source.get("coverage") == "complete" and selected != list(range(len(notebook["cells"]))):
                issues.append(f"complete notebook coverage omits/reorders cells: {source['source']}")
            if len(selected) != len(set(selected)):
                issues.append(f"duplicate selected cell: {source['source']}")
            for index in selected:
                if not isinstance(index, int) or not 0 <= index < len(notebook["cells"]):
                    issues.append(f"invalid notebook cell index: {source['source']}:{index}")
                else:
                    expected.append((path, index, notebook["cells"][index]))
        except (OSError, ValueError, KeyError) as exc:
            issues.append(f"cannot read notebook {source['source']}: {exc}")
    for source in record.get("supplemental_sources", []):
        try:
            raw = (root / source["source"]).read_bytes()
            if hashlib.sha256(raw).hexdigest() != source["source_sha256"]:
                issues.append(f"supplemental source SHA-256 differs: {source['source']}")
        except OSError as exc:
            issues.append(f"cannot read supplemental source {source['source']}: {exc}")
    try:
        handout = (root / record["handout"]).read_text()
    except OSError as exc:
        return issues + [f"cannot read handout: {exc}"], counts
    found, blocks = _blocks(handout, list(notebooks), root)
    issues.extend(found)
    observed_order = [(path, index) for path, index, _, _ in blocks]
    if observed_order != [(path, index) for path, index, _ in expected]:
        issues.append("ordered notebook cell coverage differs from manifest")
    by_cell = {(path, index): (kind, block) for path, index, kind, block in blocks}
    assets = {}
    for asset in record.get("notebook_assets", []):
        try:
            key = _asset_key(asset, root)
            if key in assets:
                issues.append(f"duplicate notebook asset record: {asset['path']}")
            assets[key] = asset
        except KeyError as exc:
            issues.append(f"invalid notebook asset record: missing {exc}")
    used_assets = set()
    observed_counts = Counter(total=len(expected), nonempty=0, markdown=0, code=0,
                              stored_outputs=0, handout_sections=len(re.findall(r"\\Sec\s*\{", handout)))
    for path, index, cell in expected:
        label = f"{path.name} cell {index}"
        source = _text(cell.get("source", []))
        observed_counts["nonempty"] += bool(source.strip())
        observed_counts[cell["cell_type"]] += 1
        observed_counts["stored_outputs"] += len(cell.get("outputs", []))
        counts["cells"] += 1
        if (path, index) not in by_cell:
            continue
        kind, block = by_cell[path, index]
        if kind != cell["cell_type"]:
            issues.append(f"{label}: cell type differs")
        try:
            figures = [(root / m[1]).resolve() for m in FIGURE.finditer(CODE.sub("", _uncomment(block)))]
            expected_figures = []

            def image(kind, item, mime, data):
                key = (path, index, kind, item, mime)
                asset = assets.get(key)
                if asset is None:
                    issues.append(f"{label}: missing manifest asset for {kind} {item}")
                    return None
                used_assets.add(key)
                asset_path = (root / asset["path"]).resolve()
                from check_figure_assets import notebook_rendering
                rendered_path = notebook_rendering(asset, root)
                expected_figures.append(rendered_path)
                embedded = base64.b64decode(re.sub(r"\s+", "", _text(data)), validate=True)
                digest = hashlib.sha256(embedded).hexdigest()
                if digest != asset["sha256"]:
                    issues.append(f"{label}: embedded image SHA-256 differs from manifest: {asset['path']}")
                try:
                    if asset_path.read_bytes() != embedded:
                        issues.append(f"{label}: extracted image differs from notebook bytes: {asset['path']}")
                except OSError as exc:
                    issues.append(f"{label}: cannot read image {asset['path']}: {exc}")
                counts["figures"] += 1
                return rendered_path

            if cell["cell_type"] == "markdown":
                source_math = [(kind, tokens) for _, _, kind, tokens in _math(source, tex_comments=False)]
                actual_math = [(kind, tokens) for _, _, kind, tokens in _math(block)]
                if source_math != actual_math:
                    issues.append(f"{label}: ordered Markdown mathematics differ (source {len(source_math)}, handout {len(actual_math)})")
                counts.update(kind + " math" for kind, _ in source_math)
                for name in re.findall(r"\]\(attachment:([^)]*)\)", source):
                    attachment = cell.get("attachments", {}).get(name, {})
                    if "image/png" not in attachment:
                        issues.append(f"{label}: unsupported or missing attachment {name}")
                    else:
                        image("attachment", name, "image/png", attachment["image/png"])
            elif cell["cell_type"] == "code":
                events = _events(block, root)
                if source.strip():
                    if not events or events[0] != ("text", _code(source)):
                        issues.append(f"{label}: source code differs from first NEunicodecode block")
                    if events and events[0][0] == "text":
                        events = events[1:]
                    counts["code"] += 1
                for output_index, output in enumerate(cell.get("outputs", [])):
                    data = output.get("data", {})
                    alternatives = []
                    if "image/png" in data:
                        target = image("output", output_index, "image/png", data["image/png"])
                        alternatives = [[("image", target)]]
                    elif "text/latex" in data:
                        latex = _text(data["text/latex"])
                        math = [("math", tokens) for _, _, _, tokens in _math(latex)]
                        if math:
                            alternatives.append(math)
                        if "text/plain" in data:
                            alternatives.append([("text", _code(_text(data["text/plain"])))])
                    elif "text" in output:
                        value = _text(output["text"])
                        alternatives = [[("text", _code(value))]] if value else [[]]
                    elif "text/plain" in data:
                        alternatives = [[("text", _code(_text(data["text/plain"])))]]
                    else:
                        issues.append(f"{label}: unsupported stored output {output_index}")
                    selected = next((candidate for candidate in alternatives if events[:len(candidate)] == candidate), None)
                    if selected is None:
                        issues.append(f"{label}: stored output {output_index} differs or is missing")
                    else:
                        events = events[len(selected):]
                        counts["stored outputs"] += 1
                if events:
                    issues.append(f"{label}: extra or changed rendered output payloads")
            else:
                issues.append(f"{label}: unsupported source cell type {cell['cell_type']}")
            if figures != expected_figures:
                issues.append(f"{label}: ordered figure references differ from notebook assets")
        except (KeyError, ValueError) as exc:
            issues.append(f"{label}: cannot audit payloads: {exc}")
    if set(assets) != used_assets:
        issues.append("manifest contains unreferenced or unselected notebook assets")
    if "cell_counts" in record and dict(observed_counts) != record["cell_counts"]:
        issues.append(f"notebook cell/section counts differ from manifest: {dict(observed_counts)}")
    try:
        metadata = _metadata(handout)
        if len(metadata) != 1:
            issues.append("expected exactly one Lesson metadata command")
        else:
            number, title, reading, focus = metadata[0]
            if number != str(record["lesson"]) or " ".join(title.split()) != record["title"]:
                issues.append("handout lesson/title metadata differs from manifest")
            for name, value in (("reading", reading), ("focus", focus)):
                if name in record.get("metadata", {}) and _tokens(value) != _tokens(record["metadata"][name]):
                    issues.append(f"handout {name} metadata differs from manifest")
    except ValueError as exc:
        issues.append(f"cannot audit handout metadata: {exc}")
    counts["sections"] = observed_counts["handout_sections"]
    return issues, counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = json.loads((root / "seeded_lessons.json").read_text())
    failed = False
    for record in manifest["lessons"]:
        if record.get("source_kind") != "notebook":
            continue
        issues, counts = audit_notebook(record, root)
        print(f"L{record['lesson']:02d}: {'FAIL' if issues else 'PASS'} {dict(counts)}")
        for issue in issues:
            print(f"  {issue}")
        failed |= bool(issues)
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
