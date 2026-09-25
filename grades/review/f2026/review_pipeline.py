#!/usr/bin/env python3
"""Deterministic, private intake and calibration preparation for NE 630.

The pipeline treats every submission byte, filename, archive member, and PDF as
untrusted evidence.  It never executes student code.  PDF inspection and page
rendering use bounded ``pdfinfo``, ``pdftotext``, and ``pdftoppm`` processes in
a no-network Bubblewrap namespace; cleared products use only a canonical
image-only PDF rebuilt by this module.
"""

from __future__ import annotations

import argparse
import contextlib
import dataclasses
import datetime as dt
import fcntl
import hashlib
import importlib.metadata
import io
import json
import os
from pathlib import Path, PurePosixPath
import platform
import re
import secrets
import shutil
import stat
import struct
import subprocess
import sys
import tempfile
import unicodedata
import unittest
import zipfile
import zlib
from collections import defaultdict
from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from typing import Any, BinaryIO

import jsonschema
import yaml


VERSION = "0.3.1"
SCHEMA_VERSION = "1.0.0"
ASSIGNMENTS = ("HW01", "HW02", "HW03", "HW04")
STAGES = (
    "SELF_TEST",
    "REFERENCE_FREEZE",
    "INTAKE",
    "PREPARE_CALIBRATION",
    "PRODUCT_REVIEW",
    "RECONCILIATION",
    "VALIDATE",
)
CALIBRATION_STRATA = (
    "READABLE_SINGLE_PDF",
    "SAFE_ZIP_UNIQUE_SOLUTION_PDF",
)
CORE_ROUTE_B_FILES = (
    "solution.tex",
    "solution.pdf",
    "discourse.tex",
    "discourse.pdf",
    "Makefile",
)
NESTED_ARCHIVE_SUFFIXES = {
    ".7z",
    ".bz2",
    ".gz",
    ".rar",
    ".tar",
    ".tbz",
    ".tbz2",
    ".tgz",
    ".txz",
    ".xz",
    ".zip",
}
NESTED_ARCHIVE_SIGNATURES = (
    b"PK\x03\x04",
    b"PK\x05\x06",
    b"PK\x07\x08",
    b"7z\xbc\xaf\x27\x1c",
    b"Rar!\x1a\x07",
    b"\x1f\x8b",
    b"BZh",
    b"\xfd7zXZ\x00",
)
MAX_TOOL_OUTPUT_BYTES = 1_048_576
TOOL_MEMORY_LIMIT_BYTES = 1_073_741_824
MAX_RASTER_PAGES = 64
MAX_RASTER_DIMENSION_PIXELS = 3300
MAX_RASTER_PAGE_BYTES = 32 * 1024 * 1024
MAX_RASTER_TOTAL_BYTES = 200 * 1024 * 1024
INERT_RASTER_PROFILE = "POPPLER_JPEG_IMAGE_ONLY_V1"
PDF_PAGE_TEXT_SEPARATOR = b"\x00NE630_PAGE_TEXT\x00"
PRIVATE_DIRECTORY_MODE = 0o700
PRIVATE_FILE_MODE = 0o600
MINIMUM_SELF_TEST_CASES = 59
CLEARANCE_ATTESTATION = (
    "I personally inspected every page of each PDF in the identified review "
    "set and confirm that no visible student identity remains."
)
IDENTIFIER_RE = re.compile(
    r"\b(?:ART|EVT|FND|OBS|DEC|CHK|REFMAN|IDMAP|SUBMAN|BLD|QUE|SEL|RSET|PKT|DOS|RND|VAL)-[0-9]{6}\b"
)
GENERIC_FILENAME_TOKENS = {
    "adobe",
    "assignment",
    "bundle",
    "camscanner",
    "combinepdf",
    "discourse",
    "files",
    "homework",
    "hw01",
    "hw02",
    "hw03",
    "hw04",
    "merged",
    "nuclear",
    "reactor",
    "scan",
    "solution",
    "submission",
    "theory",
    "work",
}


class PipelineError(RuntimeError):
    """A safe, user-facing pipeline failure."""


class ContractError(PipelineError):
    """A schema or semantic contract failure."""


class UnsafeInputError(PipelineError):
    """An untrusted input violated a containment or resource boundary."""


@dataclasses.dataclass(frozen=True)
class ExportName:
    login: str
    late_marker: bool
    user_id: str
    file_id: str
    original_name: str


@dataclasses.dataclass(frozen=True)
class SourceFile:
    path: Path
    repository_path: str
    export_name: ExportName | None
    sha256: str
    byte_count: int
    logical_path: str
    artifact_id: str
    media_type: str
    detected_type: str
    extension_match: str


@dataclasses.dataclass(frozen=True)
class SubmissionGroup:
    assignment_id: str
    source_identity_key: str
    display_name: str | None
    lms_user_id: str | None
    source_group_key: str
    source_submission_id: str
    files: tuple[SourceFile, ...]
    source_payload_sha256: str
    pseudonym: str
    attempt_number: int
    submission_record_id: str


@dataclasses.dataclass(frozen=True)
class ToolResult:
    returncode: int | None
    stdout: bytes
    stderr: bytes
    timed_out: bool


@dataclasses.dataclass(frozen=True)
class ArchiveResult:
    record: dict[str, Any]
    member_names: tuple[str, ...]
    solution_member: str | None
    solution_pdf: bytes | None


@dataclasses.dataclass(frozen=True)
class InertPdf:
    data: bytes
    page_count: int
    page_sha256s: tuple[str, ...]
    pixel_dimensions: tuple[tuple[int, int], ...]
    profile: str = INERT_RASTER_PROFILE


class IdAllocator:
    """Allocate monotonically increasing identifiers by prefix."""

    def __init__(self, initial: Mapping[str, int] | None = None) -> None:
        self._values = defaultdict(int)
        if initial:
            self._values.update(initial)

    def next(self, prefix: str) -> str:
        self._values[prefix] += 1
        return f"{prefix}-{self._values[prefix]:06d}"

    @classmethod
    def from_paths(cls, paths: Iterable[Path]) -> "IdAllocator":
        values: dict[str, int] = defaultdict(int)
        for path in paths:
            if not path.is_file() or path.is_symlink():
                continue
            if path.suffix.lower() not in {".json", ".jsonl", ".md", ".txt", ".tex"}:
                continue
            try:
                if path.stat().st_size > 50 * 1024 * 1024:
                    continue
                text = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            for match in IDENTIFIER_RE.finditer(text):
                prefix, number = match.group(0).rsplit("-", 1)
                values[prefix] = max(values[prefix], int(number))
        return cls(values)


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def parse_utc_timestamp(value: str) -> dt.datetime:
    try:
        parsed = dt.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError as exc:
        raise ContractError(f"invalid UTC timestamp: {value!r}") from exc
    return parsed.replace(tzinfo=dt.timezone.utc)


def _normalize_json(value: Any) -> Any:
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value)
    if isinstance(value, list):
        return [_normalize_json(item) for item in value]
    if isinstance(value, tuple):
        return [_normalize_json(item) for item in value]
    if isinstance(value, dict):
        return {
            unicodedata.normalize("NFC", str(key)): _normalize_json(item)
            for key, item in value.items()
        }
    return value


def canonical_json_bytes(value: Any) -> bytes:
    normalized = _normalize_json(value)
    rendered = json.dumps(
        normalized,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return (rendered + "\n").encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalized_casefold(value: str) -> str:
    return unicodedata.normalize("NFC", value).casefold()


def identity_token_present(haystack: str, token: str) -> bool:
    folded = normalized_casefold(token)
    if not folded:
        return False
    if all(character.isalnum() or character == "_" for character in folded):
        return bool(
            re.search(
                rf"(?<![\w]){re.escape(folded)}(?![\w])",
                haystack,
                flags=re.UNICODE,
            )
        )
    return folded in haystack


def identity_scan_requires_derivative(codes: Sequence[str]) -> bool:
    """Return whether a source finding requires a derivative before review."""
    for code in codes:
        if not code.startswith("IDENTITY_"):
            continue
        if code == "IDENTITY_SCAN_TEXT_UNAVAILABLE":
            continue
        if code.endswith("_BINARY_ONLY_PRESENT"):
            continue
        return True
    return False


def safe_file_bytes(path: Path, maximum_bytes: int | None = None) -> bytes:
    _assert_no_symlink_ancestors(path)
    flags = os.O_RDONLY
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        descriptor = os.open(path, flags)
    except OSError as exc:
        raise UnsafeInputError("input could not be opened without following links") from exc
    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            raise UnsafeInputError("input is not a regular file")
        if maximum_bytes is not None and metadata.st_size > maximum_bytes:
            raise UnsafeInputError("input exceeds the configured byte limit")
        chunks: list[bytes] = []
        remaining = metadata.st_size
        while remaining:
            chunk = os.read(descriptor, min(1_048_576, remaining))
            if not chunk:
                break
            chunks.append(chunk)
            remaining -= len(chunk)
        data = b"".join(chunks)
        if len(data) != metadata.st_size:
            raise UnsafeInputError("input changed or was truncated while being read")
        return data
    finally:
        os.close(descriptor)


def hash_regular_file(path: Path) -> tuple[str, int]:
    digest, byte_count, _ = inspect_regular_file(path)
    return digest, byte_count


def inspect_regular_file(
    path: Path, maximum_bytes: int | None = None
) -> tuple[str, int, bytes]:
    """Hash a regular file without retaining its full contents in memory."""
    _assert_no_symlink_ancestors(path)
    flags = os.O_RDONLY
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        descriptor = os.open(path, flags)
    except OSError as exc:
        raise UnsafeInputError("input could not be opened without following links") from exc
    try:
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode):
            raise UnsafeInputError("input is not a regular file")
        if maximum_bytes is not None and before.st_size > maximum_bytes:
            raise UnsafeInputError("input exceeds the configured byte limit")
        digest = hashlib.sha256()
        prefix = bytearray()
        total = 0
        while True:
            chunk = os.read(descriptor, 1_048_576)
            if not chunk:
                break
            total += len(chunk)
            if maximum_bytes is not None and total > maximum_bytes:
                raise UnsafeInputError("input exceeds the configured byte limit")
            digest.update(chunk)
            if len(prefix) < 8192:
                prefix.extend(chunk[: 8192 - len(prefix)])
        after = os.fstat(descriptor)
        if (
            total != before.st_size
            or after.st_size != before.st_size
            or after.st_mtime_ns != before.st_mtime_ns
            or after.st_ino != before.st_ino
            or after.st_dev != before.st_dev
        ):
            raise UnsafeInputError("input changed while being hashed")
        return digest.hexdigest(), total, bytes(prefix)
    finally:
        os.close(descriptor)


def private_mkdir(path: Path) -> None:
    _assert_no_symlink_ancestors(path)
    path.mkdir(parents=True, exist_ok=True, mode=PRIVATE_DIRECTORY_MODE)
    _assert_no_symlink_ancestors(path)
    if path.is_symlink() or not path.is_dir():
        raise UnsafeInputError("private output directory is not a real directory")
    path.chmod(PRIVATE_DIRECTORY_MODE)


def private_mkdir_exclusive(path: Path) -> None:
    """Create one private directory without accepting a pre-existing target."""
    _assert_no_symlink_ancestors(path)
    created = False
    try:
        path.mkdir(parents=False, exist_ok=False, mode=PRIVATE_DIRECTORY_MODE)
        created = True
        _assert_no_symlink_ancestors(path)
        if path.is_symlink() or not path.is_dir():
            raise UnsafeInputError("private output directory is not a real directory")
        path.chmod(PRIVATE_DIRECTORY_MODE)
    except BaseException as creation_error:
        if created:
            try:
                if path.is_symlink():
                    path.unlink()
                else:
                    path.rmdir()
            except OSError as rollback_error:
                raise PipelineError(
                    "exclusive private directory creation failed and rollback was incomplete"
                ) from creation_error
        raise


def write_private_bytes(path: Path, data: bytes) -> None:
    private_mkdir(path.parent)
    descriptor, temporary_name = tempfile.mkstemp(prefix=".tmp-", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        os.fchmod(descriptor, PRIVATE_FILE_MODE)
        with os.fdopen(descriptor, "wb", closefd=True) as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        path.chmod(PRIVATE_FILE_MODE)
        directory_descriptor = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(directory_descriptor)
        finally:
            os.close(directory_descriptor)
    except BaseException:
        with contextlib.suppress(FileNotFoundError):
            temporary.unlink()
        raise


def write_private_json(path: Path, value: Any) -> bytes:
    data = canonical_json_bytes(value)
    write_private_bytes(path, data)
    return data


def read_json(path: Path) -> Any:
    return json.loads(safe_file_bytes(path).decode("utf-8"))


def repository_relative(repository_root: Path, path: Path) -> str:
    root = repository_root.resolve()
    resolved = path.resolve(strict=False)
    try:
        relative = resolved.relative_to(root)
    except ValueError as exc:
        raise UnsafeInputError("path escapes the repository root") from exc
    if path.is_symlink():
        raise UnsafeInputError("symlinks are not allowed in protected paths")
    return relative.as_posix()


def assert_relative_path(value: str) -> str:
    if not value or "\\" in value or "\x00" in value:
        raise UnsafeInputError("invalid relative path")
    if any(ord(character) < 32 or ord(character) == 127 for character in value):
        raise UnsafeInputError("control character in relative path")
    pure = PurePosixPath(value)
    if pure.is_absolute() or any(part in {"", ".", ".."} for part in pure.parts):
        raise UnsafeInputError("unsafe relative path")
    return pure.as_posix()


def assert_no_symlink_components(repository_root: Path, path: Path) -> None:
    root = repository_root.resolve()
    absolute = path.absolute()
    try:
        relative = absolute.relative_to(root)
    except ValueError as exc:
        raise UnsafeInputError("configured path escapes the repository root") from exc
    current = root
    for part in relative.parts:
        current = current / part
        if current.exists() or current.is_symlink():
            metadata = current.lstat()
            if stat.S_ISLNK(metadata.st_mode):
                raise UnsafeInputError("configured path contains a symlink component")


def _assert_no_symlink_ancestors(path: Path) -> None:
    """Reject existing symlinks in an output path before and after creation."""
    absolute = path.absolute()
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        current = current / part
        try:
            metadata = current.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(metadata.st_mode):
            raise UnsafeInputError("private output path contains a symlink component")


def detect_media_type(data: bytes, suffix: str) -> tuple[str, str, str]:
    suffix = suffix.lower()
    if data.startswith(b"%PDF-"):
        media_type, detected, expected = "application/pdf", "PDF magic", ".pdf"
    elif data.startswith((b"PK\x03\x04", b"PK\x05\x06", b"PK\x07\x08")):
        media_type, detected, expected = "application/zip", "ZIP magic", ".zip"
    elif data.startswith(b"\xff\xd8\xff"):
        media_type, detected, expected = "image/jpeg", "JPEG magic", ".jpg"
    elif data.startswith(b"\x89PNG\r\n\x1a\n"):
        media_type, detected, expected = "image/png", "PNG magic", ".png"
    else:
        try:
            data[:8192].decode("utf-8")
        except UnicodeDecodeError:
            media_type, detected, expected = (
                "application/octet-stream",
                "unknown binary",
                "",
            )
        else:
            media_type, detected, expected = "text/plain", "UTF-8 text", ""
    if not suffix:
        extension_match = "NO_EXTENSION"
    elif expected == ".jpg":
        extension_match = "MATCH" if suffix in {".jpg", ".jpeg"} else "MISMATCH"
    elif expected:
        extension_match = "MATCH" if suffix == expected else "MISMATCH"
    else:
        extension_match = "UNKNOWN"
    return media_type, detected, extension_match


def parse_export_name(name: str) -> ExportName | None:
    candidates: list[ExportName] = []
    # Canvas filenames do not escape underscores.  Enumerate every numeric
    # user/file pair and reject ambiguous names rather than silently assigning
    # a file to the wrong person.
    for match in re.finditer(r"(?=(?:^|_)([0-9]+)_([0-9]+)_(.+)$)", name):
        start = match.start()
        separator_width = 0 if start == 0 else 1
        prefix = name[:start]
        if separator_width:
            prefix = prefix[:-1] if prefix.endswith("_") else prefix
        if not prefix:
            continue
        late_marker = prefix.endswith("_LATE")
        login = prefix[:-5] if late_marker else prefix
        if not login or not match.group(3):
            continue
        candidates.append(
            ExportName(
                login=login,
                late_marker=late_marker,
                user_id=match.group(1),
                file_id=match.group(2),
                original_name=match.group(3),
            )
        )
    if len(candidates) != 1:
        return None
    return candidates[0]


def payload_digest(files: Sequence[SourceFile]) -> str:
    payload = [
        {
            "logical_path": source.logical_path,
            "byte_count": source.byte_count,
            "sha256": source.sha256,
        }
        for source in sorted(files, key=lambda item: item.logical_path)
    ]
    return sha256_bytes(canonical_json_bytes(payload))


def source_file_bytes(source: SourceFile, maximum_bytes: int) -> bytes:
    data = safe_file_bytes(source.path, maximum_bytes)
    if len(data) != source.byte_count or sha256_bytes(data) != source.sha256:
        raise UnsafeInputError("source input changed after deterministic discovery")
    return data


def selection_rank_digest(
    seed: str, assignment_id: str, package_stratum: str, submission_record_id: str
) -> str:
    preimage = "\0".join(
        (seed, assignment_id, package_stratum, submission_record_id)
    ).encode("utf-8")
    return sha256_bytes(preimage)


def _resource_limiter(timeout_seconds: int, output_bytes: int) -> Callable[[], None] | None:
    try:
        import resource
    except ImportError:  # pragma: no cover - non-POSIX fallback
        return None

    def limit() -> None:
        resource.setrlimit(resource.RLIMIT_CPU, (timeout_seconds + 1, timeout_seconds + 1))
        resource.setrlimit(
            resource.RLIMIT_AS,
            (TOOL_MEMORY_LIMIT_BYTES, TOOL_MEMORY_LIMIT_BYTES),
        )
        resource.setrlimit(resource.RLIMIT_FSIZE, (output_bytes, output_bytes))
        resource.setrlimit(resource.RLIMIT_NOFILE, (64, 64))
        resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    return limit


def run_bounded_tool(
    argv: Sequence[str],
    *,
    working_directory: Path,
    timeout_seconds: int,
    writable_working_directory: bool = False,
    file_size_limit_bytes: int = MAX_TOOL_OUTPUT_BYTES,
) -> ToolResult:
    if not argv:
        raise ValueError("tool argument vector cannot be empty")
    sandbox = shutil.which("bwrap")
    executable = shutil.which(argv[0]) if not Path(argv[0]).is_absolute() else argv[0]
    if not sandbox or not executable:
        return ToolResult(
            returncode=None,
            stdout=b"",
            stderr=b"required parser sandbox is unavailable",
            timed_out=False,
        )
    resolved_working_directory = working_directory.resolve(strict=True)
    if writable_working_directory and (
        stat.S_IMODE(resolved_working_directory.stat().st_mode) & 0o077
    ):
        return ToolResult(
            returncode=None,
            stdout=b"",
            stderr=b"writable parser directory is not private",
            timed_out=False,
        )
    sandbox_arguments: list[str] = [
        sandbox,
        "--die-with-parent",
        "--new-session",
        "--unshare-all",
        "--proc",
        "/proc",
        "--dev",
        "/dev",
        "--tmpfs",
        "/tmp",
        "--ro-bind",
        "/usr",
        "/usr",
        "--ro-bind",
        "/etc",
        "/etc",
    ]
    for system_path in ("/lib", "/lib64"):
        if Path(system_path).exists():
            sandbox_arguments.extend(("--ro-bind", system_path, system_path))
    sandbox_arguments.extend(
        (
            "--bind" if writable_working_directory else "--ro-bind",
            str(resolved_working_directory),
            "/work",
            "--chdir",
            "/work",
            "--setenv",
            "LC_ALL",
            "C",
            "--setenv",
            "LANG",
            "C",
            "--setenv",
            "HOME",
            "/nonexistent",
            "--setenv",
            "TMPDIR",
            "/tmp",
            "--",
            str(executable),
        )
    )
    for argument in argv[1:]:
        candidate = Path(argument)
        if candidate.is_absolute():
            try:
                relative = candidate.resolve(strict=True).relative_to(
                    resolved_working_directory
                )
            except (OSError, ValueError):
                return ToolResult(
                    returncode=None,
                    stdout=b"",
                    stderr=b"parser argument escapes the private sandbox",
                    timed_out=False,
                )
            sandbox_arguments.append(f"/work/{relative.as_posix()}")
        else:
            sandbox_arguments.append(argument)
    environment = {
        "PATH": "/usr/bin:/bin",
        "LC_ALL": "C",
        "LANG": "C",
    }
    with tempfile.TemporaryFile(dir=working_directory) as stdout_file, tempfile.TemporaryFile(
        dir=working_directory
    ) as stderr_file:
        try:
            completed = subprocess.run(
                sandbox_arguments,
                cwd=working_directory,
                env=environment,
                stdin=subprocess.DEVNULL,
                stdout=stdout_file,
                stderr=stderr_file,
                check=False,
                timeout=timeout_seconds,
                preexec_fn=_resource_limiter(
                    timeout_seconds, file_size_limit_bytes
                ),
            )
            returncode: int | None = completed.returncode
            timed_out = False
        except subprocess.TimeoutExpired:
            returncode = None
            timed_out = True
        stdout_file.seek(0)
        stderr_file.seek(0)
        return ToolResult(
            returncode=returncode,
            stdout=stdout_file.read(MAX_TOOL_OUTPUT_BYTES),
            stderr=stderr_file.read(MAX_TOOL_OUTPUT_BYTES),
            timed_out=timed_out,
        )


def inspect_pdf_bytes(
    data: bytes,
    *,
    artifact_id: str,
    private_tmp: Path,
    maximum_bytes: int,
    timeout_seconds: int,
) -> tuple[dict[str, Any], bytes]:
    if len(data) > maximum_bytes:
        return (
            {
                "artifact_id": artifact_id,
                "status": "RESOURCE_LIMIT",
                "page_count": None,
                "metadata_extracted": False,
                "text_extraction": "NOT_ATTEMPTED",
                "tool_reason_code": "PDF_BYTE_LIMIT",
            },
            b"",
        )
    if not data.startswith(b"%PDF-"):
        return (
            {
                "artifact_id": artifact_id,
                "status": "TYPE_MISMATCH",
                "page_count": None,
                "metadata_extracted": False,
                "text_extraction": "NOT_ATTEMPTED",
                "tool_reason_code": "PDF_MAGIC_MISMATCH",
            },
            b"",
        )
    private_mkdir(private_tmp)
    with tempfile.NamedTemporaryFile(
        prefix="pdf-", suffix=".pdf", dir=private_tmp, delete=False
    ) as stream:
        temporary = Path(stream.name)
        os.fchmod(stream.fileno(), PRIVATE_FILE_MODE)
        stream.write(data)
    try:
        pdfinfo = shutil.which("pdfinfo")
        pdftotext = shutil.which("pdftotext")
        if not pdfinfo or not pdftotext:
            return (
                {
                    "artifact_id": artifact_id,
                    "status": "ERROR",
                    "page_count": None,
                    "metadata_extracted": False,
                    "text_extraction": "ERROR",
                    "tool_reason_code": "PDF_TOOL_UNAVAILABLE",
                },
                b"",
            )
        metadata = run_bounded_tool(
            (pdfinfo, temporary.name),
            working_directory=private_tmp,
            timeout_seconds=timeout_seconds,
        )
        if metadata.timed_out:
            reason = "PDFINFO_TIMEOUT"
        elif metadata.returncode != 0:
            reason = "PDFINFO_FAILED"
        else:
            reason = None
        page_count: int | None = None
        if reason is None:
            match = re.search(rb"(?m)^Pages:\s*([0-9]+)\s*$", metadata.stdout)
            if match:
                page_count = int(match.group(1))
            if not page_count:
                reason = "PDFINFO_NO_PAGE_COUNT"
        if reason is not None:
            return (
                {
                    "artifact_id": artifact_id,
                    "status": "UNREADABLE",
                    "page_count": None,
                    "metadata_extracted": False,
                    "text_extraction": "ERROR",
                    "tool_reason_code": reason,
                },
                b"",
            )
        text_result = run_bounded_tool(
            (pdftotext, "-f", "1", "-l", str(page_count), temporary.name, "-"),
            working_directory=private_tmp,
            timeout_seconds=timeout_seconds,
        )
        if text_result.timed_out or text_result.returncode != 0:
            text_status = "ERROR"
            extracted = b""
        else:
            extracted = text_result.stdout
            text_status = "AVAILABLE" if extracted.strip() else "EMPTY"
        return (
            {
                "artifact_id": artifact_id,
                "status": "READABLE",
                "page_count": page_count,
                "metadata_extracted": True,
                "text_extraction": text_status,
                "tool_reason_code": None,
            },
            metadata.stdout + PDF_PAGE_TEXT_SEPARATOR + extracted,
        )
    finally:
        with contextlib.suppress(FileNotFoundError):
            temporary.unlink()


INERT_PDF_HEADER = b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n% NE630-INERT-RASTER v1\n"


def _sanitized_baseline_jpeg(
    data: bytes, *, maximum_dimension_pixels: int
) -> tuple[bytes, tuple[int, int]]:
    """Remove JPEG metadata and accept only a bounded baseline RGB image."""
    if not data.startswith(b"\xff\xd8"):
        raise UnsafeInputError("raster page is not a JPEG image")
    output = bytearray(b"\xff\xd8")
    position = 2
    dimensions: tuple[int, int] | None = None
    saw_scan = False
    while position < len(data):
        marker_start = position
        if data[position] != 0xFF:
            raise UnsafeInputError("raster JPEG marker structure is invalid")
        while position < len(data) and data[position] == 0xFF:
            position += 1
        if position >= len(data):
            raise UnsafeInputError("raster JPEG ends inside a marker")
        marker = data[position]
        position += 1
        if marker in {0x00, 0xD8} or 0xD0 <= marker <= 0xD7:
            raise UnsafeInputError("raster JPEG has an unexpected standalone marker")
        if marker == 0xD9:
            raise UnsafeInputError("raster JPEG has no image scan")
        if position + 2 > len(data):
            raise UnsafeInputError("raster JPEG segment is truncated")
        segment_length = int.from_bytes(data[position : position + 2], "big")
        if segment_length < 2 or position + segment_length > len(data):
            raise UnsafeInputError("raster JPEG segment length is invalid")
        segment_end = position + segment_length
        segment = data[marker_start:segment_end]
        if marker == 0xC0:
            payload = data[position + 2 : segment_end]
            if len(payload) < 6:
                raise UnsafeInputError("raster JPEG frame header is truncated")
            precision = payload[0]
            height = int.from_bytes(payload[1:3], "big")
            width = int.from_bytes(payload[3:5], "big")
            components = payload[5]
            if any(
                (
                    precision != 8,
                    components != 3,
                    width < 1,
                    height < 1,
                    width > maximum_dimension_pixels,
                    height > maximum_dimension_pixels,
                )
            ):
                raise UnsafeInputError(
                    "raster JPEG is not a bounded eight-bit RGB image"
                )
            if dimensions is not None:
                raise UnsafeInputError("raster JPEG has multiple baseline frames")
            dimensions = (width, height)
        elif marker in {
            0xC1,
            0xC2,
            0xC3,
            0xC5,
            0xC6,
            0xC7,
            0xC9,
            0xCA,
            0xCB,
            0xCD,
            0xCE,
            0xCF,
        }:
            raise UnsafeInputError("raster JPEG is not baseline encoded")

        # APPn and COM segments are metadata and are deliberately discarded.
        if not (0xE0 <= marker <= 0xEF or marker == 0xFE):
            output.extend(segment)
        position = segment_end
        if marker != 0xDA:
            continue
        if dimensions is None:
            raise UnsafeInputError("raster JPEG scan precedes its frame header")
        saw_scan = True
        entropy_start = position
        while position < len(data):
            if data[position] != 0xFF:
                position += 1
                continue
            marker_position = position
            while position < len(data) and data[position] == 0xFF:
                position += 1
            if position >= len(data):
                raise UnsafeInputError("raster JPEG scan is truncated")
            entropy_marker = data[position]
            position += 1
            if entropy_marker == 0x00 or 0xD0 <= entropy_marker <= 0xD7:
                continue
            if entropy_marker != 0xD9:
                raise UnsafeInputError("raster JPEG scan contains an unexpected marker")
            if position != len(data):
                raise UnsafeInputError("raster JPEG contains bytes after its final image")
            output.extend(data[entropy_start:position])
            assert dimensions is not None
            return bytes(output), dimensions
    if not saw_scan:
        raise UnsafeInputError("raster JPEG has no image scan")
    raise UnsafeInputError("raster JPEG has no terminal marker")


def _pdf_dimension(value: int, maximum: int) -> str:
    thousandths = (792_000 * value + maximum // 2) // maximum
    whole, fraction = divmod(thousandths, 1000)
    if not fraction:
        return str(whole)
    return f"{whole}.{fraction:03d}".rstrip("0")


def _inert_raster_pdf_bytes(
    pages: Sequence[tuple[bytes, tuple[int, int]]],
) -> bytes:
    if not pages:
        raise UnsafeInputError("an inert PDF requires at least one raster page")
    page_object_ids = [3 + index * 3 for index in range(len(pages))]
    objects: list[bytes] = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        (
            "<< /Type /Pages /Kids ["
            + " ".join(f"{object_id} 0 R" for object_id in page_object_ids)
            + f"] /Count {len(pages)} >>"
        ).encode("ascii"),
    ]
    for index, (jpeg, (width, height)) in enumerate(pages, 1):
        page_id = 3 + (index - 1) * 3
        image_id = page_id + 1
        content_id = page_id + 2
        maximum = max(width, height)
        width_points = _pdf_dimension(width, maximum)
        height_points = _pdf_dimension(height, maximum)
        image_name = f"Im{index}"
        page = (
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {width_points} {height_points}] "
            f"/Resources << /XObject << /{image_name} {image_id} 0 R >> >> "
            f"/Contents {content_id} 0 R >>"
        ).encode("ascii")
        image = (
            f"<< /Type /XObject /Subtype /Image /Width {width} /Height {height} "
            f"/ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode "
            f"/Length {len(jpeg)} >>\nstream\n"
        ).encode("ascii") + jpeg + b"\nendstream"
        content_stream = (
            f"q\n{width_points} 0 0 {height_points} 0 0 cm\n/{image_name} Do\nQ\n"
        ).encode("ascii")
        content = (
            f"<< /Length {len(content_stream)} >>\nstream\n"
        ).encode("ascii") + content_stream + b"endstream"
        objects.extend((page, image, content))

    output = bytearray(INERT_PDF_HEADER)
    offsets = [0]
    for object_id, body in enumerate(objects, 1):
        offsets.append(len(output))
        output.extend(f"{object_id} 0 obj\n".encode("ascii"))
        output.extend(body)
        output.extend(b"\nendobj\n")
    xref = len(output)
    output.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    output.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        output.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    output.extend(
        (
            f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
            f"startxref\n{xref}\n%%EOF\n"
        ).encode("ascii")
    )
    return bytes(output)


def inspect_inert_raster_pdf(data: bytes) -> InertPdf:
    """Strictly parse the one image-only PDF profile emitted by this module."""
    if not data.startswith(INERT_PDF_HEADER):
        raise UnsafeInputError("PDF is not in the inert raster profile")
    xref_marker = data.rfind(b"\nxref\n")
    xref_position = xref_marker + 1
    if xref_marker < len(INERT_PDF_HEADER):
        raise UnsafeInputError("inert PDF has no cross-reference table")
    tail = data[xref_position:]
    match = re.fullmatch(
        rb"xref\n0 ([0-9]+)\n0000000000 65535 f \n"
        rb"((?:[0-9]{10} 00000 n \n)+)"
        rb"trailer\n<< /Size ([0-9]+) /Root 1 0 R >>\n"
        rb"startxref\n([0-9]+)\n%%EOF\n",
        tail,
    )
    if match is None:
        raise UnsafeInputError("inert PDF cross-reference table is not canonical")
    object_count_plus_one = int(match.group(1))
    if int(match.group(3)) != object_count_plus_one:
        raise UnsafeInputError("inert PDF trailer size disagrees with its xref")
    if int(match.group(4)) != xref_position:
        raise UnsafeInputError("inert PDF startxref is invalid")
    offsets = [
        int(line.split()[0]) for line in match.group(2).splitlines()
    ]
    object_count = object_count_plus_one - 1
    if object_count < 5 or (object_count - 2) % 3:
        raise UnsafeInputError("inert PDF object count is invalid")
    page_count = (object_count - 2) // 3
    if len(offsets) != object_count:
        raise UnsafeInputError("inert PDF xref row count is invalid")
    if offsets != sorted(offsets) or offsets[0] != len(INERT_PDF_HEADER):
        raise UnsafeInputError("inert PDF object offsets are invalid")
    slices: list[bytes] = []
    for index, offset in enumerate(offsets):
        end = offsets[index + 1] if index + 1 < len(offsets) else xref_position
        if offset >= end or end > xref_position:
            raise UnsafeInputError("inert PDF object bounds are invalid")
        slices.append(data[offset:end])
    if slices[0] != b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n":
        raise UnsafeInputError("inert PDF catalog is not canonical")
    page_ids = [3 + index * 3 for index in range(page_count)]
    expected_pages = (
        "2 0 obj\n<< /Type /Pages /Kids ["
        + " ".join(f"{value} 0 R" for value in page_ids)
        + f"] /Count {page_count} >>\nendobj\n"
    ).encode("ascii")
    if slices[1] != expected_pages:
        raise UnsafeInputError("inert PDF page tree is not canonical")

    jpegs: list[bytes] = []
    dimensions: list[tuple[int, int]] = []
    for index in range(1, page_count + 1):
        page_id = 3 + (index - 1) * 3
        image_id = page_id + 1
        content_id = page_id + 2
        image_object = slices[image_id - 1]
        prefix_match = re.match(
            (
                rf"{image_id} 0 obj\n<< /Type /XObject /Subtype /Image "
                rf"/Width ([0-9]+) /Height ([0-9]+) /ColorSpace /DeviceRGB "
                rf"/BitsPerComponent 8 /Filter /DCTDecode /Length ([0-9]+) >>\nstream\n"
            ).encode("ascii"),
            image_object,
        )
        if prefix_match is None:
            raise UnsafeInputError("inert PDF image object is not canonical")
        width = int(prefix_match.group(1))
        height = int(prefix_match.group(2))
        length = int(prefix_match.group(3))
        start = prefix_match.end()
        end = start + length
        if image_object[end:] != b"\nendstream\nendobj\n":
            raise UnsafeInputError("inert PDF image stream length is invalid")
        jpeg = image_object[start:end]
        sanitized, parsed_dimensions = _sanitized_baseline_jpeg(
            jpeg, maximum_dimension_pixels=MAX_RASTER_DIMENSION_PIXELS
        )
        if sanitized != jpeg or parsed_dimensions != (width, height):
            raise UnsafeInputError("inert PDF image stream is not canonical")
        maximum = max(width, height)
        width_points = _pdf_dimension(width, maximum)
        height_points = _pdf_dimension(height, maximum)
        image_name = f"Im{index}"
        expected_page = (
            f"{page_id} 0 obj\n<< /Type /Page /Parent 2 0 R "
            f"/MediaBox [0 0 {width_points} {height_points}] /Resources "
            f"<< /XObject << /{image_name} {image_id} 0 R >> >> "
            f"/Contents {content_id} 0 R >>\nendobj\n"
        ).encode("ascii")
        if slices[page_id - 1] != expected_page:
            raise UnsafeInputError("inert PDF page object is not canonical")
        content_stream = (
            f"q\n{width_points} 0 0 {height_points} 0 0 cm\n/{image_name} Do\nQ\n"
        ).encode("ascii")
        expected_content = (
            f"{content_id} 0 obj\n<< /Length {len(content_stream)} >>\nstream\n"
        ).encode("ascii") + content_stream + b"endstream\nendobj\n"
        if slices[content_id - 1] != expected_content:
            raise UnsafeInputError("inert PDF content stream is not canonical")
        jpegs.append(jpeg)
        dimensions.append((width, height))
    return InertPdf(
        data=data,
        page_count=page_count,
        page_sha256s=tuple(sha256_bytes(item) for item in jpegs),
        pixel_dimensions=tuple(dimensions),
    )


