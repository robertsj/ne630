#!/usr/bin/env python3
"""Compile real L01--L22 content with ne630handout, without changing lessons.

This is an API/macro compatibility check, not approval of a legacy lesson's new
pagination. Future migrations still need their own layout/visual review.
All source substitutions and TeX products live in a temporary directory.
"""
from pathlib import Path
import argparse
import json
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent


def migrated_source(source: str) -> str:
    if r"\documentclass{ne630boardhandout}" in source:
        return source.replace(r"\documentclass{ne630boardhandout}",
                              r"\documentclass[compact]{ne630handout}", 1)
    if r"\IfFileExists{ne630_ch04_reading_guide_common.tex}" in source:
        # L20--21 have an embedded fallback and duplicated layout helpers.
        # Retain their lesson-specific drawings and all document content.
        marker = r"\newcommand{\NEStartupFigure}"
        if marker not in source:
            raise ValueError("Late-guide preamble changed; inspect before migrating")
        return r"\documentclass{ne630handout}" + "\n" + source[source.index(marker):]
    return source.replace(r"\input{ne630_ch04_reading_guide_common.tex}",
                          r"\documentclass{ne630handout}", 1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--keep", action="store_true", help="retain isolated build files")
    args = parser.parse_args()
    if not shutil.which("latexmk") or not shutil.which("xelatex"):
        parser.error("latexmk and XeLaTeX are required")
    build = Path(tempfile.mkdtemp(prefix="ne630-class-check-"))
    print(f"Isolated build: {build}", flush=True)
    sources = sorted(p for p in ROOT.glob("lesson_??_handout.tex")
                     if int(p.name[7:9]) <= 22)
    for p in ROOT.glob("*.tex"):
        shutil.copy2(p, build / p.name)
    shutil.copy2(ROOT / "ne630handout.cls", build / "ne630handout.cls")
    for p in ROOT.glob("*.pdf"):
        if not p.name.startswith("lesson_"):
            shutil.copy2(p, build / p.name)
    shutil.copytree(ROOT / "figures", build / "figures")
    shutil.copy2(ROOT / "lesson_22_xenon_transient.py", build / "lesson_22_xenon_transient.py")
    results = []
    for p in sources:
        source = migrated_source(p.read_text())
        (build / p.name).write_text(source)
        variants = [(p.stem, source)]
        if r"\handoutsolutionsfalse" in source:
            variants.append((p.stem + "_solutions", source.replace(
                r"\handoutsolutionsfalse", r"\handoutsolutionstrue", 1)))
        if p.name == "lesson_22_handout.tex":
            variants.append((p.stem + "_fallback", source.replace(
                r"\documentclass{ne630handout}",
                r"\documentclass[fallbackfonts]{ne630handout}", 1)))
        for name, variant in variants:
            (build / (name + ".tex")).write_text(variant)
            proc = subprocess.run(
                ["latexmk", "-xelatex", "-interaction=nonstopmode", "-halt-on-error", name + ".tex"],
                cwd=build, capture_output=True, text=True,
            )
            (build / (name + ".build.txt")).write_text(proc.stdout + proc.stderr)
            log_path = build / (name + ".log")
            log = log_path.read_text(errors="replace") if log_path.exists() else ""
            issues = [line for line in log.splitlines() if re.search(
                r"Overfull|Underfull|Missing character|Undefined control|Undefined color|undefined references", line)]
            ok = proc.returncode == 0 and not any(re.search(
                r"Missing character|Undefined control|Undefined color|undefined references", x) for x in issues)
            results.append({"name": name, "ok": ok, "layout_notices": issues})
            print(f"{'PASS' if ok else 'FAIL'} {name} ({len(issues)} layout notices)", flush=True)
    report = {"lessons": len(sources), "builds": len(results),
              "passed": sum(r["ok"] for r in results), "results": results}
    (build / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"{report['passed']}/{report['builds']} builds passed across {len(sources)} existing lessons.", flush=True)
    ok = all(r["ok"] for r in results)
    if args.keep or not ok:
        print(f"Logs and report retained in {build}", flush=True)
    else:
        shutil.rmtree(build)  # only the directory created by this invocation
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
