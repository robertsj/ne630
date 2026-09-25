# NE 630 Fall 2026 Homework Review Pilot

Status: **Intake/selection and fail-closed human-clearance/resume CLI implemented and demonstrated on wholly synthetic records; live intake remains pending**

Scope: HW01–HW04

Review mode: qualitative product calibration with formative-shadow process analysis; numeric scoring disabled.

## Operational

- The current Fall 2026 syllabus is the submission-policy authority.
- `homework/markdown/HW01.md` through `HW04.md` are the authoritative problem statements.
- `homework/solutions/hw01.tex` through `hw04.tex` are the product-review keys. The keys are references, not infallible exact-answer constraints.
- Original submissions remain unchanged under Git-ignored `grades/submissions/`.
- Reusable framework files are version controlled; all run products live under Git-ignored `runs/<run_id>/`.
- Derived records use pseudonyms but remain private education records. The identity map is restricted to mode `0600` inside Git-ignored `restricted/`; run directories use mode `0700` and their files use mode `0600`.
- Intake freezes its tracked framework and references before it reads any
  student byte, then streams deterministic hashes, validates ZIP members to EOF under
  configured limits, and runs bounded PDF metadata/text extraction inside a
  no-network Bubblewrap namespace.
- Visual-review PDFs are rendered by frozen `pdftoppm` inside that namespace,
  stripped to baseline RGB page images, and rebuilt by the pipeline as a
  canonical image-only PDF with no metadata, text, actions, forms, links, or
  attachments. The raw PDF is never presented as the review candidate.
- No student Makefile, TeX source, script, notebook, or embedded command is executed.
- Product review precedes and is isolated from discourse review.
- The pilot calibration sample is selected before substantive content review using the seed recorded in `config.yaml`.
- Workflow stages are named in `config.yaml`. The CLI and its self-test do not
  run live `INTAKE`; no real submission content had been processed as of the
  2026-09-24 implementation checkpoint.
- Persisted artifacts follow the standalone contracts and cross-artifact invariants cataloged in `schemas/README.md`.
- Canvas export files are grouped by assignment and numeric LMS user ID. The
  export has no Canvas submission or attempt ID, so the restricted map labels
  the source submission ID explicitly as a synthesized group ID; `V01` means
  first locally observed immutable payload, with later changed payloads taking
  the next version while unchanged payloads retain their version.

## Proposed, not adopted as grading policy

- The five-criterion 100-point rubric reproduced in `config.yaml`.
- Archive resource limits. They are used only as processing guardrails; a limit event is not an academic penalty.
- Full discourse coding and seeded audit coverage after product calibration.

## Unresolved instructor decisions

1. Per-problem points, partial-credit conventions, and numerical/citation tolerances.
2. Whether later automated runs may suggest numeric criterion scores.
3. The authoritative source of route declarations and assignment-specific Canvas deadlines or overrides.
4. Repair deadlines and prior use of the syllabus's one scan/document-format resubmission.
5. Accommodation handling for any affected submission.
6. A verified disposable build sandbox and its limits; until then ZIP builds are `NOT_RUN_NO_SANDBOX`.
7. Retention period, appeal/contest path, and later discourse-audit sampling rate.

## Runnable entry point

The local CLI is `review_pipeline.py`. Its expanded `self-test` suite is
hermetic: it constructs invented PDF/ZIP submissions in a temporary Git
repository, proves that student Makefiles are never executed, exercises all
eight calibration slots, checks malformed/adversarial inputs, and validates
the resulting private artifacts. It also checks archive resource containment,
tamper detection, stage/event reconciliation, and identifier-safe validation
failures. Its invented artifacts exercise the explicit human-clearance and
resume gate without processing live submissions.

From the repository root:

```text
python3 grades/review/f2026/review_pipeline.py self-test
python3 grades/review/f2026/review_pipeline.py intake
python3 grades/review/f2026/review_pipeline.py prepare-calibration --run-id RUN_ID
python3 grades/review/f2026/review_pipeline.py stage-calibration-review-set --run-id RUN_ID
# The instructor now opens every review_pdfs path returned above.
python3 grades/review/f2026/review_pipeline.py record-calibration-clearance --run-id RUN_ID --review-set-id RSET_ID --review-set-sha256 SHA256 --actor-id INSTRUCTOR_ID --attest-visual-clearance
python3 grades/review/f2026/review_pipeline.py resume-calibration --run-id RUN_ID
python3 grades/review/f2026/review_pipeline.py validate --run-id RUN_ID
```

The run-targeting commands accept `--run-id`. Omitting it is allowed only when
exactly one run exists; the CLI never silently chooses the newest run.
`prepare-calibration` refuses a partial sample and locks nothing unless all
eight assignment/package slots exist. It then writes the locked selection and
an eight-item clearance request and returns a successful `status: BLOCKED`
checkpoint without writing packets. Automated denylist checks can
disprove blinding but cannot prove that an unknown visible or handwritten name
is absent.

`stage-calibration-review-set` converts the eight sources to immutable inert
review PDFs. Pass repeated `--sanitized-derivative RECORD_ID=PDF` arguments to
replace any source flagged by the request; a new immutable review-set version
is created each time. The instructor personally inspects every page at the
returned `review_pdfs` paths. `record-calibration-clearance` accepts no PDF
input: it requires the exact returned `RSET` ID and manifest SHA-256, then
records the visual attestation, an adopted `IDENTITY_CLEARANCE` decision, and
those same eight artifact references.

The local actor ID is an operator attestation, not a cryptographic identity
proof. The authorized agent must not issue this command on the instructor's
behalf; the instructor runs it personally (or gives an explicit, review-set-
specific confirmation through the trusted session) after page inspection.
Inertness is machine-enforced and is not part of the human claim.

`resume-calibration` verifies that the request, clearance, decision, locked
selection, review-set hash, accepted inert bytes, and automated scan facts still agree; only then does
it complete `PREPARE_CALIBRATION` and write the blinded packet and dossier
artifacts. Any missing, stale, altered, rejected, or mismatched evidence remains
fail-closed rather than being treated as a clearance.

As its stages occur, a run writes its `run_manifest.json`, reference manifest,
event log, human-decision log, versioned review queues, per-submission
manifests, build/nonexecution reports, calibration selection, clearance
request, adopted clearance, packets, structured dossiers and renders, later
reviews/reconciliation, and validation reports beneath `runs/<run_id>/`.
These are private handoff artifacts and remain ignored by Git. Student-facing
release remains disabled.
