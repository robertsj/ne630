from __future__ import annotations

import contextlib
import io
import json
import os
from pathlib import Path
import shutil
import stat
import struct
import subprocess
import tarfile
import tempfile
import unittest
import zipfile
from unittest import mock

import review_pipeline as pipeline


FIXED_TIME = "2026-09-24T12:00:00Z"
FIXED_RUN_ID = "run-20260924T120000Z-aaaaaaaaaaaa"
SECOND_RUN_ID = "run-20260924T120001Z-bbbbbbbbbbbb"


def zip_bytes(
    members: list[tuple[str, bytes]],
    *,
    symlink: bool = False,
    compression: int = zipfile.ZIP_DEFLATED,
) -> bytes:
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", compression=compression) as archive:
        for index, (name, data) in enumerate(members):
            if symlink and index == 0:
                info = zipfile.ZipInfo(name)
                info.create_system = 3
                info.external_attr = (stat.S_IFLNK | 0o777) << 16
                archive.writestr(info, data)
            else:
                archive.writestr(name, data)
    return output.getvalue()


def run_git(root: Path, *arguments: str) -> None:
    subprocess.run(
        ("git", *arguments),
        cwd=root,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )


class PipelineUnitTests(unittest.TestCase):
    def test_empty_self_test_suite_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            test_root = root / "tests"
            test_root.mkdir()
            (test_root / "__init__.py").write_text("", encoding="utf-8")
            self.assertFalse(pipeline.run_self_test(test_root, verbosity=0))

    def test_canonical_json_and_rank_vector(self) -> None:
        rendered = pipeline.canonical_json_bytes({"z": "e\u0301", "a": 1})
        self.assertEqual(rendered, b'{"a":1,"z":"\xc3\xa9"}\n')
        self.assertEqual(
            pipeline.selection_rank_digest(
                "ne630-f2026-hw01-hw04-calibration-v1",
                "HW01",
                "READABLE_SINGLE_PDF",
                "HW01-S001-V01",
            ),
            "dbc3dcb0204c2d601c0bf3a766908134bcb37b41476923586dfa006f918a11b4",
        )

    def test_canvas_name_parsing(self) -> None:
        ordinary = pipeline.parse_export_name(
            "invented_login_900001_45000001_solution_part_1.pdf"
        )
        self.assertIsNotNone(ordinary)
        assert ordinary is not None
        self.assertEqual(ordinary.login, "invented_login")
        self.assertEqual(ordinary.user_id, "900001")
        self.assertEqual(ordinary.file_id, "45000001")
        self.assertEqual(ordinary.original_name, "solution_part_1.pdf")
        late = pipeline.parse_export_name(
            "invented_login_LATE_900001_45000002_solution.pdf"
        )
        self.assertIsNotNone(late)
        assert late is not None
        self.assertTrue(late.late_marker)
        self.assertEqual(late.login, "invented_login")

    def test_zip_preflight(self) -> None:
        limits = {
            "max_entries": 1000,
            "max_entry_bytes": 52_428_800,
            "max_total_expanded_bytes": 209_715_200,
            "max_compression_ratio": 100.0,
        }
        safe = pipeline.inspect_zip_bytes(
            zip_bytes([("solution.pdf", pipeline._minimal_pdf_bytes("invented"))]),
            artifact_id="ART-000001",
            limits=limits,
        )
        self.assertEqual(safe.record["status"], "SAFE")
        self.assertIsNotNone(safe.solution_pdf)

        traversal = pipeline.inspect_zip_bytes(
            zip_bytes([("../solution.pdf", b"x")]),
            artifact_id="ART-000002",
            limits=limits,
        )
        self.assertEqual(traversal.record["status"], "UNSAFE")
        self.assertTrue(traversal.record["has_traversal_path"])

        absolute = pipeline.inspect_zip_bytes(
            zip_bytes([("/solution.pdf", b"x")]),
            artifact_id="ART-000006",
            limits=limits,
        )
        self.assertEqual(absolute.record["status"], "UNSAFE")
        self.assertTrue(absolute.record["has_absolute_path"])

        backslash = pipeline.inspect_zip_bytes(
            zip_bytes([("wrapper\\solution.pdf", b"x")]),
            artifact_id="ART-000007",
            limits=limits,
        )
        self.assertEqual(backslash.record["status"], "UNSAFE")

        duplicate = pipeline.inspect_zip_bytes(
            zip_bytes([("A.txt", b"a"), ("a.TXT", b"b")]),
            artifact_id="ART-000003",
            limits=limits,
        )
        self.assertEqual(duplicate.record["status"], "UNSAFE")
        self.assertTrue(duplicate.record["has_duplicate_normalized_path"])

        linked = pipeline.inspect_zip_bytes(
            zip_bytes([("solution.pdf", b"target")], symlink=True),
            artifact_id="ART-000004",
            limits=limits,
        )
        self.assertEqual(linked.record["status"], "UNSAFE")
        self.assertTrue(linked.record["has_symlink"])

        nested = pipeline.inspect_zip_bytes(
            zip_bytes([("nested.zip", b"PK\x03\x04")]),
            artifact_id="ART-000005",
            limits=limits,
        )
        self.assertEqual(nested.record["status"], "UNSAFE")
        self.assertTrue(nested.record["has_nested_archive"])

        disguised_archive = pipeline.inspect_zip_bytes(
            zip_bytes([("payload.bin", zip_bytes([("inner.txt", b"x")]))]),
            artifact_id="ART-000008",
            limits=limits,
        )
        self.assertEqual(disguised_archive.record["status"], "UNSAFE")
        self.assertTrue(disguised_archive.record["has_nested_archive"])

        prefixed_archive = pipeline.inspect_zip_bytes(
            zip_bytes(
                [
                    (
                        "payload.bin",
                        b"MZ" + b"\x00" * 30 + zip_bytes([("inner.txt", b"x")]),
                    )
                ]
            ),
            artifact_id="ART-000010",
            limits=limits,
        )
        self.assertEqual(prefixed_archive.record["status"], "UNSAFE")
        self.assertTrue(prefixed_archive.record["has_nested_archive"])

        trailing_inner_zip = pipeline.inspect_zip_bytes(
            zip_bytes(
                [
                    (
                        "payload.bin",
                        zip_bytes([("inner.txt", b"x")]) + b"trailing-junk",
                    )
                ]
            ),
            artifact_id="ART-000016",
            limits=limits,
        )
        self.assertEqual(trailing_inner_zip.record["status"], "UNSAFE")
        self.assertTrue(trailing_inner_zip.record["has_nested_archive"])

        empty_inner_zip = pipeline.inspect_zip_bytes(
            zip_bytes([("payload.bin", zip_bytes([]))]),
            artifact_id="ART-000017",
            limits=limits,
        )
        self.assertEqual(empty_inner_zip.record["status"], "UNSAFE")
        self.assertTrue(empty_inner_zip.record["has_nested_archive"])

        tar_buffer = io.BytesIO()
        with tarfile.open(fileobj=tar_buffer, mode="w") as archive:
            tar_info = tarfile.TarInfo("inner.txt")
            tar_info.size = 1
            archive.addfile(tar_info, io.BytesIO(b"x"))
        disguised_tar = pipeline.inspect_zip_bytes(
            zip_bytes(
                [("payload.bin", tar_buffer.getvalue())],
                compression=zipfile.ZIP_STORED,
            ),
            artifact_id="ART-000018",
            limits=limits,
        )
        self.assertEqual(disguised_tar.record["status"], "UNSAFE")
        self.assertTrue(disguised_tar.record["has_nested_archive"])

        for index, unsafe_name in enumerate(
            ("./solution.pdf", "a/./solution.pdf", "a//solution.pdf"), 11
        ):
            dotted = pipeline.inspect_zip_bytes(
                zip_bytes([(unsafe_name, pipeline._minimal_pdf_bytes("invented"))]),
                artifact_id=f"ART-{index:06d}",
                limits=limits,
            )
            self.assertEqual(dotted.record["status"], "UNSAFE")

        incidental_gzip_magic = pipeline.inspect_zip_bytes(
            zip_bytes(
                [
                    ("solution.pdf", pipeline._minimal_pdf_bytes("invented")),
                    ("data.bin", b"ordinary-prefix" + b"\x1f\x8b" + b"ordinary-tail"),
                ]
            ),
            artifact_id="ART-000014",
            limits=limits,
        )
        self.assertEqual(incidental_gzip_magic.record["status"], "SAFE")

        mismatched_type_buffer = io.BytesIO()
        with zipfile.ZipFile(mismatched_type_buffer, "w") as archive:
            info = zipfile.ZipInfo("solution.pdf")
            info.create_system = 3
            info.external_attr = (stat.S_IFDIR | 0o755) << 16
            archive.writestr(info, b"")
        mismatched_type = pipeline.inspect_zip_bytes(
            mismatched_type_buffer.getvalue(),
            artifact_id="ART-000015",
            limits=limits,
        )
        self.assertEqual(mismatched_type.record["status"], "UNSAFE")

        tiny_limits = dict(limits)
        tiny_limits["max_entries"] = 0
        limited = pipeline.inspect_zip_bytes(
            zip_bytes([("solution.pdf", pipeline._minimal_pdf_bytes("invented"))]),
            artifact_id="ART-000009",
            limits=tiny_limits,
        )
        self.assertEqual(limited.record["status"], "RESOURCE_LIMIT")

        forged_counts = bytearray(
            zip_bytes([(f"entry-{index:04d}.txt", b"") for index in range(1002)])
        )
        eocd_offset = forged_counts.rfind(b"PK\x05\x06")
        self.assertGreaterEqual(eocd_offset, 0)
        struct.pack_into("<HH", forged_counts, eocd_offset + 8, 1, 1)
        bounded = pipeline.inspect_zip_bytes(
            bytes(forged_counts),
            artifact_id="ART-000019",
            limits=limits,
        )
        self.assertEqual(bounded.record["status"], "RESOURCE_LIMIT")
        self.assertIn("ARCHIVE_ENTRY_LIMIT", bounded.record["limit_codes"])

        trailing_top_level = bytes(forged_counts) + b"trailing-junk"
        with mock.patch.object(
            pipeline.zipfile,
            "ZipFile",
            side_effect=AssertionError("ZipFile must not see an unbounded directory"),
        ):
            rejected_before_materialization = pipeline.inspect_zip_bytes(
                trailing_top_level,
                artifact_id="ART-000020",
                limits=limits,
            )
        self.assertEqual(rejected_before_materialization.record["status"], "UNSAFE")
        self.assertIn(
            "ARCHIVE_EOCD_INVALID",
            rejected_before_materialization.record["limit_codes"],
        )

    def test_synthetic_pdf_is_readable(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            pipeline.private_mkdir(root)
            inspection, text = pipeline.inspect_pdf_bytes(
                pipeline._minimal_pdf_bytes("Invented NE 630 solution"),
                artifact_id="ART-000001",
                private_tmp=root,
                maximum_bytes=1_000_000,
                timeout_seconds=5,
            )
        self.assertEqual(inspection["status"], "READABLE")
        self.assertEqual(inspection["page_count"], 1)
        self.assertIn(b"Invented NE 630 solution", text)

    def test_rasterized_pdf_is_deterministic_and_strictly_inert(self) -> None:
        source = pipeline._minimal_pdf_bytes("Visible answer") + (
            b"\n/Open#41ction /Java#53cript /JS (hidden)\n"
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first = pipeline.rasterize_pdf_to_inert_pdf(
                source,
                artifact_id="ART-000001",
                private_tmp=root,
                maximum_input_bytes=1_000_000,
                timeout_seconds=5,
            )
            second = pipeline.rasterize_pdf_to_inert_pdf(
                source,
                artifact_id="ART-000002",
                private_tmp=root,
                maximum_input_bytes=1_000_000,
                timeout_seconds=5,
            )
        self.assertEqual(first.data, second.data)
        self.assertEqual(first.page_count, 1)
        self.assertNotIn(b"Open#41ction", first.data)
        self.assertNotIn(b"Java#53cript", first.data)
        self.assertEqual(
            pipeline.inspect_inert_raster_pdf(first.data).page_sha256s,
            first.page_sha256s,
        )

    def test_inert_profile_rejects_incremental_update_bytes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            inert = pipeline.rasterize_pdf_to_inert_pdf(
                pipeline._minimal_pdf_bytes("answer"),
                artifact_id="ART-000001",
                private_tmp=Path(temporary),
                maximum_input_bytes=1_000_000,
                timeout_seconds=5,
            )
        with self.assertRaisesRegex(pipeline.UnsafeInputError, "cross-reference"):
            pipeline.inspect_inert_raster_pdf(
                inert.data + b"/OpenAction /JavaScript"
            )

    def test_ambiguous_canvas_name_is_not_guessed(self) -> None:
        self.assertIsNone(
            pipeline.parse_export_name(
                "john_2024_900001_45000001_solution.pdf"
            )
        )


class SyntheticEndToEndTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        source_repository = Path(pipeline.__file__).resolve().parents[3]
        source_framework = source_repository / "grades/review/f2026"
        target_framework = self.root / "grades/review/f2026"
        shutil.copytree(
            source_framework,
            target_framework,
            ignore=shutil.ignore_patterns(
                "runs", "restricted", "__pycache__", "*.pyc"
            ),
        )
        shutil.copy2(source_repository / ".gitignore", self.root / ".gitignore")
        (self.root / "administrivia").mkdir(parents=True)
        (self.root / "administrivia/syllabus.md").write_text(
            "# Synthetic syllabus\nInvented fixture only.\n", encoding="utf-8"
        )
        for assignment_number in range(1, 5):
            assignment = f"HW{assignment_number:02d}"
            (self.root / "homework/markdown").mkdir(parents=True, exist_ok=True)
            (self.root / "homework/solutions").mkdir(parents=True, exist_ok=True)
            (self.root / f"homework/markdown/{assignment}.md").write_text(
                f"# {assignment}\nSynthetic P1, P2, P3.\n", encoding="utf-8"
            )
            (self.root / f"homework/solutions/hw{assignment_number:02d}.tex").write_text(
                f"Synthetic key for {assignment}.\n", encoding="utf-8"
            )
            submission_dir = self.root / f"grades/submissions/hw{assignment_number:02d}"
            submission_dir.mkdir(parents=True)
            file_id = 45_000_000 + assignment_number * 10
            pdf_name = (
                f"invented_pdf_900001_{file_id}_submitted_work_{assignment}.pdf"
            )
            (submission_dir / pdf_name).write_bytes(
                pipeline._minimal_pdf_bytes(f"Product answer for {assignment} P1 P2 P3")
            )
            malicious_makefile = b"SENTINEL := $(shell touch should-not-exist)\nall:\n\t@false\n"
            archive_name = (
                f"invented_zip_900002_{file_id + 1}_submission_bundle_{assignment}.zip"
            )
            archive = zip_bytes(
                [
                    (
                        "solution.pdf",
                        pipeline._minimal_pdf_bytes(
                            f"Archived product answer for {assignment} P1 P2 P3"
                        ),
                    ),
                    ("solution.tex", b"Synthetic solution source.\n"),
                    ("discourse.tex", b"Synthetic discourse.\n"),
                    ("discourse.pdf", pipeline._minimal_pdf_bytes("Synthetic discourse")),
                    ("Makefile", malicious_makefile),
                ]
            )
            (submission_dir / archive_name).write_bytes(archive)
        (target_framework / "codebook.md").write_text(
            "# Synthetic codebook\nFixture-only review rules.\n", encoding="utf-8"
        )
        run_git(self.root, "init", "-q")
        run_git(self.root, "config", "user.name", "Synthetic Test")
        run_git(self.root, "config", "user.email", "synthetic@example.invalid")
        run_git(self.root, "add", ".")
        run_git(self.root, "commit", "-q", "-m", "synthetic fixture")
        self.codebook_path = target_framework / "codebook.md"
        self.pipeline = pipeline.ReviewPipeline(
            self.root,
            codebook_path=self.codebook_path,
            now=lambda: FIXED_TIME,
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def assert_failed_stage_is_sealed(self, stage: str, reason_code: str) -> None:
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        manifest = json.loads((run_root / "run_manifest.json").read_text())
        self.assertEqual(manifest["run_state"], "FAILED")
        stage_state = next(
            item for item in manifest["stages"] if item["stage"] == stage
        )
        self.assertEqual(stage_state["status"], "FAILED")
        self.assertEqual(stage_state["reason_code"], reason_code)
        event_bytes = (run_root / "events/events.jsonl").read_bytes()
        self.assertEqual(
            manifest["event_log"]["artifact"]["sha256"],
            pipeline.sha256_bytes(event_bytes),
        )
        self.assertEqual(
            manifest["event_log"]["entry_count"], len(event_bytes.splitlines())
        )

    def stage_clearance_request(self) -> dict[str, object]:
        result = self.pipeline.prepare_calibration(run_id=FIXED_RUN_ID)
        self.assertEqual(result["status"], "BLOCKED")
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        return json.loads(
            (
                run_root / "manifests/calibration_clearance_request.json"
            ).read_text()
        )

    def stage_review_set(
        self,
        *,
        derivatives: dict[str, Path] | None = None,
        review: pipeline.ReviewPipeline | None = None,
    ) -> dict[str, object]:
        active = review or self.pipeline
        result = active.stage_calibration_review_set(
            run_id=FIXED_RUN_ID,
            sanitized_derivatives=derivatives or {},
        )
        return result

    def record_clearance(
        self,
        request: dict[str, object],
        *,
        derivatives: dict[str, Path] | None = None,
        clear_original: list[str] | None = None,
    ) -> dict[str, object]:
        del request
        if clear_original is not None:
            raise pipeline.ContractError("legacy partial-clearance fixture is unsupported")
        review_set = self.stage_review_set(derivatives=derivatives)
        return self.pipeline.record_calibration_clearance(
            run_id=FIXED_RUN_ID,
            review_set_id=str(review_set["review_set_id"]),
            review_set_sha256=str(review_set["review_set_sha256"]),
            actor_id="synthetic-instructor",
            attestation=pipeline.CLEARANCE_ATTESTATION,
            rationale="Synthetic instructor clearance for hermetic test fixtures.",
        )

    def block_record_and_resume(
        self,
        *,
        derivatives: dict[str, Path] | None = None,
    ) -> dict[str, object]:
        request = self.stage_clearance_request()
        recorded = self.record_clearance(request, derivatives=derivatives)
        self.assertEqual(recorded["cleared"], 8)
        return self.pipeline.resume_calibration(run_id=FIXED_RUN_ID)

    def test_intake_prepare_and_validate(self) -> None:
        intake = self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.assertEqual(intake["source_groups"], 8)
        self.assertEqual(intake["top_level_files"], 8)
        self.assertEqual(intake["eligible"], 8)
        self.assertFalse((self.root / "should-not-exist").exists())

        intake_validation = self.pipeline.validate(run_id=FIXED_RUN_ID)
        self.assertEqual(intake_validation["status"], "PASS")

        prepared = self.block_record_and_resume()
        self.assertEqual(prepared["selected"], 8)
        self.assertEqual(prepared["product_review"], 8)
        self.assertFalse((self.root / "should-not-exist").exists())

        validated = self.pipeline.validate(run_id=FIXED_RUN_ID)
        self.assertEqual(validated["status"], "PASS")
        self.assertEqual(validated["failed"], 0)

        validation_reports = sorted(
            (
                self.root
                / f"grades/review/f2026/runs/{FIXED_RUN_ID}/reports"
            ).glob("validation-*.json")
        )
        self.assertEqual(len(validation_reports), 2)
        check_id_sets = []
        for report_path in validation_reports:
            report = json.loads(report_path.read_text())
            check_id_sets.append(
                {
                    item["check_id"]
                    for category in (
                        "schema_checks",
                        "semantic_checks",
                        "privacy_checks",
                        "hash_checks",
                    )
                    for item in report[category]
                }
            )
        self.assertTrue(check_id_sets[0].isdisjoint(check_id_sets[1]))

        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        restricted_root = self.root / f"grades/review/f2026/restricted/{FIXED_RUN_ID}"
        self.assertEqual(stat.S_IMODE(run_root.stat().st_mode), 0o700)
        self.assertEqual(stat.S_IMODE(restricted_root.stat().st_mode), 0o700)
        for path in list(run_root.rglob("*")) + list(restricted_root.rglob("*")):
            expected = 0o700 if path.is_dir() else 0o600
            self.assertEqual(stat.S_IMODE(path.stat().st_mode), expected, str(path))

        identity = json.loads((restricted_root / "identity_map.json").read_text())
        manifest = json.loads((run_root / "run_manifest.json").read_text())
        self.assertEqual(
            [item["name"] for item in manifest["tool"]["dependencies"]],
            ["bwrap", "pdfinfo", "pdftotext", "pdftoppm"],
        )
        self.assertTrue(
            all(
                len(item["executable_sha256"]) == 64 and item["version"]
                for item in manifest["tool"]["dependencies"]
            )
        )
        source_tokens = {
            subject["display_name"]
            for entry in identity["entries"]
            for subject in entry["subjects"]
            if "display_name" in subject
        }
        derived_text = "\n".join(
            path.read_text(encoding="utf-8", errors="ignore")
            for path in run_root.rglob("*")
            if path.is_file() and path.suffix in {".json", ".jsonl", ".md", ".tex"}
        )
        for token in source_tokens:
            self.assertNotIn(token, derived_text)

    def test_default_pipeline_requires_human_visual_clearance(self) -> None:
        review = pipeline.ReviewPipeline(
            self.root,
            codebook_path=self.codebook_path,
            now=lambda: FIXED_TIME,
        )
        review.intake(run_id=FIXED_RUN_ID)
        prepared = review.prepare_calibration(run_id=FIXED_RUN_ID)
        self.assertEqual(prepared["status"], "BLOCKED")
        review_set = self.stage_review_set(review=review)
        self.assertEqual(review_set["status"], "READY_FOR_VISUAL_REVIEW")
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        manifest = json.loads((run_root / "run_manifest.json").read_text())
        self.assertEqual(manifest["run_state"], "BLOCKED")
        prepare = next(
            item
            for item in manifest["stages"]
            if item["stage"] == "PREPARE_CALIBRATION"
        )
        self.assertEqual(prepare["reason_code"], "IDENTITY_SANITIZATION_REQUIRED")
        self.assertTrue(
            (run_root / "manifests/calibration_selection.json").is_file()
        )
        self.assertTrue(
            (run_root / "manifests/calibration_clearance_request.json").is_file()
        )
        candidates = sorted(
            (
                self.root
                / f"grades/review/f2026/restricted/{FIXED_RUN_ID}/clearance/review-sets/{review_set['review_set_id']}"
            ).glob("*.pdf")
        )
        self.assertEqual(len(candidates), 8)
        self.assertEqual(list((run_root / "packets").glob("*/packet_manifest.json")), [])
        manifest_before = (run_root / "run_manifest.json").read_bytes()
        events_before = (run_root / "events/events.jsonl").read_bytes()
        with self.assertRaisesRegex(
            pipeline.ContractError, "blocked or failed runs"
        ):
            review.validate(run_id=FIXED_RUN_ID)
        self.assertEqual(
            (run_root / "run_manifest.json").read_bytes(), manifest_before
        )
        self.assertEqual((run_root / "events/events.jsonl").read_bytes(), events_before)

    def test_prepare_checkpoint_repeat_is_mutation_free(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        first = self.pipeline.prepare_calibration(run_id=FIXED_RUN_ID)
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        manifest_before = (run_root / "run_manifest.json").read_bytes()
        events_before = (run_root / "events/events.jsonl").read_bytes()
        second = self.pipeline.prepare_calibration(run_id=FIXED_RUN_ID)
        self.assertEqual(first, second)
        self.assertEqual((run_root / "run_manifest.json").read_bytes(), manifest_before)
        self.assertEqual((run_root / "events/events.jsonl").read_bytes(), events_before)

    def test_review_set_postwrite_failure_rolls_back_for_retry(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.stage_clearance_request()
        original_write = pipeline.write_private_json
        failure_injected = False

        def write_then_fail(path: Path, value: object) -> None:
            nonlocal failure_injected
            original_write(path, value)
            if (
                path.name.startswith("calibration_clearance_review_set-rset-")
                and not failure_injected
            ):
                failure_injected = True
                raise OSError("synthetic post-review-set write failure")

        with mock.patch.object(
            pipeline, "write_private_json", side_effect=write_then_fail
        ):
            with self.assertRaisesRegex(
                OSError, "synthetic post-review-set write failure"
            ):
                self.stage_review_set()

        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        restricted_root = (
            self.root / f"grades/review/f2026/restricted/{FIXED_RUN_ID}"
        )
        self.assertEqual(
            list(
                (run_root / "manifests").glob(
                    "calibration_clearance_review_set-*.json"
                )
            ),
            [],
        )
        review_sets_root = restricted_root / "clearance/review-sets"
        self.assertEqual(list(review_sets_root.iterdir()), [])
        failed_manifest = json.loads((run_root / "run_manifest.json").read_text())
        self.assertFalse(
            any(
                reference["role"]
                in {
                    "CALIBRATION_REVIEW_PDF",
                    "CALIBRATION_CLEARANCE_REVIEW_SET",
                }
                for reference in failed_manifest["outputs"]
            )
        )

        retried = self.stage_review_set()
        self.assertEqual(retried["review_set_id"], "RSET-000001")
        self.assertEqual(
            len(
                list(
                    (
                        review_sets_root
                        / str(retried["review_set_id"])
                    ).glob("*.pdf")
                )
            ),
            8,
        )
        manifest = json.loads((run_root / "run_manifest.json").read_text())
        indexed_paths = {reference["path"] for reference in manifest["outputs"]}
        self.assertIn(str(retried["review_set_manifest"]), indexed_paths)
        self.assertTrue(
            set(retried["review_pdfs"]).issubset(indexed_paths)
        )

    def test_pipeline_lock_rejects_competing_mutator(self) -> None:
        with self.pipeline._mutation_lock():
            with self.assertRaisesRegex(pipeline.PipelineError, "busy"):
                self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.assertFalse(
            (self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}").exists()
        )

    def test_clearance_requires_exact_selection_without_mutation(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        request = self.stage_clearance_request()
        del request
        review_set = self.stage_review_set()
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        manifest_before = (run_root / "run_manifest.json").read_bytes()
        decisions_before = (run_root / "events/human_decisions.jsonl").read_bytes()
        with self.assertRaisesRegex(
            pipeline.ContractError, "review-set hash is not an indexed"
        ):
            self.pipeline.record_calibration_clearance(
                run_id=FIXED_RUN_ID,
                review_set_id=str(review_set["review_set_id"]),
                review_set_sha256="0" * 64,
                actor_id="synthetic-instructor",
                attestation=pipeline.CLEARANCE_ATTESTATION,
                rationale="Synthetic instructor clearance for hermetic test fixtures.",
            )
        self.assertEqual(
            (run_root / "run_manifest.json").read_bytes(), manifest_before
        )
        self.assertEqual(
            (run_root / "events/human_decisions.jsonl").read_bytes(),
            decisions_before,
        )

    def test_resume_without_recorded_clearance_is_mutation_free(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.stage_clearance_request()
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        manifest_before = (run_root / "run_manifest.json").read_bytes()
        events_before = (run_root / "events/events.jsonl").read_bytes()
        with self.assertRaisesRegex(pipeline.ContractError, "not indexed"):
            self.pipeline.resume_calibration(run_id=FIXED_RUN_ID)
        self.assertEqual(
            (run_root / "run_manifest.json").read_bytes(), manifest_before
        )
        self.assertEqual((run_root / "events/events.jsonl").read_bytes(), events_before)

    def test_completed_clearance_repeat_is_mutation_free(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.stage_clearance_request()
        review_set = self.stage_review_set()
        arguments = {
            "run_id": FIXED_RUN_ID,
            "review_set_id": str(review_set["review_set_id"]),
            "review_set_sha256": str(review_set["review_set_sha256"]),
            "actor_id": "synthetic-instructor",
            "attestation": pipeline.CLEARANCE_ATTESTATION,
            "rationale": "Synthetic instructor clearance for hermetic test fixtures.",
        }
        first = self.pipeline.record_calibration_clearance(**arguments)
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        manifest_before = (run_root / "run_manifest.json").read_bytes()
        decisions_before = (run_root / "events/human_decisions.jsonl").read_bytes()
        second = self.pipeline.record_calibration_clearance(**arguments)
        self.assertEqual(first, second)
        self.assertEqual((run_root / "run_manifest.json").read_bytes(), manifest_before)
        self.assertEqual(
            (run_root / "events/human_decisions.jsonl").read_bytes(),
            decisions_before,
        )

    def test_mixed_sanitized_derivative_hash_chain_validates(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        request = self.stage_clearance_request()
        record_id = sorted(
            item["submission_record_id"] for item in request["items"]
        )[0]
        derivative_path = self.root / "external-private-name.pdf"
        derivative_bytes = pipeline._minimal_pdf_bytes(
            "Sanitized synthetic product answer P1 P2 P3"
        )
        derivative_path.write_bytes(derivative_bytes)
        recorded = self.record_clearance(
            request, derivatives={record_id: derivative_path}
        )
        self.assertEqual(recorded["sanitized_derivative_rasters"], 1)
        resumed = self.pipeline.resume_calibration(run_id=FIXED_RUN_ID)
        self.assertEqual(resumed["product_review"], 8)
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        clearance = json.loads(
            (run_root / "manifests/calibration_clearance.json").read_text()
        )
        row = next(
            item
            for item in clearance["items"]
            if item["submission_record_id"] == record_id
        )
        self.assertEqual(
            row["disposition"], "SANITIZED_DERIVATIVE_RASTER_VISUALLY_CLEARED"
        )
        packet_pdf = run_root / f"packets/{record_id}/submitted-solution.pdf"
        self.assertNotEqual(packet_pdf.read_bytes(), derivative_bytes)
        self.assertEqual(
            packet_pdf.read_bytes(),
            (self.root / row["accepted_artifact"]["path"]).read_bytes(),
        )
        pipeline.inspect_inert_raster_pdf(packet_pdf.read_bytes())
        persisted_text = "\n".join(
            path.read_text(encoding="utf-8", errors="ignore")
            for path in [
                *run_root.rglob("*.json"),
                *run_root.rglob("*.jsonl"),
                *run_root.rglob("*.md"),
            ]
        )
        self.assertNotIn(derivative_path.name, persisted_text)
        self.assertEqual(
            self.pipeline.validate(run_id=FIXED_RUN_ID)["status"], "PASS"
        )

    def test_automated_hard_failure_cannot_clear_original(self) -> None:
        class HardFailPipeline(pipeline.ReviewPipeline):
            def _identity_scan(
                self, *args: object, **kwargs: object
            ) -> tuple[str, list[str]]:
                return "FAIL", ["IDENTITY_DISPLAY_NAME_PRESENT"]

        review = HardFailPipeline(
            self.root,
            codebook_path=self.codebook_path,
            now=lambda: FIXED_TIME,
        )
        review.intake(run_id=FIXED_RUN_ID)
        self.assertEqual(
            review.prepare_calibration(run_id=FIXED_RUN_ID)["status"], "BLOCKED"
        )
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        request = json.loads(
            (
                run_root / "manifests/calibration_clearance_request.json"
            ).read_text()
        )
        review_set = self.stage_review_set(review=review)
        self.assertEqual(review_set["status"], "REQUIRES_SANITIZED_DERIVATIVE")
        with self.assertRaisesRegex(
            pipeline.ContractError, "review set is not ready"
        ):
            review.record_calibration_clearance(
                run_id=FIXED_RUN_ID,
                review_set_id=str(review_set["review_set_id"]),
                review_set_sha256=str(review_set["review_set_sha256"]),
                actor_id="synthetic-instructor",
                attestation=pipeline.CLEARANCE_ATTESTATION,
                rationale="Synthetic hard-failure rejection test.",
            )

    def test_accepted_artifact_tampering_blocks_resume_without_mutation(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        request = self.stage_clearance_request()
        self.record_clearance(request)
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        clearance = json.loads(
            (run_root / "manifests/calibration_clearance.json").read_text()
        )
        accepted_path = self.root / clearance["items"][0]["accepted_artifact"]["path"]
        pipeline.write_private_bytes(
            accepted_path, accepted_path.read_bytes() + b"tampered"
        )
        manifest_before = (run_root / "run_manifest.json").read_bytes()
        events_before = (run_root / "events/events.jsonl").read_bytes()
        with self.assertRaisesRegex(pipeline.ContractError, "recorded run output changed"):
            self.pipeline.resume_calibration(run_id=FIXED_RUN_ID)
        self.assertEqual(
            (run_root / "run_manifest.json").read_bytes(), manifest_before
        )
        self.assertEqual((run_root / "events/events.jsonl").read_bytes(), events_before)

    def test_failed_resume_retries_without_duplicate_outputs(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        request = self.stage_clearance_request()
        self.record_clearance(request)
        original = self.pipeline._packet_and_dossier
        calls = 0

        def fail_after_third(**kwargs: object):  # type: ignore[no-untyped-def]
            nonlocal calls
            calls += 1
            result = original(**kwargs)  # type: ignore[arg-type]
            if calls == 3:
                raise OSError("synthetic packet write failure")
            return result

        with mock.patch.object(
            self.pipeline, "_packet_and_dossier", side_effect=fail_after_third
        ):
            with self.assertRaises(OSError):
                self.pipeline.resume_calibration(run_id=FIXED_RUN_ID)
        self.assert_failed_stage_is_sealed(
            "PREPARE_CALIBRATION", "PREPARE_CALIBRATION_FAILED"
        )
        resumed = self.pipeline.resume_calibration(run_id=FIXED_RUN_ID)
        self.assertEqual(resumed["product_review"], 8)
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        self.assertEqual(
            len(list((run_root / "packets").glob("*/packet_manifest.json"))),
            8,
        )
        self.assertEqual(
            self.pipeline.validate(run_id=FIXED_RUN_ID)["status"], "PASS"
        )

    def test_identity_map_tampering_blocks_prepare(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        identity_path = (
            self.root
            / f"grades/review/f2026/restricted/{FIXED_RUN_ID}/identity_map.json"
        )
        identity = json.loads(identity_path.read_text())
        identity["entries"][0]["original_files"], identity["entries"][2][
            "original_files"
        ] = (
            identity["entries"][2]["original_files"],
            identity["entries"][0]["original_files"],
        )
        pipeline.write_private_json(identity_path, identity)
        with self.assertRaisesRegex(
            pipeline.ContractError, "recorded run output changed"
        ):
            self.pipeline.prepare_calibration(run_id=FIXED_RUN_ID)

    def test_tampered_prior_identity_state_seals_new_intake_failed(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        identity_path = (
            self.root
            / f"grades/review/f2026/restricted/{FIXED_RUN_ID}/identity_map.json"
        )
        identity = json.loads(identity_path.read_text())
        target = next(
            entry for entry in identity["entries"] if entry["pseudonym"] != "S001"
        )
        target["pseudonym"] = "S001"
        pipeline.write_private_json(identity_path, identity)
        with self.assertRaisesRegex(
            pipeline.ContractError, "unusable prior identity state"
        ):
            self.pipeline.intake(run_id=SECOND_RUN_ID)
        second_root = self.root / f"grades/review/f2026/runs/{SECOND_RUN_ID}"
        manifest = json.loads((second_root / "run_manifest.json").read_text())
        intake = next(
            item for item in manifest["stages"] if item["stage"] == "INTAKE"
        )
        self.assertEqual(manifest["run_state"], "FAILED")
        self.assertEqual(intake["reason_code"], "INTAKE_FAILED")

    def test_event_log_tampering_is_rejected_before_mutation(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        event_path = (
            self.root
            / f"grades/review/f2026/runs/{FIXED_RUN_ID}/events/events.jsonl"
        )
        events = [json.loads(line) for line in event_path.read_bytes().splitlines()]
        events[0]["reason_code"] = "TAMPERED_EVENT"
        pipeline.write_private_bytes(
            event_path,
            b"".join(pipeline.canonical_json_bytes(event) for event in events),
        )
        with self.assertRaisesRegex(pipeline.ContractError, "event log differs"):
            self.pipeline.prepare_calibration(run_id=FIXED_RUN_ID)

    def test_schema_invalid_artifact_fails_validation_without_identity_leak(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        restricted_root = (
            self.root / f"grades/review/f2026/restricted/{FIXED_RUN_ID}"
        )
        identity = json.loads((restricted_root / "identity_map.json").read_text())
        sensitive_name = identity["entries"][0]["subjects"][0]["display_name"]
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        submission_path = next((run_root / "manifests/submissions").glob("*.json"))
        pipeline.write_private_json(submission_path, {"assignment_id": sensitive_name})

        result = self.pipeline.validate(run_id=FIXED_RUN_ID)
        self.assertEqual(result["status"], "FAIL")
        report_path = sorted((run_root / "reports").glob("validation-*.json"))[-1]
        report_bytes = report_path.read_bytes()
        self.assertNotIn(sensitive_name.encode("utf-8"), report_bytes)
        report = json.loads(report_bytes)
        self.assertTrue(
            any(
                item["code"] == "SCHEMA_OR_SERIALIZATION_INVALID"
                for item in report["errors"]
            )
        )

    def test_stage_manifest_tampering_fails_ledger_validation(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        manifest_path = run_root / "run_manifest.json"
        manifest = json.loads(manifest_path.read_text())
        product = next(
            item for item in manifest["stages"] if item["stage"] == "PRODUCT_REVIEW"
        )
        product.update(
            {
                "status": "COMPLETE",
                "event_sequence_start": 1,
                "event_sequence_end": 1,
                "started_at": manifest["created_at"],
                "completed_at": manifest["created_at"],
                "reason_code": None,
            }
        )
        pipeline.write_private_json(manifest_path, manifest)

        result = self.pipeline.validate(run_id=FIXED_RUN_ID)
        self.assertEqual(result["status"], "FAIL")
        report_path = sorted((run_root / "reports").glob("validation-*.json"))[-1]
        report = json.loads(report_path.read_text())
        ledger = next(
            item
            for item in report["semantic_checks"]
            if item["code"] == "STAGE_EVENT_LEDGER_VALID"
        )
        self.assertEqual(ledger["status"], "FAIL")

    def test_resumed_event_must_link_original_blocking_completion(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.block_record_and_resume()
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        event_path = run_root / "events/events.jsonl"
        events = [json.loads(line) for line in event_path.read_bytes().splitlines()]
        resumed = next(item for item in events if item["event_type"] == "RESUMED")
        resumed["parent_event_id"] = "EVT-000001"
        resumed["payload"]["from_event_id"] = "EVT-000001"
        event_bytes = b"".join(
            pipeline.canonical_json_bytes(item) for item in events
        )
        pipeline.write_private_bytes(event_path, event_bytes)
        manifest_path = run_root / "run_manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["event_log"]["artifact"]["sha256"] = pipeline.sha256_bytes(
            event_bytes
        )
        manifest["event_log"]["artifact"]["byte_count"] = len(event_bytes)
        pipeline.write_private_json(manifest_path, manifest)

        result = self.pipeline.validate(run_id=FIXED_RUN_ID)
        self.assertEqual(result["status"], "FAIL")
        report_path = sorted((run_root / "reports").glob("validation-*.json"))[-1]
        report = json.loads(report_path.read_text())
        ledger = next(
            item
            for item in report["semantic_checks"]
            if item["code"] == "STAGE_EVENT_LEDGER_VALID"
        )
        self.assertEqual(ledger["status"], "FAIL")

    def test_validation_rejects_clearance_decision_for_wrong_subject(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.block_record_and_resume()
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        decision_path = run_root / "events/human_decisions.jsonl"
        decisions = [
            json.loads(line) for line in decision_path.read_bytes().splitlines()
        ]
        decisions[0]["subject"] = {
            "subject_type": "ASSIGNMENT",
            "subject_id": "HW01",
        }
        selection = json.loads(
            (run_root / "manifests/calibration_selection.json").read_text()
        )
        decisions[0]["evidence_locators"][0]["artifact_id"] = selection[
            "selections"
        ][0]["submission_manifest"]["artifact_id"]
        decisions[0]["evidence_locators"][0]["artifact_sha256"] = selection[
            "selections"
        ][0]["submission_manifest"]["sha256"]
        decision_bytes = b"".join(
            pipeline.canonical_json_bytes(item) for item in decisions
        )
        pipeline.write_private_bytes(decision_path, decision_bytes)
        manifest_path = run_root / "run_manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["human_decision_log"]["artifact"]["sha256"] = (
            pipeline.sha256_bytes(decision_bytes)
        )
        manifest["human_decision_log"]["artifact"]["byte_count"] = len(
            decision_bytes
        )
        pipeline.write_private_json(manifest_path, manifest)

        result = self.pipeline.validate(run_id=FIXED_RUN_ID)
        self.assertEqual(result["status"], "FAIL")
        report_path = sorted((run_root / "reports").glob("validation-*.json"))[-1]
        report = json.loads(report_path.read_text())
        clearance_check = next(
            item
            for item in report["semantic_checks"]
            if item["code"] == "CALIBRATION_CLEARANCE_VALID"
        )
        self.assertEqual(clearance_check["status"], "FAIL")

    def test_revalidation_checks_prior_validation_stage_pointers(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        first = self.pipeline.validate(run_id=FIXED_RUN_ID)
        self.assertEqual(first["status"], "PASS")
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        manifest_path = run_root / "run_manifest.json"
        manifest = json.loads(manifest_path.read_text())
        validation_stage = next(
            item for item in manifest["stages"] if item["stage"] == "VALIDATE"
        )
        validation_stage["event_sequence_start"] = 1
        pipeline.write_private_json(manifest_path, manifest)

        second = self.pipeline.validate(run_id=FIXED_RUN_ID)
        self.assertEqual(second["status"], "FAIL")
        report_path = sorted((run_root / "reports").glob("validation-*.json"))[-1]
        report = json.loads(report_path.read_text())
        ledger = next(
            item
            for item in report["semantic_checks"]
            if item["code"] == "STAGE_EVENT_LEDGER_VALID"
        )
        self.assertEqual(ledger["status"], "FAIL")

    def test_validation_history_cannot_be_reset_without_prepare(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        first = self.pipeline.validate(run_id=FIXED_RUN_ID)
        self.assertEqual(first["status"], "PASS")
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        manifest_path = run_root / "run_manifest.json"
        manifest = json.loads(manifest_path.read_text())
        validation_stage = next(
            item for item in manifest["stages"] if item["stage"] == "VALIDATE"
        )
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
        manifest["validation"] = {"status": "NOT_RUN", "report": None}
        pipeline.write_private_json(manifest_path, manifest)

        second = self.pipeline.validate(run_id=FIXED_RUN_ID)
        self.assertEqual(second["status"], "FAIL")
        report_path = sorted((run_root / "reports").glob("validation-*.json"))[-1]
        report = json.loads(report_path.read_text())
        ledger = next(
            item
            for item in report["semantic_checks"]
            if item["code"] == "STAGE_EVENT_LEDGER_VALID"
        )
        self.assertEqual(ledger["status"], "FAIL")

    def test_failed_revalidation_start_does_not_resurrect_old_validation(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        first = self.pipeline.validate(run_id=FIXED_RUN_ID)
        self.assertEqual(first["status"], "PASS")

        original_append = pipeline.EventLog.append
        injected = False

        def fail_once_before_append(event_log: object, **kwargs: object):  # type: ignore[no-untyped-def]
            nonlocal injected
            if (
                not injected
                and kwargs.get("stage") == "VALIDATE"
                and kwargs.get("event_type") == "STAGE_STARTED"
            ):
                injected = True
                raise OSError("synthetic revalidation start failure")
            return original_append(event_log, **kwargs)  # type: ignore[arg-type]

        with mock.patch.object(
            pipeline.EventLog, "append", new=fail_once_before_append
        ):
            with self.assertRaises(OSError):
                self.pipeline.validate(run_id=FIXED_RUN_ID)

        self.assertTrue(injected)
        self.assert_failed_stage_is_sealed("VALIDATE", "VALIDATION_FAILED")
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        manifest = json.loads((run_root / "run_manifest.json").read_text())
        validation_stage = next(
            item for item in manifest["stages"] if item["stage"] == "VALIDATE"
        )
        self.assertEqual(validation_stage["status"], "FAILED")
        self.assertEqual(manifest["validation"], {"status": "NOT_RUN", "report": None})

    def test_validation_report_reference_must_have_validation_shape(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        first = self.pipeline.validate(run_id=FIXED_RUN_ID)
        self.assertEqual(first["status"], "PASS")
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        manifest_path = run_root / "run_manifest.json"
        manifest = json.loads(manifest_path.read_text())
        queue_reference = next(
            item
            for item in manifest["outputs"]
            if item["role"].startswith("REVIEW_QUEUE_")
            and "MARKDOWN" not in item["role"]
            and "RENDER" not in item["role"]
        )
        manifest["validation"]["report"] = queue_reference
        pipeline.write_private_json(manifest_path, manifest)

        second = self.pipeline.validate(run_id=FIXED_RUN_ID)
        self.assertEqual(second["status"], "FAIL")
        report_path = sorted((run_root / "reports").glob("validation-*.json"))[-1]
        report = json.loads(report_path.read_text())
        state_check = next(
            item
            for item in report["semantic_checks"]
            if item["code"] == "VALIDATION_STATE_RECONCILES"
        )
        self.assertEqual(state_check["status"], "FAIL")

    def test_missing_reference_fails_before_run_creation(self) -> None:
        (self.root / "homework/markdown/HW04.md").unlink()
        with self.assertRaisesRegex(pipeline.PipelineError, "required reference"):
            self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.assertFalse((self.root / "grades/review/f2026/runs").exists())
        self.assertFalse(
            (self.root / f"grades/review/f2026/restricted/{FIXED_RUN_ID}").exists()
        )

    def test_initial_manifest_failure_rolls_back_bootstrap_for_retry(self) -> None:
        original_write = pipeline.write_private_json
        injected = False

        def fail_initial_manifest(path: Path, value: object) -> None:
            nonlocal injected
            if path.name == "run_manifest.json" and not injected:
                injected = True
                raise OSError("synthetic initial manifest failure")
            original_write(path, value)

        with mock.patch.object(
            pipeline, "write_private_json", side_effect=fail_initial_manifest
        ):
            with self.assertRaises(OSError):
                self.pipeline.intake(run_id=FIXED_RUN_ID)

        self.assertTrue(injected)
        self.assertFalse(
            (self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}").exists()
        )
        self.assertFalse(
            (self.root / f"grades/review/f2026/restricted/{FIXED_RUN_ID}").exists()
        )
        retried = self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.assertEqual(retried["source_groups"], 8)
        loaded = self.pipeline._load_run(FIXED_RUN_ID)
        self.assertEqual(loaded[1]["run_id"], FIXED_RUN_ID)

    def test_run_root_hardening_failure_rolls_back_bootstrap_for_retry(self) -> None:
        original_chmod = Path.chmod
        target = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        injected = False

        def fail_run_root_chmod(path: Path, mode: int) -> None:
            nonlocal injected
            if path == target and not injected:
                injected = True
                raise OSError("synthetic run-root chmod failure")
            original_chmod(path, mode)

        with mock.patch.object(Path, "chmod", new=fail_run_root_chmod):
            with self.assertRaises(OSError):
                self.pipeline.intake(run_id=FIXED_RUN_ID)

        self.assertTrue(injected)
        self.assertFalse(target.exists())
        self.assertFalse(
            (self.root / f"grades/review/f2026/restricted/{FIXED_RUN_ID}").exists()
        )
        retried = self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.assertEqual(retried["source_groups"], 8)

    def test_restricted_root_hardening_failure_rolls_back_bootstrap_for_retry(
        self,
    ) -> None:
        original_chmod = Path.chmod
        target = self.root / f"grades/review/f2026/restricted/{FIXED_RUN_ID}"
        injected = False

        def fail_restricted_root_chmod(path: Path, mode: int) -> None:
            nonlocal injected
            if path == target and not injected:
                injected = True
                raise OSError("synthetic restricted-root chmod failure")
            original_chmod(path, mode)

        with mock.patch.object(Path, "chmod", new=fail_restricted_root_chmod):
            with self.assertRaises(OSError):
                self.pipeline.intake(run_id=FIXED_RUN_ID)

        self.assertTrue(injected)
        self.assertFalse(target.exists())
        self.assertFalse(
            (self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}").exists()
        )
        retried = self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.assertEqual(retried["source_groups"], 8)

    def test_self_test_manifest_failure_rolls_back_bootstrap_for_retry(self) -> None:
        original_write = pipeline.write_private_json
        manifest_writes = 0

        def fail_self_test_manifest(path: Path, value: object) -> None:
            nonlocal manifest_writes
            if path.name == "run_manifest.json":
                manifest_writes += 1
                if manifest_writes == 2:
                    raise OSError("synthetic SELF_TEST manifest failure")
            original_write(path, value)

        with mock.patch.object(
            pipeline, "write_private_json", side_effect=fail_self_test_manifest
        ):
            with self.assertRaises(OSError):
                self.pipeline.intake(run_id=FIXED_RUN_ID)

        self.assertEqual(manifest_writes, 2)
        self.assertFalse(
            (self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}").exists()
        )
        self.assertFalse(
            (self.root / f"grades/review/f2026/restricted/{FIXED_RUN_ID}").exists()
        )
        retried = self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.assertEqual(retried["source_groups"], 8)
        loaded = self.pipeline._load_run(FIXED_RUN_ID)
        self.assertEqual(loaded[1]["run_id"], FIXED_RUN_ID)

    def test_source_change_during_intake_is_recorded_as_failed(self) -> None:
        class SourceChangingPipeline(pipeline.ReviewPipeline):
            changed = False

            def _inspect_group(self, group: object, **kwargs: object):  # type: ignore[no-untyped-def]
                if not self.changed:
                    source = group.files[0].path  # type: ignore[attr-defined]
                    source.write_bytes(source.read_bytes() + b"changed-after-discovery")
                    self.changed = True
                return super()._inspect_group(group, **kwargs)  # type: ignore[arg-type]

        review = SourceChangingPipeline(
            self.root,
            codebook_path=self.codebook_path,
            now=lambda: FIXED_TIME,
        )
        with self.assertRaisesRegex(
            pipeline.UnsafeInputError,
            "source input changed after deterministic discovery",
        ):
            review.intake(run_id=FIXED_RUN_ID)

        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        manifest = json.loads((run_root / "run_manifest.json").read_text())
        self.assertEqual(manifest["run_state"], "FAILED")
        intake_stage = next(
            item for item in manifest["stages"] if item["stage"] == "INTAKE"
        )
        self.assertEqual(intake_stage["status"], "FAILED")
        self.assertEqual(intake_stage["reason_code"], "INTAKE_FAILED")
        identity_refs = [
            item
            for item in manifest["outputs"]
            if item["role"] == "RESTRICTED_IDENTITY_MAP"
        ]
        self.assertEqual(len(identity_refs), 1)

    def test_identity_map_write_failure_seals_failed_intake(self) -> None:
        original_write = pipeline.write_private_json

        def fail_identity(path: Path, value: object) -> None:
            if path.name == "identity_map.json":
                raise OSError("synthetic identity-map write failure")
            original_write(path, value)

        with mock.patch.object(
            pipeline, "write_private_json", side_effect=fail_identity
        ):
            with self.assertRaises(OSError):
                self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.assert_failed_stage_is_sealed("INTAKE", "INTAKE_FAILED")

    def test_unsealed_incomplete_identity_map_does_not_poison_fresh_intake(
        self,
    ) -> None:
        class HardStopAfterIdentityMap(pipeline.ReviewPipeline):
            def _inspect_group(self, *args: object, **kwargs: object):  # type: ignore[no-untyped-def]
                raise SystemExit("synthetic hard stop after identity-map write")

        interrupted = HardStopAfterIdentityMap(
            self.root,
            codebook_path=self.codebook_path,
            now=lambda: FIXED_TIME,
        )
        with self.assertRaisesRegex(SystemExit, "synthetic hard stop"):
            interrupted.intake(run_id=FIXED_RUN_ID)

        first_run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        first_restricted_root = (
            self.root / f"grades/review/f2026/restricted/{FIXED_RUN_ID}"
        )
        self.assertTrue((first_restricted_root / "identity_map.json").is_file())
        interrupted_manifest = json.loads(
            (first_run_root / "run_manifest.json").read_text()
        )
        self.assertFalse(
            any(
                reference["role"] == "RESTRICTED_IDENTITY_MAP"
                for reference in interrupted_manifest["outputs"]
            )
        )
        intake_state = next(
            item
            for item in interrupted_manifest["stages"]
            if item["stage"] == "INTAKE"
        )
        self.assertEqual(intake_state["status"], "RUNNING")

        completed = self.pipeline.intake(run_id=SECOND_RUN_ID)
        self.assertEqual(completed["source_groups"], 8)
        second_run_root = (
            self.root / f"grades/review/f2026/runs/{SECOND_RUN_ID}"
        )
        second_manifest = json.loads(
            (second_run_root / "run_manifest.json").read_text()
        )
        second_intake = next(
            item for item in second_manifest["stages"] if item["stage"] == "INTAKE"
        )
        self.assertEqual(second_intake["status"], "COMPLETE")

    def test_unexpected_stage_exception_still_seals_failed_intake(self) -> None:
        original_write = pipeline.write_private_json

        def fail_identity(path: Path, value: object) -> None:
            if path.name == "identity_map.json":
                raise RuntimeError("synthetic unexpected intake failure")
            original_write(path, value)

        with mock.patch.object(
            pipeline, "write_private_json", side_effect=fail_identity
        ):
            with self.assertRaises(RuntimeError):
                self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.assert_failed_stage_is_sealed("INTAKE", "INTAKE_FAILED")

    def test_keyboard_interrupt_still_seals_failed_intake(self) -> None:
        original_write = pipeline.write_private_json

        def interrupt_identity(path: Path, value: object) -> None:
            if path.name == "identity_map.json":
                raise KeyboardInterrupt()
            original_write(path, value)

        with mock.patch.object(
            pipeline, "write_private_json", side_effect=interrupt_identity
        ):
            with self.assertRaises(KeyboardInterrupt):
                self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.assert_failed_stage_is_sealed("INTAKE", "INTAKE_FAILED")

    def test_started_event_boundary_failure_is_reconciled_and_sealed(self) -> None:
        original_append = pipeline.EventLog.append

        def append_then_fail(event_log: object, **kwargs: object):  # type: ignore[no-untyped-def]
            prior_sequence = event_log.sequence  # type: ignore[attr-defined]
            prior_timestamp = event_log.last_timestamp  # type: ignore[attr-defined]
            event = original_append(event_log, **kwargs)  # type: ignore[arg-type]
            if (
                kwargs.get("stage") == "INTAKE"
                and kwargs.get("event_type") == "STAGE_STARTED"
            ):
                event_log.sequence = prior_sequence  # type: ignore[attr-defined]
                event_log.last_timestamp = prior_timestamp  # type: ignore[attr-defined]
                raise OSError("synthetic post-append stage-start failure")
            return event

        with mock.patch.object(pipeline.EventLog, "append", new=append_then_fail):
            with self.assertRaises(OSError):
                self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.assert_failed_stage_is_sealed("INTAKE", "INTAKE_FAILED")
        loaded = self.pipeline._load_run(FIXED_RUN_ID)
        self.assertEqual(loaded[1]["run_id"], FIXED_RUN_ID)

    def test_stage_start_preappend_failure_records_failed_stage(self) -> None:
        original_append = pipeline.EventLog.append
        injected = False

        def fail_once_before_append(event_log: object, **kwargs: object):  # type: ignore[no-untyped-def]
            nonlocal injected
            if (
                not injected
                and kwargs.get("stage") == "INTAKE"
                and kwargs.get("event_type") == "STAGE_STARTED"
            ):
                injected = True
                raise OSError("synthetic pre-append stage-start failure")
            return original_append(event_log, **kwargs)  # type: ignore[arg-type]

        with mock.patch.object(
            pipeline.EventLog, "append", new=fail_once_before_append
        ):
            with self.assertRaises(OSError):
                self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.assertTrue(injected)
        self.assert_failed_stage_is_sealed("INTAKE", "INTAKE_FAILED")
        loaded = self.pipeline._load_run(FIXED_RUN_ID)
        self.assertEqual(loaded[1]["run_id"], FIXED_RUN_ID)

    def test_partial_event_write_is_rolled_back_before_failed_stage(self) -> None:
        original_write = pipeline.os.write
        partial_pending = False
        injected = False

        def partial_then_fail(descriptor: int, data: object) -> int:
            nonlocal partial_pending, injected
            payload = bytes(data)
            if partial_pending:
                partial_pending = False
                injected = True
                raise OSError("synthetic write failure after partial event")
            if (
                not injected
                and b'"event_type":"STAGE_STARTED"' in payload
                and b'"stage":"INTAKE"' in payload
            ):
                partial_pending = True
                midpoint = max(1, len(payload) // 2)
                return original_write(descriptor, payload[:midpoint])
            return original_write(descriptor, payload)

        with mock.patch.object(pipeline.os, "write", side_effect=partial_then_fail):
            with self.assertRaises(OSError):
                self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.assertTrue(injected)
        self.assert_failed_stage_is_sealed("INTAKE", "INTAKE_FAILED")
        loaded = self.pipeline._load_run(FIXED_RUN_ID)
        self.assertEqual(loaded[1]["run_id"], FIXED_RUN_ID)

    def test_completed_event_boundary_failure_is_reconciled_without_duplicate(self) -> None:
        original_append = pipeline.EventLog.append

        def append_then_fail(event_log: object, **kwargs: object):  # type: ignore[no-untyped-def]
            prior_sequence = event_log.sequence  # type: ignore[attr-defined]
            prior_timestamp = event_log.last_timestamp  # type: ignore[attr-defined]
            event = original_append(event_log, **kwargs)  # type: ignore[arg-type]
            if (
                kwargs.get("stage") == "INTAKE"
                and kwargs.get("event_type") == "STAGE_COMPLETED"
                and kwargs.get("outcome") == "SUCCEEDED"
            ):
                event_log.sequence = prior_sequence  # type: ignore[attr-defined]
                event_log.last_timestamp = prior_timestamp  # type: ignore[attr-defined]
                raise OSError("synthetic post-append stage-completion failure")
            return event

        with mock.patch.object(pipeline.EventLog, "append", new=append_then_fail):
            with self.assertRaises(OSError):
                self.pipeline.intake(run_id=FIXED_RUN_ID)

        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        manifest = json.loads((run_root / "run_manifest.json").read_text())
        intake_stage = next(
            item for item in manifest["stages"] if item["stage"] == "INTAKE"
        )
        self.assertEqual(intake_stage["status"], "COMPLETE")
        events = [
            json.loads(line)
            for line in (run_root / "events/events.jsonl").read_bytes().splitlines()
        ]
        self.assertEqual(
            [event["sequence"] for event in events],
            list(range(1, len(events) + 1)),
        )
        loaded = self.pipeline._load_run(FIXED_RUN_ID)
        self.assertEqual(loaded[1]["run_id"], FIXED_RUN_ID)

    def test_event_log_short_write_is_completed_before_fsync(self) -> None:
        original_write = pipeline.os.write
        short_write_used = False

        def short_write_once(descriptor: int, data: object) -> int:
            nonlocal short_write_used
            payload = bytes(data)
            if (
                not short_write_used
                and b'"event_type":"STAGE_STARTED"' in payload
                and b'"stage":"INTAKE"' in payload
            ):
                short_write_used = True
                midpoint = max(1, len(payload) // 2)
                return original_write(descriptor, payload[:midpoint])
            return original_write(descriptor, payload)

        with mock.patch.object(pipeline.os, "write", side_effect=short_write_once):
            result = self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.assertEqual(result["source_groups"], 8)
        self.assertTrue(short_write_used)
        loaded = self.pipeline._load_run(FIXED_RUN_ID)
        self.assertEqual(loaded[1]["run_id"], FIXED_RUN_ID)

    def test_final_manifest_write_failure_is_healed_without_extra_event(self) -> None:
        original_write = pipeline.write_private_json
        manifest_writes = 0

        def fail_final_manifest_once(path: Path, value: object) -> None:
            nonlocal manifest_writes
            if path.name == "run_manifest.json":
                manifest_writes += 1
                if manifest_writes == 6:
                    raise OSError("synthetic final manifest commit failure")
            original_write(path, value)

        with mock.patch.object(
            pipeline, "write_private_json", side_effect=fail_final_manifest_once
        ):
            with self.assertRaises(OSError):
                self.pipeline.intake(run_id=FIXED_RUN_ID)

        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        manifest = json.loads((run_root / "run_manifest.json").read_text())
        intake_stage = next(
            item for item in manifest["stages"] if item["stage"] == "INTAKE"
        )
        self.assertEqual(intake_stage["status"], "COMPLETE")
        event_bytes = (run_root / "events/events.jsonl").read_bytes()
        self.assertEqual(
            manifest["event_log"]["artifact"]["sha256"],
            pipeline.sha256_bytes(event_bytes),
        )
        self.assertEqual(
            manifest["event_log"]["entry_count"], len(event_bytes.splitlines())
        )
        loaded = self.pipeline._load_run(FIXED_RUN_ID)
        self.assertEqual(loaded[1]["run_id"], FIXED_RUN_ID)

    def test_selection_write_failure_seals_failed_prepare(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        original_write = pipeline.write_private_json

        def fail_selection(path: Path, value: object) -> None:
            if path.name == "calibration_selection.json":
                raise OSError("synthetic selection write failure")
            original_write(path, value)

        with mock.patch.object(
            pipeline, "write_private_json", side_effect=fail_selection
        ):
            with self.assertRaises(OSError):
                self.pipeline.prepare_calibration(run_id=FIXED_RUN_ID)
        self.assert_failed_stage_is_sealed(
            "PREPARE_CALIBRATION", "PREPARE_CALIBRATION_FAILED"
        )

    def test_validation_report_write_failure_seals_failed_validation(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        original_write = pipeline.write_private_json

        def fail_report(path: Path, value: object) -> None:
            if path.parent.name == "reports" and path.name.startswith("validation-"):
                raise OSError("synthetic validation-report write failure")
            original_write(path, value)

        with mock.patch.object(
            pipeline, "write_private_json", side_effect=fail_report
        ):
            with self.assertRaises(OSError):
                self.pipeline.validate(run_id=FIXED_RUN_ID)
        self.assert_failed_stage_is_sealed("VALIDATE", "VALIDATION_FAILED")

    def test_validation_parse_exception_seals_failed_validation(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        original_write = pipeline.write_private_json

        def fail_report(path: Path, value: object) -> None:
            if path.parent.name == "reports" and path.name.startswith("validation-"):
                raise json.JSONDecodeError("synthetic parse failure", "x", 0)
            original_write(path, value)

        with mock.patch.object(
            pipeline, "write_private_json", side_effect=fail_report
        ):
            with self.assertRaises(json.JSONDecodeError):
                self.pipeline.validate(run_id=FIXED_RUN_ID)
        self.assert_failed_stage_is_sealed("VALIDATE", "VALIDATION_FAILED")

    def test_reference_change_after_preflight_is_recorded_as_failed(self) -> None:
        class ReferenceChangingPipeline(pipeline.ReviewPipeline):
            changed = False

            def preflight_framework(self, *, require_tools: bool = True):  # type: ignore[no-untyped-def]
                result = super().preflight_framework(require_tools=require_tools)
                if not self.changed:
                    (self.repository_root / "homework/markdown/HW04.md").unlink()
                    self.changed = True
                return result

        review = ReferenceChangingPipeline(
            self.root,
            codebook_path=self.codebook_path,
            now=lambda: FIXED_TIME,
        )
        with self.assertRaisesRegex(pipeline.PipelineError, "reference is missing"):
            review.intake(run_id=FIXED_RUN_ID)

        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        manifest = json.loads((run_root / "run_manifest.json").read_text())
        self.assertEqual(manifest["run_state"], "FAILED")
        reference_stage = next(
            item
            for item in manifest["stages"]
            if item["stage"] == "REFERENCE_FREEZE"
        )
        self.assertEqual(reference_stage["status"], "FAILED")
        self.assertEqual(
            reference_stage["reason_code"], "REFERENCE_FREEZE_FAILED"
        )
        event_bytes = (run_root / "events/events.jsonl").read_bytes()
        self.assertEqual(
            manifest["event_log"]["artifact"]["sha256"],
            pipeline.sha256_bytes(event_bytes),
        )

    def test_external_configuration_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as external_directory:
            external_config = Path(external_directory) / "config.yaml"
            shutil.copy2(
                self.root / "grades/review/f2026/config.yaml", external_config
            )
            with self.assertRaisesRegex(
                pipeline.UnsafeInputError, "beneath the repository root"
            ):
                pipeline.ReviewPipeline(
                    self.root,
                    config_path=external_config,
                    codebook_path=self.codebook_path,
                    now=lambda: FIXED_TIME,
                )

    def test_cli_redacts_malformed_private_json(self) -> None:
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        manifest_path = (
            self.root
            / f"grades/review/f2026/runs/{FIXED_RUN_ID}/run_manifest.json"
        )
        pipeline.write_private_bytes(manifest_path, b"{")
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            exit_code = pipeline.main(
                [
                    "--repository-root",
                    str(self.root),
                    "--codebook",
                    str(self.codebook_path),
                    "validate",
                    "--run-id",
                    FIXED_RUN_ID,
                ]
            )
        self.assertEqual(exit_code, 1)
        self.assertIn("malformed private JSON or text artifact", stderr.getvalue())
        self.assertNotIn("{", stderr.getvalue())

    def test_cli_rejects_schema_invalid_config_without_traceback(self) -> None:
        invalid_config = self.root / "invalid-config.yaml"
        invalid_config.write_text("configuration_id: invalid-v1\n", encoding="utf-8")
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            exit_code = pipeline.main(
                [
                    "--repository-root",
                    str(self.root),
                    "--config",
                    str(invalid_config),
                    "--codebook",
                    str(self.codebook_path),
                    "intake",
                    "--run-id",
                    FIXED_RUN_ID,
                ]
            )
        self.assertEqual(exit_code, 1)
        self.assertIn("configuration fails", stderr.getvalue())
        self.assertNotIn("Traceback", stderr.getvalue())
        self.assertFalse((self.root / "grades/review/f2026/runs").exists())

    def test_duplicate_solution_members_are_triaged_without_crash(self) -> None:
        archive_path = next((self.root / "grades/submissions/hw01").glob("*.zip"))
        archive_path.write_bytes(
            zip_bytes(
                [
                    ("solution.pdf", pipeline._minimal_pdf_bytes("first")),
                    ("nested/solution.pdf", pipeline._minimal_pdf_bytes("second")),
                ]
            )
        )
        result = self.pipeline.intake(run_id=FIXED_RUN_ID)
        self.assertEqual(result["eligible"], 7)
        self.assertEqual(result["human_triage"], 1)
        validated = self.pipeline.validate(run_id=FIXED_RUN_ID)
        self.assertEqual(validated["status"], "PASS")

    def test_missing_calibration_slot_blocks_without_partial_selection(self) -> None:
        next((self.root / "grades/submissions/hw04").glob("*.zip")).unlink()
        self.pipeline.intake(run_id=FIXED_RUN_ID)
        with self.assertRaisesRegex(pipeline.ContractError, "missing slots"):
            self.pipeline.prepare_calibration(run_id=FIXED_RUN_ID)
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        manifest = json.loads((run_root / "run_manifest.json").read_text())
        prepare = next(
            item
            for item in manifest["stages"]
            if item["stage"] == "PREPARE_CALIBRATION"
        )
        self.assertEqual(prepare["reason_code"], "CALIBRATION_SLOTS_MISSING")
        self.assertFalse(
            (run_root / "manifests/calibration_selection.json").exists()
        )

    def test_non_utf8_filename_fails_after_reference_freeze(self) -> None:
        directory = os.fsencode(self.root / "grades/submissions/hw01")
        filename = b"invalid-\xff-name.pdf"
        descriptor = os.open(os.path.join(directory, filename), os.O_CREAT | os.O_WRONLY, 0o600)
        try:
            os.write(descriptor, pipeline._minimal_pdf_bytes("invented"))
        finally:
            os.close(descriptor)
        with self.assertRaisesRegex(pipeline.UnsafeInputError, "non-UTF-8"):
            self.pipeline.intake(run_id=FIXED_RUN_ID)
        run_root = self.root / f"grades/review/f2026/runs/{FIXED_RUN_ID}"
        manifest = json.loads((run_root / "run_manifest.json").read_text())
        reference = next(
            item
            for item in manifest["stages"]
            if item["stage"] == "REFERENCE_FREEZE"
        )
        intake = next(
            item for item in manifest["stages"] if item["stage"] == "INTAKE"
        )
        self.assertEqual(reference["status"], "COMPLETE")
        self.assertEqual(intake["status"], "FAILED")

    def test_pdf_metadata_identity_is_detected_with_unicode_normalization(self) -> None:
        review = pipeline.ReviewPipeline(
            self.root,
            codebook_path=self.codebook_path,
            now=lambda: FIXED_TIME,
        )
        status, codes = review._identity_scan(
            pipeline._minimal_pdf_bytes("answer", author="e\u0301lan"),
            artifact_id="ART-000001",
            identities=[
                {
                    "subjects": [
                        {
                            "source_identity_key": "synthetic",
                            "display_name": "élan",
                            "lms_user_id": "900001",
                        }
                    ],
                    "original_files": [],
                }
            ],
            private_tmp=self.root / "private-pdf-test",
        )
        self.assertEqual(status, "FAIL")
        self.assertIn("IDENTITY_DISPLAY_NAME_PRESENT", codes)


if __name__ == "__main__":
    unittest.main()
