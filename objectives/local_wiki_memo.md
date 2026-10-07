# NE 630 Local Wiki Memo

## Idea

Build a local NE 630 wiki seeded from the course's learning-objective analysis, readings, handouts, notebooks, homework statements, reference solutions, and local grading artifacts. The first generated layer should use semantic coupling to propose hyperlinks among objectives, concepts, readings, lessons, homework problems, worked examples, solution atoms, and AI-dialogue/grading evidence.

This is a future course-knowledge project, separate from the immediate HW01-HW11 grading push.

## Recommended Shape

Use a local-first Markdown wiki with machine-readable metadata:

- Human-facing layer: Obsidian-friendly Markdown pages.
- Agent-facing layer: OpenClaw `memory-wiki` or an importable Open Knowledge Format bundle.
- Canonical course source layer: existing NE 630 files remain authoritative.
- Rebuildable cache layer: embeddings, chunks, and semantic-link candidates in SQLite, LanceDB, or JSONL.

The likely path is to generate a course wiki under a dedicated local folder, then either point OpenClaw `memory-wiki` at it in isolated mode or import generated OKF-style concept pages into the OpenClaw wiki vault.

## Page Types

- `concept`: reactor theory concepts such as resonance escape probability, diffusion length, reactivity, point kinetics, and cross sections.
- `learning_objective`: objectives from the local LO analysis.
- `lesson`: handout, reading, notebook, and page-level lesson material.
- `homework_problem`: statement, prompt structure, associated objectives, and required concepts.
- `reference_solution`: instructor solution atoms and evidence.
- `example`: notebook cells, worked derivations, figures, or code examples.
- `source`: raw imported material with provenance.
- `synthesis`: maintained summaries across lessons, objectives, or assessment evidence.

## Candidate Link Types

- `assesses`: homework problem to learning objective.
- `explains`: reading, handout, or notebook to concept.
- `requires`: problem or objective to prerequisite concept.
- `worked-example-for`: example to problem, objective, or concept.
- `extends`: advanced concept to earlier concept.
- `evidence-for`: source chunk to claim.
- `dialogue-about`: extracted AI-dialogue artifact to problem or concept.

Each generated edge should carry source id, target id, relation type, confidence, evidence path/chunk, generation method, and review status.

## Storage Requirements

- Stable ids for objectives, concepts, lessons, homework problems, solution atoms, and dialogue artifacts.
- YAML frontmatter on Markdown pages for ids, tags, source paths, privacy tier, freshness, and generated/human ownership.
- Provenance for every generated claim or link.
- Generated blocks clearly marked so human edits survive regeneration.
- Privacy separation between public course knowledge and private grading/student artifacts.
- A compile/lint step after imports to catch broken links, stale pages, contradictory claims, and missing provenance.

## Initial Seed Sources

- `/home/robertsj/Classes/ne630/objectives/`
- `/home/robertsj/Classes/ne630/homework/markdown/`
- `/home/robertsj/Classes/ne630/homework/html/`
- `/home/robertsj/Classes/ne630/homework/solutions/`
- `/home/robertsj/Classes/ne630/handouts/`
- `/home/robertsj/Classes/ne630/notebooks/`
- `/home/robertsj/Classes/ne630_local_grading/`

The grading tree should contribute only local-private provenance and assessment context unless explicitly exported into a sanitized course-knowledge layer.
