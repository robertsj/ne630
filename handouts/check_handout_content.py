#!/usr/bin/env python3
"""Check that formatting migrations preserve existing L01--L24 instruction.

Run before committing with ``python3 check_handout_content.py --ref HEAD`` or
supply an immutable handouts source copy using ``--baseline /path/to/copy``.
The baseline determines the lessons checked; the L07 derivation supplement is
also checked when present. L25+ seeds are intentionally out of scope.
Checks compare TeX tokens in document bodies, instructional preamble
macros (including shared and lesson-specific drawings), title/reading metadata,
solution switches, and referenced binary figures. Comments, whitespace, font
size/spacing directives, and relocation of formatting helpers are permitted.
This complements compilation and visual review; it does not replace either.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
from functools import lru_cache
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SUPPLEMENTS = ("lesson_07_derivations.tex",)
TOKEN = re.compile(r"\\[A-Za-z@]+|\\.|[A-Za-z0-9]+|[^\s]", re.DOTALL)
INPUT = re.compile(r"\\input\s*\{([^}]+)\}")
LITERAL = re.compile(r"\\begin\{(lstlisting|verbatim|minted)\}.*?\\end\{\1\}", re.DOTALL)
DEFINITION = re.compile(
    r"\\(newcommand|renewcommand|providecommand|NewDocumentCommand|"
    r"RenewDocumentCommand|ProvideDocumentCommand)\*?\s*")
# Only presentation helpers are excluded. Unknown preamble macros are audited.
LAYOUT_MACROS = {
    "arraystretch", "headrulewidth", "footrulewidth", "headrule", "LessonNo",
    "Lesson", "Sec", "eqread", "figcap", "SourceLine", "SourceEq", "colstart",
    "colnext", "colend", "NEContinue", "NEEx", "NEsmall", "NEbody", "Step",
    "PageTitle", "Reveal", "RevealMath",
}
LAYOUT_CALLS = {
    "fontsize": 2, "setlength": 2, "addtolength": 2, "vspace": 1,
    "hspace": 1, "addvspace": 1, "tcbset": 1,
}
LAYOUT_WORDS = {"selectfont", "RaggedRight"}
CLASS_CONTENT_MACROS = {"unit", "Ktrue", "Kclassical"}


def uncomment(source: str) -> str:
    """Remove TeX comments, respecting escaped percent signs."""
    lines = []
    literal = None
    for line in source.splitlines():
        if literal:
            lines.append(line)
            if rf"\end{{{literal}}}" in line:
                literal = None
            continue
        for match in re.finditer("%", line):
            pos = match.start()
            start = pos
            while start and line[start - 1] == "\\":
                start -= 1
            if (pos - start) % 2 == 0:
                line = line[:pos]
                break
        start = re.search(r"\\begin\{(lstlisting|verbatim|minted)\}", line)
        if start:
            literal = start[1]
        lines.append(line)
    return "\n".join(lines)


def group(source: str, pos: int, opening: str = "{", closing: str = "}") -> tuple[str, int]:
    while pos < len(source) and source[pos].isspace():
        pos += 1
    if pos >= len(source) or source[pos] != opening:
        raise ValueError(f"Expected {opening!r} near {source[pos:pos+60]!r}")
    start = pos + 1
    depth = 1
    pos += 1
    while pos < len(source):
        ch = source[pos]
        if ch == "\\":
            # A control symbol can escape a brace; a control word cannot.
            m = re.match(r"\\(?:[A-Za-z@]+|.)", source[pos:], re.DOTALL)
            pos += len(m.group()) if m else 1
            continue
        if ch == opening:
            depth += 1
        elif ch == closing:
            depth -= 1
            if depth == 0:
                return source[start:pos], pos + 1
        pos += 1
    raise ValueError("Unbalanced TeX group")


def without_layout(source: str) -> str:
    pattern = re.compile(r"\\(" + "|".join(set(LAYOUT_CALLS) | LAYOUT_WORDS) + r")\b\*?")
    pieces: list[str] = []
    end = 0
    for m in pattern.finditer(source):
        if m.start() < end:
            continue
        pos = m.end()
        try:
            for _ in range(LAYOUT_CALLS.get(m[1], 0)):
                _, pos = group(source, pos)
        except ValueError:
            continue  # Do not swallow a nonstandard TeX construct.
        pieces.append(source[end:m.start()])
        end = pos
    return "".join(pieces) + source[end:]


def tokens(source: str) -> list[str]:
    source = uncomment(source)
    result = []
    end = 0
    for literal in LITERAL.finditer(source):
        result += TOKEN.findall(without_layout(source[end:literal.start()]))
        # Whitespace is instructional inside code, particularly in Python.
        result.append(literal.group())
        end = literal.end()
    return result + TOKEN.findall(without_layout(source[end:]))


@dataclass(eq=False)
class Tree:
    root: Path
    ref: str | None = None

    @lru_cache(maxsize=None)
    def data(self, relative: str) -> bytes:
        if self.ref is None:
            return (self.root / relative).read_bytes()
        repository = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], cwd=self.root, text=True).strip()
        prefix = self.root.relative_to(Path(repository)).as_posix()
        proc = subprocess.run(["git", "show", f"{self.ref}:{prefix}/{relative}"],
                              cwd=self.root, capture_output=True)
        if proc.returncode:
            raise FileNotFoundError(relative)
        return proc.stdout

    def text(self, relative: str) -> str:
        return self.data(relative).decode("utf-8")

    def exists(self, relative: str) -> bool:
        try:
            self.data(relative)
            return True
        except FileNotFoundError:
            return False

    def names(self) -> list[str]:
        if self.ref is None:
            return [p.name for p in self.root.glob("lesson_*.tex")]
        repository = Path(subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], cwd=self.root, text=True).strip())
        prefix = self.root.relative_to(repository).as_posix()
        return subprocess.check_output(
            ["git", "ls-tree", "--name-only", f"{self.ref}:{prefix}"],
            cwd=repository, text=True).splitlines()

    def resolve(self, name: str, suffixes: tuple[str, ...] = ("", ".tex")) -> str | None:
        for suffix in suffixes:
            if self.exists(name + suffix):
                return name + suffix
        return None

    def expand(self, relative: str, stack: tuple[str, ...] = ()) -> str:
        if relative in stack:
            raise ValueError(f"Recursive input: {' -> '.join(stack + (relative,))}")
        source = uncomment(self.text(relative))
        def replace(m: re.Match[str]) -> str:
            target = self.resolve(m[1])
            if target and Path(target).suffix in {".tex", ".pgf"}:
                return self.expand(target, stack + (relative,))
            return m.group()
        return INPUT.sub(replace, source)

    def catalog(self, relative: str, seen: set[str] | None = None) -> str:
        """Read local class/style dependencies to find relocated definitions."""
        seen = set() if seen is None else seen
        if relative in seen:
            return ""
        seen.add(relative)
        source = uncomment(self.text(relative))
        deps = []
        for m in re.finditer(
            r"\\(?:documentclass|LoadClass|usepackage|RequirePackage)"
            r"(?:\[[^\]]*\])?\s*\{([^}]+)\}", source):
            for name in m[1].split(","):
                target = self.resolve(name.strip(), (".cls", ".sty"))
                if target:
                    deps.append(self.catalog(target, seen))
        for m in INPUT.finditer(source):
            target = self.resolve(m[1])
            if target and Path(target).suffix in {".tex", ".pgf"}:
                deps.append(self.catalog(target, seen))
        return "\n".join(deps + [source])


def definitions(source: str) -> dict[str, str]:
    result = {}
    for m in DEFINITION.finditer(source):
        pos = m.end()
        if source[pos:pos+1] == "{":
            name, pos = group(source, pos)
        else:
            name_match = re.match(r"\\[A-Za-z@]+", source[pos:])
            if not name_match:
                continue
            name = name_match.group()
            pos += len(name)
        name = name.removeprefix("\\")
        signature = ""
        if "DocumentCommand" in m[1]:
            signature, pos = group(source, pos)
        else:
            for _ in range(2):
                while pos < len(source) and source[pos].isspace():
                    pos += 1
                if source[pos:pos+1] != "[":
                    break
                argument, pos = group(source, pos, "[", "]")
                signature += "[" + argument + "]"
        try:
            payload, _ = group(source, pos)
        except ValueError:
            continue
        # The classic [1] and xparse {m} signatures express the same contract.
        if re.fullmatch(r"\[\d\]", signature):
            signature = "m" * int(signature[1])
        result[name] = signature + "{" + payload + "}"
    return result


def setup_metadata(source: str) -> list[str]:
    result = []
    for m in re.finditer(r"\\HandoutSetup\b", source):
        pos = m.end()
        try:
            args = []
            for _ in range(4):
                arg, pos = group(source, pos)
                args += ["{"] + tokens(arg) + ["}"]
            result += args
        except ValueError:
            continue
    return result


def figure_assets(tree: Tree, source: str) -> dict[str, str]:
    result = {}
    for m in re.finditer(r"\\includegraphics\*?(?:\[[^\]]*\])?\s*\{([^}]+)\}", source):
        # Filenames written as macros cannot be resolved statically.
        if "\\" in m[1]:
            continue
        name = tree.resolve(m[1], ("", ".pdf", ".png", ".jpg", ".jpeg"))
        if name:
            result[name] = hashlib.sha256(tree.data(name)).hexdigest()
    return result


def compare(label: str, old: list[str], new: list[str], failures: list[str]) -> None:
    if old == new:
        return
    diff = next((op for op in difflib.SequenceMatcher(a=old, b=new, autojunk=False).get_opcodes()
                 if op[0] != "equal"), None)
    assert diff is not None
    _, i, j, k, l = diff
    failures.append(f"{label}: {' '.join(old[max(0,i-5):min(len(old),j+5)])!r}"
                    f" -> {' '.join(new[max(0,k-5):min(len(new),l+5)])!r}")


def audit(old: Tree, new: Tree, name: str) -> list[str]:
    failures: list[str] = []
    original = old.expand(name)
    current = new.expand(name)
    before, separator, body = original.partition(r"\begin{document}")
    after, current_separator, current_body = current.partition(r"\begin{document}")
    if not separator or not current_separator:
        return ["Cannot locate document body"]
    # The old Ch4 Explore environment supplied an implicit OpenMC label. Its
    # explicit modern alias retains that label without a second formatting API.
    if 15 <= int(name[7:9]) <= 19:
        current_body = re.sub(r"(\\(?:begin|end)\{)OpenMCExplore(\})",
                              r"\1Explore\2", current_body)
    compare("instructional body", tokens(body), tokens(current_body), failures)
    compare("title/reading metadata", setup_metadata(before), setup_metadata(after), failures)
    def solution_mode(preamble: str) -> list[str]:
        flags = re.findall(r"\\handoutsolutions(true|false)\b", preamble)
        # Legacy reading guides have no solution switch and show their ordinary
        # student content. Adding an explicit false switch preserves that mode.
        return [flags[-1] if flags else "false"]
    compare("solution flags", solution_mode(before), solution_mode(after), failures)
    # Baseline preamble is the authority: cataloging the new class permits a
    # definition to move without exempting any instructional payload.
    original_macros = definitions(before)
    original_catalog = definitions(old.catalog(name))
    original_macros.update({name: original_catalog[name] for name in CLASS_CONTENT_MACROS
                            if name in original_catalog})
    current_macros = definitions(new.catalog(name))
    reachable = set(re.findall(r"\\([A-Za-z@]+)", body))
    pending = list(reachable)
    while pending:
        macro = pending.pop()
        for dependency in re.findall(r"\\([A-Za-z@]+)", original_macros.get(macro, "")):
            if dependency not in reachable:
                reachable.add(dependency)
                pending.append(dependency)
    for macro, payload in original_macros.items():
        if macro in LAYOUT_MACROS or macro not in reachable:
            continue
        if macro not in current_macros:
            failures.append(f"instructional preamble macro \\{macro} is missing")
        else:
            compare(f"preamble macro \\{macro}", tokens(payload),
                    tokens(current_macros[macro]), failures)
    original_assets = figure_assets(old, original)
    for asset, digest in original_assets.items():
        if not new.exists(asset):
            failures.append(f"referenced figure {asset} is missing")
        elif hashlib.sha256(new.data(asset)).hexdigest() != digest:
            failures.append(f"referenced figure {asset} changed")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    baseline = parser.add_mutually_exclusive_group()
    baseline.add_argument("--baseline", type=Path, help="directory containing original handouts")
    baseline.add_argument("--ref", default=None, help="baseline Git revision (default: HEAD)")
    parser.add_argument("--root", type=Path, default=ROOT, help="current handouts directory")
    args = parser.parse_args()
    old = Tree(args.baseline.resolve()) if args.baseline else Tree(args.root.resolve(), args.ref or "HEAD")
    new = Tree(args.root.resolve())
    lessons = sorted(n for n in old.names() if re.fullmatch(r"lesson_\d\d_handout\.tex", n)
                     and int(n[7:9]) <= 24)
    if not lessons:
        parser.error("baseline contains no L01--L24 handout sources")
    supplements = [name for name in SUPPLEMENTS if old.exists(name)]
    for name in set(SUPPLEMENTS) - set(supplements):
        print(f"SKIP {name} (not present in the selected baseline)")
    sources = sorted(lessons + supplements)
    failures = {}
    for name in sources:
        try:
            issues = audit(old, new, name)
        except (FileNotFoundError, ValueError) as error:
            issues = [str(error)]
        if issues:
            failures[name] = issues
            print(f"FAIL {name}")
            for issue in issues:
                print(f"  {issue}")
        else:
            print(f"PASS {name}")
    print(f"{len(sources)-len(failures)}/{len(sources)} existing documents "
          f"({len(lessons)} lessons, {len(supplements)} supplement) preserve instructional content.")
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
