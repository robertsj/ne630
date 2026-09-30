---
name: "homework-solution-transcriber"
description: "Transcribe handwritten homework from prompt, reference solution, and scan; return faithful transcribedsolution."
---

# Homework Solution Transcriber

## Contract

Accept exactly these task inputs, whether supplied as paths, attachments, pasted text, or clearly labeled sections:

- `homeworkprompt`: the student-facing prompt, often NE630 Canvas HTML.
- `referencesolution`: the instructor/reference solution, often LaTeX.
- `handwrittensolution`: the student's scanned or photographed handwritten solution, often a PDF or page images.

Return exactly one task output named `transcribedsolution`. Put the transcription in that output as Markdown unless the caller gives a stricter schema. Do not grade, score, solve missing work, or rewrite the student's reasoning.

## Procedure

1. Normalize the prompt into a problem map. Extract problem numbers, subparts, constants, requested outputs, and equations; for Canvas HTML, read equation text from `data-equation-content`, `alt`, or `title` attributes rather than describing rendered equation images. Complete this step when each prompt problem has a short reference label and expected subparts.

2. Normalize the reference solution into an orientation map. Split LaTeX at problem markers such as `\noindent{\bf Problem ...}` and solution markers such as `SOLUTION`, `DRAFT SOLUTION`, or `SOLUTION (adapted...)`; keep macros and units as clues for symbols, not as text to copy into the student transcription. Complete this step when each prompt problem has any matching reference equations, final-answer patterns, and unit conventions.

3. Inspect every page of `handwrittensolution`. If the input is a PDF, render or view every page at readable resolution before transcribing; if it is a multi-image set, preserve page order from filenames, archive order, or the caller's ordering. Complete this step when every visible page has been assigned to a prompt problem, marked as cover/discourse, or marked `unassigned`.

4. Use OCR only when it is warranted and available. Check for page-level OCR tooling such as `tesseract` when the pages contain substantial typed text, AI discourse, cover sheets, prompt snippets, or long prose that would slow manual transcription. Treat OCR output as a draft aid: compare it against the page image before using it, and do not rely on OCR for handwritten equations, isotope notation, superscripts/subscripts, signs, decimal points, units, or boxed answers. Complete this step when OCR has either produced verified helper text or has been deliberately skipped as low-value for the page.

5. Transcribe only what the student wrote. Preserve incorrect arithmetic, algebra, units, notation, crossed-out work that remains legible, and final boxes. Use LaTeX for equations and Markdown for prose, tables, and lists. Use the prompt, reference solution, and verified OCR only to disambiguate likely symbols or problem boundaries; never insert a reference-solution step or OCR hallucination that is absent from the student work. Complete this step when every legible mathematical line and explanatory sentence has a corresponding transcription.

6. Mark uncertainty explicitly. Use `[illegible]` for unreadable text, `[uncertain: ...]` for a best-effort reading, `[not present]` for a prompt subpart with no visible student response, and `[page N, location]` notes for material whose problem assignment is uncertain. Complete this step when no ambiguous reading is silently hidden.

7. Assemble `transcribedsolution` with this structure:

```markdown
# Transcribed Solution

Source: <handwrittensolution identifier>
Prompt: <homeworkprompt identifier>
Reference: <referencesolution identifier>

## Problem 1

### Student Work
<faithful transcription>

### Notes
- <only uncertainty, page-boundary, OCR-use, or illegibility notes; omit if none>

## Problem 2
...

## Unassigned or Non-solution Pages
<cover sheets, AI discourse transcripts, blank pages, or pages that cannot be matched; omit if none>
```

Complete this step when the output contains one section per prompt problem and any extra pages are accounted for.

8. Verify fidelity before returning. Compare the transcription against the handwritten pages one more time, checking boxed answers, exponents, signs, isotope superscripts/subscripts, decimal points, units, and problem numbering. Confirm any OCR-assisted text still matches the visible page. Complete this step when the returned `transcribedsolution` is a transcription of the student submission rather than a corrected solution.

## NE630 Conventions

- Student-facing homework prompts live as Canvas-ready HTML fragments and may store equations in `img.equation_image` attributes, especially `data-equation-content`.
- Instructor solutions are LaTeX and may include course macros such as `\isoAZ`, `\ISOA`, `\mega\electronvolt`, and `\atomicmassunit`; preserve the student's notation rather than normalizing everything to these macros.
- Handwritten NE630 submissions may mix photographed paper, tablet writing, typed prompt snippets, AI-discourse PDFs, and nested zip submissions. Transcribe the student's solution pages; list non-solution pages under `Unassigned or Non-solution Pages` instead of discarding them silently.
- OCR can reduce effort for typed and prose-heavy pages, but visual inspection remains required for every page and is authoritative for handwritten mathematics.
