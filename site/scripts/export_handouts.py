#!/usr/bin/env python3
"""Create student-safe public handout artifacts for the Sphinx site."""

from __future__ import annotations

import argparse
import hashlib
import io
import re
import sys
import zipfile
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[2]
SOURCE_DIRECTORY = REPOSITORY / "handouts"
OUTPUT_DIRECTORY = REPOSITORY / "site" / "_static" / "handouts"
LESSONS = (1, 2, 3, 4, 5, 6)
LESSON_SUPPORT_FILES = {
    5: ("spectra.pdf",),
    6: (
        "figures/h1_xsec.pgf",
        "figures/u235_fission.pgf",
        "figures/u238_threshold.pdf",
    ),
}
REDACTION_COMMANDS = (
    "RevealBlank",
    "MathBlank",
    "InstructorFigureContent",
    "InstructorCue",
    "ifhandoutinstructor",
)
EXPECTED_REDACTIONS = {
    1: (7, 0, 0, 0, 0),
    2: (22, 4, 3, 0, 1),
    3: (1, 12, 0, 0, 0),
    4: (12, 17, 0, 0, 0),
    5: (12, 10, 0, 0, 0),
    6: (1, 3, 0, 0, 0),
}


class ExportError(RuntimeError):
    """Raised when a handout cannot be exported safely."""


def _is_escaped(text: str, position: int) -> bool:
    backslashes = 0
    position -= 1
    while position >= 0 and text[position] == "\\":
        backslashes += 1
        position -= 1
    return bool(backslashes % 2)


def _is_in_comment(text: str, position: int) -> bool:
    line_start = text.rfind("\n", 0, position) + 1
    index = line_start
    while index < position:
        if text[index] == "%" and not _is_escaped(text, index):
            return True
        index += 1
    return False


def _find_command(text: str, command: str, start: int = 0) -> int:
    token = f"\\{command}"
    position = start
    while True:
        position = text.find(token, position)
        if position < 0:
            return -1
        following = position + len(token)
        if (
            (following == len(text) or not (text[following].isalpha() or text[following] == "@"))
            and not _is_in_comment(text, position)
        ):
            return position
        position += len(token)


def _skip_whitespace(text: str, position: int) -> int:
    while position < len(text) and text[position].isspace():
        position += 1
    return position


def _balanced_group_end(text: str, start: int, opening: str, closing: str) -> int:
    if start >= len(text) or text[start] != opening:
        raise ExportError(f"expected {opening!r} at character {start}")

    depth = 0
    position = start
    while position < len(text):
        character = text[position]
        if character == "%" and not _is_escaped(text, position):
            newline = text.find("\n", position)
            if newline < 0:
                raise ExportError("unterminated TeX comment inside a command argument")
            position = newline + 1
            continue
        if not _is_escaped(text, position):
            if character == opening:
                depth += 1
            elif character == closing:
                depth -= 1
                if depth == 0:
                    return position + 1
        position += 1
    raise ExportError(f"unbalanced {opening}{closing} group at character {start}")


def _command_argument_span(text: str, command: str, start: int) -> tuple[int, int]:
    position = start + len(command) + 1
    position = _skip_whitespace(text, position)
    if position < len(text) and text[position] == "[":
        position = _balanced_group_end(text, position, "[", "]")
        position = _skip_whitespace(text, position)
    if position >= len(text) or text[position] != "{":
        raise ExportError(f"\\{command} is missing its required argument")
    return position, _balanced_group_end(text, position, "{", "}")


def _empty_last_arguments(text: str, command: str) -> str:
    position = 0
    while True:
        command_start = _find_command(text, command, position)
        if command_start < 0:
            return text
        argument_start, argument_end = _command_argument_span(text, command, command_start)
        text = text[:argument_start] + "{}" + text[argument_end:]
        position = argument_start + 2


def _remove_commands(text: str, command: str) -> str:
    position = 0
    while True:
        command_start = _find_command(text, command, position)
        if command_start < 0:
            return text
        _, argument_end = _command_argument_span(text, command, command_start)
        text = text[:command_start] + text[argument_end:]
        position = command_start


def _command_count(text: str, command: str) -> int:
    count = 0
    position = 0
    while True:
        command_start = _find_command(text, command, position)
        if command_start < 0:
            return count
        count += 1
        position = command_start + len(command) + 1


_CONDITIONAL_TOKEN = re.compile(r"\\(if[A-Za-z@]+|else|fi)\b")