def rasterize_pdf_to_inert_pdf(
    data: bytes,
    *,
    artifact_id: str,
    private_tmp: Path,
    maximum_input_bytes: int,
    timeout_seconds: int,
) -> InertPdf:
    """Render untrusted PDF pages in a sandbox and rebuild a canonical inert PDF."""
    inspection, _ = inspect_pdf_bytes(
        data,
        artifact_id=artifact_id,
        private_tmp=private_tmp,
        maximum_bytes=maximum_input_bytes,
        timeout_seconds=timeout_seconds,
    )
    page_count = inspection.get("page_count")
    if inspection.get("status") != "READABLE" or not isinstance(page_count, int):
        raise UnsafeInputError("PDF cannot be safely rasterized because it is unreadable")
    if not 1 <= page_count <= MAX_RASTER_PAGES:
        raise UnsafeInputError("PDF exceeds the raster page limit")
    pdftoppm = shutil.which("pdftoppm")
    if not pdftoppm:
        raise PipelineError("required deterministic renderer not found: pdftoppm")
    private_mkdir(private_tmp)
    page_images: list[tuple[bytes, tuple[int, int]]] = []
    raw_total = 0
    with tempfile.TemporaryDirectory(prefix="raster-", dir=private_tmp) as temporary:
        render_root = Path(temporary)
        render_root.chmod(PRIVATE_DIRECTORY_MODE)
        input_path = render_root / "input.pdf"
        write_private_bytes(input_path, data)
        expected_names = {"input.pdf"}
        for page in range(1, page_count + 1):
            prefix = f"page-{page:04d}"
            result = run_bounded_tool(
                (
                    pdftoppm,
                    "-q",
                    "-f",
                    str(page),
                    "-l",
                    str(page),
                    "-singlefile",
                    "-scale-to",
                    str(MAX_RASTER_DIMENSION_PIXELS),
                    "-jpeg",
                    "-jpegopt",
                    "quality=92,progressive=n,optimize=y",
                    "input.pdf",
                    prefix,
                ),
                working_directory=render_root,
                timeout_seconds=timeout_seconds,
                writable_working_directory=True,
                file_size_limit_bytes=MAX_RASTER_PAGE_BYTES,
            )
            if result.timed_out:
                raise UnsafeInputError("PDF rasterization timed out")
            if result.returncode != 0:
                raise UnsafeInputError("PDF rasterization failed")
            output_path = render_root / f"{prefix}.jpg"
            expected_names.add(output_path.name)
            raw = safe_file_bytes(output_path, MAX_RASTER_PAGE_BYTES)
            raw_total += len(raw)
            if raw_total > MAX_RASTER_TOTAL_BYTES:
                raise UnsafeInputError("PDF raster output exceeds the aggregate limit")
            sanitized, dimensions = _sanitized_baseline_jpeg(
                raw, maximum_dimension_pixels=MAX_RASTER_DIMENSION_PIXELS
            )
            page_images.append((sanitized, dimensions))
            actual_names = {path.name for path in render_root.iterdir()}
            if actual_names != expected_names:
                raise UnsafeInputError("renderer created an unexpected output file")
    output = _inert_raster_pdf_bytes(page_images)
    if len(output) > MAX_RASTER_TOTAL_BYTES:
        raise UnsafeInputError("inert PDF exceeds the aggregate output limit")
    parsed = inspect_inert_raster_pdf(output)
    post_inspection, _ = inspect_pdf_bytes(
        output,
        artifact_id=artifact_id,
        private_tmp=private_tmp,
        maximum_bytes=MAX_RASTER_TOTAL_BYTES,
        timeout_seconds=timeout_seconds,
    )
    if any(
        (
            parsed.page_count != page_count,
            post_inspection.get("status") != "READABLE",
            post_inspection.get("page_count") != page_count,
            post_inspection.get("text_extraction") != "EMPTY",
        )
    ):
        raise UnsafeInputError("inert PDF failed post-render verification")
    return parsed


def _zip_member_path(name: str) -> tuple[str | None, str | None]:
    if not name or "\\" in name or "\x00" in name:
        return None, "UNSAFE_ARCHIVE_PATH"
    if "//" in name.rstrip("/"):
        return None, "UNSAFE_ARCHIVE_PATH"
    if any(ord(character) < 32 or ord(character) == 127 for character in name):
        return None, "UNSAFE_ARCHIVE_PATH"
    if name.startswith(("/", "//")) or re.match(r"^[A-Za-z]:", name):
        return None, "ABSOLUTE_ARCHIVE_PATH"
    raw_parts = name.rstrip("/").split("/")
    if any(part == ".." for part in raw_parts):
        return None, "TRAVERSAL_ARCHIVE_PATH"
    if any(part in {"", "."} for part in raw_parts):
        return None, "UNSAFE_ARCHIVE_PATH"
    pure = PurePosixPath(name)
    if pure.is_absolute() or any(part in {"", ".", ".."} for part in pure.parts):
        return None, "TRAVERSAL_ARCHIVE_PATH"
    if len(name.encode("utf-8")) > 1024 or len(pure.parts) > 32:
        return None, "ARCHIVE_PATH_LIMIT"
    normalized = unicodedata.normalize("NFC", pure.as_posix())
    return normalized, None


def _zip_directory_summary(
    data: bytes,
    *,
    maximum_entries: int,
    maximum_directory_bytes: int,
) -> tuple[int, int, bool] | None:
    """Validate/count classic central records without materializing ``ZipInfo``s.

    EOCD counters are attacker-controlled, so trusting them before calling
    :meth:`ZipFile.infolist` would permit a forged small count to hide a very
    large central directory.  This bounded structural pass stops after one
    record beyond the configured limit and reports the resource breach before
    Python allocates an object for every member.
    """
    signature = b"PK\x05\x06"
    lower = max(0, len(data) - 65_557)
    position = data.rfind(signature, lower)
    while position >= lower:
        if position + 22 <= len(data):
            fields = struct.unpack_from("<4s4H2LH", data, position)
            comment_length = fields[-1]
            if position + 22 + comment_length == len(data):
                disk_number, directory_disk = fields[1], fields[2]
                entries_on_disk, declared_entries = fields[3], fields[4]
                directory_bytes, directory_offset = fields[5], fields[6]
                if (
                    disk_number != 0
                    or directory_disk != 0
                    or entries_on_disk != declared_entries
                ):
                    raise UnsafeInputError("multi-disk ZIP archives are not supported")
                if declared_entries == 0xFFFF or directory_bytes == 0xFFFFFFFF:
                    raise UnsafeInputError("ZIP64 archives require human triage")
                if (
                    declared_entries > maximum_entries
                    or directory_bytes > maximum_directory_bytes
                ):
                    return declared_entries, directory_bytes, True

                # Account for a possible self-extracting prefix in the same
                # way as ``zipfile``: stored offsets are relative to the ZIP
                # payload, while the EOCD position is absolute in ``data``.
                prefix_bytes = position - directory_bytes - directory_offset
                if prefix_bytes < 0:
                    raise UnsafeInputError("ZIP central directory has invalid bounds")
                cursor = directory_offset + prefix_bytes
                directory_end = cursor + directory_bytes
                if directory_end != position:
                    raise UnsafeInputError("ZIP central directory is not contiguous")

                actual_entries = 0
                while cursor < directory_end:
                    if (
                        cursor + 46 > directory_end
                        or data[cursor : cursor + 4] != b"PK\x01\x02"
                    ):
                        raise UnsafeInputError("ZIP central directory is malformed")
                    name_length, extra_length, member_comment_length = struct.unpack_from(
                        "<3H", data, cursor + 28
                    )
                    disk_start = struct.unpack_from("<H", data, cursor + 34)[0]
                    if disk_start != 0:
                        raise UnsafeInputError("multi-disk ZIP members are not supported")
                    record_bytes = (
                        46 + name_length + extra_length + member_comment_length
                    )
                    if cursor + record_bytes > directory_end:
                        raise UnsafeInputError("ZIP central record exceeds directory bounds")
                    cursor += record_bytes
                    actual_entries += 1
                    if actual_entries > maximum_entries:
                        return actual_entries, directory_bytes, True
                if actual_entries != declared_entries:
                    raise UnsafeInputError("ZIP EOCD entry count does not match directory")
                return actual_entries, directory_bytes, False
        position = data.rfind(signature, lower, position)
    return None


def inspect_zip_bytes(
    data: bytes,
    *,
    artifact_id: str,
    limits: Mapping[str, Any],
) -> ArchiveResult:
    limit_codes: set[str] = set()
    unsafe_codes: set[str] = set()
    member_names: list[str] = []
    solution_member: str | None = None
    solution_pdf: bytes | None = None
    entry_count = total_bytes = maximum_entry = 0
    maximum_ratio = 0.0
    traversal = absolute = symlink = duplicate = nested = False
    seen: set[str] = set()
    try:
        maximum_entries = int(limits["max_entries"])
        # A classic central record has a 46-byte fixed header, and the local
        # path policy permits at most 1024 UTF-8 bytes. Extra/comment fields
        # are each limited by their two-byte ZIP lengths. This derived bound
        # prevents an over-wide directory even if a configured byte ceiling is
        # later increased.
        maximum_directory_bytes = min(
            int(limits["max_total_expanded_bytes"]),
            maximum_entries * (46 + 1024 + 65_535 + 65_535),
        )
        directory_summary = _zip_directory_summary(
            data,
            maximum_entries=maximum_entries,
            maximum_directory_bytes=maximum_directory_bytes,
        )
        if directory_summary is None:
            # ``zipfile`` accepts concatenated/trailing payloads and would
            # otherwise materialize their central directory before we can
            # enforce entry limits. The pilot accepts only a classic ZIP whose
            # EOCD (including its declared comment) closes the input exactly.
            unsafe_codes.add("ARCHIVE_EOCD_INVALID")
            raise UnsafeInputError("ZIP has no bounded terminal directory")
        counted_entries, directory_bytes, limit_exceeded = directory_summary
        entry_count = counted_entries
        if counted_entries > maximum_entries:
            limit_codes.add("ARCHIVE_ENTRY_LIMIT")
        if directory_bytes > maximum_directory_bytes:
            limit_codes.add("ARCHIVE_DIRECTORY_BYTE_LIMIT")
        if limit_exceeded and not limit_codes:
            limit_codes.add("ARCHIVE_DIRECTORY_BYTE_LIMIT")
        if limit_codes:
            raise UnsafeInputError("ZIP central directory exceeds configured limits")
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            entries = archive.infolist()
            entry_count = len(entries)
            if entry_count > int(limits["max_entries"]):
                limit_codes.add("ARCHIVE_ENTRY_LIMIT")
            solution_candidates: list[zipfile.ZipInfo] = []
            for info in entries:
                raw_name = getattr(info, "orig_filename", info.filename)
                normalized, path_error = _zip_member_path(raw_name)
                if path_error == "TRAVERSAL_ARCHIVE_PATH":
                    traversal = True
                    unsafe_codes.add(path_error)
                elif path_error == "ABSOLUTE_ARCHIVE_PATH":
                    absolute = True
                    unsafe_codes.add(path_error)
                elif path_error:
                    unsafe_codes.add(path_error)
                if normalized is None:
                    continue
                folded = normalized.casefold()
                if folded in seen:
                    duplicate = True
                    unsafe_codes.add("DUPLICATE_NORMALIZED_PATH")
                seen.add(folded)
                member_names.append(normalized)
                unix_mode = info.external_attr >> 16
                file_type = stat.S_IFMT(unix_mode)
                if file_type and file_type not in {stat.S_IFREG, stat.S_IFDIR}:
                    symlink = True
                    unsafe_codes.add("ARCHIVE_SPECIAL_FILE")
                name_is_directory = raw_name.endswith("/")
                if (
                    (file_type == stat.S_IFDIR and not name_is_directory)
                    or (file_type == stat.S_IFREG and name_is_directory)
                    or (name_is_directory and info.file_size != 0)
                ):
                    unsafe_codes.add("ARCHIVE_TYPE_NAME_MISMATCH")
                if info.flag_bits & 0x1:
                    unsafe_codes.add("ARCHIVE_ENCRYPTED_MEMBER")
                total_bytes += info.file_size
                maximum_entry = max(maximum_entry, info.file_size)
                ratio = info.file_size / max(info.compress_size, 1)
                maximum_ratio = max(maximum_ratio, ratio)
                if info.file_size > int(limits["max_entry_bytes"]):
                    limit_codes.add("ARCHIVE_MEMBER_BYTE_LIMIT")
                suffix = PurePosixPath(normalized).suffix.lower()
                if suffix in NESTED_ARCHIVE_SUFFIXES and not info.is_dir():
                    nested = True
                    unsafe_codes.add("NESTED_ARCHIVE")
                parts = PurePosixPath(normalized).parts
                if (
                    not info.is_dir()
                    and len(parts) <= 2
                    and parts[-1] == "solution.pdf"
                ):
                    solution_candidates.append(info)
            if total_bytes > int(limits["max_total_expanded_bytes"]):
                limit_codes.add("ARCHIVE_TOTAL_BYTE_LIMIT")
            if maximum_ratio > float(limits["max_compression_ratio"]):
                limit_codes.add("ARCHIVE_COMPRESSION_RATIO_LIMIT")
            if not unsafe_codes and not limit_codes:
                for info in entries:
                    if info.is_dir() or info.file_size == 0:
                        continue
                    try:
                        with archive.open(info, "r") as stream:
                            bytes_read = 0
                            found_nested = False
                            first_bytes = b""
                            prior_zip_prefix = b""
                            zip_structure_seen = False
                            while True:
                                chunk = stream.read(1_048_576)
                                if not chunk:
                                    break
                                bytes_read += len(chunk)
                                if (
                                    bytes_read > int(limits["max_entry_bytes"])
                                    or bytes_read > info.file_size
                                ):
                                    raise zipfile.BadZipFile(
                                        "member expanded beyond declared limits"
                                    )
                                if len(first_bytes) < 512:
                                    first_bytes += chunk[: 512 - len(first_bytes)]
                                zip_window = prior_zip_prefix + chunk
                                if any(
                                    signature in zip_window
                                    for signature in (
                                        b"PK\x03\x04",
                                        b"PK\x01\x02",
                                        b"PK\x05\x06",
                                    )
                                ):
                                    zip_structure_seen = True
                                prior_zip_prefix = zip_window[-3:]
                            if bytes_read != info.file_size:
                                raise zipfile.BadZipFile("member size changed while reading")
                            non_zip_signatures = tuple(
                                signature
                                for signature in NESTED_ARCHIVE_SIGNATURES
                                if not signature.startswith(b"PK")
                            )
                            found_nested = any(
                                first_bytes.startswith(signature)
                                for signature in non_zip_signatures
                            )
                            found_nested = found_nested or zip_structure_seen
                            found_nested = found_nested or first_bytes[257:263] in {
                                b"ustar\x00",
                                b"ustar ",
                            }
                    except (OSError, RuntimeError, UnicodeError, ValueError, zlib.error, zipfile.BadZipFile):
                        unsafe_codes.add("ARCHIVE_MEMBER_READ_ERROR")
                        break
                    if found_nested:
                        nested = True
                        unsafe_codes.add("NESTED_ARCHIVE")
                        break
            if not unsafe_codes and not limit_codes and len(solution_candidates) == 1:
                candidate = solution_candidates[0]
                if candidate.file_size <= int(limits["max_entry_bytes"]):
                    with archive.open(candidate, "r") as stream:
                        solution_pdf = stream.read(int(limits["max_entry_bytes"]) + 1)
                    if len(solution_pdf) != candidate.file_size:
                        raise zipfile.BadZipFile("member size changed while reading")
                    solution_member = unicodedata.normalize(
                        "NFC", getattr(candidate, "orig_filename", candidate.filename)
                    )
    except UnsafeInputError:
        status = "RESOURCE_LIMIT" if limit_codes else "UNSAFE"
        if not limit_codes:
            unsafe_codes.add("ARCHIVE_UNSUPPORTED")
        solution_member = None
        solution_pdf = None
    except (OSError, RuntimeError, UnicodeError, ValueError, zlib.error, zipfile.BadZipFile, zipfile.LargeZipFile):
        status = "ERROR"
        unsafe_codes.add("ARCHIVE_READ_ERROR")
        solution_member = None
        solution_pdf = None
    else:
        if unsafe_codes:
            status = "UNSAFE"
        elif limit_codes:
            status = "RESOURCE_LIMIT"
        else:
            status = "SAFE"
    all_codes = sorted(unsafe_codes | limit_codes)
    record = {
        "artifact_id": artifact_id,
        "status": status,
        "entry_count": entry_count,
        "total_expanded_bytes": total_bytes,
        "maximum_entry_bytes": maximum_entry,
        "maximum_compression_ratio": round(maximum_ratio, 12),
        "has_traversal_path": traversal,
        "has_absolute_path": absolute,
        "has_symlink": symlink,
        "has_duplicate_normalized_path": duplicate,
        "has_nested_archive": nested,
        "limit_codes": all_codes,
    }
    return ArchiveResult(
        record=record,
        member_names=tuple(member_names),
        solution_member=solution_member,
        solution_pdf=solution_pdf,
    )


def artifact_ref(
    repository_root: Path,
    path: Path,
    *,
    artifact_id: str,
    role: str,
    media_type: str,
) -> dict[str, Any]:
    data = safe_file_bytes(path)
    return {
        "artifact_id": artifact_id,
        "role": role,
        "path": repository_relative(repository_root, path),
        "sha256": sha256_bytes(data),
        "byte_count": len(data),
        "media_type": media_type,
    }


def hash_ref(
    data: bytes, *, artifact_id: str, role: str, media_type: str
) -> dict[str, Any]:
    return {
        "artifact_id": artifact_id,
        "role": role,
        "sha256": sha256_bytes(data),
        "byte_count": len(data),
        "media_type": media_type,
    }


def media_type_for_path(path: Path) -> str:
    suffix = path.suffix.lower()
    return {
        ".json": "application/json",
        ".jsonl": "application/x-ndjson",
        ".yaml": "application/yaml",
        ".yml": "application/yaml",
        ".md": "text/markdown",
        ".tmpl": "text/plain",
        ".tex": "application/x-tex",
        ".pdf": "application/pdf",
        ".py": "text/x-python",
    }.get(suffix, "application/octet-stream")


def _minimal_pdf_bytes(text: str, *, author: str | None = None) -> bytes:
    """Create a tiny deterministic one-page PDF for wholly synthetic tests."""
    escaped = text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    stream = f"BT /F1 12 Tf 72 720 Td ({escaped}) Tj ET\n".encode("ascii")
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
        b"/Resources << /Font << /F1 5 0 R >> >> /Contents 4 0 R >>",
        b"<< /Length " + str(len(stream)).encode("ascii") + b" >>\nstream\n" + stream + b"endstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]
    if author is not None:
        encoded_author = (b"\xfe\xff" + author.encode("utf-16-be")).hex().upper()
        objects.append(f"<< /Author <{encoded_author}> >>".encode("ascii"))
    output = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for index, body in enumerate(objects, 1):
        offsets.append(len(output))
        output.extend(f"{index} 0 obj\n".encode("ascii"))
        output.extend(body)
        output.extend(b"\nendobj\n")
    xref = len(output)
    output.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    output.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        output.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    output.extend(
        (
            f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R"
            f"{' /Info 6 0 R' if author is not None else ''} >>\n"
            f"startxref\n{xref}\n%%EOF\n"
        ).encode("ascii")
    )
    return bytes(output)


class EventLog:
    def __init__(
        self,
        path: Path,
        *,
        run_id: str,
        validator: jsonschema.Draft202012Validator,
        now: Callable[[], str],
    ) -> None:
        self.path = path
        self.run_id = run_id
        self.validator = validator
        self.now = now
        if path.exists():
            lines = safe_file_bytes(path).splitlines()
            self.sequence = len(lines)
            self.last_timestamp = None
            for expected_sequence, raw_line in enumerate(lines, 1):
                event = json.loads(raw_line)
                self.validator.validate(event)
                if raw_line + b"\n" != canonical_json_bytes(event):
                    raise ContractError("event log contains noncanonical JSON")
                occurred_at = parse_utc_timestamp(event["occurred_at"])
                if any(
                    (
                        event["run_id"] != self.run_id,
                        event["sequence"] != expected_sequence,
                        event["event_id"] != f"EVT-{expected_sequence:06d}",
                        self.last_timestamp is not None
                        and occurred_at < self.last_timestamp,
                    )
                ):
                    raise ContractError(
                        "event log is not contiguous, chronological, and run-bound"
                    )
                self.last_timestamp = occurred_at
        else:
            write_private_bytes(path, b"")
            self.sequence = 0
            self.last_timestamp = None

    @property
    def next_event_id(self) -> str:
        return f"EVT-{self.sequence + 1:06d}"

    def append(
        self,
        *,
        stage: str,
        event_type: str,
        subject_type: str,
        subject_id: str,
        outcome: str,
        reason_code: str,
        inputs: Sequence[dict[str, Any]] = (),
        outputs: Sequence[dict[str, Any]] = (),
        payload: Mapping[str, Any] | None = None,
        parent_event_id: str | None = None,
    ) -> dict[str, Any]:
        sequence = self.sequence + 1
        occurred_at = self.now()
        parsed = parse_utc_timestamp(occurred_at)
        if self.last_timestamp is not None and parsed < self.last_timestamp:
            raise ContractError("event timestamps must be chronological")
        event: dict[str, Any] = {
            "schema_version": SCHEMA_VERSION,
            "event_id": f"EVT-{sequence:06d}",
            "run_id": self.run_id,
            "sequence": sequence,
            "occurred_at": occurred_at,
            "stage": stage,
            "event_type": event_type,
            "actor": {
                "actor_type": "TOOL",
                "actor_id": "ne630-review-pipeline",
                "version": VERSION,
            },
            "subject": {"subject_type": subject_type, "subject_id": subject_id},
            "outcome": outcome,
            "reason_code": reason_code,
            "inputs": list(inputs),
            "outputs": list(outputs),
            "payload": dict(payload or {}),
        }
        if parent_event_id is not None:
            event["parent_event_id"] = parent_event_id
        errors = sorted(self.validator.iter_errors(event), key=lambda item: list(item.path))
        if errors:
            joined = "; ".join(error.message for error in errors[:5])
            raise ContractError(f"invalid event: {joined}")
        data = canonical_json_bytes(event)
        flags = os.O_WRONLY | os.O_APPEND
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        descriptor = os.open(self.path, flags)
        try:
            append_offset = os.fstat(descriptor).st_size
            view = memoryview(data)
            written_total = 0
            try:
                while written_total < len(view):
                    try:
                        written = os.write(descriptor, view[written_total:])
                    except InterruptedError:
                        continue
                    if written <= 0:
                        raise OSError("event log append made no progress")
                    written_total += written
            except BaseException:
                # A partial JSONL record is never a valid append. Roll back to
                # the known record boundary before surfacing the interruption.
                os.ftruncate(descriptor, append_offset)
                os.fsync(descriptor)
                raise
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        self.path.chmod(PRIVATE_FILE_MODE)
        self.sequence = sequence
        self.last_timestamp = parsed
        return event


class HumanDecisionLog:
    """Canonical, append-only instructor decisions bound to one run."""

    def __init__(
        self,
        path: Path,
        *,
        run_id: str,
        validator: jsonschema.Draft202012Validator,
        now: Callable[[], str],
    ) -> None:
        self.path = path
        self.run_id = run_id
        self.validator = validator
        self.now = now
        if path.exists():
            lines = safe_file_bytes(path).splitlines()
            self.sequence = len(lines)
            self.last_timestamp: dt.datetime | None = None
            for expected_sequence, raw_line in enumerate(lines, 1):
                decision = json.loads(raw_line)
                self.validator.validate(decision)
                if raw_line + b"\n" != canonical_json_bytes(decision):
                    raise ContractError("human-decision log contains noncanonical JSON")
                made_at = parse_utc_timestamp(decision["made_at"])
                if any(
                    (
                        decision["run_id"] != self.run_id,
                        decision["sequence"] != expected_sequence,
                        decision["decision_id"] != f"DEC-{expected_sequence:06d}",
                        self.last_timestamp is not None
                        and made_at < self.last_timestamp,
                    )
                ):
                    raise ContractError(
                        "human-decision log is not contiguous, chronological, and run-bound"
                    )
                self.last_timestamp = made_at
        else:
            write_private_bytes(path, b"")
            self.sequence = 0
            self.last_timestamp = None

    @property
    def next_decision_id(self) -> str:
        return f"DEC-{self.sequence + 1:06d}"

    def append(
        self,
        *,
        decision_id: str,
        actor_id: str,
        authority: str,
        decision_type: str,
        subject_type: str,
        subject_id: str,
        prior_state: str | None,
        resulting_state: str,
        rationale: str,
        evidence_locators: Sequence[dict[str, Any]],
        affected_record_ids: Sequence[str],
    ) -> dict[str, Any]:
        sequence = self.sequence + 1
        if decision_id != f"DEC-{sequence:06d}":
            raise ContractError("human decision ID is not the next contiguous ID")
        made_at = self.now()
        parsed = parse_utc_timestamp(made_at)
        if self.last_timestamp is not None and parsed < self.last_timestamp:
            raise ContractError("human-decision timestamps must be chronological")
        decision = {
            "schema_version": SCHEMA_VERSION,
            "decision_id": decision_id,
            "run_id": self.run_id,
            "sequence": sequence,
            "made_at": made_at,
            "decision_maker": {
                "actor_type": "HUMAN",
                "actor_id": actor_id,
                "role": "INSTRUCTOR",
            },
            "authority": authority,
            "decision_type": decision_type,
            "subject": {
                "subject_type": subject_type,
                "subject_id": subject_id,
            },
            "prior_state": prior_state,
            "resulting_state": resulting_state,
            "rationale": rationale,
            "state": "ADOPTED",
            "evidence_locators": list(evidence_locators),
            "affected_record_ids": list(affected_record_ids),
            "contains_source_identifiers": False,
        }
        errors = sorted(
            self.validator.iter_errors(decision), key=lambda item: list(item.path)
        )
        if errors:
            joined = "; ".join(error.message for error in errors[:5])
            raise ContractError(f"invalid human decision: {joined}")
        data = canonical_json_bytes(decision)
        flags = os.O_WRONLY | os.O_APPEND
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        descriptor = os.open(self.path, flags)
        try:
            append_offset = os.fstat(descriptor).st_size
            view = memoryview(data)
            written_total = 0
            try:
                while written_total < len(view):
                    try:
                        written = os.write(descriptor, view[written_total:])
                    except InterruptedError:
                        continue
                    if written <= 0:
                        raise OSError("human-decision log append made no progress")
                    written_total += written
            except BaseException:
                os.ftruncate(descriptor, append_offset)
                os.fsync(descriptor)
                raise
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        self.path.chmod(PRIVATE_FILE_MODE)
        self.sequence = sequence
        self.last_timestamp = parsed
        return decision


