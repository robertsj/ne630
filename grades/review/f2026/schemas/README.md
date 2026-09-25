# Review data contracts

These Draft 2020-12 JSON Schemas define every persisted artifact in the Fall
2026 pilot. Each schema is standalone so the locally available validator can
check it without network access or cross-file reference resolution.

## Contract catalog

| Schema | Artifact | Privacy class |
| --- | --- | --- |
| `config.schema.json` | `config.yaml` | tracked framework |
| `reference_manifest.schema.json` | frozen policy, statement, key, configuration, and protocol hashes | private run state |
| `identity_map.schema.json` | source identities and original paths mapped to pseudonyms | restricted |
| `run_manifest.schema.json` | run provenance, stages, counts, and artifact index | private run state |
| `submission_manifest.schema.json` | pseudonymized deterministic intake record | private run state |
| `build_report.schema.json` | nonexecution or future sandboxed-build record | private run state |
| `review_queue.schema.json` | deterministic work queue | private run state |
| `calibration_selection.schema.json` | seed-locked eight-item selection | private run state |
| `calibration_clearance_request.schema.json` | eight locked source scan records awaiting inert review-set staging | private run state |
| `calibration_clearance_review_set.schema.json` | immutable eight-item image-only visual-review set | restricted run state |
| `calibration_clearance.schema.json` | adopted human clearance and accepted PDF references | restricted run state |
| `calibration_packet_manifest.schema.json` | product-blinded packet contents | restricted run state |
| `dossier_data.schema.json` | structured source for a blinded dossier | private run state |
| `render_manifest.schema.json` | deterministic Markdown rendering provenance | private run state |
| `review.schema.json` | qualitative product-calibration review | private run state |
| `calibration_reconciliation.schema.json` | post-calibration reconciliation | private run state |
| `event.schema.json` | one append-only `events.jsonl` record | private run state |
| `human_decision.schema.json` | one append-only human-decision record | restricted run state |
| `validation_report.schema.json` | schema, privacy, hash, and cross-artifact checks | private run state |

Free-form Markdown files are not schema-validated. `dossier.md` and
`review_queue.md` are deterministic renders of structured JSON; their source,
template, renderer, and output hashes are recorded by `render_manifest`.

## Identifier and serialization rules

- Schema version is `1.0.0`.
- A run ID is `run-YYYYMMDDTHHMMSSZ-xxxxxxxxxxxx`, with twelve lowercase hex
  characters as the collision suffix.
- A person-level pseudonym is `S` followed by at least three digits and is
  stable across this pilot. Allocation is recorded only in the restricted map.
- A nonidentifying submission record ID is
  `<assignment>-<pseudonym>-V<attempt>`, for example `HW02-S014-V01`.
- Source/LMS submission IDs, names, usernames, and original basenames are
  forbidden outside `identity_map` and the original submission tree.
- Record IDs use an uppercase type prefix and a six-or-more digit sequence:
  `ART-000001`, `EVT-000001`, `DEC-000001`, `FND-000001`, and `OBS-000001`.
- Decision lines are immutable. A new adopted decision may name the earlier
  decision it supersedes; the earlier JSONL record is never rewritten.
- Timestamps use UTC seconds as `YYYY-MM-DDTHH:MM:SSZ`. Semantic validation
  must reject impossible calendar values and enforce event chronology.
- Paths are normalized POSIX paths relative to the run or repository root.
  Absolute paths, backslashes, NULs, and `..` components are invalid.
- SHA-256 values are 64 lowercase hexadecimal characters.
- Persisted JSON uses the canonical settings in `config.yaml`. Artifact hashes
  cover the exact bytes on disk, including the configured terminal newline.

## Evidence rules

Consequential observations and every `QUESTION` carry typed evidence locators.
A locator identifies the immutable artifact and its hash, source role,
sanitized logical path, extraction method, and the narrowest available page,
line, JSON-pointer, archive-member, problem, or subpart anchor. Bounded excerpts
are optional and never substitute for an artifact hash and location.

Product-calibration evidence is limited to `SUBMITTED_SOLUTION`,
`PROBLEM_STATEMENT`, and `SOLUTION_KEY`. Product packets, dossiers, and reviews
must not expose discourse, identity, original filenames, intake/late flags, or
route guesses.

Automated PDF scans are denylist checks: they may report `FAIL` or
`NEEDS_HUMAN_TRIAGE`, but they cannot by themselves establish visual blinding.
Identity matches in extracted page text require a sanitized derivative.
Metadata/raw-byte-only matches are normalized into the canonical image-only
candidate but are not assumed nonvisual; they and unextractable page images
remain for human visual clearance.
`prepare-calibration` therefore emits a clearance request for all eight locked
sources. `stage-calibration-review-set` sandbox-renders the chosen source or
derivative and rebuilds canonical image-only PDFs. An adopted
`IDENTITY_CLEARANCE` decision and matching clearance record bind the exact
review-set ID, manifest hash, and eight PDF hashes. Packet manifests preserve
the automated status and codes, cite that review set, clearance, and decision,
and record `PASS` only as the final combined human-visible-identity outcome.

## Validation beyond JSON Schema

`validate` must additionally check invariants that JSON Schema cannot express:

1. IDs are unique and all cross-artifact references resolve within one run.
2. Declared counts equal actual records; assignment, pseudonym, and version
   embedded in each submission record ID agree with its fields.
3. Hashes match exact bytes and every path resolves beneath its allowed root
   without symlink escape.
4. Identity mappings are one-to-one, restricted directories are mode `0700`,
   and restricted/private files are mode `0600`.
5. The reference set has exactly one statement and one key for each homework.
6. Calibration locks before substantive review and contains exactly one
   eligible item per assignment and package stratum, for eight total.
7. Clearance requests resolve to the locked selection, contain eight
   semantically unique submission records, and preserve each assignment,
   stratum, source-payload hash, source-solution hash, scan status, and scan-code
   set. Review sets and adopted clearances contain the same eight
   assignment/submission pairs and match those request facts.
8. Each accepted PDF is the exact canonical image-only artifact in an immutable
   review set and is bound to an adopted `IDENTITY_CLEARANCE` decision whose
   evidence names both the review-set and clearance hashes. Packet sanitization
   fields must reproduce the corresponding clearance item.
9. Product packets and reviews obey blinding, evidence, excerpt, comment, and
   no-numeric-scoring constraints.
10. Student code remains unexecuted while the sandbox decision is unresolved.
11. Event and decision sequences are contiguous and chronological; decision
   supersession and approval references are consistent.
12. Feedback remains unreleased unless an adopted instructor decision
    explicitly authorizes it.
