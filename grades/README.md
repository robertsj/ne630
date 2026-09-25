# Course-grading workspace

This tree deliberately separates reusable review framework files from private
course records and generated review state.

## Version-controlled framework

The following material is safe to track when it contains no copied student
content or identifying data:

- `review/<term>/config.yaml` and framework source;
- schemas, protocols, and documentation;
- tests and wholly synthetic fixtures.

Synthetic fixtures must use invented names, identifiers, prose, and files.
Student-derived examples remain private even after pseudonymization.

## Private source records

`submissions/` contains original student work and is ignored by Git. Original
bytes are immutable inputs to the review pipeline. File names, LMS identifiers,
and any other identity-bearing metadata may appear only in this source tree or
in the restricted identity map.

## Private generated state

For each term, generated artifacts live under `review/<term>/runs/<run_id>/`.
This includes manifests, queues, dossiers, rendered or sanitized copies,
reviews, logs, validation reports, and temporary work. Identity maps and other
direct identifiers live under `review/<term>/restricted/`. Both trees are
ignored by Git; pseudonymization does not make an education record suitable
for source control.

Runtime code must create private directories with mode `0700` and private files
with mode `0600`. Before staging framework changes, verify the boundary with:

```text
git check-ignore -q grades/submissions/example
git check-ignore -q grades/review/f2026/runs/example
git check-ignore -q grades/review/f2026/restricted/example
git check-ignore -q grades/review/f2026/config.yaml && exit 1 || true
```

## Review CLI

Run the hermetic synthetic demonstration before any live processing:

```text
python3 grades/review/f2026/review_pipeline.py self-test
```

The test suite never reads `grades/submissions/`. Live `intake` creates a new
private run, freezes the policy/statements/keys/configuration/protocol/schemas,
and records deterministic pseudonymized manifests without executing student
TeX, Makefiles, scripts, notebooks, or links. See
`review/f2026/setup_review.md` for lifecycle and authorization details.

Production packet creation is fail-closed: deterministic selection is followed
by a separate sandboxed raster stage that creates an immutable eight-PDF,
image-only review set. The instructor inspects those exact bytes and binds an
attestation to the review-set ID and SHA-256; sanitized derivatives are supplied
before that review set is built. `resume-calibration` re-verifies the locked
selection, source/request/review-set/accepted hash chain, adopted decision, and
canonical inert-PDF structure before any solution is labeled product-blinded.
