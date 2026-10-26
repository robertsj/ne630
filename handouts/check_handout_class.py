#!/usr/bin/env python3
"""Build canonical handouts and check the shared class API without modifying them.

Compile from the source directory so relative slide/figure paths resolve normally.
All variants, PDFs, and compiler products stay in an isolated temporary directory.
Layout notices and page counts are reported; no page limit is imposed.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import time

ROOT = Path(__file__).resolve().parent
CLASS_RE = re.compile(r"\\documentclass\s*(?:\[([^\]]*)\])?\s*\{ne630handout\}")
FALSE_RE = re.compile(r"\\handoutsolutionsfalse\b")
ERROR_RE = re.compile(
    r"Missing character:|Undefined control sequence|Undefined color|"
    r"There were undefined references|^!\s", re.I | re.M)
SECRET_MARKERS = (
    "NE630RevealSecret", "MathSecret", "NE630CueSecret",
    "NE630FigureSecret", "NE630ConditionalSecret")
CODE_LINES = (
    "def step(ρ, β, Λ, λ):", "ω = (ρ - β)/Λ", "return ω + λ")
API_SOURCE = r"""\documentclass{ne630handout}
\handoutsolutionsfalse
\begin{document}
\Lesson{00}{Shared class API check}{Compatibility fixture.}{NE630CommonVisible}
\Sec{1}{Roles, equations, and breakable boxes}
\begin{KeyBox}{Reference API}[breakable]
\Primary{Primary}; \Alert{Alert}; \Example{Example};
\textcolor{KSUPurple}{legacy color}; \nucl{235}{U}.
\[
  1\unit{cm}=1\,\si{\centi\meter},\qquad
  \sfrac{1}{2}+\cancelto{0}{0}=\frac12.
\]
\end{KeyBox}
\begin{boardbox}{Writing space}[breakable]
\Blank[.5in]\quad\RevealBlank[1.8in]{NE630RevealSecret}\quad
\MathBlank[1.5in]{\mathrm{MathSecret}}
\RuledLines{1}
\end{boardbox}
\begin{checkpoint}[Solution visibility][breakable]
\SolutionCue{NE630CueSecret}
\SolutionFigureContent{NE630FigureSecret\par}
\ifhandoutsolutions NE630ConditionalSecret\else NE630StudentVisible\fi
\end{checkpoint}
\begin{takeawaybox}[Shared synthesis][breakable]
The same source supports student and instructor modes.
\end{takeawaybox}
\Sec{2}{Python styles and Unicode identifiers}
\begin{lstlisting}[style=NEpython]
def square(x):
    return x*x
\end{lstlisting}
\begin{NEunicodecode}
def step(ρ, β, Λ, λ):
    ω = (ρ - β)/Λ
    return ω + λ
\end{NEunicodecode}
\end{document}
"""


@dataclass(frozen=True)
class BuildCase:
    name: str
    source: Path
    variant: str
    lesson: int | None = None
    api: bool = False


def without_comments(source: str) -> str:
    return re.sub(r"(?<!\\)%[^\n]*", "", source)


def requested_lessons(values: list[str], available: set[int]) -> set[int]:
    """Accept 1 22,25-27 L30 without requiring zero padding."""
    selected: set[int] = set()
    for value in values:
        for token in value.split(","):
            match = re.fullmatch(r"[Ll]?(\d{1,2})(?:-[Ll]?(\d{1,2}))?", token.strip())
            if not match:
                raise ValueError(f"invalid lesson selector: {token!r}")
            first, last = int(match[1]), int(match[2] or match[1])
            if first > last:
                raise ValueError(f"descending lesson range: {token!r}")
            selected.update(range(first, last + 1))
    missing = selected - available
    if missing:
        raise ValueError("no canonical wrapper for " +
                         ", ".join(f"L{n:02}" for n in sorted(missing)))
    return selected


def instructor_source(source: str) -> str:
    """Change only the wrapper's uncommented student-mode declaration."""
    for match in FALSE_RE.finditer(source):
        line_start = source.rfind("\n", 0, match.start()) + 1
        if not re.search(r"(?<!\\)%", source[line_start:match.start()]):
            return source[:match.start()] + r"\handoutsolutionstrue" + source[match.end():]
    raise ValueError("no uncommented handoutsolutionsfalse declaration")