class ReviewPipeline:
    def __init__(
        self,
        repository_root: Path,
        *,
        config_path: Path | None = None,
        codebook_path: Path | None = None,
        now: Callable[[], str] = utc_now,
    ) -> None:
        self.repository_root = repository_root.resolve()
        self.framework_root = self.repository_root / "grades/review/f2026"
        self.config_path = (
            config_path.resolve()
            if config_path is not None
            else self.framework_root / "config.yaml"
        )
        try:
            self.config_path.relative_to(self.repository_root)
        except ValueError as exc:
            raise UnsafeInputError(
                "configuration must be stored beneath the repository root"
            ) from exc
        self.schema_root = self.framework_root / "schemas"
        self.templates_root = self.framework_root / "templates"
        self.now = now
        self.codebook_path = codebook_path.resolve() if codebook_path else None
        if not self.config_path.is_file():
            raise PipelineError(f"configuration not found: {self.config_path}")
        self.config_bytes = safe_file_bytes(self.config_path)
        self.config = yaml.safe_load(self.config_bytes)
        if not isinstance(self.config, dict):
            raise ContractError("config.yaml must contain a mapping")
        self.schemas: dict[str, dict[str, Any]] = {}
        self.validators: dict[str, jsonschema.Draft202012Validator] = {}
        for path in sorted(self.schema_root.glob("*.schema.json")):
            document = json.loads(safe_file_bytes(path).decode("utf-8"))
            name = path.name.removesuffix(".schema.json")
            self.schemas[name] = document
            self.validators[name] = jsonschema.Draft202012Validator(document)
        config_validator = self.validators.get("config")
        if config_validator is None:
            raise ContractError("configuration schema is missing")
        config_errors = sorted(
            config_validator.iter_errors(self.config), key=lambda item: list(item.path)
        )
        if config_errors:
            first = config_errors[0]
            location = "/" + "/".join(
                str(part) for part in first.absolute_path
            )
            raise ContractError(
                f"configuration fails {first.validator or 'schema'} at {location}"
            )
        processing = self.config["processing"]
        self.submission_root = self.repository_root / assert_relative_path(
            processing["submission_root"]
        )
        self.review_root = self.repository_root / assert_relative_path(
            processing["review_root"]
        )
        self.runs_root = self.repository_root / assert_relative_path(
            processing["runs_root"]
        )
        self.restricted_root = self.repository_root / assert_relative_path(
            processing["restricted_root"]
        )
        for configured_path in (
            self.submission_root,
            self.review_root,
            self.runs_root,
            self.restricted_root,
        ):
            assert_no_symlink_components(self.repository_root, configured_path)

    @contextlib.contextmanager
    def _mutation_lock(self) -> Iterator[None]:
        """Serialize all run mutations across this repository."""
        lock_root = self.restricted_root / ".locks"
        private_mkdir(lock_root)
        lock_path = lock_root / "pipeline.lock"
        flags = os.O_RDWR | os.O_CREAT
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        descriptor = os.open(lock_path, flags, PRIVATE_FILE_MODE)
        try:
            os.fchmod(descriptor, PRIVATE_FILE_MODE)
            try:
                fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError as exc:
                raise PipelineError("review pipeline is busy with another mutation") from exc
            yield
        finally:
            with contextlib.suppress(OSError):
                fcntl.flock(descriptor, fcntl.LOCK_UN)
            os.close(descriptor)

    @property
    def configuration_id(self) -> str:
        return str(self.config["configuration_id"])

    @property
    def config_sha256(self) -> str:
        return sha256_bytes(self.config_bytes)

    @property
    def executable_sha256(self) -> str:
        return hash_regular_file(Path(__file__).resolve())[0]

    def schema_set_sha256(self) -> str:
        records = []
        for path in sorted(self.schema_root.glob("*.schema.json")):
            digest, size = hash_regular_file(path)
            records.append(
                {
                    "path": repository_relative(self.repository_root, path),
                    "sha256": digest,
                    "byte_count": size,
                }
            )
        return sha256_bytes(canonical_json_bytes(records))

    def discover_codebook(self) -> Path:
        candidates: list[Path] = []
        if self.codebook_path is not None:
            candidates.append(self.codebook_path)
        candidates.append(self.framework_root / "codebook.md")
        candidates.append(
            Path.home()
            / ".openclaw/workspace/peppermint/skills/ne630-homework-review/SKILL.md"
        )
        for candidate in candidates:
            if candidate.is_file() and not candidate.is_symlink():
                return candidate.resolve()
        raise PipelineError(
            "NE 630 review codebook not found; pass --codebook with the approved skill file"
        )

    def preflight_framework(self, *, require_tools: bool = True) -> dict[str, Any]:
        for configured_path in (
            self.submission_root,
            self.review_root,
            self.runs_root,
            self.restricted_root,
        ):
            assert_no_symlink_components(self.repository_root, configured_path)
        if len(self.schemas) != 19:
            raise ContractError(f"expected 19 schemas, found {len(self.schemas)}")
        for name, schema in sorted(self.schemas.items()):
            try:
                jsonschema.Draft202012Validator.check_schema(schema)
            except jsonschema.SchemaError as exc:
                raise ContractError(f"invalid {name} schema: {exc.message}") from exc
        errors = sorted(
            self.validators["config"].iter_errors(self.config),
            key=lambda item: list(item.path),
        )
        if errors:
            joined = "; ".join(error.message for error in errors[:10])
            raise ContractError(f"config.yaml does not validate: {joined}")
        for protected_root in (
            self.submission_root,
            self.runs_root,
            self.restricted_root,
        ):
            probe = protected_root / ".ne630-ignore-probe"
            relative_probe = repository_relative(self.repository_root, probe)
            ignored = self._git(
                "check-ignore", "-q", "--", relative_probe, check=False
            )
            if ignored.returncode != 0:
                raise ContractError(
                    f"protected path is not covered by .gitignore: {relative_probe}"
                )
        required_templates = (
            self.templates_root / "dossier.md.tmpl",
            self.templates_root / "review_queue.md.tmpl",
        )
        missing_templates = [
            str(path)
            for path in required_templates
            if not path.is_file() or path.is_symlink()
        ]
        if missing_templates:
            raise ContractError("missing render templates: " + ", ".join(missing_templates))
        reference_sources = [
            self.config_path,
            self.repository_root
            / assert_relative_path(
                self.config["submission_rules"]["policy_source"]["value"]
            ),
            self.framework_root / "calibration/product_review_protocol.md",
            *required_templates,
            *sorted(self.schema_root.glob("*.schema.json")),
            self.discover_codebook(),
        ]
        configured_assignments = {
            item["id"]: item for item in self.config["assignment"]["assignments"]
        }
        for assignment_id in ASSIGNMENTS:
            assignment = configured_assignments[assignment_id]
            reference_sources.extend(
                (
                    self.repository_root
                    / assert_relative_path(assignment["statement"]),
                    self.repository_root
                    / assert_relative_path(assignment["solution_key"]),
                )
            )
        for reference_source in reference_sources:
            if not reference_source.is_file() or reference_source.is_symlink():
                raise PipelineError(
                    f"required reference is missing or unsafe: {reference_source}"
                )
            safe_file_bytes(reference_source)
        critical_framework_paths = [
            self.repository_root / ".gitignore",
            self.framework_root / "review_pipeline.py",
            self.config_path,
            self.framework_root / "calibration/product_review_protocol.md",
            *required_templates,
            *sorted(self.schema_root.glob("*.schema.json")),
        ]
        for critical_path in critical_framework_paths:
            relative = repository_relative(self.repository_root, critical_path)
            tracked = self._git(
                "ls-files", "--error-unmatch", "--", relative, check=False
            )
            worktree = self._git("diff", "--quiet", "--", relative, check=False)
            index = self._git(
                "diff", "--cached", "--quiet", "--", relative, check=False
            )
            if tracked.returncode != 0 or worktree.returncode != 0 or index.returncode != 0:
                raise ContractError(
                    f"critical review framework file is not tracked and clean: {relative}"
                )
        self.repository_commit()
        tool_paths: dict[str, str] = {}
        tool_dependencies: list[dict[str, str]] = []
        if require_tools:
            for name in ("bwrap", "pdfinfo", "pdftotext", "pdftoppm"):
                resolved = shutil.which(name)
                if not resolved:
                    raise PipelineError(f"required deterministic parser not found: {name}")
                executable = Path(resolved).resolve(strict=True)
                digest, _ = hash_regular_file(executable)
                try:
                    version_result = subprocess.run(
                        (str(executable), "--version" if name == "bwrap" else "-v"),
                        stdin=subprocess.DEVNULL,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        env={"PATH": "/usr/bin:/bin", "LC_ALL": "C", "LANG": "C"},
                        check=False,
                        timeout=5,
                    )
                    version_lines = (
                        version_result.stdout + b"\n" + version_result.stderr
                    ).decode("utf-8").splitlines()
                except (OSError, subprocess.TimeoutExpired, UnicodeDecodeError) as exc:
                    raise PipelineError(
                        f"could not fingerprint deterministic parser: {name}"
                    ) from exc
                version = next((line.strip() for line in version_lines if line.strip()), "")
                if version_result.returncode != 0 or not version or len(version) > 256:
                    raise PipelineError(
                        f"could not fingerprint deterministic parser: {name}"
                    )
                tool_paths[name] = str(executable)
                tool_dependencies.append(
                    {
                        "name": name,
                        "version": version,
                        "executable_sha256": digest,
                    }
                )
            with tempfile.TemporaryDirectory(prefix="ne630-parser-probe-") as temporary:
                probe_root = Path(temporary)
                private_mkdir(probe_root)
                probe_inspection, probe_text = inspect_pdf_bytes(
                    _minimal_pdf_bytes("NE630 parser sandbox probe"),
                    artifact_id="ART-000001",
                    private_tmp=probe_root,
                    maximum_bytes=1_000_000,
                    timeout_seconds=2,
                )
            if (
                probe_inspection["status"] != "READABLE"
                or b"NE630 parser sandbox probe" not in probe_text
            ):
                raise PipelineError(
                    "required parser sandbox could not inspect the synthetic probe PDF"
                )
            with tempfile.TemporaryDirectory(prefix="ne630-renderer-probe-") as temporary:
                rendered_probe = rasterize_pdf_to_inert_pdf(
                    _minimal_pdf_bytes("NE630 renderer sandbox probe"),
                    artifact_id="ART-000001",
                    private_tmp=Path(temporary),
                    maximum_input_bytes=1_000_000,
                    timeout_seconds=5,
                )
            if rendered_probe.page_count != 1:
                raise PipelineError(
                    "required renderer sandbox could not normalize the synthetic probe PDF"
                )
        return {
            "schema_count": len(self.schemas),
            "configuration_id": self.configuration_id,
            "tools": tool_paths,
            "tool_dependencies": tool_dependencies,
        }

    def _git(self, *arguments: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
        return subprocess.run(
            ("git", *arguments),
            cwd=self.repository_root,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=check,
        )

    def repository_commit(self) -> str:
        try:
            value = self._git("rev-parse", "HEAD").stdout.decode("ascii").strip()
        except (OSError, subprocess.CalledProcessError, UnicodeDecodeError) as exc:
            raise PipelineError("repository must have a readable Git HEAD") from exc
        if not re.fullmatch(r"[0-9a-f]{40}(?:[0-9a-f]{24})?", value):
            raise ContractError("Git HEAD is not a supported object ID")
        return value

    def _git_state(self, path: Path) -> tuple[str, str | None]:
        relative = repository_relative(self.repository_root, path)
        tracked = self._git("ls-files", "--error-unmatch", "--", relative, check=False)
        if tracked.returncode != 0:
            return "UNTRACKED", None
        worktree = self._git("diff", "--quiet", "--", relative, check=False)
        index = self._git("diff", "--cached", "--quiet", "--", relative, check=False)
        state = "TRACKED_CLEAN" if worktree.returncode == index.returncode == 0 else "TRACKED_MODIFIED"
        blob = self._git("rev-parse", f"HEAD:{relative}", check=False)
        blob_id = blob.stdout.decode("ascii", errors="ignore").strip()
        if not re.fullmatch(r"[0-9a-f]{40}(?:[0-9a-f]{24})?", blob_id):
            blob_id = None
        return state, blob_id

    def generate_run_id(self) -> str:
        timestamp = self.now()
        parse_utc_timestamp(timestamp)
        compact = timestamp.replace("-", "").replace(":", "")
        suffix = secrets.token_hex(6)
        return f"run-{compact}-{suffix}"

    def _new_stages(self) -> list[dict[str, Any]]:
        return [
            {
                "stage": stage,
                "position": position,
                "status": "NOT_STARTED",
                "event_sequence_start": None,
                "event_sequence_end": None,
                "started_at": None,
                "completed_at": None,
                "reason_code": None,
            }
            for position, stage in enumerate(STAGES, 1)
        ]

    @staticmethod
    def _stage(manifest: dict[str, Any], stage: str) -> dict[str, Any]:
        return next(item for item in manifest["stages"] if item["stage"] == stage)

    def _start_stage(
        self,
        manifest: dict[str, Any],
        events: EventLog,
        stage: str,
        *,
        inputs: Sequence[dict[str, Any]] = (),
    ) -> dict[str, Any]:
        state = self._stage(manifest, stage)
        event = events.append(
            stage=stage,
            event_type="STAGE_STARTED",
            subject_type="RUN",
            subject_id=manifest["run_id"],
            outcome="STARTED",
            reason_code=f"{stage}_STARTED",
            inputs=inputs,
            payload={"stage_status": "RUNNING"},
        )
        state.update(
            {
                "status": "RUNNING",
                "event_sequence_start": event["sequence"],
                "event_sequence_end": None,
                "started_at": event["occurred_at"],
                "completed_at": None,
                "reason_code": None,
            }
        )
        manifest["run_state"] = "RUNNING"
        manifest["updated_at"] = event["occurred_at"]
        return event

    def _complete_stage(
        self,
        manifest: dict[str, Any],
        events: EventLog,
        stage: str,
        *,
        outputs: Sequence[dict[str, Any]] = (),
        message: str | None = None,
    ) -> dict[str, Any]:
        state = self._stage(manifest, stage)
        event = events.append(
            stage=stage,
            event_type="STAGE_COMPLETED",
            subject_type="RUN",
            subject_id=manifest["run_id"],
            outcome="SUCCEEDED",
            reason_code=f"{stage}_COMPLETE",
            outputs=outputs,
            payload={
                "stage_status": "COMPLETE",
                **({"message": message} if message else {}),
            },
        )
        state.update(
            {
                "status": "COMPLETE",
                "event_sequence_end": event["sequence"],
                "completed_at": event["occurred_at"],
                "reason_code": None,
            }
        )
        manifest["run_state"] = "RUNNING"
        manifest["updated_at"] = event["occurred_at"]
        return event

    def _block_stage(
        self,
        manifest: dict[str, Any],
        events: EventLog,
        stage: str,
        code: str,
        message: str,
    ) -> None:
        state = self._stage(manifest, stage)
        event = events.append(
            stage=stage,
            event_type="STAGE_COMPLETED",
            subject_type="RUN",
            subject_id=manifest["run_id"],
            outcome="BLOCKED",
            reason_code=code,
            payload={"stage_status": "BLOCKED", "message": message},
        )
        state.update(
            {
                "status": "BLOCKED",
                "event_sequence_end": event["sequence"],
                "completed_at": event["occurred_at"],
                "reason_code": code,
            }
        )
        manifest["run_state"] = "BLOCKED"
        manifest["updated_at"] = event["occurred_at"]

    def _resume_stage(
        self,
        manifest: dict[str, Any],
        events: EventLog,
        stage: str,
        *,
        inputs: Sequence[dict[str, Any]] = (),
        message: str,
    ) -> dict[str, Any]:
        state = self._stage(manifest, stage)
        if any(
            (
                state["status"] not in {"BLOCKED", "FAILED"},
                state["event_sequence_end"] is None,
                state["reason_code"]
                not in {
                    "IDENTITY_SANITIZATION_REQUIRED",
                    "PREPARE_CALIBRATION_FAILED",
                },
            )
        ):
            raise ContractError("only a blocked or retryable failed stage can be resumed")
        from_event_id = f"EVT-{state['event_sequence_end']:06d}"
        event = events.append(
            stage=stage,
            event_type="RESUMED",
            subject_type="RUN",
            subject_id=manifest["run_id"],
            outcome="STARTED",
            reason_code=f"{stage}_RESUMED",
            inputs=inputs,
            payload={"from_event_id": from_event_id, "message": message},
            parent_event_id=from_event_id,
        )
        state.update(
            {
                "status": "RUNNING",
                "event_sequence_start": event["sequence"],
                "event_sequence_end": None,
                "started_at": event["occurred_at"],
                "completed_at": None,
                "reason_code": None,
            }
        )
        manifest["run_state"] = "RUNNING"
        manifest["updated_at"] = event["occurred_at"]
        return event

    def _skip_stage(
        self,
        manifest: dict[str, Any],
        events: EventLog,
        stage: str,
        code: str,
        message: str,
    ) -> None:
        state = self._stage(manifest, stage)
        event = events.append(
            stage=stage,
            event_type="STAGE_COMPLETED",
            subject_type="RUN",
            subject_id=manifest["run_id"],
            outcome="SKIPPED",
            reason_code=code,
            payload={"stage_status": "SKIPPED", "message": message},
        )
        state.update(
            {
                "status": "SKIPPED",
                "event_sequence_start": event["sequence"],
                "event_sequence_end": event["sequence"],
                "started_at": None,
                "completed_at": event["occurred_at"],
                "reason_code": code,
            }
        )
        manifest["run_state"] = "RUNNING"
        manifest["updated_at"] = event["occurred_at"]

    def _initial_manifest(
        self,
        run_id: str,
        created_at: str,
        *,
        event_ref: dict[str, Any],
        decision_ref: dict[str, Any],
        tool_dependencies: Sequence[Mapping[str, str]],
    ) -> dict[str, Any]:
        return {
            "schema_version": SCHEMA_VERSION,
            "run_id": run_id,
            "configuration_id": self.configuration_id,
            "created_at": created_at,
            "updated_at": created_at,
            "run_state": "INITIALIZED",
            "tool": {
                "name": "ne630-review-pipeline",
                "version": VERSION,
                "python_version": platform.python_version(),
                "executable_sha256": self.executable_sha256,
                "dependencies": [dict(item) for item in tool_dependencies],
            },
            "config_sha256": self.config_sha256,
            "reference_manifest_state": "NOT_FROZEN",
            "reference_manifest_sha256": None,
            "schema_set_sha256": self.schema_set_sha256(),
            "input_summary": {
                "assignment_count": 4,
                "source_group_count": 0,
                "top_level_file_count": 0,
            },
            "inputs": [],
            "sample_seed": self.config["review"]["sample_seed"],
            "stages": self._new_stages(),
            "reconciliation": {
                "source_groups": 0,
                "submission_manifests": 0,
                "queue_items": 0,
                "calibration_selected": 0,
                "reviews": 0,
                "unresolved_errors": 0,
            },
            "event_log": {
                "artifact": event_ref,
                "entry_count": 0,
                "last_sequence": 0,
            },
            "human_decision_log": {
                "artifact": decision_ref,
                "entry_count": 0,
                "last_sequence": 0,
            },
            "outputs": [],
            "validation": {"status": "NOT_RUN", "report": None},
            "privacy": {
                "run_directory_mode": "0700",
                "private_file_mode": "0600",
                "contains_source_identifiers": False,
                "student_facing_release": False,
            },
        }

    def _refresh_logs(
        self,
        manifest: dict[str, Any],
        events: EventLog,
        event_path: Path,
        decision_path: Path,
    ) -> None:
        event_id = manifest["event_log"]["artifact"]["artifact_id"]
        decision_id = manifest["human_decision_log"]["artifact"]["artifact_id"]
        manifest["event_log"] = {
            "artifact": artifact_ref(
                self.repository_root,
                event_path,
                artifact_id=event_id,
                role="EVENT_LOG",
                media_type="application/x-ndjson",
            ),
            "entry_count": events.sequence,
            "last_sequence": events.sequence,
        }
        decision_count = len(safe_file_bytes(decision_path).splitlines())
        manifest["human_decision_log"] = {
            "artifact": artifact_ref(
                self.repository_root,
                decision_path,
                artifact_id=decision_id,
                role="HUMAN_DECISION_LOG",
                media_type="application/x-ndjson",
            ),
            "entry_count": decision_count,
            "last_sequence": decision_count,
        }

    def _write_manifest(self, run_root: Path, manifest: dict[str, Any]) -> None:
        errors = sorted(
            self.validators["run_manifest"].iter_errors(manifest),
            key=lambda item: list(item.path),
        )
        if errors:
            joined = "; ".join(error.message for error in errors[:10])
            raise ContractError(f"run manifest invalid: {joined}")
        write_private_json(run_root / "run_manifest.json", manifest)

    def _freeze_references(
        self,
        run_root: Path,
        allocator: IdAllocator,
        created_at: str,
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        codebook_source = self.discover_codebook()
        snapshot_path = run_root / "references/ne630-homework-review.SKILL.md"
        write_private_bytes(snapshot_path, safe_file_bytes(codebook_source))
        configured_assignments = {
            item["id"]: item for item in self.config["assignment"]["assignments"]
        }
        reference_specs: list[tuple[str, str, Path, str | None, str | None]] = [
            (
                "REF-POLICY",
                "POLICY",
                self.repository_root / self.config["submission_rules"]["policy_source"]["value"],
                None,
                None,
            ),
            ("REF-CONFIGURATION", "CONFIGURATION", self.config_path, None, None),
            (
                "REF-REVIEW-PROTOCOL",
                "REVIEW_PROTOCOL",
                self.framework_root / "calibration/product_review_protocol.md",
                None,
                None,
            ),
            (
                "REF-CODEBOOK",
                "CODEBOOK",
                snapshot_path,
                None,
                "Private run snapshot of the approved NE 630 review skill.",
            ),
            (
                "REF-TEMPLATE-DOSSIER",
                "TEMPLATE",
                self.templates_root / "dossier.md.tmpl",
                None,
                None,
            ),
            (
                "REF-TEMPLATE-QUEUE",
                "TEMPLATE",
                self.templates_root / "review_queue.md.tmpl",
                None,
                None,
            ),
        ]
        for assignment_id in ASSIGNMENTS:
            assignment = configured_assignments[assignment_id]
            reference_specs.extend(
                (
                    (
                        f"REF-{assignment_id}-STATEMENT",
                        "PROBLEM_STATEMENT",
                        self.repository_root / assignment["statement"],
                        assignment_id,
                        None,
                    ),
                    (
                        f"REF-{assignment_id}-KEY",
                        "SOLUTION_KEY",
                        self.repository_root / assignment["solution_key"],
                        assignment_id,
                        None,
                    ),
                )
            )
        for index, schema_path in enumerate(
            sorted(self.schema_root.glob("*.schema.json")), 1
        ):
            reference_specs.append(
                (f"REF-SCHEMA-{index:03d}", "SCHEMA", schema_path, None, None)
            )
        references: list[dict[str, Any]] = []
        for reference_id, role, path, assignment_id, note in reference_specs:
            if not path.is_file() or path.is_symlink():
                raise PipelineError(f"reference is missing or unsafe: {path}")
            data = safe_file_bytes(path)
            state, blob_id = self._git_state(path)
            item: dict[str, Any] = {
                "reference_id": reference_id,
                "role": role,
                "path": repository_relative(self.repository_root, path),
                "sha256": sha256_bytes(data),
                "byte_count": len(data),
                "media_type": media_type_for_path(path),
                "working_tree_state": state,
                "frozen_at": created_at,
            }
            if assignment_id:
                item["assignment_id"] = assignment_id
            if blob_id:
                item["git_blob_id"] = blob_id
            if note:
                item["note"] = note
            references.append(item)
        manifest = {
            "schema_version": SCHEMA_VERSION,
            "manifest_id": "REFMAN-000001",
            "configuration_id": self.configuration_id,
            "created_at": created_at,
            "repository_commit": self.repository_commit(),
            "references": references,
        }
        self.validators["reference_manifest"].validate(manifest)
        path = run_root / "manifests/reference_manifest.json"
        write_private_json(path, manifest)
        reference = artifact_ref(
            self.repository_root,
            path,
            artifact_id=allocator.next("ART"),
            role="REFERENCE_MANIFEST",
            media_type="application/json",
        )
        return manifest, reference

    def _prior_identity_state(
        self,
    ) -> tuple[dict[str, str], dict[str, dict[str, int]], int]:
        pseudonyms: dict[str, str] = {}
        identities_by_pseudonym: dict[str, str] = {}
        attempts: dict[str, dict[str, int]] = defaultdict(dict)
        payloads_by_attempt: dict[str, dict[int, str]] = defaultdict(dict)
        maximum_pseudonym = 0
        if not self.restricted_root.exists():
            return pseudonyms, attempts, maximum_pseudonym
        for path in sorted(self.restricted_root.glob("run-*/identity_map.json")):
            if path.is_symlink() or not path.is_file():
                continue
            try:
                run_id = path.parent.name
                if not re.fullmatch(
                    r"run-[0-9]{8}T[0-9]{6}Z-[0-9a-f]{12}", run_id
                ):
                    raise ContractError("prior identity map has an invalid run directory")
                identity_bytes = safe_file_bytes(path)
                document = json.loads(identity_bytes)
                if identity_bytes != canonical_json_bytes(document):
                    raise ContractError("prior identity map is not canonical JSON")
                self.validators["identity_map"].validate(document)
                if (
                    document["run_id"] != run_id
                    or document["configuration_id"] != self.configuration_id
                ):
                    raise ContractError("prior identity map is not run/configuration-bound")

                manifest_path = self.runs_root / run_id / "run_manifest.json"
                if manifest_path.is_symlink() or not manifest_path.is_file():
                    raise ContractError("prior identity map has no corresponding run manifest")
                manifest_bytes = safe_file_bytes(manifest_path)
                prior_manifest = json.loads(manifest_bytes)
                if manifest_bytes != canonical_json_bytes(prior_manifest):
                    raise ContractError("prior run manifest is not canonical JSON")
                self.validators["run_manifest"].validate(prior_manifest)
                if prior_manifest["run_id"] != run_id:
                    raise ContractError("prior run manifest is not directory-bound")
                prior_intake_complete = (
                    self._stage(prior_manifest, "INTAKE")["status"] == "COMPLETE"
                )
                identity_repository_path = repository_relative(
                    self.repository_root, path
                )
                sealed_references = [
                    reference
                    for reference in prior_manifest["outputs"]
                    if reference["role"] == "RESTRICTED_IDENTITY_MAP"
                    and reference["path"] == identity_repository_path
                ]
                if not sealed_references and not prior_intake_complete:
                    # A hard stop can occur after the private map replacement
                    # but before its reference reaches the run manifest.  Such
                    # an incomplete map is not durable identity state and must
                    # not poison every later fresh intake.
                    continue
                if len(sealed_references) != 1:
                    raise ContractError("prior identity map is not sealed as a run output")
                sealed = sealed_references[0]
                if (
                    sealed["sha256"] != sha256_bytes(identity_bytes)
                    or sealed["byte_count"] != len(identity_bytes)
                ):
                    raise ContractError("prior identity map differs from its run seal")
            except (OSError, ValueError, jsonschema.ValidationError, PipelineError) as exc:
                raise ContractError(f"unusable prior identity state: {path.parent.name}") from exc
            for entry in document["entries"]:
                pseudonym = entry["pseudonym"]
                maximum_pseudonym = max(maximum_pseudonym, int(pseudonym[1:]))
                for subject in entry["subjects"]:
                    identity_key = subject["source_identity_key"]
                    prior_pseudonym = pseudonyms.setdefault(identity_key, pseudonym)
                    prior_identity = identities_by_pseudonym.setdefault(
                        pseudonym, identity_key
                    )
                    if prior_pseudonym != pseudonym or prior_identity != identity_key:
                        raise ContractError(
                            "prior identity maps violate the pseudonym bijection"
                        )
                if not prior_intake_complete:
                    # A failed intake may reserve a stable pseudonym, but it
                    # must not create version/attempt history for uncommitted
                    # source payloads.
                    continue
                normalized_files = []
                for index, source in enumerate(
                    sorted(entry["original_files"], key=lambda item: item["source_path"]), 1
                ):
                    suffix = Path(source["source_path"]).suffix.lower()
                    logical = f"input-{index:04d}{suffix}"
                    normalized_files.append(
                        {
                            "logical_path": logical,
                            "byte_count": source["byte_count"],
                            "sha256": source["sha256"],
                        }
                    )
                prior_digest = sha256_bytes(canonical_json_bytes(normalized_files))
                group_key = entry["source_group_key"]
                attempt_number = entry["attempt_number"]
                prior_attempt = attempts[group_key].setdefault(
                    prior_digest, attempt_number
                )
                prior_payload = payloads_by_attempt[group_key].setdefault(
                    attempt_number, prior_digest
                )
                if prior_attempt != attempt_number or prior_payload != prior_digest:
                    raise ContractError(
                        "prior identity maps contain conflicting attempt history"
                    )
        return pseudonyms, attempts, maximum_pseudonym

    def _discover_groups(
        self, allocator: IdAllocator
    ) -> tuple[list[SubmissionGroup], list[dict[str, Any]], list[dict[str, Any]]]:
        raw_groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
        assignment_counts: dict[str, int] = defaultdict(int)
        maximum_source_bytes = int(
            self.config["processing"]["archive_limits"]["max_total_expanded_bytes"]
        )
        for assignment_id in ASSIGNMENTS:
            directory = self.submission_root / assignment_id.lower()
            if not directory.is_dir() or directory.is_symlink():
                raise PipelineError(f"submission directory missing or unsafe: {directory}")
            for path in sorted(directory.iterdir(), key=lambda item: item.name):
                metadata = path.lstat()
                if not stat.S_ISREG(metadata.st_mode) or path.is_symlink():
                    raise UnsafeInputError(
                        f"non-regular top-level input blocks intake in {assignment_id}"
                    )
                try:
                    encoded_name = path.name.encode("utf-8", errors="strict")
                except UnicodeEncodeError as exc:
                    raise UnsafeInputError(
                        f"non-UTF-8 top-level filename blocks intake in {assignment_id}"
                    ) from exc
                if unicodedata.normalize("NFC", path.name) != path.name:
                    raise UnsafeInputError(
                        f"non-NFC top-level filename blocks intake in {assignment_id}"
                    )
                digest, byte_count, prefix = inspect_regular_file(
                    path, maximum_source_bytes
                )
                parsed = parse_export_name(path.name)
                if parsed:
                    identity_key = f"canvas-user:{parsed.user_id}"
                    grouping_key = parsed.user_id
                else:
                    fallback = sha256_bytes(encoded_name)[:16]
                    identity_key = f"unparsed-export:{fallback}"
                    grouping_key = identity_key
                raw_groups[(assignment_id, grouping_key)].append(
                    {
                        "path": path,
                        "parsed": parsed,
                        "prefix": prefix,
                        "byte_count": byte_count,
                        "sha256": digest,
                        "identity_key": identity_key,
                    }
                )
                assignment_counts[assignment_id] += 1
        prior_pseudonyms, prior_attempts, maximum_pseudonym = self._prior_identity_state()
        identity_keys = sorted(
            {entry[0]["identity_key"] for entry in raw_groups.values()}
        )
        for identity_key in identity_keys:
            if identity_key not in prior_pseudonyms:
                maximum_pseudonym += 1
                prior_pseudonyms[identity_key] = f"S{maximum_pseudonym:03d}"
        groups: list[SubmissionGroup] = []
        identity_entries: list[dict[str, Any]] = []
        input_summaries: list[dict[str, Any]] = []
        for assignment_id in ASSIGNMENTS:
            assignment_groups = [
                (key, value)
                for key, value in raw_groups.items()
                if key[0] == assignment_id
            ]
            assignment_payloads: list[dict[str, Any]] = []
            for (_, grouping_key), records in sorted(
                assignment_groups, key=lambda item: item[0][1]
            ):
                ordered = sorted(records, key=lambda item: item["path"].name)
                source_files: list[SourceFile] = []
                for index, record in enumerate(ordered, 1):
                    parsed: ExportName | None = record["parsed"]
                    source_suffix = Path(
                        parsed.original_name if parsed else record["path"].name
                    ).suffix.lower()
                    if not re.fullmatch(r"\.[a-z0-9]{1,10}", source_suffix):
                        source_suffix = ""
                    logical_path = f"input-{index:04d}{source_suffix}"
                    media_type, detected_type, extension_match = detect_media_type(
                        record["prefix"], source_suffix
                    )
                    source_files.append(
                        SourceFile(
                            path=record["path"],
                            repository_path=repository_relative(
                                self.repository_root, record["path"]
                            ),
                            export_name=parsed,
                            sha256=record["sha256"],
                            byte_count=record["byte_count"],
                            logical_path=logical_path,
                            artifact_id=allocator.next("ART"),
                            media_type=media_type,
                            detected_type=detected_type,
                            extension_match=extension_match,
                        )
                    )
                identity_key = ordered[0]["identity_key"]
                parsed_records = [item["parsed"] for item in ordered if item["parsed"]]
                display_name = parsed_records[0].login if parsed_records else None
                lms_user_id = parsed_records[0].user_id if parsed_records else None
                group_key = f"{assignment_id}|{identity_key}"
                source_submission_id = f"SYNTHESIZED-GROUP:{group_key}"
                digest = payload_digest(source_files)
                known_attempts = prior_attempts[group_key]
                if digest in known_attempts:
                    attempt_number = known_attempts[digest]
                else:
                    attempt_number = max(known_attempts.values(), default=0) + 1
                    known_attempts[digest] = attempt_number
                pseudonym = prior_pseudonyms[identity_key]
                record_id = f"{assignment_id}-{pseudonym}-V{attempt_number:02d}"
                group = SubmissionGroup(
                    assignment_id=assignment_id,
                    source_identity_key=identity_key,
                    display_name=display_name,
                    lms_user_id=lms_user_id,
                    source_group_key=group_key,
                    source_submission_id=source_submission_id,
                    files=tuple(source_files),
                    source_payload_sha256=digest,
                    pseudonym=pseudonym,
                    attempt_number=attempt_number,
                    submission_record_id=record_id,
                )
                groups.append(group)
                subjects: dict[str, Any] = {"source_identity_key": identity_key}
                if display_name:
                    subjects["display_name"] = display_name
                if lms_user_id:
                    subjects["lms_user_id"] = lms_user_id
                original_files = []
                for source in source_files:
                    original: dict[str, Any] = {
                        "source_path": source.repository_path,
                        "sha256": source.sha256,
                        "byte_count": source.byte_count,
                    }
                    if source.export_name:
                        original["lms_file_id"] = source.export_name.file_id
                    original_files.append(original)
                identity_entries.append(
                    {
                        "assignment_id": assignment_id,
                        "submission_record_id": record_id,
                        "pseudonym": pseudonym,
                        "attempt_number": attempt_number,
                        "source_submission_id": source_submission_id,
                        "source_group_key": group_key,
                        "subjects": [subjects],
                        "original_files": original_files,
                    }
                )
                assignment_payloads.append(
                    {
                        "submission_record_id": record_id,
                        "source_payload_sha256": digest,
                    }
                )
            input_summaries.append(
                {
                    "assignment_id": assignment_id,
                    "source_directory": repository_relative(
                        self.repository_root, self.submission_root / assignment_id.lower()
                    ),
                    "source_group_count": len(assignment_groups),
                    "top_level_file_count": assignment_counts[assignment_id],
                    "snapshot_sha256": sha256_bytes(
                        canonical_json_bytes(sorted(assignment_payloads, key=lambda item: item["submission_record_id"]))
                    ),
                }
            )
        return groups, identity_entries, input_summaries

    @staticmethod
    def _file_locator(
        source: SourceFile,
        *,
        source_role: str,
        extraction_method: str,
        archive_member: str | None = None,
    ) -> dict[str, Any]:
        locator: dict[str, Any] = {
            "artifact_id": source.artifact_id,
            "artifact_sha256": source.sha256,
            "source_role": source_role,
            "logical_path": source.logical_path,
            "locator_type": "ARCHIVE_MEMBER" if archive_member else "FILE",
            "extraction_method": extraction_method,
            "uncertainty": "NONE",
        }
        if archive_member:
            locator["archive_member"] = archive_member
        return locator

    def _inspect_group(
        self,
        group: SubmissionGroup,
        *,
        allocator: IdAllocator,
        private_tmp: Path,
        created_at: str,
        reference_manifest_sha256: str,
    ) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
        limits = self.config["processing"]["archive_limits"]
        files = list(group.files)
        archive_inspections: list[dict[str, Any]] = []
        pdf_inspections: list[dict[str, Any]] = []
        archive_result: ArchiveResult | None = None
        if len(files) == 1 and files[0].media_type == "application/pdf":
            package_shape = "SINGLE_PDF"
            pdf_record, _ = inspect_pdf_bytes(
                source_file_bytes(files[0], int(limits["max_total_expanded_bytes"])),
                artifact_id=files[0].artifact_id,
                private_tmp=private_tmp,
                maximum_bytes=int(limits["max_pdf_bytes_for_text_check"]),
                timeout_seconds=int(limits["tool_timeout_seconds"]),
            )
            pdf_inspections.append(pdf_record)
        elif len(files) == 1 and files[0].media_type == "application/zip":
            package_shape = "ZIP"
            archive_result = inspect_zip_bytes(
                source_file_bytes(files[0], int(limits["max_total_expanded_bytes"])),
                artifact_id=files[0].artifact_id,
                limits=limits,
            )
            archive_inspections.append(archive_result.record)
            if archive_result.solution_pdf is not None:
                pdf_record, _ = inspect_pdf_bytes(
                    archive_result.solution_pdf,
                    artifact_id=files[0].artifact_id,
                    private_tmp=private_tmp,
                    maximum_bytes=int(limits["max_pdf_bytes_for_text_check"]),
                    timeout_seconds=int(limits["tool_timeout_seconds"]),
                )
                pdf_inspections.append(pdf_record)
        elif len(files) > 1:
            package_shape = "MULTI_FILE"
            for source in files:
                if source.media_type == "application/pdf":
                    pdf_record, _ = inspect_pdf_bytes(
                        source_file_bytes(
                            source, int(limits["max_total_expanded_bytes"])
                        ),
                        artifact_id=source.artifact_id,
                        private_tmp=private_tmp,
                        maximum_bytes=int(limits["max_pdf_bytes_for_text_check"]),
                        timeout_seconds=int(limits["tool_timeout_seconds"]),
                    )
                    pdf_inspections.append(pdf_record)
                elif source.media_type == "application/zip":
                    nested_result = inspect_zip_bytes(
                        source_file_bytes(
                            source, int(limits["max_total_expanded_bytes"])
                        ),
                        artifact_id=source.artifact_id,
                        limits=limits,
                    )
                    archive_inspections.append(nested_result.record)
        else:
            package_shape = "OTHER"

        core_file_checks: list[dict[str, Any]] = []
        if package_shape == "SINGLE_PDF":
            for logical_name in CORE_ROUTE_B_FILES:
                core_file_checks.append(
                    {
                        "logical_name": logical_name,
                        "status": "NOT_APPLICABLE",
                        "matches": [],
                    }
                )
        else:
            for logical_name in CORE_ROUTE_B_FILES:
                matches: list[Any] = []
                if package_shape == "ZIP" and archive_result is not None:
                    for member_index, member_name in enumerate(
                        archive_result.member_names, 1
                    ):
                        parts = PurePosixPath(member_name).parts
                        if len(parts) <= 2 and parts[-1] == logical_name:
                            matches.append(
                                {
                                    "container_artifact_id": files[0].artifact_id,
                                    "archive_member": (
                                        f"member-{member_index:04d}/{logical_name}"
                                    ),
                                }
                            )
                elif package_shape == "MULTI_FILE":
                    for source in files:
                        original_name = (
                            source.export_name.original_name
                            if source.export_name
                            else source.path.name
                        )
                        if PurePosixPath(original_name).name == logical_name:
                            matches.append(source.artifact_id)
                status = (
                    "MISSING"
                    if not matches
                    else "PRESENT_UNIQUE"
                    if len(matches) == 1
                    else "DUPLICATE"
                )
                core_file_checks.append(
                    {
                        "logical_name": logical_name,
                        "status": status,
                        "matches": matches,
                    }
                )

        readable_pdf = any(item["status"] == "READABLE" for item in pdf_inspections)
        unique_solution = next(
            item
            for item in core_file_checks
            if item["logical_name"] == "solution.pdf"
        )["status"] == "PRESENT_UNIQUE"
        archive_safe = bool(
            archive_inspections
            and all(item["status"] == "SAFE" for item in archive_inspections)
        )
        identity_parse_complete = all(source.export_name is not None for source in files)
        if not identity_parse_complete:
            calibration_stratum = "INELIGIBLE"
            status_axes = {
                "intake": "NEEDS_HUMAN_TRIAGE",
                "build": (
                    "NOT_RUN_NO_SANDBOX"
                    if package_shape in {"ZIP", "MULTI_FILE"}
                    else "NOT_RUN_POLICY"
                ),
                "coverage": "NOT_CHECKED",
                "processing": "PENDING",
                "human_review": "PENDING",
            }
            action = "HUMAN_TRIAGE"
            reason_code = "AMBIGUOUS_OR_UNPARSED_EXPORT_NAME"
            reason_message = (
                "Canvas identity fields could not be parsed unambiguously from the export name."
            )
            severity = "WARNING"
        elif package_shape == "SINGLE_PDF" and readable_pdf:
            calibration_stratum = "READABLE_SINGLE_PDF"
            status_axes = {
                "intake": "READY",
                "build": "NOT_APPLICABLE",
                "coverage": "NOT_CHECKED",
                "processing": "READY",
                "human_review": "PENDING",
            }
            action = "AWAIT_CALIBRATION_SELECTION"
            reason_code = "ELIGIBLE_READABLE_SINGLE_PDF"
            reason_message = "Eligible for the pre-review PDF calibration stratum."
            severity = "INFO"
        elif (
            package_shape == "ZIP"
            and archive_safe
            and unique_solution
            and readable_pdf
        ):
            calibration_stratum = "SAFE_ZIP_UNIQUE_SOLUTION_PDF"
            status_axes = {
                "intake": "READY",
                "build": "NOT_RUN_NO_SANDBOX",
                "coverage": "NOT_CHECKED",
                "processing": "READY",
                "human_review": "PENDING",
            }
            action = "AWAIT_CALIBRATION_SELECTION"
            reason_code = "ELIGIBLE_SAFE_ZIP"
            reason_message = "Eligible for the pre-review safe-ZIP calibration stratum."
            severity = "INFO"
        else:
            calibration_stratum = "INELIGIBLE"
            unsafe_archive = any(
                item["status"] in {"UNSAFE", "RESOURCE_LIMIT", "ERROR"}
                for item in archive_inspections
            )
            if unsafe_archive:
                status_axes = {
                    "intake": "BLOCKED",
                    "build": "NOT_RUN_NO_SANDBOX",
                    "coverage": "NOT_CHECKED",
                    "processing": "BLOCKED",
                    "human_review": "PENDING",
                }
                action = "HOLD"
                reason_code = "ARCHIVE_PROCESSING_BLOCKED"
                reason_message = "Archive safety or resource checks blocked processing."
                severity = "BLOCKING_PROCESSING"
            else:
                build_status = (
                    "NOT_RUN_NO_SANDBOX"
                    if package_shape in {"ZIP", "MULTI_FILE"}
                    else "NOT_RUN_POLICY"
                )
                status_axes = {
                    "intake": "NEEDS_HUMAN_TRIAGE",
                    "build": build_status,
                    "coverage": "NOT_CHECKED",
                    "processing": "PENDING",
                    "human_review": "PENDING",
                }
                action = "HUMAN_TRIAGE"
                reason_code = "NOT_CALIBRATION_ELIGIBLE"
                reason_message = "Package does not meet either calibration stratum."
                severity = "WARNING"

        findings: list[dict[str, Any]] = []
        finding_ids: list[str] = []
        if calibration_stratum == "INELIGIBLE":
            finding_id = allocator.next("FND")
            finding_ids.append(finding_id)
            source = files[0]
            findings.append(
                {
                    "finding_id": finding_id,
                    "finding_type": reason_code,
                    "severity": severity,
                    "observation": reason_message,
                    "evidence_locators": [
                        self._file_locator(
                            source,
                            source_role="SUBMITTED_SUPPORTING_FILE",
                            extraction_method=(
                                "ARCHIVE_METADATA"
                                if source.media_type == "application/zip"
                                else "VISUAL"
                            ),
                        )
                    ],
                    "uncertainty": "NONE",
                    "proposed_action": (
                        "HOLD_PROCESSING"
                        if action == "HOLD"
                        else "HUMAN_TRIAGE"
                    ),
                    "origin": "DETERMINISTIC",
                    "academic_effect": "NONE",
                }
            )

        input_files = [
            {
                "artifact_id": source.artifact_id,
                "logical_path": source.logical_path,
                "sha256": source.sha256,
                "byte_count": source.byte_count,
                "media_type": source.media_type,
                "detected_type": source.detected_type,
                "extension_match": source.extension_match,
            }
            for source in files
        ]
        submission_manifest = {
            "schema_version": SCHEMA_VERSION,
            "manifest_id": allocator.next("SUBMAN"),
            "run_id": "",  # filled by intake
            "configuration_id": self.configuration_id,
            "config_sha256": self.config_sha256,
            "reference_manifest_sha256": reference_manifest_sha256,
            "created_at": created_at,
            "assignment_id": group.assignment_id,
            "submission_record_id": group.submission_record_id,
            "pseudonym": group.pseudonym,
            "attempt_number": group.attempt_number,
            "source_payload_sha256": group.source_payload_sha256,
            "route_declaration": {
                "state": "UNAVAILABLE",
                "route": None,
                "source": "NONE",
            },
            "observed_package_shape": package_shape,
            "calibration_stratum": calibration_stratum,
            "input_files": input_files,
            "archive_inspections": archive_inspections,
            "pdf_inspections": pdf_inspections,
            "core_file_checks": core_file_checks,
            "marker_candidates": [
                {
                    "marker_type": "OPENING_NOTICE",
                    "status": "NOT_CHECKED",
                    "evidence_locators": [],
                },
                {
                    "marker_type": "END_OF_GRADED_DISCOURSE",
                    "status": "NOT_CHECKED",
                    "evidence_locators": [],
                },
            ],
            "status_axes": status_axes,
            "deterministic_findings": findings,
            "coverage": {
                "status": "NOT_CHECKED",
                "expected_problem_count": next(
                    item["expected_problem_count"]
                    for item in self.config["assignment"]["assignments"]
                    if item["id"] == group.assignment_id
                ),
                "detected_problem_ids": [],
                "evidence_locators": [],
            },
            "contains_source_identifiers": False,
        }
        build_status = status_axes["build"]
        report_status = (
            build_status
            if build_status
            in {"NOT_RUN_NO_SANDBOX", "NOT_RUN_POLICY", "NOT_APPLICABLE"}
            else "NOT_CHECKABLE"
        )
        build_report = {
            "schema_version": SCHEMA_VERSION,
            "report_id": allocator.next("BLD"),
            "run_id": "",  # filled by intake
            "configuration_id": self.configuration_id,
            "created_at": created_at,
            "assignment_id": group.assignment_id,
            "submission_record_id": group.submission_record_id,
            "pseudonym": group.pseudonym,
            "execution_performed": False,
            "status": report_status,
            "reason_code": (
                "SANDBOX_NOT_APPROVED"
                if report_status == "NOT_RUN_NO_SANDBOX"
                else "BUILD_NOT_APPLICABLE"
                if report_status == "NOT_APPLICABLE"
                else "BUILD_NOT_AUTHORIZED"
            ),
            "sandbox": None,
            "environment": {
                "platform": platform.platform(),
                "tools": [],
            },
            "commands": [],
            "bounded_logs": [],
            "resource_usage": None,
            "outputs": [],
            "contains_source_identifiers": False,
        }
        queue_item = {
            "position": 0,
            "assignment_id": group.assignment_id,
            "submission_record_id": group.submission_record_id,
            "pseudonym": group.pseudonym,
            "observed_package_shape": package_shape,
            "calibration_stratum": calibration_stratum,
            "status_axes": status_axes,
            "action": action,
            "reasons": [
                {
                    "code": reason_code,
                    "severity": severity,
                    "message": reason_message,
                    "finding_ids": finding_ids,
                }
            ],
            "calibration_state": (
                "PENDING_SELECTION"
                if calibration_stratum != "INELIGIBLE"
                else "INELIGIBLE"
            ),
            "random_audit_state": "NOT_CONFIGURED",
            "dossier_data": None,
            "reviewer_state": "PENDING",
            "decision_ids": [],
        }
        return submission_manifest, build_report, queue_item

    @staticmethod
    def _add_output(manifest: dict[str, Any], reference: dict[str, Any]) -> None:
        for existing in manifest["outputs"]:
            if existing["artifact_id"] == reference["artifact_id"]:
                raise ContractError("duplicate artifact identifier in run outputs")
            if existing["path"] == reference["path"]:
                raise ContractError("duplicate artifact path in run outputs")
        manifest["outputs"].append(reference)

    def _arm_stage_failure_guard(
        self,
        *,
        manifest: dict[str, Any],
        events: EventLog,
        run_root: Path,
        event_path: Path,
        decision_path: Path,
        stage: str,
        code: str,
        message: str,
        start_inputs: Sequence[dict[str, Any]] = (),
        resume: bool = False,
        preserve_terminal: bool = False,
    ) -> None:
        self._active_stage_failure = {
            "manifest": manifest,
            "events": events,
            "run_root": run_root,
            "event_path": event_path,
            "decision_path": decision_path,
            "stage": stage,
            "code": code,
            "message": message,
            "event_sequence_before": events.sequence,
            "start_inputs": [dict(item) for item in start_inputs],
            "resume": resume,
            "preserve_terminal": preserve_terminal,
        }

    def _clear_stage_failure_guard(self) -> None:
        self._active_stage_failure = None

    def _seal_active_stage_failure(self) -> None:
        context = getattr(self, "_active_stage_failure", None)
        if not context:
            return
        manifest = context["manifest"]
        stage = context["stage"]
        # A durable append can raise before EventLog updates its in-memory
        # sequence (for example, an acknowledged fsync followed by an I/O
        # error). Re-read and validate the complete ledger, synchronize the
        # writer cursor, and mirror the latest lifecycle event before deciding
        # whether a failure event is still needed.
        try:
            raw_lines = safe_file_bytes(context["event_path"]).splitlines()
            recovered_log = EventLog(
                context["event_path"],
                run_id=manifest["run_id"],
                validator=self.validators["event"],
                now=self.now,
            )
            recovered_events = [json.loads(line) for line in raw_lines]
        except (OSError, ValueError, PipelineError, jsonschema.ValidationError):
            return
        context["events"].sequence = recovered_log.sequence
        context["events"].last_timestamp = recovered_log.last_timestamp
        new_events = [
            event
            for event in recovered_events
            if event["sequence"] > context["event_sequence_before"]
        ]
        lifecycle = [
            event
            for event in new_events
            if event["stage"] == stage
            and event["event_type"]
            in {"STAGE_STARTED", "RESUMED", "STAGE_COMPLETED"}
        ]
        if not lifecycle and recovered_log.sequence == context["event_sequence_before"]:
            if context["preserve_terminal"]:
                pass
            elif context["resume"]:
                self._resume_stage(
                    manifest,
                    context["events"],
                    stage,
                    inputs=context["start_inputs"],
                    message="Resumed stage failed before its work completed.",
                )
            else:
                self._start_stage(
                    manifest,
                    context["events"],
                    stage,
                    inputs=context["start_inputs"],
                )
        elif lifecycle:
            last_lifecycle = lifecycle[-1]
            state = self._stage(manifest, stage)
            if last_lifecycle["event_type"] in {"STAGE_STARTED", "RESUMED"}:
                state.update(
                    {
                        "status": "RUNNING",
                        "event_sequence_start": last_lifecycle["sequence"],
                        "event_sequence_end": None,
                        "started_at": last_lifecycle["occurred_at"],
                        "completed_at": None,
                        "reason_code": None,
                    }
                )
                manifest["run_state"] = "RUNNING"
            else:
                terminal_status = last_lifecycle["payload"]["stage_status"]
                if terminal_status == "SKIPPED":
                    start_event = last_lifecycle
                else:
                    start_event = next(
                        (
                            event
                            for event in reversed(lifecycle[:-1])
                            if event["event_type"] in {"STAGE_STARTED", "RESUMED"}
                        ),
                        None,
                    )
                    if start_event is None:
                        return
                state.update(
                    {
                        "status": terminal_status,
                        "event_sequence_start": start_event["sequence"],
                        "event_sequence_end": last_lifecycle["sequence"],
                        "started_at": (
                            None
                            if terminal_status == "SKIPPED"
                            else start_event["occurred_at"]
                        ),
                        "completed_at": last_lifecycle["occurred_at"],
                        "reason_code": (
                            last_lifecycle["reason_code"]
                            if terminal_status in {"SKIPPED", "BLOCKED", "FAILED"}
                            else None
                        ),
                    }
                )
                manifest["run_state"] = (
                    terminal_status
                    if terminal_status in {"BLOCKED", "FAILED"}
                    else "RUNNING"
                )
            manifest["updated_at"] = last_lifecycle["occurred_at"]

        stage_status = self._stage(manifest, stage)["status"]
        if stage_status == "RUNNING":
            self._fail_stage(
                manifest,
                context["events"],
                stage,
                context["code"],
                context["message"],
            )
        elif stage_status not in {"COMPLETE", "BLOCKED", "FAILED", "SKIPPED"}:
            return
        # A terminal event may already have been appended when the atomic
        # manifest replacement failed. Retry that exact in-memory seal;
        # appending a second completion event would corrupt the stage ledger.
        self._refresh_logs(
            manifest,
            context["events"],
            context["event_path"],
            context["decision_path"],
        )
        self._write_manifest(context["run_root"], manifest)

    def _queue_document(
        self,
        *,
        run_id: str,
        created_at: str,
        reference_manifest_sha256: str,
        items: list[dict[str, Any]],
        allocator: IdAllocator,
    ) -> dict[str, Any]:
        action_priority = {
            "AWAIT_CALIBRATION_SELECTION": 1,
            "PRODUCT_REVIEW": 2,
            "HUMAN_TRIAGE": 3,
            "HOLD": 4,
            "EXCLUDE": 5,
            "DEFERRED_NOT_SELECTED": 6,
        }
        items.sort(
            key=lambda item: (
                item["assignment_id"],
                action_priority[item["action"]],
                item["submission_record_id"],
            )
        )
        for position, item in enumerate(items, 1):
            item["position"] = position
        counts = {
            "total": len(items),
            "awaiting_selection": sum(
                item["action"] == "AWAIT_CALIBRATION_SELECTION" for item in items
            ),
            "not_selected": sum(
                item["action"] == "DEFERRED_NOT_SELECTED" for item in items
            ),
            "product_review": sum(item["action"] == "PRODUCT_REVIEW" for item in items),
            "human_triage": sum(item["action"] == "HUMAN_TRIAGE" for item in items),
            "hold": sum(item["action"] == "HOLD" for item in items),
            "exclude": sum(item["action"] == "EXCLUDE" for item in items),
            "calibration_selected": sum(
                item["calibration_state"] == "SELECTED" for item in items
            ),
        }
        return {
            "schema_version": SCHEMA_VERSION,
            "queue_id": allocator.next("QUE"),
            "run_id": run_id,
            "configuration_id": self.configuration_id,
            "config_sha256": self.config_sha256,
            "reference_manifest_sha256": reference_manifest_sha256,
            "created_at": created_at,
            "ordering": {
                "method": "assignment_id, action_priority, submission_record_id",
                "ascending": True,
            },
            "counts": counts,
            "items": items,
            "contains_source_identifiers": False,
        }

    def _render_queue(
        self,
        queue: dict[str, Any],
        *,
        run_root: Path,
        allocator: IdAllocator,
        version: str,
        phase: str,
        frozen_template: tuple[bytes, Mapping[str, Any]] | None = None,
    ) -> tuple[list[dict[str, Any]], dict[str, Any]]:
        role_version = re.sub(r"[^A-Z0-9_]", "_", version.upper())
        queue_path = run_root / f"manifests/review_queue-{version}.json"
        self.validators["review_queue"].validate(queue)
        write_private_json(queue_path, queue)
        queue_ref = artifact_ref(
            self.repository_root,
            queue_path,
            artifact_id=allocator.next("ART"),
            role=f"REVIEW_QUEUE_{role_version}",
            media_type="application/json",
        )
        rows = []
        for item in queue["items"]:
            cells = (
                str(item["position"]),
                item["assignment_id"],
                item["submission_record_id"],
                item["observed_package_shape"],
                item["calibration_state"],
                item["action"],
                item["reviewer_state"],
            )
            rows.append("| " + " | ".join(value.replace("|", "\\|") for value in cells) + " |")
        count_lines = [
            f"- `{key}`: {value}" for key, value in sorted(queue["counts"].items())
        ]
        template_path = self.templates_root / "review_queue.md.tmpl"
        if frozen_template is None:
            template_bytes = safe_file_bytes(template_path)
            template_reference = None
        else:
            template_bytes, template_reference = frozen_template
        template = template_bytes.decode("utf-8")
        markdown = template.format(
            run_id=queue["run_id"],
            created_at=queue["created_at"],
            phase=phase,
            rows="\n".join(rows),
            counts="\n".join(count_lines),
        ).encode("utf-8")
        markdown_path = run_root / f"reports/review_queue-{version}.md"
        write_private_bytes(markdown_path, markdown)
        markdown_ref = artifact_ref(
            self.repository_root,
            markdown_path,
            artifact_id=allocator.next("ART"),
            role=f"REVIEW_QUEUE_MARKDOWN_{role_version}",
            media_type="text/markdown",
        )
        template_ref = {
            "artifact_id": allocator.next("ART"),
            "role": "REVIEW_QUEUE_TEMPLATE",
            "path": repository_relative(self.repository_root, template_path),
            "sha256": sha256_bytes(template_bytes),
            "byte_count": len(template_bytes),
            "media_type": "text/plain",
        }
        if template_reference is not None and any(
            (
                template_reference["sha256"] != template_ref["sha256"],
                template_reference["byte_count"] != template_ref["byte_count"],
            )
        ):
            raise ContractError("queue template differs from the frozen reference")
        render_manifest = {
            "schema_version": SCHEMA_VERSION,
            "render_id": allocator.next("RND"),
            "run_id": queue["run_id"],
            "created_at": queue["created_at"],
            "render_kind": "REVIEW_QUEUE_MARKDOWN",
            "source": queue_ref,
            "template": template_ref,
            "renderer": {
                "name": "ne630-review-pipeline",
                "version": VERSION,
                "sha256": self.executable_sha256,
            },
            "output": markdown_ref,
            "deterministic": True,
            "contains_source_identifiers": False,
        }
        self.validators["render_manifest"].validate(render_manifest)
        render_path = run_root / f"reports/review_queue-{version}.render.json"
        write_private_json(render_path, render_manifest)
        render_ref = artifact_ref(
            self.repository_root,
            render_path,
            artifact_id=allocator.next("ART"),
            role=f"REVIEW_QUEUE_RENDER_{role_version}",
            media_type="application/json",
        )
        return [queue_ref, markdown_ref, render_ref], queue_ref

    def intake(self, *, run_id: str | None = None) -> dict[str, Any]:
        with self._mutation_lock():
            self._clear_stage_failure_guard()
            try:
                return self._intake(run_id=run_id)
            except (Exception, KeyboardInterrupt):
                self._seal_active_stage_failure()
                raise
            finally:
                self._clear_stage_failure_guard()

    def _intake(self, *, run_id: str | None = None) -> dict[str, Any]:
        preflight = self.preflight_framework(require_tools=True)
        run_id = run_id or self.generate_run_id()
        if not re.fullmatch(r"run-[0-9]{8}T[0-9]{6}Z-[0-9a-f]{12}", run_id):
            raise PipelineError("run ID does not match the required format")
        run_root = self.runs_root / run_id
        restricted_run_root = self.restricted_root / run_id
        if run_root.exists() or restricted_run_root.exists():
            raise PipelineError(f"run already exists: {run_id}")
        allocator = IdAllocator()
        event_artifact_id = allocator.next("ART")
        decision_artifact_id = allocator.next("ART")
        private_mkdir(self.runs_root)
        private_mkdir(self.restricted_root)
        owned_bootstrap_roots: list[Path] = []
        bootstrap_committed = False
        try:
            # The two per-run roots are exclusively owned by this invocation.
            # Until the SELF_TEST skip and its manifest seal both commit, no
            # submission or identity artifact has been written, so an error can
            # be rolled back without discarding review evidence.  This also
            # leaves an explicit run ID reusable after a bootstrap I/O failure.
            private_mkdir_exclusive(run_root)
            owned_bootstrap_roots.append(run_root)
            private_mkdir_exclusive(restricted_run_root)
            owned_bootstrap_roots.append(restricted_run_root)
            for name in self.config["processing"]["run_layout"]["directories"]:
                private_mkdir(run_root / name)
            private_mkdir(run_root / "references")
            private_mkdir(run_root / "manifests/submissions")
            event_path = (
                run_root / self.config["processing"]["run_layout"]["event_log"]
            )
            decision_path = (
                run_root
                / self.config["processing"]["run_layout"]["human_decision_log"]
            )
            write_private_bytes(event_path, b"")
            write_private_bytes(decision_path, b"")
            event_ref = artifact_ref(
                self.repository_root,
                event_path,
                artifact_id=event_artifact_id,
                role="EVENT_LOG",
                media_type="application/x-ndjson",
            )
            decision_ref = artifact_ref(
                self.repository_root,
                decision_path,
                artifact_id=decision_artifact_id,
                role="HUMAN_DECISION_LOG",
                media_type="application/x-ndjson",
            )
            events = EventLog(
                event_path,
                run_id=run_id,
                validator=self.validators["event"],
                now=self.now,
            )
            created_at = self.now()
            manifest = self._initial_manifest(
                run_id,
                created_at,
                event_ref=event_ref,
                decision_ref=decision_ref,
                tool_dependencies=preflight["tool_dependencies"],
            )
            events.append(
                stage="RUN",
                event_type="RUN_CREATED",
                subject_type="RUN",
                subject_id=run_id,
                outcome="RECORDED",
                reason_code="RUN_CREATED",
                payload={"message": "Private review run created."},
            )
            self._refresh_logs(manifest, events, event_path, decision_path)
            self._write_manifest(run_root, manifest)
            self._skip_stage(
                manifest,
                events,
                "SELF_TEST",
                "SYNTHETIC_SUITE_NOT_ATTESTED_IN_RUN",
                "Framework/parser preflight passed; run the separate hermetic self-test command for synthetic-suite evidence.",
            )
            self._refresh_logs(manifest, events, event_path, decision_path)
            self._write_manifest(run_root, manifest)
            self._arm_stage_failure_guard(
                manifest=manifest,
                events=events,
                run_root=run_root,
                event_path=event_path,
                decision_path=decision_path,
                stage="REFERENCE_FREEZE",
                code="REFERENCE_FREEZE_FAILED",
                message="Reference freeze stopped safely because an approved source changed or became unavailable.",
            )
            bootstrap_committed = True
        except (Exception, KeyboardInterrupt) as bootstrap_error:
            if not bootstrap_committed:
                rollback_failed = False
                for owned_root in reversed(owned_bootstrap_roots):
                    try:
                        if owned_root.is_symlink():
                            owned_root.unlink()
                        elif owned_root.exists():
                            shutil.rmtree(owned_root)
                    except OSError:
                        rollback_failed = True
                if rollback_failed:
                    raise PipelineError(
                        "run bootstrap failed and its private rollback was incomplete"
                    ) from bootstrap_error
            raise
        self._start_stage(manifest, events, "REFERENCE_FREEZE")
        self._refresh_logs(manifest, events, event_path, decision_path)
        self._write_manifest(run_root, manifest)
        try:
            reference_manifest, reference_ref = self._freeze_references(
                run_root, allocator, self.now()
            )
        except (Exception, KeyboardInterrupt):
            self._fail_stage(
                manifest,
                events,
                "REFERENCE_FREEZE",
                "REFERENCE_FREEZE_FAILED",
                "Reference freeze stopped safely because an approved source changed or became unavailable.",
            )
            self._refresh_logs(manifest, events, event_path, decision_path)
            self._write_manifest(run_root, manifest)
            raise
        self._add_output(manifest, reference_ref)
        manifest["reference_manifest_state"] = "FROZEN"
        manifest["reference_manifest_sha256"] = reference_ref["sha256"]
        self._complete_stage(
            manifest,
            events,
            "REFERENCE_FREEZE",
            outputs=[reference_ref],
        )
        self._refresh_logs(manifest, events, event_path, decision_path)
        self._write_manifest(run_root, manifest)
        self._clear_stage_failure_guard()
        self._arm_stage_failure_guard(
            manifest=manifest,
            events=events,
            run_root=run_root,
            event_path=event_path,
            decision_path=decision_path,
            stage="INTAKE",
            code="INTAKE_FAILED",
            message="Intake stopped safely because an input changed or could not be processed.",
            start_inputs=[reference_ref],
        )
        self._start_stage(manifest, events, "INTAKE", inputs=[reference_ref])
        self._refresh_logs(manifest, events, event_path, decision_path)
        self._write_manifest(run_root, manifest)
        # Student bytes are not enumerated, named, or hashed until the exact
        # executable, schemas, policy, statements, keys, and templates have a
        # durable frozen reference manifest for this run.
        groups, identity_entries, input_summaries = self._discover_groups(allocator)
        identity_map = {
            "schema_version": SCHEMA_VERSION,
            "map_id": allocator.next("IDMAP"),
            "run_id": run_id,
            "configuration_id": self.configuration_id,
            "created_at": self.now(),
            "classification": "RESTRICTED_IDENTITY_DATA",
            "required_file_mode": "0600",
            "pseudonym_scope": "PERSON_ACROSS_PILOT",
            "entries": identity_entries,
        }
        self.validators["identity_map"].validate(identity_map)
        identity_path = restricted_run_root / "identity_map.json"
        write_private_json(identity_path, identity_map)
        identity_ref = artifact_ref(
            self.repository_root,
            identity_path,
            artifact_id=allocator.next("ART"),
            role="RESTRICTED_IDENTITY_MAP",
            media_type="application/json",
        )
        self._add_output(manifest, identity_ref)

        output_refs: list[dict[str, Any]] = [identity_ref]
        queue_items: list[dict[str, Any]] = []
        private_tmp = run_root / "tmp"
        manifest["inputs"] = input_summaries
        manifest["input_summary"] = {
            "assignment_count": 4,
            "source_group_count": len(groups),
            "top_level_file_count": sum(
                item["top_level_file_count"] for item in input_summaries
            ),
        }
        manifest["reconciliation"]["source_groups"] = len(groups)
        try:
            for group in groups:
                submission, build, queue_item = self._inspect_group(
                    group,
                    allocator=allocator,
                    private_tmp=private_tmp,
                    created_at=self.now(),
                    reference_manifest_sha256=reference_ref["sha256"],
                )
                submission["run_id"] = run_id
                build["run_id"] = run_id
                self.validators["submission_manifest"].validate(submission)
                self.validators["build_report"].validate(build)
                submission_path = (
                    run_root
                    / "manifests/submissions"
                    / f"{group.submission_record_id}.json"
                )
                build_path = run_root / "builds" / f"{group.submission_record_id}.json"
                write_private_json(submission_path, submission)
                write_private_json(build_path, build)
                submission_ref = artifact_ref(
                    self.repository_root,
                    submission_path,
                    artifact_id=allocator.next("ART"),
                    role="SUBMISSION_MANIFEST",
                    media_type="application/json",
                )
                build_ref = artifact_ref(
                    self.repository_root,
                    build_path,
                    artifact_id=allocator.next("ART"),
                    role="BUILD_REPORT",
                    media_type="application/json",
                )
                output_refs.extend((submission_ref, build_ref))
                self._add_output(manifest, submission_ref)
                self._add_output(manifest, build_ref)
                manifest["reconciliation"]["submission_manifests"] += 1
                queue_item["_submission_manifest_ref"] = submission_ref
                queue_items.append(queue_item)
        except (OSError, PipelineError, jsonschema.ValidationError) as exc:
            self._fail_stage(
                manifest,
                events,
                "INTAKE",
                "INTAKE_FAILED",
                "Intake stopped safely because an input changed or could not be processed.",
            )
            self._refresh_logs(manifest, events, event_path, decision_path)
            self._write_manifest(run_root, manifest)
            raise

        for item in queue_items:
            item.pop("_submission_manifest_ref", None)
        queue = self._queue_document(
            run_id=run_id,
            created_at=self.now(),
            reference_manifest_sha256=reference_ref["sha256"],
            items=queue_items,
            allocator=allocator,
        )
        queue_refs, _ = self._render_queue(
            queue,
            run_root=run_root,
            allocator=allocator,
            version="intake-v1",
            phase="INTAKE",
        )
        output_refs.extend(queue_refs)
        for reference in queue_refs:
            self._add_output(manifest, reference)
        manifest["reconciliation"].update(
            {
                "source_groups": len(groups),
                "submission_manifests": len(groups),
                "queue_items": len(queue_items),
            }
        )
        self._complete_stage(
            manifest,
            events,
            "INTAKE",
            outputs=output_refs,
            message="Deterministic intake completed; no student code was executed.",
        )
        self._refresh_logs(manifest, events, event_path, decision_path)
        self._write_manifest(run_root, manifest)
        return {
            "run_id": run_id,
            "source_groups": len(groups),
            "top_level_files": manifest["input_summary"]["top_level_file_count"],
            "eligible": queue["counts"]["awaiting_selection"],
            "human_triage": queue["counts"]["human_triage"],
            "hold": queue["counts"]["hold"],
            "reference_count": len(reference_manifest["references"]),
        }

    def resolve_run_id(self, run_id: str | None) -> str:
        if run_id is not None:
            if not re.fullmatch(r"run-[0-9]{8}T[0-9]{6}Z-[0-9a-f]{12}", run_id):
                raise PipelineError("run ID does not match the required format")
            candidate = self.runs_root / run_id
            if not candidate.is_dir() or candidate.is_symlink():
                raise PipelineError(f"run not found: {run_id}")
            return run_id
        if not self.runs_root.exists():
            raise PipelineError("no review runs exist; pass --run-id after intake")
        candidates = sorted(
            path.name
            for path in self.runs_root.iterdir()
            if path.is_dir()
            and not path.is_symlink()
            and re.fullmatch(r"run-[0-9]{8}T[0-9]{6}Z-[0-9a-f]{12}", path.name)
        )
        if len(candidates) != 1:
            raise PipelineError(
                "--run-id is required unless exactly one review run exists"
            )
        return candidates[0]

    def _load_run(
        self, run_id: str
    ) -> tuple[Path, dict[str, Any], EventLog, Path, Path, IdAllocator]:
        run_root = self.runs_root / run_id
        manifest_path = run_root / "run_manifest.json"
        manifest = read_json(manifest_path)
        self.validators["run_manifest"].validate(manifest)
        if manifest["run_id"] != run_id:
            raise ContractError("run manifest ID does not match its directory")
        event_path = run_root / self.config["processing"]["run_layout"]["event_log"]
        decision_path = (
            run_root
            / self.config["processing"]["run_layout"]["human_decision_log"]
        )
        for path, log_state, label in (
            (event_path, manifest["event_log"], "event"),
            (decision_path, manifest["human_decision_log"], "human-decision"),
        ):
            reference = log_state["artifact"]
            data = safe_file_bytes(path)
            line_count = len(data.splitlines())
            if any(
                (
                    reference["path"]
                    != repository_relative(self.repository_root, path),
                    reference["sha256"] != sha256_bytes(data),
                    reference["byte_count"] != len(data),
                    log_state["entry_count"] != line_count,
                    log_state["last_sequence"] != line_count,
                )
            ):
                raise ContractError(f"{label} log differs from the sealed run manifest")
        events = EventLog(
            event_path,
            run_id=run_id,
            validator=self.validators["event"],
            now=self.now,
        )
        paths = list(run_root.rglob("*"))
        restricted = self.restricted_root / run_id
        if restricted.exists():
            paths.extend(restricted.rglob("*"))
        allocator = IdAllocator.from_paths(paths)
        return run_root, manifest, events, event_path, decision_path, allocator

    def _assert_frozen_run_compatible(
        self,
        manifest: Mapping[str, Any],
        preflight: Mapping[str, Any],
    ) -> None:
        if manifest["tool"]["executable_sha256"] != self.executable_sha256:
            raise ContractError("pipeline executable differs from the frozen run")
        if manifest["tool"]["dependencies"] != preflight["tool_dependencies"]:
            raise ContractError("parser toolchain differs from the frozen run")
        if manifest["config_sha256"] != self.config_sha256:
            raise ContractError("current configuration differs from the frozen run")
        if manifest["schema_set_sha256"] != self.schema_set_sha256():
            raise ContractError("current schema set differs from the frozen run")

    def _human_decision_documents(
        self, decision_path: Path, run_id: str
    ) -> tuple[HumanDecisionLog, list[dict[str, Any]]]:
        log = HumanDecisionLog(
            decision_path,
            run_id=run_id,
            validator=self.validators["human_decision"],
            now=self.now,
        )
        documents = [
            json.loads(line)
            for line in safe_file_bytes(decision_path).splitlines()
        ]
        return log, documents

    @staticmethod
    def _output_for_path(
        manifest: Mapping[str, Any], repository_path: str
    ) -> dict[str, Any] | None:
        for reference in manifest["outputs"]:
            if reference["path"] == repository_path:
                return dict(reference)
        return None

    def _verified_output_for_path(
        self, manifest: Mapping[str, Any], path: Path
    ) -> dict[str, Any]:
        repository_path = repository_relative(self.repository_root, path)
        reference = self._output_for_path(manifest, repository_path)
        if reference is None:
            raise ContractError(f"run output is not indexed: {repository_path}")
        data = safe_file_bytes(path)
        if (
            sha256_bytes(data) != reference["sha256"]
            or len(data) != reference["byte_count"]
        ):
            raise ContractError(f"recorded run output changed: {repository_path}")
        return reference

    @staticmethod
    def _latest_queue_reference(manifest: Mapping[str, Any]) -> dict[str, Any]:
        references = [
            reference
            for reference in manifest["outputs"]
            if reference["role"].startswith("REVIEW_QUEUE_")
            and "MARKDOWN" not in reference["role"]
            and "RENDER" not in reference["role"]
        ]
        if not references:
            raise ContractError("run has no review queue artifact")
        return dict(references[-1])

    def _identity_map(self, run_id: str) -> dict[str, Any]:
        path = self.restricted_root / run_id / "identity_map.json"
        document = read_json(path)
        self.validators["identity_map"].validate(document)
        if document["run_id"] != run_id:
            raise ContractError("identity map belongs to a different run")
        return document

    @staticmethod
    def _identity_map_matches_submissions(
        identity_map: Mapping[str, Any],
        submissions: Mapping[str, tuple[dict[str, Any], Path]],
    ) -> bool:
        entries = list(identity_map["entries"])
        if len(entries) != len(submissions):
            return False
        if {entry["submission_record_id"] for entry in entries} != set(submissions):
            return False
        if len({entry["submission_record_id"] for entry in entries}) != len(entries):
            return False
        if len({entry["source_group_key"] for entry in entries}) != len(entries):
            return False
        identity_to_pseudonym: dict[str, str] = {}
        pseudonym_to_identity: dict[str, str] = {}
        for entry in entries:
            record_id = entry["submission_record_id"]
            submission = submissions[record_id][0]
            if any(
                (
                    entry["assignment_id"] != submission["assignment_id"],
                    entry["pseudonym"] != submission["pseudonym"],
                    entry["attempt_number"] != submission["attempt_number"],
                    record_id
                    != f"{entry['assignment_id']}-{entry['pseudonym']}-V{entry['attempt_number']:02d}",
                )
            ):
                return False
            original_inventory = sorted(
                (item["sha256"], item["byte_count"])
                for item in entry["original_files"]
            )
            submission_inventory = sorted(
                (item["sha256"], item["byte_count"])
                for item in submission["input_files"]
            )
            if original_inventory != submission_inventory:
                return False
            for subject in entry["subjects"]:
                identity_key = subject["source_identity_key"]
                prior_pseudonym = identity_to_pseudonym.setdefault(
                    identity_key, entry["pseudonym"]
                )
                if prior_pseudonym != entry["pseudonym"]:
                    return False
                prior_identity = pseudonym_to_identity.setdefault(
                    entry["pseudonym"], identity_key
                )
                if prior_identity != identity_key:
                    return False
        return True

    def _submission_manifests(
        self, run_root: Path, run_id: str
    ) -> dict[str, tuple[dict[str, Any], Path]]:
        result: dict[str, tuple[dict[str, Any], Path]] = {}
        for path in sorted((run_root / "manifests/submissions").glob("*.json")):
            document = read_json(path)
            self.validators["submission_manifest"].validate(document)
            if document["run_id"] != run_id:
                raise ContractError("submission manifest belongs to a different run")
            record_id = document["submission_record_id"]
            if record_id in result:
                raise ContractError("duplicate submission record ID")
            result[record_id] = (document, path)
        return result

    def _selection_document(
        self,
        *,
        run_id: str,
        manifest: dict[str, Any],
        submissions: Mapping[str, tuple[dict[str, Any], Path]],
        allocator: IdAllocator,
        lock_event_id: str,
    ) -> dict[str, Any]:
        eligible_snapshot = sorted(
            (
                {
                    "assignment_id": document["assignment_id"],
                    "package_stratum": document["calibration_stratum"],
                    "submission_record_id": record_id,
                    "source_payload_sha256": document["source_payload_sha256"],
                }
                for record_id, (document, _) in submissions.items()
                if document["calibration_stratum"] in CALIBRATION_STRATA
            ),
            key=lambda item: (
                item["assignment_id"],
                item["package_stratum"],
                item["submission_record_id"],
            ),
        )
        seed = manifest["sample_seed"]
        selections: list[dict[str, Any]] = []
        missing_slots: list[str] = []
        for assignment_id in ASSIGNMENTS:
            for stratum in CALIBRATION_STRATA:
                candidates = [
                    item
                    for item in eligible_snapshot
                    if item["assignment_id"] == assignment_id
                    and item["package_stratum"] == stratum
                ]
                ranked = sorted(
                    (
                        (
                            selection_rank_digest(
                                seed,
                                assignment_id,
                                stratum,
                                item["submission_record_id"],
                            ),
                            item,
                        )
                        for item in candidates
                    ),
                    key=lambda pair: (pair[0], pair[1]["submission_record_id"]),
                )
                if not ranked:
                    missing_slots.append(f"{assignment_id}:{stratum}")
                    continue
                rank_digest, selected = ranked[0]
                _, path = submissions[selected["submission_record_id"]]
                path_string = repository_relative(self.repository_root, path)
                source_ref = self._output_for_path(manifest, path_string)
                if source_ref is None:
                    raise ContractError("submission manifest is absent from run outputs")
                selections.append(
                    {
                        "assignment_id": assignment_id,
                        "package_stratum": stratum,
                        "submission_record_id": selected["submission_record_id"],
                        "pseudonym": submissions[selected["submission_record_id"]][0][
                            "pseudonym"
                        ],
                        "rank_digest": rank_digest,
                        "rank": 1,
                        "eligible_count": len(ranked),
                        "submission_manifest": source_ref,
                    }
                )
        if missing_slots:
            raise ContractError(
                "calibration cannot lock; missing slots: " + ", ".join(missing_slots)
            )
        selected_ids = [item["submission_record_id"] for item in selections]
        if len(selections) != 8 or len(set(selected_ids)) != 8:
            raise ContractError("calibration selection is not eight distinct submissions")
        now = self.now()
        return {
            "schema_version": SCHEMA_VERSION,
            "selection_id": allocator.next("SEL"),
            "run_id": run_id,
            "configuration_id": self.configuration_id,
            "config_sha256": self.config_sha256,
            "reference_manifest_sha256": manifest["reference_manifest_sha256"],
            "created_at": now,
            "locked_at": now,
            "lock_event_id": lock_event_id,
            "status": "LOCKED",
            "seed": seed,
            "method": self.config["review"]["sample_method"],
            "rank_digest_definition": self.config["review"]["sample_rank_digest"],
            "eligibility_snapshot_sha256": sha256_bytes(
                canonical_json_bytes(eligible_snapshot)
            ),
            "sample_size": 8,
            "content_review_started": False,
            "selections": selections,
            "reconciliation": {
                "expected_slots": 8,
                "filled_slots": 8,
                "duplicate_submission_record_ids": 0,
                "missing_slots": [],
            },
            "contains_source_identifiers": False,
        }

    def _references_match_frozen_bytes(
        self, reference_manifest: Mapping[str, Any]
    ) -> bool:
        for reference in reference_manifest["references"]:
            try:
                relative = assert_relative_path(reference["path"])
                path = self.repository_root / relative
                resolved = path.resolve(strict=True)
                resolved.relative_to(self.repository_root)
                if path.is_symlink() or not path.is_file():
                    return False
                data = safe_file_bytes(path)
            except (OSError, ValueError, PipelineError):
                return False
            if (
                sha256_bytes(data) != reference["sha256"]
                or len(data) != reference["byte_count"]
            ):
                return False
        return True

    def _frozen_reference_bytes(
        self, reference: Mapping[str, Any]
    ) -> bytes:
        path = self.repository_root / assert_relative_path(reference["path"])
        data = safe_file_bytes(path)
        if any(
            (
                sha256_bytes(data) != reference["sha256"],
                len(data) != reference["byte_count"],
            )
        ):
            raise ContractError("frozen reference changed at point of use")
        return data

    def _solution_bytes(
        self,
        submission: Mapping[str, Any],
        identity_entry: Mapping[str, Any],
    ) -> tuple[bytes, str]:
        originals = identity_entry["original_files"]
        if len(originals) != 1:
            raise ContractError("calibration source must have exactly one top-level file")
        source_path = self.repository_root / originals[0]["source_path"]
        data = safe_file_bytes(
            source_path,
            int(self.config["processing"]["archive_limits"]["max_total_expanded_bytes"]),
        )
        if sha256_bytes(data) != originals[0]["sha256"]:
            raise ContractError("preserved source bytes changed after intake")
        if submission["calibration_stratum"] == "READABLE_SINGLE_PDF":
            return data, submission["input_files"][0]["artifact_id"]
        archive = inspect_zip_bytes(
            data,
            artifact_id=submission["input_files"][0]["artifact_id"],
            limits=self.config["processing"]["archive_limits"],
        )
        if archive.record["status"] != "SAFE" or archive.solution_pdf is None:
            raise ContractError("selected ZIP no longer has one safe solution PDF")
        return archive.solution_pdf, submission["input_files"][0]["artifact_id"]

    def _identity_scan(
        self,
        solution_pdf: bytes,
        *,
        artifact_id: str,
        identities: Sequence[Mapping[str, Any]],
        private_tmp: Path,
    ) -> tuple[str, list[str]]:
        inspection, text = inspect_pdf_bytes(
            solution_pdf,
            artifact_id=artifact_id,
            private_tmp=private_tmp,
            maximum_bytes=int(
                self.config["processing"]["archive_limits"]["max_pdf_bytes_for_text_check"]
            ),
            timeout_seconds=int(
                self.config["processing"]["archive_limits"]["tool_timeout_seconds"]
            ),
        )
        if PDF_PAGE_TEXT_SEPARATOR not in text:
            raise ContractError("PDF parser output lacks the page-text boundary")
        metadata_text, page_text = text.split(PDF_PAGE_TEXT_SEPARATOR, 1)
        text_value = normalized_casefold(
            page_text.decode("utf-8", errors="replace")
        )
        nonvisible_value = normalized_casefold(
            metadata_text.decode("utf-8", errors="replace")
        )
        binary_value = normalized_casefold(
            solution_pdf.decode("latin-1", errors="ignore")
        )
        nonvisible_value += "\n" + binary_value
        matched_codes: set[str] = set()
        active_pdf_tokens = (
            "/openaction",
            "/javascript",
            "/launch",
            "/embeddedfiles",
            "/richmedia",
            "/submitform",
            "/importdata",
            "/gotor",
        )
        if any(token in binary_value for token in active_pdf_tokens) or re.search(
            r"(?m)^javascript:\s*yes\s*$", text_value
        ):
            matched_codes.add("PDF_ACTIVE_CONTENT_PRESENT")

        for entry in identities:
            for subject in entry["subjects"]:
                display = subject.get("display_name")
                if display and identity_token_present(text_value, display):
                    matched_codes.add(
                        "IDENTITY_DISPLAY_NAME_VISIBLE_TEXT_PRESENT"
                    )
                if display and identity_token_present(nonvisible_value, display):
                    matched_codes.add(
                        "IDENTITY_DISPLAY_NAME_BINARY_ONLY_PRESENT"
                    )
                user_id = subject.get("lms_user_id")
                if user_id and re.search(
                    rf"(?<![0-9]){re.escape(user_id)}(?![0-9])", text_value
                ):
                    matched_codes.add("IDENTITY_LMS_ID_VISIBLE_TEXT_PRESENT")
                if user_id and re.search(
                    rf"(?<![0-9]){re.escape(user_id)}(?![0-9])", nonvisible_value
                ):
                    matched_codes.add("IDENTITY_LMS_ID_BINARY_ONLY_PRESENT")
            for source in entry["original_files"]:
                basename = PurePosixPath(source["source_path"]).name
                if len(basename) >= 6 and basename.casefold() in nonvisible_value:
                    matched_codes.add(
                        "IDENTITY_ORIGINAL_FILENAME_BINARY_ONLY_PRESENT"
                    )
                original_tail = basename.split("_", 3)[-1]
                for token in re.findall(r"[A-Za-z][A-Za-z0-9]{3,}", original_tail):
                    folded = token.casefold()
                    if folded in GENERIC_FILENAME_TOKENS:
                        continue
                    if identity_token_present(text_value, folded):
                        matched_codes.add(
                            "IDENTITY_FILENAME_TOKEN_VISIBLE_TEXT_PRESENT"
                        )
                    if identity_token_present(nonvisible_value, folded):
                        matched_codes.add(
                            "IDENTITY_FILENAME_TOKEN_BINARY_ONLY_PRESENT"
                        )
        if matched_codes:
            return "FAIL", sorted(matched_codes)
        if (
            inspection["status"] != "READABLE"
            or inspection["text_extraction"] != "AVAILABLE"
        ):
            return "NEEDS_HUMAN_TRIAGE", ["IDENTITY_SCAN_TEXT_UNAVAILABLE"]
        # A denylist can disprove blinding, but it cannot prove that an unknown
        # visible name, signature, or handwritten identifier is absent.  Only
        # an explicit human visual clearance may advance a real packet to PASS.
        return "NEEDS_HUMAN_TRIAGE", [
            "HUMAN_VISUAL_IDENTITY_CLEARANCE_REQUIRED"
        ]

    def _stage_clearance_request(
        self,
        *,
        run_root: Path,
        run_id: str,
        selection: Mapping[str, Any],
        selection_ref: Mapping[str, Any],
        submissions: Mapping[str, tuple[dict[str, Any], Path]],
        identity_by_record: Mapping[str, Mapping[str, Any]],
        identity_entries: Sequence[Mapping[str, Any]],
        allocator: IdAllocator,
    ) -> tuple[dict[str, Any], list[dict[str, Any]]]:
        request_path = run_root / "manifests/calibration_clearance_request.json"
        if request_path.exists():
            raise ContractError("calibration clearance request already exists")
        items: list[dict[str, Any]] = []
        for selected in selection["selections"]:
            record_id = selected["submission_record_id"]
            if record_id not in identity_by_record:
                raise ContractError("selected record is absent from the identity map")
            submission = submissions[record_id][0]
            solution_pdf, source_artifact_id = self._solution_bytes(
                submission, identity_by_record[record_id]
            )
            scan_status, scan_codes = self._identity_scan(
                solution_pdf,
                artifact_id=source_artifact_id,
                identities=identity_entries,
                private_tmp=run_root / "tmp",
            )
            if scan_status == "PASS":
                # A machine-only PASS is not sufficient for production packet
                # blinding, even if a test double or future scanner emits it.
                scan_status = "NEEDS_HUMAN_TRIAGE"
                scan_codes = ["HUMAN_VISUAL_IDENTITY_CLEARANCE_REQUIRED"]
            identity_failure = identity_scan_requires_derivative(scan_codes)
            if scan_status == "FAIL" and not identity_failure:
                scan_status = "NEEDS_HUMAN_TRIAGE"
                scan_codes = sorted(
                    {
                        *scan_codes,
                        "SOURCE_UNEXTRACTED_CONTENT_NORMALIZED_BY_RASTERIZATION",
                    }
                )
            items.append(
                {
                    "assignment_id": selected["assignment_id"],
                    "submission_record_id": record_id,
                    "package_stratum": selected["package_stratum"],
                    "source_payload_sha256": submission["source_payload_sha256"],
                    "submission_manifest": selected["submission_manifest"],
                    "source_solution_sha256": sha256_bytes(solution_pdf),
                    "source_solution_byte_count": len(solution_pdf),
                    "automated_scan_status": scan_status,
                    "automated_scan_codes": scan_codes,
                    "required_action": (
                        "SANITIZED_DERIVATIVE_REQUIRED"
                        if identity_failure
                        else "VISUAL_CLEARANCE_ALLOWED"
                    ),
                }
            )
        request = {
            "schema_version": SCHEMA_VERSION,
            "run_id": run_id,
            "selection_id": selection["selection_id"],
            "created_at": self.now(),
            "selection": dict(selection_ref),
            "status": "PENDING_HUMAN_REVIEW",
            "items": items,
            "contains_source_identifiers": False,
        }
        self.validators["calibration_clearance_request"].validate(request)
        write_private_json(request_path, request)
        request_ref = artifact_ref(
            self.repository_root,
            request_path,
            artifact_id=allocator.next("ART"),
            role="CALIBRATION_CLEARANCE_REQUEST",
            media_type="application/json",
        )
        return request, [request_ref]

    def _packet_and_dossier(
        self,
        *,
        run_root: Path,
        selection: Mapping[str, Any],
        selected: Mapping[str, Any],
        accepted_solution: bytes,
        accepted_ref: Mapping[str, Any],
        clearance_ref: Mapping[str, Any],
        review_set_ref: Mapping[str, Any],
        clearance_item: Mapping[str, Any],
        decision_id: str,
        reference_materials: Mapping[tuple[str, str], tuple[bytes, Mapping[str, Any]]],
        dossier_template: tuple[bytes, Mapping[str, Any]],
        allocator: IdAllocator,
    ) -> tuple[list[dict[str, Any]], dict[str, Any]]:
        record_id = selected["submission_record_id"]
        assignment_id = selected["assignment_id"]
        solution_pdf = accepted_solution
        if (
            sha256_bytes(solution_pdf) != accepted_ref["sha256"]
            or len(solution_pdf) != accepted_ref["byte_count"]
        ):
            raise ContractError("accepted clearance bytes differ from their artifact")
        source_artifact_id = accepted_ref["artifact_id"]
        statement_bytes, statement_reference = reference_materials[
            (assignment_id, "PROBLEM_STATEMENT")
        ]
        key_bytes, key_reference = reference_materials[
            (assignment_id, "SOLUTION_KEY")
        ]
        packet_root = run_root / "packets" / record_id
        private_mkdir(packet_root)
        material_specs = (
            (
                "SUBMITTED_SOLUTION",
                solution_pdf,
                "submitted-solution.pdf",
                "application/pdf",
                source_artifact_id,
            ),
            (
                "PROBLEM_STATEMENT",
                statement_bytes,
                "problem-statement.md",
                "text/markdown",
                statement_reference["reference_id"],
            ),
            (
                "SOLUTION_KEY",
                key_bytes,
                "solution-key.tex",
                "application/x-tex",
                key_reference["reference_id"],
            ),
        )
        materials: list[dict[str, Any]] = []
        for role, data, filename, media_type, source_id in material_specs:
            destination = packet_root / filename
            write_private_bytes(destination, data)
            packet_reference = artifact_ref(
                self.repository_root,
                destination,
                artifact_id=allocator.next("ART"),
                role=role,
                media_type=media_type,
            )
            materials.append(
                {
                    "source_role": role,
                    "source_artifact": {
                        "artifact_id": (
                            source_id
                            if str(source_id).startswith("ART-")
                            else allocator.next("ART")
                        ),
                        "role": role,
                        "sha256": sha256_bytes(data),
                        "byte_count": len(data),
                        "media_type": media_type,
                    },
                    "source_path_classification": "SANITIZED_RUN_ARTIFACT",
                    "packet_artifact": packet_reference,
                }
            )
        created_at = self.now()
        exclusions = {
            "discourse": True,
            "identity": True,
            "original_filenames": True,
            "intake_flags": True,
            "late_metadata": True,
            "route_metadata": True,
        }
        packet_manifest = {
            "schema_version": SCHEMA_VERSION,
            "packet_id": allocator.next("PKT"),
            "run_id": selection["run_id"],
            "selection_id": selection["selection_id"],
            "created_at": created_at,
            "assignment_id": assignment_id,
            "submission_record_id": record_id,
            "pseudonym": selected["pseudonym"],
            "classification": "RESTRICTED_CALIBRATION_PACKET",
            "required_file_mode": "0600",
            "materials": materials,
            "sanitization": {
                "tool": {
                    "name": "ne630-review-pipeline",
                    "version": VERSION,
                    "executable_sha256": self.executable_sha256,
                },
                "method": "Instructor-cleared, canonical image-only raster PDF from an immutable review set; discourse, metadata, active content, and non-product files excluded.",
                "clearance_artifact": dict(clearance_ref),
                "review_set_artifact": dict(review_set_ref),
                "decision_id": decision_id,
                "disposition": clearance_item["disposition"],
                "automated_scan_status": clearance_item[
                    "automated_scan_status"
                ],
                "automated_scan_codes": list(
                    clearance_item["automated_scan_codes"]
                ),
                "identity_scan_status": "PASS",
            },
            "exclusions": exclusions,
            "product_review_opened": False,
            "contains_source_identifiers": False,
        }
        self.validators["calibration_packet_manifest"].validate(packet_manifest)
        packet_manifest_path = packet_root / "packet_manifest.json"
        write_private_json(packet_manifest_path, packet_manifest)
        packet_manifest_ref = artifact_ref(
            self.repository_root,
            packet_manifest_path,
            artifact_id=allocator.next("ART"),
            role="CALIBRATION_PACKET_MANIFEST",
            media_type="application/json",
        )
        sections: list[dict[str, Any]] = []
        for index, material in enumerate(materials, 1):
            packet_artifact = material["packet_artifact"]
            sections.append(
                {
                    "section_id": f"SEC-{index:06d}",
                    "title": material["source_role"].replace("_", " ").title(),
                    "source_role": material["source_role"],
                    "summary": "Pending qualitative product review.",
                    "evidence_locators": [
                        {
                            "artifact_id": packet_artifact["artifact_id"],
                            "artifact_sha256": packet_artifact["sha256"],
                            "source_role": material["source_role"],
                            "logical_path": PurePosixPath(packet_artifact["path"]).name,
                            "locator_type": "FILE",
                            "extraction_method": (
                                "PDFTOTEXT"
                                if material["source_role"] == "SUBMITTED_SOLUTION"
                                else "NATIVE_TEXT"
                            ),
                            "uncertainty": "NONE",
                        }
                    ],
                }
            )
        expected_problem_count = next(
            item["expected_problem_count"]
            for item in self.config["assignment"]["assignments"]
            if item["id"] == assignment_id
        )
        dossier = {
            "schema_version": SCHEMA_VERSION,
            "dossier_id": allocator.next("DOS"),
            "run_id": selection["run_id"],
            "selection_id": selection["selection_id"],
            "created_at": created_at,
            "assignment_id": assignment_id,
            "submission_record_id": record_id,
            "pseudonym": selected["pseudonym"],
            "view": "PRODUCT_BLINDED",
            "packet_manifest": packet_manifest_ref,
            "coverage": {
                "status": "NOT_CHECKABLE",
                "expected_problem_count": expected_problem_count,
                "problem_ids": [],
                "reviewable_pages": [],
            },
            "sections": sections,
            "exclusions": exclusions,
            "reviewer_state": "PENDING",
            "student_facing": False,
            "contains_source_identifiers": False,
        }
        self.validators["dossier_data"].validate(dossier)
        dossier_root = run_root / "dossiers" / record_id
        private_mkdir(dossier_root)
        dossier_path = dossier_root / "dossier_data.json"
        write_private_json(dossier_path, dossier)
        dossier_ref = artifact_ref(
            self.repository_root,
            dossier_path,
            artifact_id=allocator.next("ART"),
            role="DOSSIER_DATA",
            media_type="application/json",
        )
        template_path = self.templates_root / "dossier.md.tmpl"
        template_bytes, template_reference = dossier_template
        template = template_bytes.decode("utf-8")
        material_lines = "\n".join(
            f"- `{material['source_role']}` — `{PurePosixPath(material['packet_artifact']['path']).name}`"
            for material in materials
        )
        markdown = template.format(
            assignment_id=assignment_id,
            submission_record_id=record_id,
            run_id=selection["run_id"],
            materials=material_lines,
        ).encode("utf-8")
        markdown_path = dossier_root / "dossier.md"
        write_private_bytes(markdown_path, markdown)
        markdown_ref = artifact_ref(
            self.repository_root,
            markdown_path,
            artifact_id=allocator.next("ART"),
            role="DOSSIER_MARKDOWN",
            media_type="text/markdown",
        )
        template_ref = {
            "artifact_id": allocator.next("ART"),
            "role": "DOSSIER_TEMPLATE",
            "path": repository_relative(self.repository_root, template_path),
            "sha256": sha256_bytes(template_bytes),
            "byte_count": len(template_bytes),
            "media_type": "text/plain",
        }
        if any(
            (
                template_reference["sha256"] != template_ref["sha256"],
                template_reference["byte_count"] != template_ref["byte_count"],
            )
        ):
            raise ContractError("dossier template differs from the frozen reference")
        render = {
            "schema_version": SCHEMA_VERSION,
            "render_id": allocator.next("RND"),
            "run_id": selection["run_id"],
            "created_at": created_at,
            "render_kind": "DOSSIER_MARKDOWN",
            "source": dossier_ref,
            "template": template_ref,
            "renderer": {
                "name": "ne630-review-pipeline",
                "version": VERSION,
                "sha256": self.executable_sha256,
            },
            "output": markdown_ref,
            "deterministic": True,
            "contains_source_identifiers": False,
        }
        self.validators["render_manifest"].validate(render)
        render_path = dossier_root / "dossier.render.json"
        write_private_json(render_path, render)
        render_ref = artifact_ref(
            self.repository_root,
            render_path,
            artifact_id=allocator.next("ART"),
            role="DOSSIER_RENDER_MANIFEST",
            media_type="application/json",
        )
        output_refs = [packet_manifest_ref, dossier_ref, markdown_ref, render_ref]
        output_refs.extend(material["packet_artifact"] for material in materials)
        return output_refs, dossier_ref

    def prepare_calibration(self, *, run_id: str | None = None) -> dict[str, Any]:
        with self._mutation_lock():
            self._clear_stage_failure_guard()
            try:
                return self._prepare_calibration(run_id=run_id)
            except (Exception, KeyboardInterrupt):
                self._seal_active_stage_failure()
                raise
            finally:
                self._clear_stage_failure_guard()

    def _prepare_calibration(self, *, run_id: str | None = None) -> dict[str, Any]:
        preflight = self.preflight_framework(require_tools=True)
        run_id = self.resolve_run_id(run_id)
        run_root, manifest, events, event_path, decision_path, allocator = self._load_run(
            run_id
        )
        self._assert_frozen_run_compatible(manifest, preflight)
        prepare_state = self._stage(manifest, "PREPARE_CALIBRATION")
        if (
            manifest["run_state"] == "BLOCKED"
            and prepare_state["status"] == "BLOCKED"
            and prepare_state["reason_code"] == "IDENTITY_SANITIZATION_REQUIRED"
        ):
            selection_path = run_root / "manifests/calibration_selection.json"
            request_path = run_root / "manifests/calibration_clearance_request.json"
            self._verified_output_for_path(manifest, selection_path)
            self._verified_output_for_path(manifest, request_path)
            selection = read_json(selection_path)
            request = read_json(request_path)
            self.validators["calibration_selection"].validate(selection)
            self.validators["calibration_clearance_request"].validate(request)
            if any(
                (
                    selection["run_id"] != run_id,
                    request["run_id"] != run_id,
                    request["selection_id"] != selection["selection_id"],
                )
            ):
                raise ContractError("existing calibration checkpoint is inconsistent")
            return {
                "run_id": run_id,
                "selection_id": selection["selection_id"],
                "selected": 8,
                "status": "BLOCKED",
                "reason_code": "IDENTITY_SANITIZATION_REQUIRED",
                "next_command": "stage-calibration-review-set",
            }
        if manifest["run_state"] in {"BLOCKED", "FAILED"}:
            raise ContractError(
                "blocked or failed runs must be explicitly repaired/resumed before calibration preparation"
            )
        if self._stage(manifest, "INTAKE")["status"] != "COMPLETE":
            raise ContractError("intake must be complete before calibration preparation")
        if self._stage(manifest, "PREPARE_CALIBRATION")["status"] != "NOT_STARTED":
            raise ContractError("calibration preparation has already started for this run")
        reference_path = run_root / "manifests/reference_manifest.json"
        reference_bytes = safe_file_bytes(reference_path)
        if sha256_bytes(reference_bytes) != manifest["reference_manifest_sha256"]:
            raise ContractError("frozen reference manifest hash changed")
        reference_manifest = json.loads(reference_bytes)
        self.validators["reference_manifest"].validate(reference_manifest)
        if not self._references_match_frozen_bytes(reference_manifest):
            raise ContractError("one or more frozen reference bytes changed")
        submissions = self._submission_manifests(run_root, run_id)
        for _, path in submissions.values():
            self._verified_output_for_path(manifest, path)
        intake_queue_ref = self._latest_queue_reference(manifest)
        self._verified_output_for_path(
            manifest, self.repository_root / intake_queue_ref["path"]
        )
        identity_path = self.restricted_root / run_id / "identity_map.json"
        self._verified_output_for_path(manifest, identity_path)
        identity_map = self._identity_map(run_id)
        if not self._identity_map_matches_submissions(identity_map, submissions):
            raise ContractError("identity map does not reconcile with submission manifests")
        identity_by_record = {
            entry["submission_record_id"]: entry for entry in identity_map["entries"]
        }
        manifest["validation"] = {"status": "NOT_RUN", "report": None}
        validation_stage = self._stage(manifest, "VALIDATE")
        if validation_stage["status"] != "NOT_STARTED":
            validation_stage.update(
                {
                    "status": "NOT_STARTED",
                    "event_sequence_start": None,
                    "event_sequence_end": None,
                    "started_at": None,
                    "completed_at": None,
                    "reason_code": None,
                }
            )
        self._arm_stage_failure_guard(
            manifest=manifest,
            events=events,
            run_root=run_root,
            event_path=event_path,
            decision_path=decision_path,
            stage="PREPARE_CALIBRATION",
            code="PREPARE_CALIBRATION_FAILED",
            message="Calibration preparation stopped safely before completion.",
        )
        self._start_stage(manifest, events, "PREPARE_CALIBRATION")
        try:
            selection = self._selection_document(
                run_id=run_id,
                manifest=manifest,
                submissions=submissions,
                allocator=allocator,
                lock_event_id=events.next_event_id,
            )
        except ContractError as exc:
            self._block_stage(
                manifest,
                events,
                "PREPARE_CALIBRATION",
                "CALIBRATION_SLOTS_MISSING",
                str(exc),
            )
            self._refresh_logs(manifest, events, event_path, decision_path)
            self._write_manifest(run_root, manifest)
            raise
        self.validators["calibration_selection"].validate(selection)
        selection_path = run_root / "manifests/calibration_selection.json"
        write_private_json(selection_path, selection)
        selection_ref = artifact_ref(
            self.repository_root,
            selection_path,
            artifact_id=allocator.next("ART"),
            role="CALIBRATION_SELECTION",
            media_type="application/json",
        )
        self._add_output(manifest, selection_ref)
        lock_event = events.append(
            stage="PREPARE_CALIBRATION",
            event_type="SELECTION_LOCKED",
            subject_type="SELECTION",
            subject_id=selection["selection_id"],
            outcome="RECORDED",
            reason_code="CALIBRATION_SELECTION_LOCKED",
            outputs=[selection_ref],
            payload={"selection_id": selection["selection_id"]},
        )
        if lock_event["event_id"] != selection["lock_event_id"]:
            raise ContractError("selection lock event ID changed during write")
        _, clearance_request_refs = self._stage_clearance_request(
            run_root=run_root,
            run_id=run_id,
            selection=selection,
            selection_ref=selection_ref,
            submissions=submissions,
            identity_by_record=identity_by_record,
            identity_entries=identity_map["entries"],
            allocator=allocator,
        )
        for reference in clearance_request_refs:
            self._add_output(manifest, reference)
        self._block_stage(
            manifest,
            events,
            "PREPARE_CALIBRATION",
            "IDENTITY_SANITIZATION_REQUIRED",
            "Eight selected products are locked; an inert visual-review set must be staged and explicitly cleared before packet creation.",
        )
        manifest["reconciliation"]["calibration_selected"] = 8
        self._refresh_logs(manifest, events, event_path, decision_path)
        self._write_manifest(run_root, manifest)
        return {
            "run_id": run_id,
            "selection_id": selection["selection_id"],
            "selected": 8,
            "status": "BLOCKED",
            "reason_code": "IDENTITY_SANITIZATION_REQUIRED",
            "next_command": "stage-calibration-review-set",
        }

    def stage_calibration_review_set(
        self,
        *,
        run_id: str | None = None,
        sanitized_derivatives: Mapping[str, Path],
    ) -> dict[str, Any]:
        with self._mutation_lock():
            self._clear_stage_failure_guard()
            try:
                return self._stage_calibration_review_set(
                    run_id=run_id,
                    sanitized_derivatives=sanitized_derivatives,
                )
            except (Exception, KeyboardInterrupt):
                self._seal_active_stage_failure()
                raise
            finally:
                self._clear_stage_failure_guard()

    def _stage_calibration_review_set(
        self,
        *,
        run_id: str | None,
        sanitized_derivatives: Mapping[str, Path],
    ) -> dict[str, Any]:
        preflight = self.preflight_framework(require_tools=True)
        run_id = self.resolve_run_id(run_id)
        run_root, manifest, events, event_path, decision_path, allocator = self._load_run(
            run_id
        )
        prepare_state = self._stage(manifest, "PREPARE_CALIBRATION")
        if any(
            (
                manifest["run_state"] != "BLOCKED",
                prepare_state["status"] != "BLOCKED",
                prepare_state["reason_code"] != "IDENTITY_SANITIZATION_REQUIRED",
            )
        ):
            raise ContractError(
                "a review set may be staged only for an identity-clearance-blocked preparation"
            )
        self._assert_frozen_run_compatible(manifest, preflight)
        selection_path = run_root / "manifests/calibration_selection.json"
        request_path = run_root / "manifests/calibration_clearance_request.json"
        selection_ref = self._verified_output_for_path(manifest, selection_path)
        request_ref = self._verified_output_for_path(manifest, request_path)
        selection = read_json(selection_path)
        request = read_json(request_path)
        self.validators["calibration_selection"].validate(selection)
        self.validators["calibration_clearance_request"].validate(request)
        if any(
            (
                selection["run_id"] != run_id,
                request["run_id"] != run_id,
                request["selection_id"] != selection["selection_id"],
                request["selection"] != selection_ref,
            )
        ):
            raise ContractError("clearance request does not match the locked selection")
        selected_by_record = {
            item["submission_record_id"]: item for item in selection["selections"]
        }
        request_by_record = {
            item["submission_record_id"]: item for item in request["items"]
        }
        selected_ids = set(selected_by_record)
        if len(selected_ids) != 8 or set(request_by_record) != selected_ids:
            raise ContractError("clearance request does not contain the exact selection")
        unknown_derivatives = set(sanitized_derivatives) - selected_ids
        if unknown_derivatives:
            raise ContractError(
                "sanitized derivative names an unselected record: "
                + ",".join(sorted(unknown_derivatives))
            )
        submissions = self._submission_manifests(run_root, run_id)
        identity_path = self.restricted_root / run_id / "identity_map.json"
        self._verified_output_for_path(manifest, identity_path)
        identity_map = self._identity_map(run_id)
        if not self._identity_map_matches_submissions(identity_map, submissions):
            raise ContractError("identity map does not reconcile with submission manifests")
        identity_by_record = {
            item["submission_record_id"]: item for item in identity_map["entries"]
        }
        maximum_bytes = int(
            self.config["processing"]["archive_limits"]["max_pdf_bytes_for_text_check"]
        )
        timeout_seconds = int(
            self.config["processing"]["archive_limits"]["tool_timeout_seconds"]
        )
        prepared: dict[
            str, tuple[bytes, InertPdf, str, str, list[str], str]
        ] = {}
        for record_id in sorted(selected_ids):
            request_item = request_by_record[record_id]
            if record_id in sanitized_derivatives:
                source_bytes = safe_file_bytes(
                    sanitized_derivatives[record_id], maximum_bytes
                )
                scan_status, scan_codes = self._identity_scan(
                    source_bytes,
                    artifact_id=allocator.next("ART"),
                    identities=identity_map["entries"],
                    private_tmp=run_root / "tmp",
                )
                identity_failure = identity_scan_requires_derivative(scan_codes)
                if identity_failure:
                    raise ContractError(
                        "a sanitized derivative still contains a known identity"
                    )
                if scan_status == "FAIL":
                    scan_status = "NEEDS_HUMAN_TRIAGE"
                    scan_codes = sorted(
                        {
                            *scan_codes,
                            "SOURCE_UNEXTRACTED_CONTENT_NORMALIZED_BY_RASTERIZATION",
                        }
                    )
                disposition = "SANITIZED_DERIVATIVE_RASTER"
                required_action = "VISUAL_CLEARANCE_ALLOWED"
            else:
                submission = submissions.get(record_id)
                identity_entry = identity_by_record.get(record_id)
                if submission is None or identity_entry is None:
                    raise ContractError("selected record is absent from frozen intake state")
                source_bytes, _ = self._solution_bytes(
                    submission[0], identity_entry
                )
                if any(
                    (
                        sha256_bytes(source_bytes)
                        != request_item["source_solution_sha256"],
                        len(source_bytes)
                        != request_item["source_solution_byte_count"],
                    )
                ):
                    raise ContractError("selected source PDF differs from its request")
                scan_status = request_item["automated_scan_status"]
                scan_codes = list(request_item["automated_scan_codes"])
                disposition = "SOURCE_RASTER"
                required_action = request_item["required_action"]
            inert = rasterize_pdf_to_inert_pdf(
                source_bytes,
                artifact_id=allocator.next("ART"),
                private_tmp=run_root / "tmp",
                maximum_input_bytes=maximum_bytes,
                timeout_seconds=timeout_seconds,
            )
            prepared[record_id] = (
                source_bytes,
                inert,
                disposition,
                scan_status,
                list(scan_codes),
                required_action,
            )

        review_set_id = allocator.next("RSET")
        clearance_root = self.restricted_root / run_id / "clearance"
        review_sets_root = clearance_root / "review-sets"
        review_root = review_sets_root / review_set_id
        private_mkdir(clearance_root)
        private_mkdir(review_sets_root)
        private_mkdir_exclusive(review_root)
        review_set_path = (
            run_root
            / "manifests"
            / f"calibration_clearance_review_set-{review_set_id.lower()}.json"
        )
        original_output_count = len(manifest["outputs"])
        output_batch: list[dict[str, Any]] = []
        self._arm_stage_failure_guard(
            manifest=manifest,
            events=events,
            run_root=run_root,
            event_path=event_path,
            decision_path=decision_path,
            stage="PREPARE_CALIBRATION",
            code="PREPARE_CALIBRATION_FAILED",
            message="Review-set staging stopped safely before human clearance.",
            preserve_terminal=True,
        )
        try:
            review_items: list[dict[str, Any]] = []
            review_refs: list[dict[str, Any]] = []
            for record_id in sorted(selected_ids):
                (
                    source_bytes,
                    inert,
                    disposition,
                    scan_status,
                    scan_codes,
                    required_action,
                ) = prepared[record_id]
                output_path = review_root / f"{record_id}.pdf"
                write_private_bytes(output_path, inert.data)
                review_ref = artifact_ref(
                    self.repository_root,
                    output_path,
                    artifact_id=allocator.next("ART"),
                    role="CALIBRATION_REVIEW_PDF",
                    media_type="application/pdf",
                )
                review_refs.append(review_ref)
                review_items.append(
                    {
                        "assignment_id": selected_by_record[record_id]["assignment_id"],
                        "submission_record_id": record_id,
                        "disposition": disposition,
                        "source_input_sha256": sha256_bytes(source_bytes),
                        "source_input_byte_count": len(source_bytes),
                        "review_artifact": review_ref,
                        "page_count": inert.page_count,
                        "page_sha256s": list(inert.page_sha256s),
                        "pixel_dimensions": [
                            list(item) for item in inert.pixel_dimensions
                        ],
                        "automated_scan_status": scan_status,
                        "automated_scan_codes": scan_codes,
                        "required_action": required_action,
                    }
                )
            ready = all(
                item["required_action"] == "VISUAL_CLEARANCE_ALLOWED"
                for item in review_items
            )
            review_set = {
                "schema_version": SCHEMA_VERSION,
                "run_id": run_id,
                "selection_id": selection["selection_id"],
                "review_set_id": review_set_id,
                "created_at": self.now(),
                "selection": selection_ref,
                "clearance_request": request_ref,
                "status": (
                    "READY_FOR_VISUAL_REVIEW"
                    if ready
                    else "REQUIRES_SANITIZED_DERIVATIVE"
                ),
                "normalization": {
                    "profile": INERT_RASTER_PROFILE,
                    "tool_name": "ne630-review-pipeline",
                    "tool_version": VERSION,
                    "executable_sha256": self.executable_sha256,
                },
                "items": review_items,
                "contains_source_identifiers": False,
            }
            self.validators["calibration_clearance_review_set"].validate(review_set)
            write_private_json(review_set_path, review_set)
            review_set_ref = artifact_ref(
                self.repository_root,
                review_set_path,
                artifact_id=allocator.next("ART"),
                role="CALIBRATION_CLEARANCE_REVIEW_SET",
                media_type="application/json",
            )

            output_batch = [*review_refs, review_set_ref]
            existing_ids = {
                reference["artifact_id"] for reference in manifest["outputs"]
            }
            existing_paths = {reference["path"] for reference in manifest["outputs"]}
            batch_ids = [reference["artifact_id"] for reference in output_batch]
            batch_paths = [reference["path"] for reference in output_batch]
            if any(
                (
                    len(batch_ids) != len(set(batch_ids)),
                    len(batch_paths) != len(set(batch_paths)),
                    bool(existing_ids.intersection(batch_ids)),
                    bool(existing_paths.intersection(batch_paths)),
                )
            ):
                raise ContractError("review-set output batch conflicts with run outputs")
            manifest["outputs"].extend(output_batch)
        except BaseException as staging_error:
            batch_fully_indexed = bool(output_batch) and all(
                reference in manifest["outputs"] for reference in output_batch
            )
            if not batch_fully_indexed:
                del manifest["outputs"][original_output_count:]
                cleanup_failed = False
                try:
                    if review_set_path.is_symlink() or review_set_path.is_file():
                        review_set_path.unlink()
                    manifests_descriptor = os.open(
                        review_set_path.parent, os.O_RDONLY | os.O_DIRECTORY
                    )
                    try:
                        os.fsync(manifests_descriptor)
                    finally:
                        os.close(manifests_descriptor)
                    if review_root.is_symlink():
                        review_root.unlink()
                    elif review_root.exists():
                        shutil.rmtree(review_root)
                    review_sets_descriptor = os.open(
                        review_sets_root, os.O_RDONLY | os.O_DIRECTORY
                    )
                    try:
                        os.fsync(review_sets_descriptor)
                    finally:
                        os.close(review_sets_descriptor)
                except OSError:
                    cleanup_failed = True
                if cleanup_failed:
                    raise PipelineError(
                        "review-set staging failed and its private rollback was incomplete"
                    ) from staging_error
            raise
        event = events.append(
            stage="RUN",
            event_type="ARTIFACT_WRITTEN",
            subject_type="ARTIFACT",
            subject_id=review_set_ref["artifact_id"],
            outcome="RECORDED",
            reason_code="CALIBRATION_REVIEW_SET_STAGED",
            inputs=[selection_ref, request_ref],
            outputs=[review_set_ref, *review_refs],
            payload={
                "artifact_id": review_set_ref["artifact_id"],
                "message": "Immutable inert visual-review set staged.",
            },
        )
        manifest["updated_at"] = event["occurred_at"]
        self._refresh_logs(manifest, events, event_path, decision_path)
        self._write_manifest(run_root, manifest)
        return {
            "run_id": run_id,
            "selection_id": selection["selection_id"],
            "review_set_id": review_set_id,
            "review_set_sha256": review_set_ref["sha256"],
            "status": review_set["status"],
            "review_set_manifest": review_set_ref["path"],
            "review_pdfs": [item["review_artifact"]["path"] for item in review_items],
            "requires_sanitized_derivative": [
                item["submission_record_id"]
                for item in review_items
                if item["required_action"] == "SANITIZED_DERIVATIVE_REQUIRED"
            ],
        }

    def record_calibration_clearance(
        self,
        *,
        run_id: str | None = None,
        review_set_id: str,
        review_set_sha256: str,
        actor_id: str,
        attestation: str,
        rationale: str,
    ) -> dict[str, Any]:
        with self._mutation_lock():
            self._clear_stage_failure_guard()
            try:
                return self._record_calibration_clearance(
                    run_id=run_id,
                    review_set_id=review_set_id,
                    review_set_sha256=review_set_sha256,
                    actor_id=actor_id,
                    attestation=attestation,
                    rationale=rationale,
                )
            except (Exception, KeyboardInterrupt):
                self._seal_active_stage_failure()
                raise
            finally:
                self._clear_stage_failure_guard()

    def _record_calibration_clearance(
        self,
        *,
        run_id: str | None,
        review_set_id: str,
        review_set_sha256: str,
        actor_id: str,
        attestation: str,
        rationale: str,
    ) -> dict[str, Any]:
        if not actor_id.strip() or len(actor_id) > 128:
            raise ContractError("instructor actor ID must contain 1 to 128 characters")
        if attestation != CLEARANCE_ATTESTATION:
            raise ContractError("the exact visual-clearance attestation is required")
        if not rationale.strip() or len(rationale) > 10_000:
            raise ContractError("clearance rationale must contain 1 to 10000 characters")
        if not re.fullmatch(r"RSET-[0-9]{6,}", review_set_id):
            raise ContractError("review-set ID is invalid")
        if not re.fullmatch(r"[0-9a-f]{64}", review_set_sha256):
            raise ContractError("review-set SHA-256 is invalid")

        preflight = self.preflight_framework(require_tools=True)
        run_id = self.resolve_run_id(run_id)
        run_root, manifest, events, event_path, decision_path, allocator = self._load_run(
            run_id
        )
        prepare_state = self._stage(manifest, "PREPARE_CALIBRATION")
        if any(
            (
                manifest["run_state"] != "BLOCKED",
                prepare_state["status"] != "BLOCKED",
                prepare_state["reason_code"] != "IDENTITY_SANITIZATION_REQUIRED",
            )
        ):
            raise ContractError(
                "clearance may be recorded only for an identity-clearance-blocked preparation"
            )
        self._assert_frozen_run_compatible(manifest, preflight)
        selection_path = run_root / "manifests/calibration_selection.json"
        request_path = run_root / "manifests/calibration_clearance_request.json"
        selection_ref = self._verified_output_for_path(manifest, selection_path)
        request_ref = self._verified_output_for_path(manifest, request_path)
        selection = read_json(selection_path)
        request = read_json(request_path)
        self.validators["calibration_selection"].validate(selection)
        self.validators["calibration_clearance_request"].validate(request)
        if any(
            (
                selection["run_id"] != run_id,
                request["run_id"] != run_id,
                request["selection_id"] != selection["selection_id"],
                request["selection"] != selection_ref,
            )
        ):
            raise ContractError("clearance request does not match the locked selection")
        selected_ids = {
            item["submission_record_id"] for item in selection["selections"]
        }
        request_by_record = {
            item["submission_record_id"]: item for item in request["items"]
        }
        if len(selected_ids) != 8 or set(request_by_record) != selected_ids:
            raise ContractError("clearance request does not contain the exact selection")
        identity_path = self.restricted_root / run_id / "identity_map.json"
        self._verified_output_for_path(manifest, identity_path)
        identity_map = self._identity_map(run_id)
        free_text = normalized_casefold(f"{actor_id}\n{rationale}")
        for entry in identity_map["entries"]:
            for subject in entry["subjects"]:
                for key in ("display_name", "lms_user_id", "source_identity_key"):
                    value = subject.get(key)
                    if value and identity_token_present(free_text, str(value)):
                        raise ContractError(
                            "actor ID and rationale must not contain source identifiers"
                        )

        review_set_references = [
            item
            for item in manifest["outputs"]
            if item["role"] == "CALIBRATION_CLEARANCE_REVIEW_SET"
            and item["sha256"] == review_set_sha256
        ]
        if len(review_set_references) != 1:
            raise ContractError("review-set hash is not an indexed run artifact")
        review_set_ref = dict(review_set_references[0])
        review_set_path = self.repository_root / assert_relative_path(
            review_set_ref["path"]
        )
        self._verified_output_for_path(manifest, review_set_path)
        review_set = read_json(review_set_path)
        self.validators["calibration_clearance_review_set"].validate(review_set)
        if any(
            (
                review_set["run_id"] != run_id,
                review_set["selection_id"] != selection["selection_id"],
                review_set["review_set_id"] != review_set_id,
                review_set["selection"] != selection_ref,
                review_set["clearance_request"] != request_ref,
                review_set["status"] != "READY_FOR_VISUAL_REVIEW",
                review_set["normalization"]["profile"] != INERT_RASTER_PROFILE,
                review_set["normalization"]["executable_sha256"]
                != self.executable_sha256,
            )
        ):
            raise ContractError("review set is not ready for this exact selection")
        review_by_record = {
            item["submission_record_id"]: item for item in review_set["items"]
        }
        if set(review_by_record) != selected_ids:
            raise ContractError("review set does not cover the exact selection")
        clearance_items: list[dict[str, Any]] = []
        for record_id in sorted(selected_ids):
            request_item = request_by_record[record_id]
            review_item = review_by_record[record_id]
            review_ref = review_item["review_artifact"]
            review_path = self.repository_root / assert_relative_path(
                review_ref["path"]
            )
            if self._verified_output_for_path(manifest, review_path) != review_ref:
                raise ContractError("review PDF reference changed")
            inert = inspect_inert_raster_pdf(
                safe_file_bytes(review_path, MAX_RASTER_TOTAL_BYTES)
            )
            if any(
                (
                    review_ref["role"] != "CALIBRATION_REVIEW_PDF",
                    review_item["assignment_id"]
                    != request_item["assignment_id"],
                    review_item["required_action"]
                    != "VISUAL_CLEARANCE_ALLOWED",
                    review_item["page_count"] != inert.page_count,
                    review_item["page_sha256s"] != list(inert.page_sha256s),
                    review_item["pixel_dimensions"]
                    != [list(item) for item in inert.pixel_dimensions],
                )
            ):
                raise ContractError("review-set row does not reconcile with its PDF")
            disposition = (
                "SOURCE_RASTER_VISUALLY_CLEARED"
                if review_item["disposition"] == "SOURCE_RASTER"
                else "SANITIZED_DERIVATIVE_RASTER_VISUALLY_CLEARED"
            )
            clearance_items.append(
                {
                    "assignment_id": request_item["assignment_id"],
                    "submission_record_id": record_id,
                    "disposition": disposition,
                    "review_artifact": review_ref,
                    "accepted_artifact": review_ref,
                    "automated_scan_status": review_item[
                        "automated_scan_status"
                    ],
                    "automated_scan_codes": list(
                        review_item["automated_scan_codes"]
                    ),
                    "contains_source_identifiers": False,
                }
            )

        decision_log, decision_documents = self._human_decision_documents(
            decision_path, run_id
        )
        self._arm_stage_failure_guard(
            manifest=manifest,
            events=events,
            run_root=run_root,
            event_path=event_path,
            decision_path=decision_path,
            stage="PREPARE_CALIBRATION",
            code="PREPARE_CALIBRATION_FAILED",
            message="Clearance recording stopped safely before calibration resumed.",
            preserve_terminal=True,
        )
        clearance_path = run_root / "manifests/calibration_clearance.json"
        existing_clearance_ref = self._output_for_path(
            manifest, repository_relative(self.repository_root, clearance_path)
        )
        if existing_clearance_ref is not None:
            clearance_ref = self._verified_output_for_path(manifest, clearance_path)
            clearance = read_json(clearance_path)
            self.validators["calibration_clearance"].validate(clearance)
            decision_id = clearance["decision_id"]
            if any(
                (
                    clearance["run_id"] != run_id,
                    clearance["selection_id"] != selection["selection_id"],
                    clearance["selection"] != selection_ref,
                    clearance["clearance_request"] != request_ref,
                    clearance["review_set_id"] != review_set_id,
                    clearance["review_set"] != review_set_ref,
                    clearance["attestation"] != attestation,
                    clearance["items"] != clearance_items,
                )
            ):
                raise ContractError("existing clearance differs from this attestation")
        else:
            if clearance_path.exists():
                raise ContractError("unindexed clearance artifact requires recovery")
            decision_id = decision_log.next_decision_id
            clearance = {
                "schema_version": SCHEMA_VERSION,
                "run_id": run_id,
                "selection_id": selection["selection_id"],
                "created_at": self.now(),
                "selection": selection_ref,
                "clearance_request": request_ref,
                "review_set_id": review_set_id,
                "review_set": review_set_ref,
                "decision_id": decision_id,
                "status": "ADOPTED",
                "attestation": attestation,
                "items": clearance_items,
                "contains_source_identifiers": False,
            }
            self.validators["calibration_clearance"].validate(clearance)
            write_private_json(clearance_path, clearance)
            clearance_ref = artifact_ref(
                self.repository_root,
                clearance_path,
                artifact_id=allocator.next("ART"),
                role="CALIBRATION_CLEARANCE",
                media_type="application/json",
            )
            self._add_output(manifest, clearance_ref)
            manifest["updated_at"] = clearance["created_at"]
            self._refresh_logs(manifest, events, event_path, decision_path)
            self._write_manifest(run_root, manifest)

        matching_decisions = [
            item for item in decision_documents if item["decision_id"] == decision_id
        ]
        evidence_locators = [
            {
                "artifact_id": review_set_ref["artifact_id"],
                "artifact_sha256": review_set_ref["sha256"],
                "source_role": "HUMAN_NOTE",
                "logical_path": PurePosixPath(review_set_ref["path"]).name,
                "locator_type": "FILE",
                "extraction_method": "VISUAL",
                "uncertainty": "NONE",
            },
            {
                "artifact_id": clearance_ref["artifact_id"],
                "artifact_sha256": clearance_ref["sha256"],
                "source_role": "HUMAN_NOTE",
                "logical_path": PurePosixPath(clearance_ref["path"]).name,
                "locator_type": "FILE",
                "extraction_method": "JSON_PARSE",
                "uncertainty": "NONE",
            },
        ]
        if len(matching_decisions) > 1:
            raise ContractError("clearance decision is duplicated")
        if matching_decisions:
            decision = matching_decisions[0]
            if any(
                (
                    decision["decision_maker"]["actor_id"] != actor_id.strip(),
                    decision["rationale"] != rationale.strip(),
                    decision["subject"]
                    != {"subject_type": "RUN", "subject_id": run_id},
                    decision["evidence_locators"] != evidence_locators,
                    set(decision["affected_record_ids"])
                    != {selection["selection_id"], review_set_id, *selected_ids},
                )
            ):
                raise ContractError("existing clearance decision differs from this attestation")
            return {
                "run_id": run_id,
                "selection_id": selection["selection_id"],
                "review_set_id": review_set_id,
                "review_set_sha256": review_set_sha256,
                "decision_id": decision["decision_id"],
                "cleared": len(clearance_items),
                "source_rasters": sum(
                    item["disposition"] == "SOURCE_RASTER_VISUALLY_CLEARED"
                    for item in clearance_items
                ),
                "sanitized_derivative_rasters": sum(
                    item["disposition"]
                    == "SANITIZED_DERIVATIVE_RASTER_VISUALLY_CLEARED"
                    for item in clearance_items
                ),
            }
        else:
            if decision_documents:
                raise ContractError(
                    "an unexpected prior human decision blocks clearance recording"
                )
        decision = decision_log.append(
            decision_id=decision_id,
            actor_id=actor_id.strip(),
            authority="COURSE_INSTRUCTOR",
            decision_type="IDENTITY_CLEARANCE",
            subject_type="RUN",
            subject_id=run_id,
            prior_state="EIGHT_PRODUCTS_PENDING_VISUAL_IDENTITY_CLEARANCE",
            resulting_state="EIGHT_PRODUCTS_VISUALLY_CLEARED_FOR_CALIBRATION",
            rationale=rationale.strip(),
            evidence_locators=evidence_locators,
            affected_record_ids=[
                selection["selection_id"], review_set_id, *sorted(selected_ids)
            ],
        )
        manifest["updated_at"] = decision["made_at"]
        self._refresh_logs(manifest, events, event_path, decision_path)
        self._write_manifest(run_root, manifest)
        return {
            "run_id": run_id,
            "selection_id": selection["selection_id"],
            "review_set_id": review_set_id,
            "review_set_sha256": review_set_sha256,
            "decision_id": decision["decision_id"],
            "cleared": len(clearance_items),
            "source_rasters": sum(
                item["disposition"] == "SOURCE_RASTER_VISUALLY_CLEARED"
                for item in clearance_items
            ),
            "sanitized_derivative_rasters": sum(
                item["disposition"]
                == "SANITIZED_DERIVATIVE_RASTER_VISUALLY_CLEARED"
                for item in clearance_items
            ),
        }

    def _prepare_failed_resume_retry(
        self,
        *,
        manifest: dict[str, Any],
        run_root: Path,
        selected_ids: set[str],
    ) -> None:
        """Verify and forget only retry-owned partial outputs before overwrite."""
        allowed_packet_names = {
            "submitted-solution.pdf",
            "problem-statement.md",
            "solution-key.tex",
            "packet_manifest.json",
        }
        allowed_dossier_names = {
            "dossier_data.json",
            "dossier.md",
            "dossier.render.json",
        }
        for root, allowed_names in (
            (run_root / "packets", allowed_packet_names),
            (run_root / "dossiers", allowed_dossier_names),
        ):
            for child in root.iterdir():
                if child.is_symlink() or not child.is_dir() or child.name not in selected_ids:
                    raise ContractError("failed resume left an unexpected output directory")
                for path in child.iterdir():
                    if (
                        path.is_symlink()
                        or not path.is_file()
                        or path.name not in allowed_names
                    ):
                        raise ContractError("failed resume left an unexpected output file")
        retry_paths = {
            repository_relative(
                self.repository_root,
                run_root / "manifests/review_queue-calibration-v1.json",
            ),
            repository_relative(
                self.repository_root,
                run_root / "reports/review_queue-calibration-v1.md",
            ),
            repository_relative(
                self.repository_root,
                run_root / "reports/review_queue-calibration-v1.render.json",
            ),
        }
        for path_value in retry_paths:
            path = self.repository_root / path_value
            if path.exists() and (path.is_symlink() or not path.is_file()):
                raise ContractError("failed resume left an unsafe queue output")
        packet_prefix = repository_relative(
            self.repository_root, run_root / "packets"
        ) + "/"
        dossier_prefix = repository_relative(
            self.repository_root, run_root / "dossiers"
        ) + "/"
        manifest["outputs"] = [
            reference
            for reference in manifest["outputs"]
            if not (
                reference["path"].startswith(packet_prefix)
                or reference["path"].startswith(dossier_prefix)
                or reference["path"] in retry_paths
            )
        ]
        manifest["validation"] = {"status": "NOT_RUN", "report": None}

    def resume_calibration(self, *, run_id: str | None = None) -> dict[str, Any]:
        with self._mutation_lock():
            self._clear_stage_failure_guard()
            try:
                return self._resume_calibration(run_id=run_id)
            except (Exception, KeyboardInterrupt):
                self._seal_active_stage_failure()
                raise
            finally:
                self._clear_stage_failure_guard()

    def _resume_calibration(self, *, run_id: str | None) -> dict[str, Any]:
        preflight = self.preflight_framework(require_tools=True)
        run_id = self.resolve_run_id(run_id)
        run_root, manifest, events, event_path, decision_path, allocator = self._load_run(
            run_id
        )
        prepare_state = self._stage(manifest, "PREPARE_CALIBRATION")
        retrying_failed = (
            manifest["run_state"] == "FAILED"
            and prepare_state["status"] == "FAILED"
            and prepare_state["reason_code"] == "PREPARE_CALIBRATION_FAILED"
        )
        resuming_blocked = (
            manifest["run_state"] == "BLOCKED"
            and prepare_state["status"] == "BLOCKED"
            and prepare_state["reason_code"] == "IDENTITY_SANITIZATION_REQUIRED"
        )
        if not (resuming_blocked or retrying_failed):
            raise ContractError(
                "resume requires a cleared blocked preparation or retryable failed resume"
            )
        self._assert_frozen_run_compatible(manifest, preflight)

        reference_path = run_root / "manifests/reference_manifest.json"
        reference_bytes = safe_file_bytes(reference_path)
        if sha256_bytes(reference_bytes) != manifest["reference_manifest_sha256"]:
            raise ContractError("frozen reference manifest hash changed")
        reference_manifest = json.loads(reference_bytes)
        self.validators["reference_manifest"].validate(reference_manifest)
        if not self._references_match_frozen_bytes(reference_manifest):
            raise ContractError("one or more frozen reference bytes changed")

        selection_path = run_root / "manifests/calibration_selection.json"
        request_path = run_root / "manifests/calibration_clearance_request.json"
        clearance_path = run_root / "manifests/calibration_clearance.json"
        selection_ref = self._verified_output_for_path(manifest, selection_path)
        request_ref = self._verified_output_for_path(manifest, request_path)
        clearance_ref = self._verified_output_for_path(manifest, clearance_path)
        selection = read_json(selection_path)
        request = read_json(request_path)
        clearance = read_json(clearance_path)
        self.validators["calibration_selection"].validate(selection)
        self.validators["calibration_clearance_request"].validate(request)
        self.validators["calibration_clearance"].validate(clearance)
        review_set_ref = clearance["review_set"]
        review_set_path = self.repository_root / assert_relative_path(
            review_set_ref["path"]
        )
        if self._verified_output_for_path(manifest, review_set_path) != review_set_ref:
            raise ContractError("clearance review-set reference changed")
        review_set = read_json(review_set_path)
        self.validators["calibration_clearance_review_set"].validate(review_set)
        if any(
            (
                selection["run_id"] != run_id,
                request["run_id"] != run_id,
                clearance["run_id"] != run_id,
                request["selection_id"] != selection["selection_id"],
                clearance["selection_id"] != selection["selection_id"],
                request["selection"] != selection_ref,
                clearance["selection"] != selection_ref,
                clearance["clearance_request"] != request_ref,
                clearance["attestation"] != CLEARANCE_ATTESTATION,
                review_set["run_id"] != run_id,
                review_set["selection_id"] != selection["selection_id"],
                review_set["review_set_id"] != clearance["review_set_id"],
                review_set["selection"] != selection_ref,
                review_set["clearance_request"] != request_ref,
                review_set["status"] != "READY_FOR_VISUAL_REVIEW",
            )
        ):
            raise ContractError("clearance artifacts do not match the locked selection")

        selected_by_record = {
            item["submission_record_id"]: item for item in selection["selections"]
        }
        request_by_record = {
            item["submission_record_id"]: item for item in request["items"]
        }
        clearance_by_record = {
            item["submission_record_id"]: item for item in clearance["items"]
        }
        review_by_record = {
            item["submission_record_id"]: item for item in review_set["items"]
        }
        selected_ids = set(selected_by_record)
        if (
            len(selected_ids) != 8
            or set(request_by_record) != selected_ids
            or set(clearance_by_record) != selected_ids
            or set(review_by_record) != selected_ids
        ):
            raise ContractError("clearance artifacts do not cover the exact selection")

        if retrying_failed:
            self._prepare_failed_resume_retry(
                manifest=manifest,
                run_root=run_root,
                selected_ids=selected_ids,
            )

        decision_log, decision_documents = self._human_decision_documents(
            decision_path, run_id
        )
        del decision_log
        matching_decisions = [
            item
            for item in decision_documents
            if item["decision_id"] == clearance["decision_id"]
        ]
        if len(matching_decisions) != 1:
            raise ContractError("clearance decision is missing or duplicated")
        decision = matching_decisions[0]
        if any(
            (
                decision["state"] != "ADOPTED",
                decision["decision_type"] != "IDENTITY_CLEARANCE",
                decision["subject"]
                != {"subject_type": "RUN", "subject_id": run_id},
                set(decision["affected_record_ids"])
                != {
                    selection["selection_id"],
                    review_set["review_set_id"],
                    *selected_ids,
                },
                not any(
                    locator["artifact_id"] == clearance_ref["artifact_id"]
                    and locator["artifact_sha256"] == clearance_ref["sha256"]
                    for locator in decision["evidence_locators"]
                ),
                not any(
                    locator["artifact_id"] == review_set_ref["artifact_id"]
                    and locator["artifact_sha256"] == review_set_ref["sha256"]
                    for locator in decision["evidence_locators"]
                ),
            )
        ):
            raise ContractError("clearance decision does not authorize this exact selection")

        submissions = self._submission_manifests(run_root, run_id)
        identity_path = self.restricted_root / run_id / "identity_map.json"
        self._verified_output_for_path(manifest, identity_path)
        identity_map = self._identity_map(run_id)
        if not self._identity_map_matches_submissions(identity_map, submissions):
            raise ContractError("identity map does not reconcile with submission manifests")
        identity_by_record = {
            entry["submission_record_id"]: entry for entry in identity_map["entries"]
        }
        accepted_materials: dict[
            str, tuple[bytes, dict[str, Any], dict[str, Any]]
        ] = {}
        for record_id in sorted(selected_ids):
            selected = selected_by_record[record_id]
            request_item = request_by_record[record_id]
            review_item = review_by_record[record_id]
            clearance_item = clearance_by_record[record_id]
            submission = submissions.get(record_id)
            identity_entry = identity_by_record.get(record_id)
            if submission is None or identity_entry is None:
                raise ContractError("selected record is absent from frozen intake state")
            if any(
                (
                    request_item["assignment_id"] != selected["assignment_id"],
                    request_item["package_stratum"] != selected["package_stratum"],
                    request_item["source_payload_sha256"]
                    != submission[0]["source_payload_sha256"],
                    request_item["submission_manifest"]
                    != selected["submission_manifest"],
                    review_item["assignment_id"] != selected["assignment_id"],
                    review_item["review_artifact"]["role"]
                    != "CALIBRATION_REVIEW_PDF",
                    clearance_item["assignment_id"] != selected["assignment_id"],
                    clearance_item["review_artifact"]
                    != review_item["review_artifact"],
                    clearance_item["accepted_artifact"]
                    != review_item["review_artifact"],
                    clearance_item["automated_scan_status"]
                    != review_item["automated_scan_status"],
                    clearance_item["automated_scan_codes"]
                    != review_item["automated_scan_codes"],
                    review_item["required_action"]
                    != "VISUAL_CLEARANCE_ALLOWED",
                    clearance_item["automated_scan_status"] == "FAIL",
                )
            ):
                raise ContractError("clearance row does not reconcile with selection")
            if review_item["disposition"] == "SOURCE_RASTER":
                source_solution, _ = self._solution_bytes(
                    submission[0], identity_entry
                )
                if any(
                    (
                        sha256_bytes(source_solution)
                        != request_item["source_solution_sha256"],
                        len(source_solution)
                        != request_item["source_solution_byte_count"],
                        review_item["source_input_sha256"]
                        != request_item["source_solution_sha256"],
                        review_item["source_input_byte_count"]
                        != request_item["source_solution_byte_count"],
                        clearance_item["disposition"]
                        != "SOURCE_RASTER_VISUALLY_CLEARED",
                    )
                ):
                    raise ContractError("source raster provenance does not reconcile")
            elif review_item["disposition"] == "SANITIZED_DERIVATIVE_RASTER":
                if clearance_item["disposition"] != (
                    "SANITIZED_DERIVATIVE_RASTER_VISUALLY_CLEARED"
                ):
                    raise ContractError("derivative raster disposition does not reconcile")
            else:
                raise ContractError("unknown review-set disposition")
            accepted_ref = clearance_item["accepted_artifact"]
            accepted_path = self.repository_root / assert_relative_path(
                accepted_ref["path"]
            )
            if self._verified_output_for_path(manifest, accepted_path) != accepted_ref:
                raise ContractError("accepted clearance artifact reference changed")
            accepted_bytes = safe_file_bytes(
                accepted_path, MAX_RASTER_TOTAL_BYTES
            )
            inert = inspect_inert_raster_pdf(accepted_bytes)
            if any(
                (
                    review_item["page_count"] != inert.page_count,
                    review_item["page_sha256s"] != list(inert.page_sha256s),
                    review_item["pixel_dimensions"]
                    != [list(item) for item in inert.pixel_dimensions],
                )
            ):
                raise ContractError("accepted inert PDF differs from its review-set row")
            accepted_materials[record_id] = (
                accepted_bytes,
                dict(accepted_ref),
                clearance_item,
            )

        queue_ref = self._latest_queue_reference(manifest)
        self._verified_output_for_path(
            manifest, self.repository_root / queue_ref["path"]
        )
        queue = read_json(self.repository_root / queue_ref["path"])
        self.validators["review_queue"].validate(queue)

        reference_materials: dict[
            tuple[str, str], tuple[bytes, Mapping[str, Any]]
        ] = {}
        dossier_template: tuple[bytes, Mapping[str, Any]] | None = None
        queue_template: tuple[bytes, Mapping[str, Any]] | None = None
        for reference in reference_manifest["references"]:
            if reference["role"] in {"PROBLEM_STATEMENT", "SOLUTION_KEY"}:
                key = (reference["assignment_id"], reference["role"])
                if key in reference_materials:
                    raise ContractError("frozen packet reference is duplicated")
                reference_materials[key] = (
                    self._frozen_reference_bytes(reference),
                    reference,
                )
            elif reference["role"] == "TEMPLATE":
                frozen_template = (
                    self._frozen_reference_bytes(reference),
                    reference,
                )
                if reference["path"].endswith("dossier.md.tmpl"):
                    dossier_template = frozen_template
                elif reference["path"].endswith("review_queue.md.tmpl"):
                    queue_template = frozen_template
        expected_reference_keys = {
            (assignment_id, role)
            for assignment_id in ASSIGNMENTS
            for role in ("PROBLEM_STATEMENT", "SOLUTION_KEY")
        }
        if (
            set(reference_materials) != expected_reference_keys
            or dossier_template is None
            or queue_template is None
        ):
            raise ContractError("frozen packet references are incomplete")

        self._arm_stage_failure_guard(
            manifest=manifest,
            events=events,
            run_root=run_root,
            event_path=event_path,
            decision_path=decision_path,
            stage="PREPARE_CALIBRATION",
            code="PREPARE_CALIBRATION_FAILED",
            message="Resumed calibration preparation stopped safely before completion.",
            start_inputs=[clearance_ref],
            resume=True,
        )
        self._resume_stage(
            manifest,
            events,
            "PREPARE_CALIBRATION",
            inputs=[clearance_ref],
            message="Instructor identity clearance recorded for all eight selected products.",
        )

        output_refs: list[dict[str, Any]] = []
        dossier_refs: dict[str, dict[str, Any]] = {}
        for selected in selection["selections"]:
            record_id = selected["submission_record_id"]
            accepted_bytes, accepted_ref, clearance_item = accepted_materials[
                record_id
            ]
            refs, dossier_ref = self._packet_and_dossier(
                run_root=run_root,
                selection=selection,
                selected=selected,
                accepted_solution=accepted_bytes,
                accepted_ref=accepted_ref,
                clearance_ref=clearance_ref,
                review_set_ref=review_set_ref,
                clearance_item=clearance_item,
                decision_id=clearance["decision_id"],
                reference_materials=reference_materials,
                dossier_template=dossier_template,
                allocator=allocator,
            )
            output_refs.extend(refs)
            dossier_refs[record_id] = dossier_ref

        for item in queue["items"]:
            record_id = item["submission_record_id"]
            if record_id in selected_ids:
                item.update(
                    {
                        "action": "PRODUCT_REVIEW",
                        "reasons": [
                            {
                                "code": "CALIBRATION_SELECTED",
                                "severity": "INFO",
                                "message": "Selected deterministically and visually cleared for product calibration.",
                                "finding_ids": [],
                            }
                        ],
                        "calibration_state": "SELECTED",
                        "dossier_data": dossier_refs[record_id],
                        "reviewer_state": "PENDING",
                        "decision_ids": [clearance["decision_id"]],
                    }
                )
            elif item["calibration_state"] == "PENDING_SELECTION":
                item["status_axes"]["human_review"] = "NOT_REQUIRED"
                item.update(
                    {
                        "action": "DEFERRED_NOT_SELECTED",
                        "reasons": [
                            {
                                "code": "CALIBRATION_NOT_SELECTED",
                                "severity": "INFO",
                                "message": "Eligible but not selected for the eight-item calibration set.",
                                "finding_ids": [],
                            }
                        ],
                        "calibration_state": "NOT_SELECTED",
                        "dossier_data": None,
                        "reviewer_state": "NOT_REQUIRED",
                    }
                )
        calibration_queue = self._queue_document(
            run_id=run_id,
            created_at=self.now(),
            reference_manifest_sha256=manifest["reference_manifest_sha256"],
            items=queue["items"],
            allocator=allocator,
        )
        queue_refs, _ = self._render_queue(
            calibration_queue,
            run_root=run_root,
            allocator=allocator,
            version="calibration-v1",
            phase="PREPARE_CALIBRATION",
            frozen_template=queue_template,
        )
        output_refs.extend(queue_refs)
        for reference in output_refs:
            self._add_output(manifest, reference)
        manifest["reconciliation"]["calibration_selected"] = 8
        self._complete_stage(
            manifest,
            events,
            "PREPARE_CALIBRATION",
            outputs=output_refs,
            message="Eight instructor-cleared product calibration packets and dossier shells prepared.",
        )
        self._refresh_logs(manifest, events, event_path, decision_path)
        self._write_manifest(run_root, manifest)
        return {
            "run_id": run_id,
            "selection_id": selection["selection_id"],
            "decision_id": clearance["decision_id"],
            "selected": 8,
            "eligible_not_selected": calibration_queue["counts"]["not_selected"],
            "product_review": calibration_queue["counts"]["product_review"],
        }

    def _validation_artifacts(
        self,
        run_root: Path,
        run_id: str,
        manifest: Mapping[str, Any],
        allocator: IdAllocator,
    ) -> list[tuple[str, Path, str, str]]:
        artifacts: list[tuple[str, Path, str, str]] = []
        known_by_path = {
            reference["path"]: reference for reference in manifest["outputs"]
        }

        def add(path: Path, schema_name: str, artifact_id: str | None = None) -> None:
            repository_path = repository_relative(self.repository_root, path)
            existing = known_by_path.get(repository_path)
            selected_id = artifact_id or (
                existing["artifact_id"] if existing else allocator.next("ART")
            )
            artifacts.append((selected_id, path, schema_name, repository_path))

        add(self.config_path, "config")
        add(run_root / "run_manifest.json", "run_manifest")
        add(run_root / "manifests/reference_manifest.json", "reference_manifest")
        add(
            self.restricted_root / run_id / "identity_map.json",
            "identity_map",
        )
        for path in sorted((run_root / "manifests/submissions").glob("*.json")):
            add(path, "submission_manifest")
        for path in sorted((run_root / "builds").glob("*.json")):
            add(path, "build_report")
        for path in sorted((run_root / "manifests").glob("review_queue-*.json")):
            add(path, "review_queue")
        selection_path = run_root / "manifests/calibration_selection.json"
        if selection_path.exists():
            add(selection_path, "calibration_selection")
        clearance_request_path = (
            run_root / "manifests/calibration_clearance_request.json"
        )
        if clearance_request_path.exists():
            add(clearance_request_path, "calibration_clearance_request")
        for path in sorted(
            (run_root / "manifests").glob(
                "calibration_clearance_review_set-rset-*.json"
            )
        ):
            add(path, "calibration_clearance_review_set")
        clearance_path = run_root / "manifests/calibration_clearance.json"
        if clearance_path.exists():
            add(clearance_path, "calibration_clearance")
        for path in sorted((run_root / "packets").glob("*/packet_manifest.json")):
            add(path, "calibration_packet_manifest")
        for path in sorted((run_root / "dossiers").glob("*/dossier_data.json")):
            add(path, "dossier_data")
        for path in sorted(run_root.glob("reports/*.render.json")):
            add(path, "render_manifest")
        for path in sorted(run_root.glob("reports/validation-*.json")):
            add(path, "validation_report")
        for path in sorted((run_root / "dossiers").glob("*/dossier.render.json")):
            add(path, "render_manifest")
        for path in sorted((run_root / "reviews").glob("*.json")):
            add(path, "review")
        reconciliation_path = run_root / "manifests/calibration_reconciliation.json"
        if reconciliation_path.exists():
            add(reconciliation_path, "calibration_reconciliation")
        return artifacts

    @staticmethod
    def _iter_artifact_refs(value: Any) -> Iterator[dict[str, Any]]:
        if isinstance(value, dict):
            required = {
                "artifact_id",
                "path",
                "sha256",
                "byte_count",
                "media_type",
            }
            if required.issubset(value):
                yield value
            for child in value.values():
                yield from ReviewPipeline._iter_artifact_refs(child)
        elif isinstance(value, list):
            for child in value:
                yield from ReviewPipeline._iter_artifact_refs(child)

    @staticmethod
    def _iter_mappings(value: Any) -> Iterator[dict[str, Any]]:
        if isinstance(value, dict):
            yield value
            for child in value.values():
                yield from ReviewPipeline._iter_mappings(child)
        elif isinstance(value, list):
            for child in value:
                yield from ReviewPipeline._iter_mappings(child)

    @staticmethod
    def _queue_counts(items: Sequence[Mapping[str, Any]]) -> dict[str, int]:
        return {
            "total": len(items),
            "awaiting_selection": sum(
                item["action"] == "AWAIT_CALIBRATION_SELECTION" for item in items
            ),
            "not_selected": sum(
                item["action"] == "DEFERRED_NOT_SELECTED" for item in items
            ),
            "product_review": sum(item["action"] == "PRODUCT_REVIEW" for item in items),
            "human_triage": sum(item["action"] == "HUMAN_TRIAGE" for item in items),
            "hold": sum(item["action"] == "HOLD" for item in items),
            "exclude": sum(item["action"] == "EXCLUDE" for item in items),
            "calibration_selected": sum(
                item["calibration_state"] == "SELECTED" for item in items
            ),
        }

    def build_validation_report(
        self,
        *,
        run_id: str,
        run_root: Path,
        manifest: Mapping[str, Any],
        allocator: IdAllocator,
        tool_dependencies: Sequence[Mapping[str, str]],
    ) -> dict[str, Any]:
        errors: list[dict[str, Any]] = []
        warnings: list[dict[str, Any]] = []
        schema_checks: list[dict[str, Any]] = []
        semantic_checks: list[dict[str, Any]] = []
        privacy_checks: list[dict[str, Any]] = []
        hash_checks: list[dict[str, Any]] = []

        def next_check() -> str:
            return allocator.next("CHK")

        def issue(
            code: str,
            message: str,
            *,
            artifact_id: str | None = None,
            instance_path: str | None = None,
            warning: bool = False,
        ) -> None:
            target = warnings if warning else errors
            target.append(
                {
                    "code": code,
                    "message": message,
                    "artifact_id": artifact_id,
                    "instance_path": instance_path,
                }
            )

        def check(
            target: list[dict[str, Any]],
            code: str,
            passed: bool | None,
            message: str,
            artifact_ids: Sequence[str] = (),
        ) -> None:
            target.append(
                {
                    "check_id": next_check(),
                    "code": code,
                    "status": "SKIP" if passed is None else "PASS" if passed else "FAIL",
                    "message": message,
                    "artifact_ids": list(dict.fromkeys(artifact_ids)),
                }
            )
            if passed is False:
                issue(code, message, artifact_id=artifact_ids[0] if artifact_ids else None)

        documents: dict[str, Any] = {}
        validation_artifacts = self._validation_artifacts(
            run_root, run_id, manifest, allocator
        )
        for artifact_id, path, schema_name, repository_path in validation_artifacts:
            schema = self.schemas[schema_name]
            problems: list[str] = []
            try:
                raw = safe_file_bytes(path)
                if schema_name == "config":
                    document = yaml.safe_load(raw)
                else:
                    document = json.loads(raw)
                    if raw != canonical_json_bytes(document):
                        problems.append("generated JSON is not canonical")
                problems.extend(
                    (
                        f"{error.validator or 'schema'} violation at /"
                        + "/".join(str(part) for part in error.absolute_path)
                    )
                    for error in sorted(
                        self.validators[schema_name].iter_errors(document),
                        key=lambda item: list(item.path),
                    )
                )
                # Semantic validation only consumes schema-valid canonical
                # documents. A parseable but structurally corrupt artifact
                # must produce a FAIL report, never a KeyError in later
                # reconciliation code.
                if not problems:
                    documents[repository_path] = document
            except (OSError, UnicodeDecodeError, ValueError, PipelineError) as exc:
                problems.append(type(exc).__name__)
            status = "PASS" if not problems else "FAIL"
            schema_checks.append(
                {
                    "check_id": next_check(),
                    "schema_id": schema["$id"],
                    "artifact_id": artifact_id,
                    "artifact_path": repository_path,
                    "status": status,
                    "issue_count": len(problems),
                }
            )
            for problem in problems:
                issue(
                    "SCHEMA_OR_SERIALIZATION_INVALID",
                    f"{repository_path}: {problem}",
                    artifact_id=artifact_id,
                    instance_path=repository_path,
                )

        event_path = run_root / self.config["processing"]["run_layout"]["event_log"]
        decision_path = (
            run_root
            / self.config["processing"]["run_layout"]["human_decision_log"]
        )
        event_ref = manifest["event_log"]["artifact"]
        decision_ref = manifest["human_decision_log"]["artifact"]
        event_documents: list[dict[str, Any]] = []
        decision_documents: list[dict[str, Any]] = []
        for path, schema_name, artifact_reference, target in (
            (event_path, "event", event_ref, event_documents),
            (decision_path, "human_decision", decision_ref, decision_documents),
        ):
            problems: list[str] = []
            try:
                raw_lines = safe_file_bytes(path).splitlines()
                for line_number, raw_line in enumerate(raw_lines, 1):
                    document = json.loads(raw_line)
                    line_problems: list[str] = []
                    if raw_line + b"\n" != canonical_json_bytes(document):
                        line_problems.append(f"line {line_number} is not canonical")
                    for validation_error in self.validators[schema_name].iter_errors(document):
                        location = "/".join(
                            str(part) for part in validation_error.absolute_path
                        )
                        line_problems.append(
                            f"line {line_number}: "
                            f"{validation_error.validator or 'schema'} violation at /{location}"
                        )
                    problems.extend(line_problems)
                    if not line_problems:
                        target.append(document)
            except (OSError, ValueError, PipelineError) as exc:
                problems.append(type(exc).__name__)
            schema_checks.append(
                {
                    "check_id": next_check(),
                    "schema_id": self.schemas[schema_name]["$id"],
                    "artifact_id": artifact_reference["artifact_id"],
                    "artifact_path": artifact_reference["path"],
                    "status": "PASS" if not problems else "FAIL",
                    "issue_count": len(problems),
                }
            )
            for problem in problems:
                issue(
                    "JSONL_INVALID",
                    f"{artifact_reference['path']}: {problem}",
                    artifact_id=artifact_reference["artifact_id"],
                    instance_path=artifact_reference["path"],
                )

        reference_path = repository_relative(
            self.repository_root, run_root / "manifests/reference_manifest.json"
        )
        reference_document = documents.get(reference_path)
        reference_ok = isinstance(reference_document, dict)
        if reference_ok:
            for assignment_id in ASSIGNMENTS:
                statements = [
                    item
                    for item in reference_document["references"]
                    if item["role"] == "PROBLEM_STATEMENT"
                    and item.get("assignment_id") == assignment_id
                ]
                keys = [
                    item
                    for item in reference_document["references"]
                    if item["role"] == "SOLUTION_KEY"
                    and item.get("assignment_id") == assignment_id
                ]
                reference_ok = reference_ok and len(statements) == len(keys) == 1
            reference_ok = reference_ok and self._references_match_frozen_bytes(
                reference_document
            )
        check(
            semantic_checks,
            "REFERENCE_SET_COMPLETE",
            reference_ok,
            "Frozen references contain exactly one statement and key for every homework.",
        )
        frozen_hashes_ok = (
            manifest["config_sha256"] == self.config_sha256
            and manifest["schema_set_sha256"] == self.schema_set_sha256()
            and manifest["tool"]["executable_sha256"] == self.executable_sha256
            and manifest["tool"]["dependencies"]
            == [dict(item) for item in tool_dependencies]
        )
        try:
            frozen_hashes_ok = frozen_hashes_ok and (
                sha256_bytes(
                    safe_file_bytes(run_root / "manifests/reference_manifest.json")
                )
                == manifest["reference_manifest_sha256"]
            )
        except PipelineError:
            frozen_hashes_ok = False
        check(
            semantic_checks,
            "FROZEN_FRAMEWORK_HASHES_MATCH",
            frozen_hashes_ok,
            "Configuration, schema set, pipeline, parser toolchain, and reference-manifest hashes match the run freeze.",
        )

        submission_paths = sorted(
            path
            for path in documents
            if "/manifests/submissions/" in path
        )
        queue_paths = sorted(
            path
            for path in documents
            if "/manifests/review_queue-" in path
        )
        try:
            latest_queue_path = self._latest_queue_reference(manifest)["path"]
        except ContractError:
            latest_queue_path = ""
        latest_queue = documents.get(latest_queue_path)
        embedded_ids_ok = True
        record_ids: set[str] = set()
        for path in submission_paths:
            document = documents[path]
            expected = (
                f"{document['assignment_id']}-{document['pseudonym']}-"
                f"V{document['attempt_number']:02d}"
            )
            if document["submission_record_id"] != expected:
                embedded_ids_ok = False
            if document["submission_record_id"] in record_ids:
                embedded_ids_ok = False
            record_ids.add(document["submission_record_id"])
        queue_record_ids = (
            {item["submission_record_id"] for item in latest_queue["items"]}
            if isinstance(latest_queue, dict)
            else set()
        )
        counts_ok = (
            len(submission_paths) == manifest["reconciliation"]["submission_manifests"]
            == manifest["reconciliation"]["source_groups"]
            and isinstance(latest_queue, dict)
            and len(latest_queue["items"]) == manifest["reconciliation"]["queue_items"]
            and latest_queue["counts"] == self._queue_counts(latest_queue["items"])
            and [item["position"] for item in latest_queue["items"]]
            == list(range(1, len(latest_queue["items"]) + 1))
            and queue_record_ids == record_ids
        )
        check(
            semantic_checks,
            "COUNTS_RECONCILE",
            counts_ok,
            "Source groups, manifests, queue rows, positions, and queue counts reconcile.",
        )
        check(
            semantic_checks,
            "RECORD_IDS_CONSISTENT",
            embedded_ids_ok,
            "Submission IDs are unique and agree with assignment, pseudonym, and version fields.",
        )
        payload_digests_ok = True
        for path in submission_paths:
            document = documents[path]
            digest_input = [
                {
                    "logical_path": item["logical_path"],
                    "byte_count": item["byte_count"],
                    "sha256": item["sha256"],
                }
                for item in sorted(
                    document["input_files"], key=lambda item: item["logical_path"]
                )
            ]
            if sha256_bytes(canonical_json_bytes(digest_input)) != document[
                "source_payload_sha256"
            ]:
                payload_digests_ok = False
        check(
            semantic_checks,
            "SOURCE_PAYLOAD_DIGESTS_MATCH",
            payload_digests_ok,
            "Every source-payload digest matches its sanitized file inventory.",
        )

        chronological = True
        previous: dt.datetime | None = None
        seen_event_ids: set[str] = set()
        for expected_sequence, event in enumerate(event_documents, 1):
            try:
                timestamp = parse_utc_timestamp(event["occurred_at"])
            except ContractError:
                chronological = False
                continue
            if (
                event["sequence"] != expected_sequence
                or event["event_id"] != f"EVT-{expected_sequence:06d}"
                or event["run_id"] != run_id
                or event["event_id"] in seen_event_ids
            ):
                chronological = False
            if previous is not None and timestamp < previous:
                chronological = False
            seen_event_ids.add(event["event_id"])
            previous = timestamp
        check(
            semantic_checks,
            "EVENT_SEQUENCE_VALID",
            chronological
            and manifest["event_log"]["entry_count"] == len(event_documents)
            and manifest["event_log"]["last_sequence"] == len(event_documents),
            "Event records are contiguous, chronological, and match the run manifest.",
            [event_ref["artifact_id"]],
        )

        stage_ledger_ok = True
        stage_segments: dict[str, list[dict[str, Any]]] = {
            stage: [] for stage in STAGES
        }
        open_stages: dict[str, dict[str, Any]] = {}
        for event in event_documents:
            stage = event["stage"]
            event_type = event["event_type"]
            if stage not in stage_segments:
                continue
            if event_type in {"STAGE_STARTED", "RESUMED"}:
                if event_type == "RESUMED":
                    prior_segments = stage_segments[stage]
                    expected_from = (
                        prior_segments[-1]["end"]["event_id"]
                        if prior_segments
                        else None
                    )
                    if any(
                        (
                            stage != "PREPARE_CALIBRATION",
                            stage in open_stages,
                            not prior_segments
                            or prior_segments[-1]["status"]
                            not in {"BLOCKED", "FAILED"},
                            not prior_segments
                            or (
                                prior_segments[-1]["status"] == "BLOCKED"
                                and prior_segments[-1]["end"]["reason_code"]
                                != "IDENTITY_SANITIZATION_REQUIRED"
                            ),
                            not prior_segments
                            or (
                                prior_segments[-1]["status"] == "FAILED"
                                and prior_segments[-1]["end"]["reason_code"]
                                != "PREPARE_CALIBRATION_FAILED"
                            ),
                            event.get("parent_event_id") != expected_from,
                            event["payload"].get("from_event_id") != expected_from,
                        )
                    ):
                        stage_ledger_ok = False
                elif stage in open_stages or (
                    stage != "VALIDATE" and stage_segments[stage]
                ):
                    stage_ledger_ok = False
                open_stages[stage] = event
            elif event_type == "STAGE_COMPLETED":
                completed_status = event["payload"]["stage_status"]
                if completed_status == "SKIPPED":
                    if stage in open_stages or stage_segments[stage]:
                        stage_ledger_ok = False
                    start_event = event
                else:
                    start_event = open_stages.pop(stage, None)
                    if start_event is None:
                        stage_ledger_ok = False
                        start_event = event
                stage_segments[stage].append(
                    {
                        "start": start_event,
                        "end": event,
                        "status": completed_status,
                    }
                )
            elif stage not in open_stages:
                # Selection/review/validation records must be bracketed by
                # that stage's lifecycle events.
                stage_ledger_ok = False

        for state in manifest["stages"]:
            stage = state["stage"]
            status = state["status"]
            segments = stage_segments[stage]
            open_event = open_stages.get(stage)
            if stage != "VALIDATE" and len(segments) > 1:
                valid_prepare_resume = stage == "PREPARE_CALIBRATION" and all(
                    (
                        segments[0]["status"] == "BLOCKED",
                        segments[0]["end"]["reason_code"]
                        == "IDENTITY_SANITIZATION_REQUIRED",
                        all(
                            segment["start"]["event_type"] == "RESUMED"
                            for segment in segments[1:]
                        ),
                        all(
                            segment["status"] == "FAILED"
                            and segment["end"]["reason_code"]
                            == "PREPARE_CALIBRATION_FAILED"
                            for segment in segments[1:-1]
                        ),
                        segments[-1]["status"] in {"COMPLETE", "FAILED"},
                    )
                )
                if not valid_prepare_resume:
                    stage_ledger_ok = False
            if stage in {"PRODUCT_REVIEW", "RECONCILIATION"} and (
                status != "NOT_STARTED" or segments or open_event is not None
            ):
                # No command implements these stages in this pilot revision.
                stage_ledger_ok = False
            if status == "NOT_STARTED":
                if open_event is not None or (stage != "VALIDATE" and segments):
                    stage_ledger_ok = False
                if stage == "VALIDATE" and segments:
                    latest_validation_end = segments[-1]["end"]["sequence"]
                    invalidated_by_prepare = any(
                        segment["status"] == "COMPLETE"
                        and segment["end"]["sequence"] > latest_validation_end
                        for segment in stage_segments["PREPARE_CALIBRATION"]
                    )
                    if not invalidated_by_prepare:
                        stage_ledger_ok = False
                continue
            if status == "RUNNING":
                if open_event is None:
                    stage_ledger_ok = False
                    continue
                if any(
                    (
                        state["event_sequence_start"] != open_event["sequence"],
                        state["event_sequence_end"] is not None,
                        state["started_at"] != open_event["occurred_at"],
                        state["completed_at"] is not None,
                        state["reason_code"] is not None,
                    )
                ):
                    stage_ledger_ok = False
                continue
            if open_event is not None or not segments:
                stage_ledger_ok = False
                continue
            latest = segments[-1]
            if latest["status"] != status:
                stage_ledger_ok = False
            skipped = status == "SKIPPED"
            expected_reason = (
                latest["end"]["reason_code"]
                if status in {"SKIPPED", "BLOCKED", "FAILED"}
                else None
            )
            if any(
                (
                    state["event_sequence_start"]
                    != latest["start"]["sequence"],
                    state["event_sequence_end"] != latest["end"]["sequence"],
                    state["started_at"]
                    != (None if skipped else latest["start"]["occurred_at"]),
                    state["completed_at"] != latest["end"]["occurred_at"],
                    state["reason_code"] != expected_reason,
                )
            ):
                stage_ledger_ok = False

        def first_stage_sequence(stage: str) -> int | None:
            candidates = [
                segment["start"]["sequence"] for segment in stage_segments[stage]
            ]
            if stage in open_stages:
                candidates.append(open_stages[stage]["sequence"])
            return min(candidates) if candidates else None

        reference_completions = stage_segments["REFERENCE_FREEZE"]
        intake_completions = stage_segments["INTAKE"]
        reference_end = (
            reference_completions[-1]["end"]["sequence"]
            if reference_completions
            and reference_completions[-1]["status"] == "COMPLETE"
            else None
        )
        intake_end = (
            intake_completions[-1]["end"]["sequence"]
            if intake_completions
            and intake_completions[-1]["status"] == "COMPLETE"
            else None
        )
        intake_start = first_stage_sequence("INTAKE")
        if intake_start is not None and (
            reference_end is None or reference_end >= intake_start
        ):
            stage_ledger_ok = False
        for dependent_stage in ("PREPARE_CALIBRATION", "VALIDATE"):
            dependent_start = first_stage_sequence(dependent_stage)
            if dependent_start is not None and (
                intake_end is None or intake_end >= dependent_start
            ):
                stage_ledger_ok = False
        validation_stage_state = self._stage(dict(manifest), "VALIDATE")["status"]
        if validation_stage_state == "COMPLETE":
            if (
                manifest["validation"]["status"] != "PASS"
                or not isinstance(manifest["validation"]["report"], dict)
            ):
                stage_ledger_ok = False
        elif validation_stage_state == "NOT_STARTED":
            if manifest["validation"] != {"status": "NOT_RUN", "report": None}:
                stage_ledger_ok = False
        check(
            semantic_checks,
            "STAGE_EVENT_LEDGER_VALID",
            stage_ledger_ok,
            "Stage state, lifecycle events, pointers, timestamps, and supported ordering agree.",
            [event_ref["artifact_id"]],
        )

        validation_state_ok = True
        validation_state = manifest["validation"]
        if validation_stage_state == "NOT_STARTED":
            validation_state_ok = validation_state == {
                "status": "NOT_RUN",
                "report": None,
            }
        elif validation_stage_state == "COMPLETE":
            report_reference = validation_state.get("report")
            validation_segments = stage_segments["VALIDATE"]
            if not isinstance(report_reference, dict) or not validation_segments:
                validation_state_ok = False
            else:
                latest_segment = validation_segments[-1]
                report_document = documents.get(report_reference.get("path", ""))
                recorded_events = [
                    event
                    for event in event_documents
                    if latest_segment["start"]["sequence"]
                    <= event["sequence"]
                    <= latest_segment["end"]["sequence"]
                    and event["event_type"] == "VALIDATION_RECORDED"
                ]
                indexed_reference = self._output_for_path(
                    manifest, report_reference.get("path", "")
                )
                validation_state_ok = bool(
                    validation_state.get("status") == "PASS"
                    and isinstance(report_document, dict)
                    and report_reference.get("role") == "VALIDATION_REPORT"
                    and report_document.get("overall_status") == "PASS"
                    and isinstance(
                        report_document.get("validation_report_id"), str
                    )
                    and indexed_reference == report_reference
                    and len(recorded_events) == 1
                    and recorded_events[0]["subject"]["subject_id"]
                    == report_document["validation_report_id"]
                    and recorded_events[0]["payload"]["validation_report_id"]
                    == report_document["validation_report_id"]
                    and report_reference in recorded_events[0]["outputs"]
                )
        else:
            # build_validation_report is called only before a new validation
            # attempt; blocked/failed/running validation stages are not
            # resumable through this command.
            validation_state_ok = False
        check(
            semantic_checks,
            "VALIDATION_STATE_RECONCILES",
            validation_state_ok,
            "Validation status, report reference, stage segment, and recorded event agree.",
            [event_ref["artifact_id"]],
        )

        decision_sequence_ok = True
        previous_decision_time: dt.datetime | None = None
        seen_decisions: set[str] = set()
        for index, decision in enumerate(decision_documents, 1):
            try:
                decision_time = parse_utc_timestamp(decision["made_at"])
            except ContractError:
                decision_sequence_ok = False
                continue
            if (
                decision["sequence"] != index
                or decision["run_id"] != run_id
                or decision["decision_id"] in seen_decisions
                or (
                    previous_decision_time is not None
                    and decision_time < previous_decision_time
                )
            ):
                decision_sequence_ok = False
            supersedes = decision.get("supersedes_decision_id")
            if supersedes is not None and supersedes not in seen_decisions:
                decision_sequence_ok = False
            seen_decisions.add(decision["decision_id"])
            previous_decision_time = decision_time
        check(
            semantic_checks,
            "DECISION_SEQUENCE_VALID",
            decision_sequence_ok
            and manifest["human_decision_log"]["entry_count"]
            == len(decision_documents)
            and manifest["human_decision_log"]["last_sequence"]
            == len(decision_documents),
            "Human decisions are append-only and contiguous.",
            [decision_ref["artifact_id"]],
        )

        build_paths = sorted(path for path in documents if "/builds/" in path)
        no_execution = all(
            not documents[path]["execution_performed"] for path in build_paths
        )
        build_records_ok = (
            len(build_paths) == len(record_ids)
            and {
                documents[path]["submission_record_id"] for path in build_paths
            }
            == record_ids
        )
        check(
            semantic_checks,
            "BUILD_REPORTS_RECONCILE",
            build_records_ok,
            "Exactly one build/nonexecution report exists for every submission record.",
        )
        check(
            semantic_checks,
            "STUDENT_CODE_NOT_EXECUTED",
            no_execution,
            "All build reports record nonexecution while no sandbox is approved.",
        )

        selection_path = repository_relative(
            self.repository_root, run_root / "manifests/calibration_selection.json"
        )
        selection = documents.get(selection_path)
        prepare_complete = self._stage(dict(manifest), "PREPARE_CALIBRATION")[
            "status"
        ] == "COMPLETE"
        if selection is None:
            selection_ok: bool | None = None if not prepare_complete else False
        else:
            submissions_by_id = {
                documents[path]["submission_record_id"]: (documents[path], path)
                for path in submission_paths
            }
            eligible_snapshot = sorted(
                (
                    {
                        "assignment_id": document["assignment_id"],
                        "package_stratum": document["calibration_stratum"],
                        "submission_record_id": record_id,
                        "source_payload_sha256": document["source_payload_sha256"],
                    }
                    for record_id, (document, _) in submissions_by_id.items()
                    if document["calibration_stratum"] in CALIBRATION_STRATA
                ),
                key=lambda item: (
                    item["assignment_id"],
                    item["package_stratum"],
                    item["submission_record_id"],
                ),
            )
            slots = {
                (item["assignment_id"], item["package_stratum"])
                for item in selection["selections"]
            }
            expected_slots = {
                (assignment, stratum)
                for assignment in ASSIGNMENTS
                for stratum in CALIBRATION_STRATA
            }
            rows_ok = True
            for item in selection["selections"]:
                record_id = item["submission_record_id"]
                source = submissions_by_id.get(record_id)
                if source is None:
                    rows_ok = False
                    continue
                source_document, source_path = source
                candidates = [
                    candidate
                    for candidate in eligible_snapshot
                    if candidate["assignment_id"] == item["assignment_id"]
                    and candidate["package_stratum"] == item["package_stratum"]
                ]
                ranked = sorted(
                    (
                        selection_rank_digest(
                            selection["seed"],
                            item["assignment_id"],
                            item["package_stratum"],
                            candidate["submission_record_id"],
                        ),
                        candidate["submission_record_id"],
                    )
                    for candidate in candidates
                )
                expected_reference = self._output_for_path(manifest, source_path)
                rows_ok = rows_ok and bool(ranked) and all(
                    (
                        item["assignment_id"] == source_document["assignment_id"],
                        item["package_stratum"]
                        == source_document["calibration_stratum"],
                        item["pseudonym"] == source_document["pseudonym"],
                        item["rank"] == 1,
                        item["eligible_count"] == len(ranked),
                        item["rank_digest"] == ranked[0][0],
                        record_id == ranked[0][1],
                        expected_reference is not None,
                        item["submission_manifest"] == expected_reference,
                    )
                )
            selection_ok = (
                selection["run_id"] == run_id
                and selection["configuration_id"] == self.configuration_id
                and selection["config_sha256"] == manifest["config_sha256"]
                and selection["reference_manifest_sha256"]
                == manifest["reference_manifest_sha256"]
                and selection["seed"] == manifest["sample_seed"]
                and selection["eligibility_snapshot_sha256"]
                == sha256_bytes(canonical_json_bytes(eligible_snapshot))
                and len(selection["selections"]) == 8
                and len({item["submission_record_id"] for item in selection["selections"]})
                == 8
                and slots == expected_slots
                and rows_ok
                and any(
                    event["event_id"] == selection["lock_event_id"]
                    and event["event_type"] == "SELECTION_LOCKED"
                    and event["subject"]["subject_id"] == selection["selection_id"]
                    and event["outcome"] == "RECORDED"
                    for event in event_documents
                )
            )
        check(
            semantic_checks,
            "CALIBRATION_SELECTION_VALID",
            selection_ok,
            "Calibration is absent before preparation or locked as eight distinct assignment/stratum slots.",
        )

        clearance_request_path = repository_relative(
            self.repository_root,
            run_root / "manifests/calibration_clearance_request.json",
        )
        clearance_path = repository_relative(
            self.repository_root,
            run_root / "manifests/calibration_clearance.json",
        )
        clearance_request = documents.get(clearance_request_path)
        clearance = documents.get(clearance_path)
        clearance_by_id: dict[str, dict[str, Any]] = {}
        clearance_ok: bool | None
        if not prepare_complete:
            clearance_ok = None
        elif not all(
            isinstance(item, dict)
            for item in (selection, clearance_request, clearance)
        ):
            clearance_ok = False
        else:
            selection_reference = self._output_for_path(manifest, selection_path)
            request_reference = self._output_for_path(
                manifest, clearance_request_path
            )
            review_set_reference = clearance.get("review_set")
            review_set = (
                documents.get(review_set_reference["path"])
                if isinstance(review_set_reference, dict)
                else None
            )
            selected_ids_for_clearance = {
                item["submission_record_id"] for item in selection["selections"]
            }
            selected_by_id = {
                item["submission_record_id"]: item
                for item in selection["selections"]
            }
            submission_by_id = {
                document["submission_record_id"]: document
                for path, document in documents.items()
                if "/manifests/submissions/" in path
                and isinstance(document, dict)
                and "submission_record_id" in document
            }
            request_by_id = {
                item["submission_record_id"]: item
                for item in clearance_request["items"]
            }
            clearance_by_id = {
                item["submission_record_id"]: item
                for item in clearance["items"]
            }
            review_by_id = (
                {
                    item["submission_record_id"]: item
                    for item in review_set["items"]
                }
                if isinstance(review_set, dict)
                else {}
            )
            matching_decisions = [
                item
                for item in decision_documents
                if item["decision_id"] == clearance["decision_id"]
            ]
            clearance_ok = all(
                (
                    selection_reference is not None,
                    request_reference is not None,
                    clearance_request["run_id"] == run_id,
                    clearance["run_id"] == run_id,
                    clearance_request["selection_id"]
                    == selection["selection_id"],
                    clearance["selection_id"] == selection["selection_id"],
                    clearance_request["selection"] == selection_reference,
                    clearance["selection"] == selection_reference,
                    clearance["clearance_request"] == request_reference,
                    isinstance(review_set, dict),
                    self._output_for_path(
                        manifest,
                        review_set_reference["path"]
                        if isinstance(review_set_reference, dict)
                        else "",
                    )
                    == review_set_reference,
                    isinstance(review_set, dict)
                    and review_set["run_id"] == run_id,
                    isinstance(review_set, dict)
                    and review_set["selection_id"] == selection["selection_id"],
                    isinstance(review_set, dict)
                    and review_set["review_set_id"] == clearance["review_set_id"],
                    isinstance(review_set, dict)
                    and review_set["selection"] == selection_reference,
                    isinstance(review_set, dict)
                    and review_set["clearance_request"] == request_reference,
                    isinstance(review_set, dict)
                    and review_set["status"] == "READY_FOR_VISUAL_REVIEW",
                    isinstance(review_set, dict)
                    and review_set["normalization"]["profile"]
                    == INERT_RASTER_PROFILE,
                    clearance["attestation"] == CLEARANCE_ATTESTATION,
                    set(request_by_id) == selected_ids_for_clearance,
                    set(clearance_by_id) == selected_ids_for_clearance,
                    set(review_by_id) == selected_ids_for_clearance,
                    len(matching_decisions) == 1,
                )
            )
            if len(matching_decisions) == 1:
                clearance_decision = matching_decisions[0]
                clearance_ok = clearance_ok and all(
                    (
                        clearance_decision["state"] == "ADOPTED",
                        clearance_decision["decision_type"]
                        == "IDENTITY_CLEARANCE",
                        clearance_decision["subject"]
                        == {"subject_type": "RUN", "subject_id": run_id},
                        set(clearance_decision["affected_record_ids"])
                        == {
                            selection["selection_id"],
                            clearance["review_set_id"],
                            *selected_ids_for_clearance,
                        },
                        any(
                            locator["artifact_id"]
                            == review_set_reference["artifact_id"]
                            and locator["artifact_sha256"]
                            == review_set_reference["sha256"]
                            for locator in clearance_decision[
                                "evidence_locators"
                            ]
                        ),
                        any(
                            locator["artifact_id"]
                            == self._output_for_path(
                                manifest, clearance_path
                            )["artifact_id"]
                            and locator["artifact_sha256"]
                            == self._output_for_path(
                                manifest, clearance_path
                            )["sha256"]
                            for locator in clearance_decision[
                                "evidence_locators"
                            ]
                        )
                        if self._output_for_path(manifest, clearance_path)
                        is not None
                        else False,
                    )
                )
            for record_id in selected_ids_for_clearance:
                selected_item = selected_by_id.get(record_id)
                submission_item = submission_by_id.get(record_id)
                request_item = request_by_id.get(record_id)
                review_item = review_by_id.get(record_id)
                clearance_item = clearance_by_id.get(record_id)
                if any(
                    item is None
                    for item in (
                        selected_item,
                        submission_item,
                        request_item,
                        review_item,
                        clearance_item,
                    )
                ):
                    clearance_ok = False
                    continue
                assert selected_item is not None
                assert submission_item is not None
                assert request_item is not None
                assert review_item is not None
                assert clearance_item is not None
                review_ref = review_item["review_artifact"]
                accepted_ref = clearance_item["accepted_artifact"]
                review_output = self._output_for_path(
                    manifest, review_ref["path"]
                )
                accepted_output = self._output_for_path(
                    manifest, accepted_ref["path"]
                )
                if any(
                    (
                        request_item["assignment_id"]
                        != selected_item["assignment_id"],
                        request_item["package_stratum"]
                        != selected_item["package_stratum"],
                        request_item["source_payload_sha256"]
                        != submission_item["source_payload_sha256"],
                        request_item["submission_manifest"]
                        != selected_item["submission_manifest"],
                        review_item["assignment_id"]
                        != selected_item["assignment_id"],
                        review_ref["role"] != "CALIBRATION_REVIEW_PDF",
                        review_output != review_ref,
                        accepted_output != accepted_ref,
                        clearance_item["review_artifact"] != review_ref,
                        accepted_ref != review_ref,
                        review_item["required_action"]
                        != "VISUAL_CLEARANCE_ALLOWED",
                        clearance_item["automated_scan_status"] == "FAIL",
                        clearance_item["automated_scan_status"]
                        != review_item["automated_scan_status"],
                        clearance_item["automated_scan_codes"]
                        != review_item["automated_scan_codes"],
                        clearance_item["assignment_id"]
                        != request_item["assignment_id"],
                        review_item["disposition"] == "SOURCE_RASTER"
                        and clearance_item["disposition"]
                        != "SOURCE_RASTER_VISUALLY_CLEARED",
                        review_item["disposition"]
                        == "SANITIZED_DERIVATIVE_RASTER"
                        and clearance_item["disposition"]
                        != "SANITIZED_DERIVATIVE_RASTER_VISUALLY_CLEARED",
                    )
                ):
                    clearance_ok = False
                    continue
                try:
                    inert = inspect_inert_raster_pdf(
                        safe_file_bytes(
                            self.repository_root
                            / assert_relative_path(review_ref["path"]),
                            MAX_RASTER_TOTAL_BYTES,
                        )
                    )
                except (OSError, PipelineError, ValueError):
                    clearance_ok = False
                    continue
                if any(
                    (
                        review_item["page_count"] != inert.page_count,
                        review_item["page_sha256s"]
                        != list(inert.page_sha256s),
                        review_item["pixel_dimensions"]
                        != [list(item) for item in inert.pixel_dimensions],
                        review_item["disposition"] == "SOURCE_RASTER"
                        and (
                            review_item["source_input_sha256"]
                            != request_item["source_solution_sha256"]
                            or review_item["source_input_byte_count"]
                            != request_item["source_solution_byte_count"]
                        ),
                    )
                ):
                    clearance_ok = False
        check(
            semantic_checks,
            "CALIBRATION_CLEARANCE_VALID",
            clearance_ok,
            "Completed calibration uses one adopted, hash-bound instructor clearance covering the exact selection.",
        )

        calibration_products_ok: bool | None
        if not prepare_complete:
            calibration_products_ok = None
        elif not isinstance(selection, dict) or not isinstance(latest_queue, dict):
            calibration_products_ok = False
        else:
            selected_ids = {
                item["submission_record_id"] for item in selection["selections"]
            }
            packet_documents = {
                document["submission_record_id"]: document
                for path, document in documents.items()
                if "/packets/" in path
                and path.endswith("/packet_manifest.json")
                and isinstance(document, dict)
            }
            dossier_documents = {
                document["submission_record_id"]: document
                for path, document in documents.items()
                if "/dossiers/" in path
                and path.endswith("/dossier_data.json")
                and isinstance(document, dict)
            }
            selected_queue_ids = {
                item["submission_record_id"]
                for item in latest_queue["items"]
                if item["calibration_state"] == "SELECTED"
                and item["action"] == "PRODUCT_REVIEW"
                and item["dossier_data"] is not None
                and isinstance(clearance, dict)
                and item["decision_ids"] == [clearance["decision_id"]]
            }
            calibration_products_ok = (
                set(packet_documents) == selected_ids
                and set(dossier_documents) == selected_ids
                and selected_queue_ids == selected_ids
            )
            frozen_packet_references = {
                (item.get("assignment_id"), item["role"]): item
                for item in reference_document["references"]
                if item["role"] in {"PROBLEM_STATEMENT", "SOLUTION_KEY"}
            }
            for record_id in selected_ids:
                packet = packet_documents.get(record_id)
                dossier = dossier_documents.get(record_id)
                selected = next(
                    item
                    for item in selection["selections"]
                    if item["submission_record_id"] == record_id
                )
                if packet is None or dossier is None:
                    calibration_products_ok = False
                    continue
                clearance_item = clearance_by_id.get(record_id)
                if clearance_item is None or not isinstance(clearance, dict):
                    calibration_products_ok = False
                    continue
                roles = {item["source_role"] for item in packet["materials"]}
                submitted_material = next(
                    (
                        item
                        for item in packet["materials"]
                        if item["source_role"] == "SUBMITTED_SOLUTION"
                    ),
                    None,
                )
                statement_material = next(
                    (
                        item
                        for item in packet["materials"]
                        if item["source_role"] == "PROBLEM_STATEMENT"
                    ),
                    None,
                )
                key_material = next(
                    (
                        item
                        for item in packet["materials"]
                        if item["source_role"] == "SOLUTION_KEY"
                    ),
                    None,
                )
                frozen_statement = frozen_packet_references.get(
                    (selected["assignment_id"], "PROBLEM_STATEMENT")
                )
                frozen_key = frozen_packet_references.get(
                    (selected["assignment_id"], "SOLUTION_KEY")
                )
                clearance_reference = self._output_for_path(
                    manifest, clearance_path
                )
                packet_root = run_root / "packets" / record_id
                dossier_root = run_root / "dossiers" / record_id
                actual_packet_names = {
                    path.name for path in packet_root.iterdir()
                }
                actual_dossier_names = {
                    path.name for path in dossier_root.iterdir()
                }
                if any(
                    (
                        packet["selection_id"] != selection["selection_id"],
                        dossier["selection_id"] != selection["selection_id"],
                        packet["assignment_id"] != selected["assignment_id"],
                        dossier["assignment_id"] != selected["assignment_id"],
                        packet["pseudonym"] != selected["pseudonym"],
                        dossier["pseudonym"] != selected["pseudonym"],
                        submitted_material is None,
                        statement_material is None,
                        key_material is None,
                        frozen_statement is None,
                        frozen_key is None,
                        clearance_reference is None,
                        packet["sanitization"]["clearance_artifact"]
                        != clearance_reference,
                        packet["sanitization"]["review_set_artifact"]
                        != clearance["review_set"],
                        packet["sanitization"]["decision_id"]
                        != clearance["decision_id"],
                        packet["sanitization"]["disposition"]
                        != clearance_item["disposition"],
                        packet["sanitization"]["automated_scan_status"]
                        != clearance_item["automated_scan_status"],
                        packet["sanitization"]["automated_scan_codes"]
                        != clearance_item["automated_scan_codes"],
                        submitted_material is not None
                        and (
                            submitted_material["source_artifact"]["artifact_id"]
                            != clearance_item["accepted_artifact"]["artifact_id"]
                            or submitted_material["source_artifact"]["sha256"]
                            != clearance_item["accepted_artifact"]["sha256"]
                            or submitted_material["source_artifact"]["byte_count"]
                            != clearance_item["accepted_artifact"]["byte_count"]
                            or submitted_material["packet_artifact"]["sha256"]
                            != clearance_item["accepted_artifact"]["sha256"]
                            or submitted_material["packet_artifact"]["byte_count"]
                            != clearance_item["accepted_artifact"]["byte_count"]
                        ),
                        statement_material is not None
                        and frozen_statement is not None
                        and (
                            statement_material["source_artifact"]["sha256"]
                            != frozen_statement["sha256"]
                            or statement_material["source_artifact"]["byte_count"]
                            != frozen_statement["byte_count"]
                            or statement_material["packet_artifact"]["sha256"]
                            != frozen_statement["sha256"]
                            or statement_material["packet_artifact"]["byte_count"]
                            != frozen_statement["byte_count"]
                        ),
                        key_material is not None
                        and frozen_key is not None
                        and (
                            key_material["source_artifact"]["sha256"]
                            != frozen_key["sha256"]
                            or key_material["source_artifact"]["byte_count"]
                            != frozen_key["byte_count"]
                            or key_material["packet_artifact"]["sha256"]
                            != frozen_key["sha256"]
                            or key_material["packet_artifact"]["byte_count"]
                            != frozen_key["byte_count"]
                        ),
                        roles
                        != {
                            "SUBMITTED_SOLUTION",
                            "PROBLEM_STATEMENT",
                            "SOLUTION_KEY",
                        },
                        actual_packet_names
                        != {
                            "submitted-solution.pdf",
                            "problem-statement.md",
                            "solution-key.tex",
                            "packet_manifest.json",
                        },
                        actual_dossier_names
                        != {
                            "dossier_data.json",
                            "dossier.md",
                            "dossier.render.json",
                        },
                    )
                ):
                    calibration_products_ok = False
        check(
            semantic_checks,
            "CALIBRATION_PRODUCTS_RECONCILE",
            calibration_products_ok,
            "Completed calibration packets, dossiers, and selected queue rows reconcile exactly.",
        )

        feedback_released = any(
            isinstance(document, dict)
            and (
                document.get("student_facing") is True
                or document.get("release", {}).get("state")
                not in {None, "NOT_RELEASED", "NOT_AUTHORIZED"}
            )
            for document in documents.values()
        )
        check(
            semantic_checks,
            "FEEDBACK_NOT_RELEASED",
            not feedback_released,
            "No generated artifact is student-facing or released.",
        )

        ref_consistency: dict[str, tuple[str, int, str, str]] = {}
        reference_hashes_ok = True
        checked_ref_ids: list[str] = []
        for document in list(documents.values()) + event_documents + decision_documents:
            for reference in self._iter_artifact_refs(document):
                artifact_id = reference["artifact_id"]
                checked_ref_ids.append(artifact_id)
                signature = (
                    reference["sha256"],
                    reference["byte_count"],
                    reference["media_type"],
                    reference["path"],
                )
                if artifact_id in ref_consistency and ref_consistency[artifact_id] != signature:
                    reference_hashes_ok = False
                ref_consistency.setdefault(artifact_id, signature)
                try:
                    target = self.repository_root / assert_relative_path(reference["path"])
                    target_relative = target.resolve(strict=True).relative_to(
                        self.repository_root
                    )
                    del target_relative
                    if target.is_symlink() or not target.is_file():
                        raise UnsafeInputError("artifact target is not a regular file")
                    data = safe_file_bytes(target)
                    if (
                        sha256_bytes(data) != reference["sha256"]
                        or len(data) != reference["byte_count"]
                    ):
                        reference_hashes_ok = False
                except (OSError, ValueError, PipelineError):
                    reference_hashes_ok = False
        check(
            hash_checks,
            "ARTIFACT_HASHES_RESOLVE",
            reference_hashes_ok,
            "Artifact references resolve beneath the repository and match exact bytes.",
            checked_ref_ids,
        )

        artifact_hashes: dict[str, str] = {}
        evidence_locators_ok = True
        validation_values: list[Any] = (
            list(documents.values()) + event_documents + decision_documents
        )
        for document in validation_values:
            for mapping in self._iter_mappings(document):
                if {
                    "artifact_id",
                    "sha256",
                    "byte_count",
                    "media_type",
                } <= mapping.keys():
                    artifact_id = mapping["artifact_id"]
                    digest = mapping["sha256"]
                    prior_digest = artifact_hashes.setdefault(artifact_id, digest)
                    if prior_digest != digest:
                        evidence_locators_ok = False
        for document in validation_values:
            for mapping in self._iter_mappings(document):
                if {"artifact_id", "artifact_sha256"} <= mapping.keys():
                    if artifact_hashes.get(mapping["artifact_id"]) != mapping[
                        "artifact_sha256"
                    ]:
                        evidence_locators_ok = False
                if {"container_artifact_id", "archive_member"} <= mapping.keys():
                    if mapping["container_artifact_id"] not in artifact_hashes:
                        evidence_locators_ok = False
        check(
            hash_checks,
            "EVIDENCE_LOCATORS_RESOLVE",
            evidence_locators_ok,
            "Evidence locators and sanitized archive-member references resolve to one immutable artifact hash.",
            sorted(artifact_hashes),
        )

        source_hashes_ok = True
        identity_path = repository_relative(
            self.repository_root, self.restricted_root / run_id / "identity_map.json"
        )
        identity_document = documents.get(identity_path)
        if not isinstance(identity_document, dict):
            source_hashes_ok = False
            identity_entries: list[dict[str, Any]] = []
        else:
            identity_entries = identity_document["entries"]
            for entry in identity_entries:
                for source in entry["original_files"]:
                    try:
                        data = safe_file_bytes(
                            self.repository_root
                            / assert_relative_path(source["source_path"])
                        )
                        if (
                            sha256_bytes(data) != source["sha256"]
                            or len(data) != source["byte_count"]
                        ):
                            source_hashes_ok = False
                    except (OSError, PipelineError):
                        source_hashes_ok = False
        check(
            hash_checks,
            "SOURCE_BYTES_UNCHANGED",
            source_hashes_ok,
            "Restricted source hashes still match preserved input bytes.",
        )
        validation_submissions = {
            documents[path]["submission_record_id"]: (documents[path], Path(path))
            for path in submission_paths
        }
        identity_one_to_one = isinstance(identity_document, dict) and self._identity_map_matches_submissions(
            identity_document, validation_submissions
        )
        check(
            privacy_checks,
            "IDENTITY_MAP_ONE_TO_ONE",
            identity_one_to_one,
            "Restricted identity entries map one source group per submission and one pseudonym per person.",
        )

        modes_ok = True
        for path in [
            self.runs_root,
            self.restricted_root,
            run_root,
            self.restricted_root / run_id,
        ]:
            if not path.is_dir() or stat.S_IMODE(path.stat().st_mode) != PRIVATE_DIRECTORY_MODE:
                modes_ok = False
        for path in run_root.rglob("*"):
            if path.is_symlink():
                modes_ok = False
            elif path.is_dir() and stat.S_IMODE(path.stat().st_mode) != PRIVATE_DIRECTORY_MODE:
                modes_ok = False
            elif path.is_file() and stat.S_IMODE(path.stat().st_mode) != PRIVATE_FILE_MODE:
                modes_ok = False
        restricted_run = self.restricted_root / run_id
        for path in restricted_run.rglob("*"):
            if path.is_symlink():
                modes_ok = False
            elif path.is_dir() and stat.S_IMODE(path.stat().st_mode) != PRIVATE_DIRECTORY_MODE:
                modes_ok = False
            elif path.is_file() and stat.S_IMODE(path.stat().st_mode) != PRIVATE_FILE_MODE:
                modes_ok = False
        check(
            privacy_checks,
            "PRIVATE_MODES_ENFORCED",
            modes_ok,
            "Generated private directories are 0700 and files are 0600 with no symlinks.",
        )

        identity_tokens: set[str] = set()
        numeric_tokens: set[str] = set()
        for entry in identity_entries:
            for subject in entry["subjects"]:
                display = subject.get("display_name")
                if display:
                    identity_tokens.add(
                        unicodedata.normalize("NFC", display).casefold()
                    )
                user_id = subject.get("lms_user_id")
                if user_id:
                    numeric_tokens.add(user_id)
            for source in entry["original_files"]:
                basename = PurePosixPath(source["source_path"]).name
                if len(basename) >= 10:
                    identity_tokens.add(basename.casefold())
        identifiers_absent = True
        for path in run_root.rglob("*"):
            if not path.is_file() or path.is_symlink():
                continue
            if path.suffix.lower() not in {".json", ".jsonl", ".md", ".txt", ".tex"}:
                continue
            text = normalized_casefold(
                safe_file_bytes(path).decode("utf-8", errors="ignore")
            )
            if any(identity_token_present(text, token) for token in identity_tokens):
                identifiers_absent = False
            if any(
                re.search(rf"(?<![0-9]){re.escape(token)}(?![0-9])", text)
                for token in numeric_tokens
            ):
                identifiers_absent = False
        for path in sorted((run_root / "packets").glob("*/submitted-solution.pdf")):
            try:
                scan_status, _ = self._identity_scan(
                    safe_file_bytes(path),
                    artifact_id=allocator.next("ART"),
                    identities=identity_entries,
                    private_tmp=run_root / "tmp",
                )
            except PipelineError:
                scan_status = "FAIL"
            if scan_status == "FAIL":
                identifiers_absent = False
        check(
            privacy_checks,
            "SOURCE_IDENTIFIERS_ABSENT",
            identifiers_absent,
            "Known source names, LMS IDs, active PDF content, and original basenames are absent outside restricted state; completed packets are bound to human clearance.",
        )

        indexed_paths = {reference["path"] for reference in manifest["outputs"]}
        indexed_paths.update(
            {
                repository_relative(
                    self.repository_root, run_root / "run_manifest.json"
                ),
                event_ref["path"],
                decision_ref["path"],
            }
        )
        if isinstance(reference_document, dict):
            indexed_paths.update(
                reference["path"] for reference in reference_document["references"]
            )
        actual_run_files = {
            repository_relative(self.repository_root, path)
            for path in run_root.rglob("*")
            if path.is_file() and not path.is_symlink()
        }
        restricted_files = {
            repository_relative(self.repository_root, path)
            for path in (self.restricted_root / run_id).rglob("*")
            if path.is_file() and not path.is_symlink()
        }
        restricted_prefix = repository_relative(
            self.repository_root, self.restricted_root / run_id
        ) + "/"
        expected_restricted_files = {identity_path} | {
            reference["path"]
            for reference in manifest["outputs"]
            if reference["path"].startswith(restricted_prefix)
        }
        closed_file_set = (
            actual_run_files <= indexed_paths
            and restricted_files == expected_restricted_files
        )
        check(
            semantic_checks,
            "RUN_FILE_SET_CLOSED",
            closed_file_set,
            "Every persisted run or restricted file is indexed; restricted state contains only sealed identity and clearance artifacts.",
        )

        all_checks = schema_checks + semantic_checks + privacy_checks + hash_checks
        passed = sum(item["status"] == "PASS" for item in all_checks)
        failed = sum(item["status"] == "FAIL" for item in all_checks)
        skipped = sum(item["status"] == "SKIP" for item in all_checks)
        report = {
            "schema_version": SCHEMA_VERSION,
            "validation_report_id": allocator.next("VAL"),
            "run_id": run_id,
            "created_at": self.now(),
            "validator": {
                "name": "ne630-review-validator",
                "version": VERSION,
                "jsonschema_version": importlib.metadata.version("jsonschema"),
                "python_version": platform.python_version(),
                "executable_sha256": self.executable_sha256,
            },
            "overall_status": "PASS" if failed == 0 else "FAIL",
            "schema_checks": schema_checks,
            "semantic_checks": semantic_checks,
            "privacy_checks": privacy_checks,
            "hash_checks": hash_checks,
            "summary": {
                "total": len(all_checks),
                "passed": passed,
                "failed": failed,
                "skipped": skipped,
            },
            "errors": errors,
            "warnings": warnings,
            "contains_source_identifiers": False,
        }
        report_errors = sorted(
            self.validators["validation_report"].iter_errors(report),
            key=lambda item: list(item.path),
        )
        if report_errors:
            joined = "; ".join(error.message for error in report_errors[:10])
            raise ContractError(f"validation report does not satisfy its schema: {joined}")
        return report

    def _fail_stage(
        self,
        manifest: dict[str, Any],
        events: EventLog,
        stage: str,
        code: str,
        message: str,
    ) -> None:
        state = self._stage(manifest, stage)
        event = events.append(
            stage=stage,
            event_type="STAGE_COMPLETED",
            subject_type="RUN",
            subject_id=manifest["run_id"],
            outcome="FAILED",
            reason_code=code,
            payload={"stage_status": "FAILED", "message": message},
        )
        state.update(
            {
                "status": "FAILED",
                "event_sequence_end": event["sequence"],
                "completed_at": event["occurred_at"],
                "reason_code": code,
            }
        )
        manifest["run_state"] = "FAILED"
        manifest["updated_at"] = event["occurred_at"]

    def validate(self, *, run_id: str | None = None) -> dict[str, Any]:
        with self._mutation_lock():
            self._clear_stage_failure_guard()
            try:
                return self._validate(run_id=run_id)
            except (Exception, KeyboardInterrupt):
                self._seal_active_stage_failure()
                raise
            finally:
                self._clear_stage_failure_guard()

    def _validate(self, *, run_id: str | None = None) -> dict[str, Any]:
        preflight = self.preflight_framework(require_tools=True)
        run_id = self.resolve_run_id(run_id)
        run_root, manifest, events, event_path, decision_path, allocator = self._load_run(
            run_id
        )
        if manifest["run_state"] in {"BLOCKED", "FAILED"}:
            raise ContractError(
                "blocked or failed runs must be explicitly repaired/resumed before validation"
            )
        validation_stage = self._stage(manifest, "VALIDATE")
        if validation_stage["status"] in {"RUNNING", "BLOCKED", "FAILED"}:
            raise ContractError("validation stage is not in a resumable state")
        report = self.build_validation_report(
            run_id=run_id,
            run_root=run_root,
            manifest=manifest,
            allocator=allocator,
            tool_dependencies=preflight["tool_dependencies"],
        )
        # The report above deliberately audits the prior validation seal.  A
        # new attempt must not keep advertising that prior result once its own
        # lifecycle begins: if STAGE_STARTED or any later write fails, recovery
        # seals this attempt with validation explicitly NOT_RUN.
        manifest["validation"] = {"status": "NOT_RUN", "report": None}
        self._arm_stage_failure_guard(
            manifest=manifest,
            events=events,
            run_root=run_root,
            event_path=event_path,
            decision_path=decision_path,
            stage="VALIDATE",
            code="VALIDATION_FAILED",
            message="Validation stopped safely before its report was committed.",
        )
        self._start_stage(manifest, events, "VALIDATE")
        report_path = (
            run_root
            / "reports"
            / f"validation-{report['validation_report_id'].lower()}.json"
        )
        write_private_json(report_path, report)
        report_ref = artifact_ref(
            self.repository_root,
            report_path,
            artifact_id=allocator.next("ART"),
            role="VALIDATION_REPORT",
            media_type="application/json",
        )
        self._add_output(manifest, report_ref)
        events.append(
            stage="VALIDATE",
            event_type="VALIDATION_RECORDED",
            subject_type="VALIDATION_REPORT",
            subject_id=report["validation_report_id"],
            outcome="RECORDED",
            reason_code="VALIDATION_RECORDED",
            outputs=[report_ref],
            payload={"validation_report_id": report["validation_report_id"]},
        )
        manifest["validation"] = {
            "status": report["overall_status"],
            "report": report_ref,
        }
        if report["overall_status"] == "PASS":
            self._complete_stage(
                manifest,
                events,
                "VALIDATE",
                outputs=[report_ref],
                message="Phase-aware schema, semantic, privacy, and hash checks passed.",
            )
        else:
            self._fail_stage(
                manifest,
                events,
                "VALIDATE",
                "VALIDATION_FAILED",
                "One or more validation checks failed.",
            )
        self._refresh_logs(manifest, events, event_path, decision_path)
        self._write_manifest(run_root, manifest)
        return {
            "run_id": run_id,
            "validation_report_id": report["validation_report_id"],
            "status": report["overall_status"],
            **report["summary"],
        }


def run_self_test(test_root: Path, *, verbosity: int = 1) -> bool:
    suite = unittest.defaultTestLoader.discover(
        str(test_root), pattern="test_*.py", top_level_dir=str(test_root.parent)
    )
    discovered = suite.countTestCases()
    if discovered < MINIMUM_SELF_TEST_CASES:
        print(
            "self-test failed: "
            f"discovered {discovered} cases; expected at least {MINIMUM_SELF_TEST_CASES}",
            file=sys.stderr,
        )
        return False
    result = unittest.TextTestRunner(verbosity=verbosity).run(suite)
    return result.wasSuccessful()


def build_parser() -> argparse.ArgumentParser:
    default_repository_root = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(
        description="Private NE 630 homework review intake and calibration pipeline."
    )
    parser.add_argument(
        "--repository-root",
        type=Path,
        default=default_repository_root,
        help="NE 630 repository root (default: inferred from this script)",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="configuration path (default: grades/review/f2026/config.yaml)",
    )
    parser.add_argument(
        "--codebook",
        type=Path,
        default=None,
        help="approved ne630-homework-review SKILL.md path",
    )
    commands = parser.add_subparsers(dest="command", required=True)
    self_test = commands.add_parser(
        "self-test",
        help="run hermetic synthetic tests; never reads live submissions",
    )
    self_test.add_argument("-v", "--verbose", action="count", default=0)
    intake = commands.add_parser(
        "intake",
        help="create a private frozen run and deterministic pseudonymized intake",
    )
    intake.add_argument(
        "--run-id",
        help="explicit run ID for reproducible tests; normally generated automatically",
    )
    prepare = commands.add_parser(
        "prepare-calibration",
        help=(
            "lock the eight-item selection and create its clearance request"
        ),
    )
    prepare.add_argument("--run-id", help="review run ID")
    stage_review_set = commands.add_parser(
        "stage-calibration-review-set",
        help=(
            "sandbox-rasterize the locked products into an immutable inert review set"
        ),
    )
    stage_review_set.add_argument("--run-id", help="review run ID")
    stage_review_set.add_argument(
        "--sanitized-derivative",
        action="append",
        default=[],
        metavar="RECORD_ID=PDF",
        help=(
            "use a sanitized replacement as the raster source for this record; "
            "unlisted records use the frozen submitted solution"
        ),
    )
    record_clearance = commands.add_parser(
        "record-calibration-clearance",
        help="record one instructor attestation covering the exact locked selection",
    )
    record_clearance.add_argument("--run-id", help="review run ID")
    record_clearance.add_argument(
        "--review-set-id",
        required=True,
        help="immutable RSET identifier shown by stage-calibration-review-set",
    )
    record_clearance.add_argument(
        "--review-set-sha256",
        required=True,
        help="exact review-set manifest SHA-256 shown after staging",
    )
    record_clearance.add_argument(
        "--actor-id",
        required=True,
        help="instructor identity recorded in the append-only decision log",
    )
    record_clearance.add_argument(
        "--attest-visual-clearance",
        action="store_true",
        help=f'affirm exactly: "{CLEARANCE_ATTESTATION}"',
    )
    record_clearance.add_argument(
        "--rationale",
        default=(
            "Instructor visually inspected every page in the identified inert "
            "review set and confirmed that visible student identity is absent."
        ),
        help="nonidentifying instructor rationale stored with the decision",
    )
    resume = commands.add_parser(
        "resume-calibration",
        help="verify recorded clearance and create the eight blinded packets",
    )
    resume.add_argument("--run-id", help="review run ID")
    validate = commands.add_parser(
        "validate",
        help="write a phase-aware schema, semantic, privacy, and hash report",
    )
    validate.add_argument("--run-id", help="review run ID")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    arguments = parser.parse_args(argv)
    repository_root = arguments.repository_root.resolve()
    if arguments.command == "self-test":
        test_root = Path(__file__).resolve().parent / "tests"
        if not test_root.is_dir():
            print("self-test failed: synthetic test suite is missing", file=sys.stderr)
            return 1
        success = run_self_test(test_root, verbosity=1 + arguments.verbose)
        return 0 if success else 1
    try:
        pipeline = ReviewPipeline(
            repository_root,
            config_path=arguments.config,
            codebook_path=arguments.codebook,
        )
        if arguments.command == "intake":
            result = pipeline.intake(run_id=arguments.run_id)
        elif arguments.command == "prepare-calibration":
            result = pipeline.prepare_calibration(run_id=arguments.run_id)
        elif arguments.command == "stage-calibration-review-set":
            derivative_pairs: dict[str, Path] = {}
            for value in arguments.sanitized_derivative:
                if "=" not in value:
                    raise ContractError(
                        "each sanitized derivative must use RECORD_ID=PDF syntax"
                    )
                record_id, path_value = value.split("=", 1)
                if not record_id or not path_value or record_id in derivative_pairs:
                    raise ContractError("sanitized derivative arguments are invalid")
                derivative_pairs[record_id] = Path(path_value)
            result = pipeline.stage_calibration_review_set(
                run_id=arguments.run_id,
                sanitized_derivatives=derivative_pairs,
            )
        elif arguments.command == "record-calibration-clearance":
            result = pipeline.record_calibration_clearance(
                run_id=arguments.run_id,
                review_set_id=arguments.review_set_id,
                review_set_sha256=arguments.review_set_sha256,
                actor_id=arguments.actor_id,
                attestation=(
                    CLEARANCE_ATTESTATION
                    if arguments.attest_visual_clearance
                    else ""
                ),
                rationale=arguments.rationale,
            )
        elif arguments.command == "resume-calibration":
            result = pipeline.resume_calibration(run_id=arguments.run_id)
        elif arguments.command == "validate":
            result = pipeline.validate(run_id=arguments.run_id)
        else:  # pragma: no cover - argparse enforces the command set
            parser.error("unknown command")
        print(json.dumps(result, sort_keys=True))
        return 0 if result.get("status") != "FAIL" else 1
    except (json.JSONDecodeError, UnicodeDecodeError):
        print(
            f"{arguments.command} failed safely: malformed private JSON or text artifact",
            file=sys.stderr,
        )
        return 1
    except jsonschema.ValidationError as exc:
        location = "/" + "/".join(str(part) for part in exc.absolute_path)
        validator = exc.validator or "schema"
        print(
            f"{arguments.command} failed safely: {validator} violation at {location}",
            file=sys.stderr,
        )
        return 1
    except OSError:
        print(
            f"{arguments.command} failed safely: local private I/O failure",
            file=sys.stderr,
        )
        return 1
    except (PipelineError, yaml.YAMLError) as exc:
        print(f"{arguments.command} failed safely: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