def _student_conditional_branch(text: str) -> str:
    while True:
        conditional_start = _find_command(text, "ifhandoutinstructor")
        if conditional_start < 0:
            return text

        depth = 1
        else_span: tuple[int, int] | None = None
        conditional_end: tuple[int, int] | None = None
        search_start = conditional_start + len("\\ifhandoutinstructor")
        for match in _CONDITIONAL_TOKEN.finditer(text, search_start):
            if _is_in_comment(text, match.start()):
                continue
            token = match.group(1)
            if token.startswith("if"):
                depth += 1
            elif token == "fi":
                depth -= 1
                if depth == 0:
                    conditional_end = (match.start(), match.end())
                    break
            elif token == "else" and depth == 1:
                if else_span is not None:
                    raise ExportError("multiple top-level else branches in instructor conditional")
                else_span = (match.start(), match.end())

        if conditional_end is None:
            raise ExportError("unterminated \\ifhandoutinstructor conditional")
        if else_span is None:
            student_text = ""
        else:
            student_text = text[else_span[1] : conditional_end[0]]
            # The surrounding source already supplies the newlines before the
            # conditional and after ``\\fi``. Retaining the branch's boundary
            # newlines would create blank paragraphs and alter student layout.
            student_text = re.sub(r"^[ \t]*\r?\n", "", student_text, count=1)
            student_text = re.sub(r"\r?\n[ \t]*$", "", student_text, count=1)
        text = text[:conditional_start] + student_text + text[conditional_end[1] :]


def _strip_comments(text: str) -> str:
    """Remove unescaped TeX comments without changing line-continuation semantics."""

    public_lines: list[str] = []
    for line in text.splitlines(keepends=True):
        comment_start = next(
            (
                position
                for position, character in enumerate(line)
                if character == "%" and not _is_escaped(line, position)
            ),
            None,
        )
        if comment_start is None:
            public_lines.append(re.sub(r"[ \t]+(?=\r?\n?$)", "", line))
            continue

        prefix = line[:comment_start]
        if prefix.strip():
            # TeX discards both the comment and its line ending. Keeping only
            # the prefix joins it directly to the following physical line.
            public_lines.append(prefix)

    return "".join(public_lines)


def _audit_redaction_counts(source: str, lesson: int) -> None:
    actual = tuple(_command_count(source, command) for command in REDACTION_COMMANDS)
    expected = EXPECTED_REDACTIONS.get(lesson)
    if expected is None or actual != expected:
        details = ", ".join(
            f"{command}={count}" for command, count in zip(REDACTION_COMMANDS, actual, strict=True)
        )
        raise ExportError(
            f"Lesson {lesson:02d} instructor-bearing construct count changed ({details}). "
            "Review the source-safety policy and update EXPECTED_REDACTIONS deliberately."
        )


def sanitize_body(source: str) -> str:
    """Remove every known instructor-only payload while preserving student output."""

    public = _student_conditional_branch(source)
    public = _remove_commands(public, "InstructorFigureContent")
    public = _remove_commands(public, "InstructorCue")
    public = _empty_last_arguments(public, "RevealBlank")
    public = _empty_last_arguments(public, "MathBlank")
    public = _strip_comments(public)

    if re.search(r"\binstructor\b", public, flags=re.IGNORECASE):
        raise ExportError("sanitized body still contains the word 'instructor'")
    if "\\ifhandoutinstructor" in public:
        raise ExportError("sanitized body still contains an instructor conditional")
    for position, character in enumerate(public):
        if character == "%" and not _is_escaped(public, position):
            raise ExportError("sanitized body still contains a TeX comment")

    for command in ("RevealBlank", "MathBlank"):
        position = 0
        while True:
            command_start = _find_command(public, command, position)
            if command_start < 0:
                break
            argument_start, argument_end = _command_argument_span(public, command, command_start)
            if public[argument_start:argument_end] != "{}":
                raise ExportError(f"sanitized \\{command} still contains a reveal value")
            position = argument_end

    return public


def _read_required(path: Path) -> bytes:
    if not path.is_file():
        raise ExportError(f"required handout artifact is missing: {path.relative_to(REPOSITORY)}")
    return path.read_bytes()


def _source_readme(lesson: int, support_files: tuple[str, ...]) -> bytes:
    basename = f"lesson_{lesson:02d}_handout"
    file_lines = [
        f"  {basename}.tex       student document wrapper",
        f"  {basename}_body.tex  student-safe handout body",
        "  ne630boardhandout.cls     shared document class",
    ]
    file_lines.extend(f"  {name:<24} supporting figure" for name in support_files)
    files = "\n".join(file_lines)
    content = f"""NE 630 Lesson {lesson:02d} student handout source

Files:
{files}

Compile with XeLaTeX:

  latexmk -xelatex -interaction=nonstopmode -halt-on-error {basename}.tex

The public body intentionally omits instructor reveal values, instructor-only
figures, and teaching cues. Myriad Pro is used when it is installed in one of
the paths recognized by the class; otherwise the class falls back to TeX Gyre
Heros. Libertinus Math and the standard packages named by the class are also
required.
"""
    return content.encode("utf-8")