def fallback_source(source: str) -> str:
    match = CLASS_RE.search(source)
    if match is None:
        raise ValueError("wrapper does not load ne630handout directly")
    options = [item.strip() for item in (match[1] or "").split(",") if item.strip()]
    if "fallbackfonts" not in options:
        options.append("fallbackfonts")
    declaration = r"\documentclass[" + ",".join(options) + r"]{ne630handout}"
    return source[:match.start()] + declaration + source[match.end():]


def diagnostics(log: str) -> tuple[list[str], list[str]]:
    errors = [line.strip() for line in log.splitlines() if ERROR_RE.search(line)]
    # References/citations can wrap across lines. Stop at the next blank line.
    for match in re.finditer(
        r"LaTeX Warning:\s*(?:Reference|Citation)\b"
        r"(?:(?!\n\s*\n).){0,300}?\bundefined\b[^\n]*",
        log, re.I | re.S,
    ):
        errors.append(" ".join(match[0].split()))
    notices = [line.strip() for line in log.splitlines()
               if re.search(r"\b(?:Overfull|Underfull)\b", line)]
    return list(dict.fromkeys(errors)), notices


def build_case(case: BuildCase, build: Path) -> dict:
    output = build / "builds" / case.name
    output.mkdir(parents=True)
    command = [
        "latexmk", "-norc", "-xelatex", "-interaction=nonstopmode",
        "-halt-on-error", "-file-line-error", f"-outdir={output}",
        f"-jobname={case.name}", str(case.source)]
    environment = os.environ.copy()
    environment["TEXINPUTS"] = str(ROOT) + os.pathsep + environment.get("TEXINPUTS", "")
    started = time.monotonic()
    errors, returncode = [], None
    try:
        process = subprocess.run(
            command, cwd=ROOT, env=environment, capture_output=True,
            text=True, errors="replace", timeout=240)
        returncode, console = process.returncode, process.stdout + process.stderr
        if returncode:
            errors.append(f"latexmk exited with status {returncode}")
    except subprocess.TimeoutExpired as exc:
        def decoded(value: str | bytes | None) -> str:
            return value.decode(errors="replace") if isinstance(value, bytes) else value or ""
        console = decoded(exc.stdout) + decoded(exc.stderr)
        errors.append("build exceeded 240 seconds")
    except OSError as exc:
        console = str(exc)
        errors.append(f"could not execute latexmk: {exc}")
    (output / "console.txt").write_text(console)
    log_path = output / (case.name + ".log")
    log = log_path.read_text(errors="replace") if log_path.exists() else ""
    if not log_path.exists():
        errors.append("LaTeX did not produce a log")
    log_errors, notices = diagnostics(log)
    errors.extend(log_errors)
    pdf, pages = output / (case.name + ".pdf"), None
    if pdf.exists():
        info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True)
        match = re.search(r"^Pages:\s+(\d+)\s*$", info.stdout, re.M)
        if info.returncode or match is None:
            errors.append("pdfinfo could not determine the page count")
        else:
            pages = int(match[1])
    else:
        errors.append("LaTeX did not produce a PDF")
    if case.api and pdf.exists():
        text_path = output / "text.txt"
        extracted = subprocess.run(
            ["pdftotext", "-layout", str(pdf), str(text_path)],
            capture_output=True, text=True)
        if extracted.returncode:
            errors.append("pdftotext could not inspect the class API fixture")
        else:
            text = text_path.read_text()
            if "NE630CommonVisible" not in text:
                errors.append("API fixture's common content is missing")
            for marker in SECRET_MARKERS:
                if (marker in text) != (case.variant == "instructor"):
                    errors.append(f"incorrect {case.variant} visibility for {marker}")
            if ("NE630StudentVisible" in text) != (case.variant == "public"):
                errors.append("API fixture's student-only branch has incorrect visibility")
            lines = {line.strip() for line in text.splitlines()}
            for line in CODE_LINES:
                if line not in lines:
                    errors.append(f"Unicode code was lost or reordered: {line}")
    return {
        "name": case.name, "lesson": case.lesson, "variant": case.variant,
        "source": str(case.source), "api": case.api, "ok": not errors,
        "returncode": returncode, "pages": pages,
        "elapsed_seconds": round(time.monotonic() - started, 2),
        "errors": errors, "layout_notices": notices,
        "overfull_count": sum("Overfull" in line for line in notices),
        "underfull_count": sum("Underfull" in line for line in notices),
        "output_directory": str(output), "command": command}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lessons", nargs="+", metavar="N[,N-M]",
                        help="selected lessons, e.g. 1 22,25-31")
    parser.add_argument("--jobs", type=int, default=3, help="parallel builds (default: 3)")
    parser.add_argument("--keep", action="store_true",
                        help="retain isolated PDFs, logs, variants, and report.json")
    args = parser.parse_args()
    if args.jobs < 1:
        parser.error("--jobs must be positive")
    missing_tools = [name for name in ("latexmk", "xelatex", "pdfinfo", "pdftotext")
                     if not shutil.which(name)]
    if missing_tools:
        parser.error("required tools unavailable: " + ", ".join(missing_tools))
    discovered = {int(path.name[7:9]): path
                  for path in sorted(ROOT.glob("lesson_??_handout.tex"))}
    if not discovered:
        parser.error("no canonical lesson wrappers were found")
    try:
        selected = (requested_lessons(args.lessons, set(discovered))
                    if args.lessons else set(discovered))
    except ValueError as exc:
        parser.error(str(exc))
    source_texts = {discovered[n]: discovered[n].read_text() for n in sorted(selected)}
    for path, source in source_texts.items():
        if CLASS_RE.search(without_comments(source)) is None:
            parser.error(f"{path.name} does not load ne630handout directly")
    build = Path(tempfile.mkdtemp(prefix="ne630-class-check-"))
    variants = build / "variants"
    variants.mkdir()
    print(f"Isolated build: {build}", flush=True)
    cases = []
    for path, source in source_texts.items():
        lesson = int(path.name[7:9])
        cases.append(BuildCase(path.stem, path, "public", lesson))
        if FALSE_RE.search(without_comments(source)):
            name = path.stem + "_instructor"
            variant = variants / (name + ".tex")
            variant.write_text(instructor_source(source))
            cases.append(BuildCase(name, variant, "instructor", lesson))
        if lesson == 22:
            name = path.stem + "_fallback"
            variant = variants / (name + ".tex")
            variant.write_text(fallback_source(source))
            cases.append(BuildCase(name, variant, "fallback", lesson))
    for kind, source in (("public", API_SOURCE),
                         ("instructor", instructor_source(API_SOURCE))):
        name = "class_api_" + kind
        path = variants / (name + ".tex")
        path.write_text(source)
        cases.append(BuildCase(name, path, kind, api=True))
    by_name = {}
    try:
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            pending = {pool.submit(build_case, case, build): case for case in cases}
            for future in as_completed(pending):
                case = pending[future]
                try:
                    result = future.result()
                except Exception as exc:
                    result = {
                        "name": case.name, "lesson": case.lesson,
                        "variant": case.variant, "api": case.api, "ok": False,
                        "errors": [f"checker error: {exc}"], "pages": None,
                        "layout_notices": []}
                by_name[case.name] = result
                state = "PASS" if result["ok"] else "FAIL"
                print(f"{state} {case.name}: {result['pages']} pages; "
                      f"{len(result['layout_notices'])} layout notices", flush=True)
                for error in result["errors"]:
                    print(f"  {error}", flush=True)
    finally:
        results = [by_name[case.name] for case in cases if case.name in by_name]
        report = {
            "canonical_class": str(ROOT / "ne630handout.cls"),
            "working_directory": str(ROOT), "lessons": len(source_texts),
            "lesson_numbers": sorted(selected), "jobs": args.jobs,
            "builds": len(results), "expected_builds": len(cases),
            "passed": sum(result["ok"] for result in results),
            "complete": len(results) == len(cases),
            "fallback_lesson_22_checked": 22 in selected, "results": results}
        (build / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    ok = report["complete"] and all(result["ok"] for result in results)
    print(f"{report['passed']}/{report['builds']} builds passed across "
          f"{len(source_texts)} canonical lessons and the shared API fixture.", flush=True)
    if args.keep or not ok:
        print(f"PDFs, logs, and report retained in {build}", flush=True)
    else:
        shutil.rmtree(build)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