def _zip_bytes(files: dict[str, bytes]) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(files):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, files[name])
    return buffer.getvalue()


def expected_exports() -> dict[Path, bytes]:
    class_bytes = _read_required(SOURCE_DIRECTORY / "ne630boardhandout.cls")
    exports: dict[Path, bytes] = {Path("ne630boardhandout.cls"): class_bytes}

    for lesson in LESSONS:
        basename = f"lesson_{lesson:02d}_handout"
        directory = Path(f"lesson-{lesson:02d}")
        wrapper_path = SOURCE_DIRECTORY / f"{basename}.tex"
        body_path = SOURCE_DIRECTORY / f"{basename}_body.tex"
        pdf_path = SOURCE_DIRECTORY / f"{basename}.pdf"

        wrapper = _read_required(wrapper_path)
        wrapper_text = wrapper.decode("utf-8")
        if not re.search(r"\\documentclass\s*\[student\]\s*\{ne630boardhandout\}", wrapper_text):
            raise ExportError(f"{wrapper_path.name} is not an explicit student wrapper")
        if re.search(r"\binstructor\b", wrapper_text, flags=re.IGNORECASE):
            raise ExportError(f"{wrapper_path.name} contains instructor-facing content")

        body_source = _read_required(body_path).decode("utf-8")
        _audit_redaction_counts(body_source, lesson)
        body = sanitize_body(body_source).encode("utf-8")
        pdf = _read_required(pdf_path)
        if not pdf.startswith(b"%PDF-"):
            raise ExportError(f"{pdf_path.name} is not a PDF file")

        support_files = LESSON_SUPPORT_FILES.get(lesson, ())
        support_contents = {
            name: _read_required(SOURCE_DIRECTORY / name) for name in support_files
        }
        readme = _source_readme(lesson, support_files)
        bundle_files = {
            "README.txt": readme,
            f"{basename}.tex": wrapper,
            f"{basename}_body.tex": body,
            "ne630boardhandout.cls": class_bytes,
            **support_contents,
        }

        exports[directory / f"{basename}.pdf"] = pdf
        exports[directory / f"{basename}.tex"] = wrapper
        exports[directory / f"{basename}_body.tex"] = body
        for name, content in support_contents.items():
            exports[directory / name] = content
        exports[directory / f"{basename}_source.zip"] = _zip_bytes(bundle_files)

    return exports


def _digest(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def check_exports(exports: dict[Path, bytes]) -> list[str]:
    errors: list[str] = []
    expected_paths = {OUTPUT_DIRECTORY / relative for relative in exports}
    actual_paths = {path for path in OUTPUT_DIRECTORY.rglob("*") if path.is_file()}

    for relative, expected in exports.items():
        destination = OUTPUT_DIRECTORY / relative
        if not destination.is_file():
            errors.append(f"missing generated file: {destination.relative_to(REPOSITORY)}")
        elif destination.read_bytes() != expected:
            errors.append(
                f"stale generated file: {destination.relative_to(REPOSITORY)} "
                f"(expected sha256 {_digest(expected)[:12]})"
            )

    for unexpected in sorted(actual_paths - expected_paths):
        errors.append(f"unexpected public handout file: {unexpected.relative_to(REPOSITORY)}")
    return errors


def write_exports(exports: dict[Path, bytes]) -> None:
    errors = [error for error in check_exports(exports) if error.startswith("unexpected")]
    if errors:
        raise ExportError("\n".join(errors) + "\nRefusing to delete an unrecognized public file.")

    for relative, content in exports.items():
        destination = OUTPUT_DIRECTORY / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.is_file() or destination.read_bytes() != content:
            destination.write_bytes(content)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify generated exports without modifying them",
    )
    arguments = parser.parse_args()

    try:
        exports = expected_exports()
        if arguments.check:
            errors = check_exports(exports)
            if errors:
                raise ExportError("\n".join(errors))
            print(f"Verified {len(exports)} public handout files.")
        else:
            write_exports(exports)
            print(f"Exported {len(exports)} public handout files.")
    except (ExportError, UnicodeDecodeError) as error:
        print(f"handout export failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
