#!/usr/bin/env python3
"""Extract NE630 Route-B AI-dialogue artifacts from a Canvas ZIP.

This script initializes only the AI-dialogue grading workspace:

  <grading-root>/<assignment>/raw/
  <grading-root>/<assignment>/extracted/ai_dialogues/

It preserves full nested ZIP submissions for detected Route-B submissions, but
the smaller dialogue view contains only discourse/transcript/screenshot-like
artifacts and LaTeX include dependencies.
"""

import argparse
import csv
import hashlib
import io
import re
import shutil
import subprocess
import zipfile
from pathlib import Path, PurePosixPath


DIALOGUE_RE = re.compile(
    r"(discourse|transcript|dialogue|conversation|chatgpt|gpt|claude|"
    r"copilot|(^|[_\W])ai([_\W]|$)|screenshot)",
    re.IGNORECASE,
)
INCLUDE_RE = re.compile(
    r"\\(?:input|include|verbatiminput|lstinputlisting|includegraphics)"
    r"(?:\[[^\]]*\])?\{([^}]+)\}"
)
TEXT_EXTS = (".tex", ".txt", ".md", ".csv", ".json", ".log")
IMAGE_EXTS = (".pdf", ".png", ".jpg", ".jpeg")
PROMPT_TEXT_EXTS = (".txt", ".md", ".tex", ".pdf")

THEMES = [
    {
        "id": "P01",
        "theme": "Route B disclosure and AI-use setup",
        "representative_prompt": (
            "I am using the AI-disclosure route for this homework; follow the "
            "course requirements and preserve the complete visible dialogue."
        ),
        "common_variations": (
            "Opening notice; Route B/full-disclosure policy; session metadata; "
            "what must be included in the discourse record."
        ),
        "patterns": [
            r"route\s*b",
            r"full[- ]disclosure",
            r"visible dialogue",
            r"ai[- ]disclosure",
            r"generative ai",
            r"discourse",
            r"session metadata",
        ],
    },
    {
        "id": "P02",
        "theme": "Submission package and generated files",
        "representative_prompt": (
            "Create the self-contained Route B submission package with solution, "
            "discourse transcript, Makefile, PDFs, and any supporting files."
        ),
        "common_variations": (
            "Make the ZIP; build solution.tex and discourse.tex; include a "
            "Makefile; compile the PDFs; prepare final submission files."
        ),
        "patterns": [
            r"\bzip\b",
            r"makefile",
            r"submission package",
            r"solution\.tex",
            r"discourse\.tex",
            r"compile",
            r"pdf",
            r"archive",
        ],
    },
    {
        "id": "P03",
        "theme": "LaTeX formatting and document templates",
        "representative_prompt": (
            "Put the homework solution and transcript into my usual LaTeX format "
            "with clean problem sections and course headers."
        ),
        "common_variations": (
            "Use an existing template; format headers; preserve equations; make "
            "the document compile; transcribe handwritten work into LaTeX."
        ),
        "patterns": [
            r"latex",
            r"overleaf",
            r"documentclass",
            r"template",
            r"format",
            r"typeset",
            r"transcribe",
            r"handwritten",
        ],
    },
    {
        "id": "P04",
        "theme": "Detailed breakdown and source-of-equation explanation",
        "representative_prompt": (
            "Give a detailed breakdown of the calculations and explain where the "
            "equations and numerical values come from."
        ),
        "common_variations": (
            "Show the logic; explain assumptions; state where constants come "
            "from; walk through the calculation step by step."
        ),
        "patterns": [
            r"detailed breakdown",
            r"logic",
            r"where (you are )?getting",
            r"equations?",
            r"numerical values",
            r"step[- ]by[- ]step",
            r"walk me through",
            r"explain",
        ],
    },
    {
        "id": "P05",
        "theme": "Guided part-by-part tutoring",
        "representative_prompt": (
            "Do not give all the answers at once; work through the homework "
            "part by part and check each step as I go."
        ),
        "common_variations": (
            "Socratic workflow; one problem at a time; wait for my answer; "
            "confirm before moving on."
        ),
        "patterns": [
            r"don't give all",
            r"do not give all",
            r"work through",
            r"part by part",
            r"one at a time",
            r"moving to",
            r"ready for",
        ],
    },
    {
        "id": "P06",
        "theme": "Check or verify existing solution work",
        "representative_prompt": (
            "Check my solution or handwritten work, verify the calculations, and "
            "tell me what is correct or needs fixing."
        ),
        "common_variations": (
            "Check solutions and work; verify a numeric answer; review handwritten "
            "pages; confirm whether my setup is right."
        ),
        "patterns": [
            r"\bcheck\b",
            r"\bverify\b",
            r"correct",
            r"what i have",
            r"my work",
            r"solution",
            r"handwritten",
        ],
    },
    {
        "id": "P07",
        "theme": "Problem 1 point-source flux setup",
        "representative_prompt": (
            "Use the uncollided point-source flux equation to compute the flux "
            "from a 1 Ci neutron source at 1 m."
        ),
        "common_variations": (
            "Apply Eq. 2.9; convert 1 m to 100 cm; assume one neutron per "
            "disintegration; neglect air attenuation."
        ),
        "required_any": [
            [
                r"point source",
                r"1\s*ci",
                r"uncollided flux",
                r"eq\.?\s*\(?2\.9\)?",
                r"3\.7\s*[x*]\s*10",
            ]
        ],
        "patterns": [
            r"point source",
            r"1\s*ci",
            r"uncollided flux",
            r"flux",
            r"eq\.?\s*\(?2\.9\)?",
            r"3\.7\s*[x*]\s*10",
        ],
    },
    {
        "id": "P08",
        "theme": "Shield attenuation and factor-of-ten reduction",
        "representative_prompt": (
            "Use exponential attenuation to find the shield macroscopic cross "
            "section or the distance needed for the same factor-of-ten reduction."
        ),
        "common_variations": (
            "Solve exp(-Sigma x)=1/10; use a 1 m or 0.5 m shield; combine "
            "attenuation with inverse-square distance."
        ),
        "patterns": [
            r"shield",
            r"factor of 10",
            r"factor-of-10",
            r"attenuation",
            r"e\^\(-",
            r"exp\(-",
            r"distance",
            r"0\.5\s*m",
        ],
    },
    {
        "id": "P09",
        "theme": "Problem 2 water and steam macroscopic cross sections",
        "representative_prompt": (
            "Compute the macroscopic total cross section of water, steam, a "
            "steam-water mixture, and room-temperature water."
        ),
        "common_variations": (
            "Use BWR densities; compare water and steam; volume-weight the "
            "mixture; atmospheric water density."
        ),
        "required_any": [
            [
                r"water",
                r"steam",
                r"boiling water reactor",
                r"1000\s*psi",
                r"0\.74",
                r"0\.036",
            ]
        ],
        "patterns": [
            r"water",
            r"steam",
            r"boiling water reactor",
            r"1000\s*psi",
            r"0\.74",
            r"0\.036",
            r"mixture",
            r"atmospheric",
        ],
    },
    {
        "id": "P10",
        "theme": "Microscopic-to-macroscopic cross-section conversion",
        "representative_prompt": (
            "Convert microscopic cross sections in barns and material density "
            "into macroscopic total cross section in inverse centimeters."
        ),
        "common_variations": (
            "Use number density; apply Avogadro's number; account for H and O "
            "atoms per molecule; convert barns to cm^2."
        ),
        "patterns": [
            r"macroscopic",
            r"microscopic",
            r"cross section",
            r"\bsigma\b",
            r"\bsigma_t\b",
            r"barn",
            r"number density",
            r"avogadro",
            r"molecules?/cm",
        ],
    },
    {
        "id": "P11",
        "theme": "Problem 3 enriched UO2 macroscopic cross section",
        "representative_prompt": (
            "Compute the macroscopic total cross section for enriched UO2 using "
            "isotopic abundance, molar mass, density, and microscopic cross sections."
        ),
        "common_variations": (
            "Average U-235/U-238 masses; include oxygen; use 4% enrichment; "
            "calculate UO2 number density and final Sigma_t."
        ),
        "required_any": [
            [
                r"uo2",
                r"u[- ]?235",
                r"u[- ]?238",
                r"enrich",
                r"uranium",
                r"607\.5",
            ]
        ],
        "patterns": [
            r"uo2",
            r"u[- ]?235",
            r"u[- ]?238",
            r"enrich",
            r"uranium",
            r"4%",
            r"10\.5",
            r"607\.5",
        ],
    },
    {
        "id": "P12",
        "theme": "Uploaded problem statements, figures, and supporting files",
        "representative_prompt": (
            "Use the attached problem statement, equation sheet, lecture notes, "
            "or handwritten pages as the basis for the homework work."
        ),
        "common_variations": (
            "Uploaded screenshots; attached Eq. 2.9; uploaded handwritten work; "
            "lecture notes or textbook excerpts."
        ),
        "patterns": [
            r"uploaded",
            r"attached",
            r"image",
            r"screenshot",
            r"photo",
            r"file",
            r"lecture",
            r"textbook",
        ],
    },
    {
        "id": "P13",
        "theme": "Short numeric answer checks",
        "representative_prompt": (
            "Here is my numerical answer for the current step; check whether it "
            "is right before we continue."
        ),
        "common_variations": (
            "Single-value replies such as 178 cm, 2.47E22, 1.17, 0.057, 0.725, "
            "or 1.01."
        ),
        "patterns": [
            r"^\s*[-+]?\d+(\.\d+)?(e[-+]?\d+)?\s*([a-z/%^-]+)?\s*$",
        ],
    },
    {
        "id": "P14",
        "theme": "Fission channel and fission-fragment setup",
        "representative_prompt": (
            "Identify or use a representative neutron-induced fission channel "
            "and reason about the resulting fission fragments."
        ),
        "common_variations": (
            "Find a published fission channel; discuss fission fragments; "
            "distinguish prompt neutrons from fragment products."
        ),
        "required_any": [[r"fission"]],
        "patterns": [
            r"fission channel",
            r"fission fragments?",
            r"fragments?",
            r"u[- ]?235",
            r"thermal neutron",
        ],
    },
    {
        "id": "P15",
        "theme": "Neutron-rich fragments and beta decay",
        "representative_prompt": (
            "Explain why fission fragments are neutron rich and why beta-minus "
            "decay is the likely principal decay mode."
        ),
        "common_variations": (
            "Why fragments are neutron rich; beta decay changes a neutron into "
            "a proton; antineutrinos/gammas; principal decay mode."
        ),
        "patterns": [
            r"neutron rich",
            r"beta decay",
            r"beta[- ]minus",
            r"principal decay",
            r"antineutrino",
            r"fragments? is most likely",
        ],
    },
    {
        "id": "P16",
        "theme": "Reactor power, fission rate, and energy release",
        "representative_prompt": (
            "Use reactor power, operating time, and energy per fission to compute "
            "fission rate, total fissions, or fuel consumption."
        ),
        "common_variations": (
            "MW(t) for one year; energy per fission; convert joules and MeV; "
            "calculate atoms or mass consumed."
        ),
        "patterns": [
            r"reactor operates",
            r"\bmw\(t\)",
            r"power",
            r"one year",
            r"1 year",
            r"fission rate",
            r"energy per fission",
            r"fuel",
        ],
    },
    {
        "id": "P17",
        "theme": "Multiplication factor and criticality behavior",
        "representative_prompt": (
            "Interpret a multiplication factor and describe the long-term neutron "
            "population behavior of a subcritical, critical, or supercritical system."
        ),
        "common_variations": (
            "k = 0.995; subcritical behavior; neutron population over generations; "
            "criticality wording."
        ),
        "patterns": [
            r"\bk\s*=\s*",
            r"multiplication factor",
            r"subcritical",
            r"critical",
            r"supercritical",
            r"neutron population",
            r"generations?",
        ],
    },
    {
        "id": "P18",
        "theme": "Prompt, delayed, and thermal neutron terminology",
        "representative_prompt": (
            "Clarify neutron terminology such as prompt, delayed, fast, or thermal "
            "neutrons in the context of fission and reactor problems."
        ),
        "common_variations": (
            "Prompt versus thermal neutron wording; delayed neutron emissions; "
            "whether a neutron is part of the fission event or later decay."
        ),
        "patterns": [
            r"prompt neutron",
            r"thermal neutron",
            r"delayed neutron",
            r"fast neutron",
            r"neutron terminology",
        ],
    },
    {
        "id": "P19",
        "theme": "Final-answer formatting and citation cleanup",
        "representative_prompt": (
            "Clean up the final document by boxing answers, removing stray citation "
            "markers, and making the final responses readable."
        ),
        "common_variations": (
            "Box final answers; remove [cite] markers; word-check the solution; "
            "polish final answer formatting."
        ),
        "patterns": [
            r"box(ed)? the final",
            r"final answers?",
            r"remove .*cite",
            r"\[cite",
            r"word check",
            r"polish",
        ],
    },
    {
        "id": "P20",
        "theme": "Mass, molar-mass, and composition inputs",
        "representative_prompt": (
            "Check molar masses, isotope masses, density, atom fraction, or weight "
            "percent assumptions before using them in number-density calculations."
        ),
        "common_variations": (
            "Molar mass of water or UO2; exact oxygen mass; atom percent versus "
            "weight percent; material density and composition basis."
        ),
        "patterns": [
            r"molar mass",
            r"atomic mass",
            r"exact .*mass",
            r"weight percent",
            r"atom percent",
            r"density",
            r"composition",
        ],
    },
    {
        "id": "P21",
        "theme": "Stable isobars and mass-chain endpoints",
        "representative_prompt": (
            "Clarify what a stable isobar is and identify the stable isobar or "
            "endpoint for a given fission-product mass chain."
        ),
        "common_variations": (
            "Define stable isobar; distinguish stable isotope and isobar; find "
            "the stable isobar for a specified mass number or nuclide."
        ),
        "patterns": [
            r"stable isobar",
            r"stable isotope",
            r"\bisobar",
            r"mass number",
            r"mass chain",
        ],
    },
    {
        "id": "P22",
        "theme": "Pace control and narrow-answer requests",
        "representative_prompt": (
            "Slow down, answer only the specific question asked, or set up a part "
            "without solving more than requested."
        ),
        "common_variations": (
            "Stop solving the whole problem; answer exactly what I ask; walk "
            "through it slower; set up each part without jumping ahead."
        ),
        "patterns": [
            r"stop solving",
            r"only answer exactly",
            r"exactly what i ask",
            r"walk through .*slower",
            r"little slower",
            r"without solving",
            r"set up each part",
        ],
    },
    {
        "id": "P23",
        "theme": "Exact and approximate expression checks",
        "representative_prompt": (
            "Ask which exact and approximate expressions should be used, or check "
            "a logarithmic/algebraic form before numerical substitution."
        ),
        "common_variations": (
            "Exact versus approximate expressions; use the natural log; verify "
            "the algebraic setup for a particular part."
        ),
        "patterns": [
            r"exact and approximate",
            r"approximate expressions?",
            r"natural log",
            r"algebraic",
            r"expressions? should be used",
        ],
    },
]


def assignment_label(value):
    raw = value.strip().lower()
    match = re.search(r"(\d+)", raw)
    if not match:
        raise SystemExit(f"cannot find assignment number in {value!r}")
    return f"hw{int(match.group(1)):02d}"


def safe_rel(name):
    rel = PurePosixPath(name)
    if rel.is_absolute() or any(part in ("", "..") for part in rel.parts):
        raise ValueError(f"unsafe archive path: {name!r}")
    return Path(*rel.parts)


def write_bytes(root, rel_name, data):
    target = root / safe_rel(rel_name)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    return target


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def is_zip_name(name):
    return PurePosixPath(name).name.lower().endswith(".zip")


def is_dialogue_artifact(name):
    # Match on the file basename only. A directory named "AI" should not cause
    # ordinary solution files inside it to be copied into the dialogue view.
    base = PurePosixPath(name).name
    return bool(DIALOGUE_RE.search(base))


def parse_canvas_key(filename):
    stem = PurePosixPath(filename).name
    # Strip only archive/document suffixes used by Canvas entries.
    for suffix in (".zip", ".pdf", ".docx", ".txt"):
        if stem.lower().endswith(suffix):
            stem = stem[: -len(suffix)]
            break
    parts = stem.split("_")
    user_idx = None
    for idx, part in enumerate(parts):
        if part.isdigit() and len(part) >= 5:
            user_idx = idx
            break
    if user_idx is None or user_idx == 0:
        slug = re.sub(r"[^A-Za-z0-9]+", "", parts[0]).lower() or "unknown"
        return f"{slug}_unknown"
    slug = "_".join(parts[:user_idx])
    slug = re.sub(r"[^A-Za-z0-9_]+", "", slug).strip("_").lower()
    return f"{slug}_{parts[user_idx]}"


def referenced_paths(zf, tex_name):
    refs = set()
    try:
        raw = zf.read(tex_name)
    except KeyError:
        return refs
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("latin-1", errors="replace")

    names = set(zf.namelist())
    lower_map = {name.lower(): name for name in names}
    base = PurePosixPath(tex_name).parent
    for ref in INCLUDE_RE.findall(text):
        ref = ref.strip()
        candidates = [str(base / ref)]
        if not PurePosixPath(ref).suffix:
            candidates.extend(str(base / (ref + ext)) for ext in TEXT_EXTS)
            candidates.extend(str(base / (ref + ext)) for ext in IMAGE_EXTS)
        for cand in candidates:
            if cand in names:
                refs.add(cand)
            elif cand.lower() in lower_map:
                refs.add(lower_map[cand.lower()])
    return refs


def copy_top_level_dialogue(outer, info, row, out_root):
    student_dir = out_root / "by_student" / row["student_key"]
    dialogue_dir = student_dir / "dialogue"
    dialogue_dir.mkdir(parents=True, exist_ok=True)
    data = outer.read(info.filename)
    target = dialogue_dir / PurePosixPath(info.filename).name
    target.write_bytes(data)
    return {
        **row,
        "source_container": "canvas_archive",
        "internal_path": info.filename,
        "artifact_path": str(target.relative_to(out_root)),
        "size_bytes": len(data),
        "sha256": sha256(data),
        "notes": "top-level dialogue filename match",
    }


def extract_nested_zip(outer, info, row, out_root):
    data = outer.read(info.filename)
    try:
        nested = zipfile.ZipFile(io.BytesIO(data))
    except zipfile.BadZipFile:
        return [], False

    with nested:
        names = [item.filename for item in nested.infolist() if not item.is_dir()]
        candidates = {name for name in names if is_dialogue_artifact(name)}
        for name in list(candidates):
            if PurePosixPath(name).suffix.lower() == ".tex":
                candidates.update(referenced_paths(nested, name))
        if not candidates:
            return [], False

        student_dir = out_root / "by_student" / row["student_key"]
        dialogue_dir = student_dir / "dialogue"
        full_dir = student_dir / "full_submission"
        dialogue_dir.mkdir(parents=True, exist_ok=True)
        full_dir.mkdir(parents=True, exist_ok=True)

        for item in nested.infolist():
            if item.is_dir():
                continue
            write_bytes(full_dir, item.filename, nested.read(item.filename))

        artifact_rows = []
        for name in sorted(candidates):
            file_data = nested.read(name)
            target = write_bytes(dialogue_dir, name, file_data)
            artifact_rows.append(
                {
                    **row,
                    "source_container": info.filename,
                    "internal_path": name,
                    "artifact_path": str(target.relative_to(out_root)),
                    "size_bytes": len(file_data),
                    "sha256": sha256(file_data),
                    "notes": "dialogue filename match or dependency referenced by dialogue tex",
                }
            )
    return artifact_rows, True


def write_student_readme(out_root, row, artifacts, has_full_submission):
    student_dir = out_root / "by_student" / row["student_key"]
    lines = [
        f"# {row['student_key']} AI Dialogue Artifacts\n\n",
        f"- Canvas entry: `{row['canvas_entry']}`\n",
        f"- Source archive: `{row['source_archive']}`\n",
        f"- Route cue: `{row['route_cue']}`\n",
        "\n## Dialogue Files\n",
    ]
    for artifact in artifacts:
        lines.append(
            f"- `{artifact['artifact_path']}` from `{artifact['internal_path']}`\n"
        )
    lines.append("\n## Full Submission\n")
    if has_full_submission:
        lines.append(
            "`full_submission/` contains the extracted nested ZIP submission "
            "with original internal paths preserved.\n"
        )
    else:
        lines.append(
            "No nested ZIP was extracted for this source; only the top-level "
            "dialogue artifact was copied.\n"
        )
    (student_dir / "README.md").write_text("".join(lines), encoding="utf-8")


def write_reports(out_root, source_archive, raw_copy, summaries, artifacts):
    with (out_root / "students.csv").open("w", newline="", encoding="utf-8") as fh:
        fields = [
            "student_key",
            "canvas_entry",
            "route_cue",
            "artifact_count",
            "has_full_submission_extract",
            "student_dir",
        ]
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in sorted(summaries, key=lambda item: item["student_key"]):
            writer.writerow(row)

    with (out_root / "manifest.csv").open("w", newline="", encoding="utf-8") as fh:
        fields = [
            "student_key",
            "canvas_entry",
            "route_cue",
            "source_container",
            "internal_path",
            "artifact_path",
            "size_bytes",
            "sha256",
            "notes",
        ]
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in sorted(artifacts, key=lambda item: (item["student_key"], item["artifact_path"])):
            writer.writerow({field: row[field] for field in fields})

    readme = f"""# NE630 AI Dialogue Extraction

This directory collects submission artifacts that appear to represent disclosed
AI-agent dialogue for the assignment.

Source archive: `{source_archive}`
Raw local copy: `{raw_copy}`

## Layout

- `students.csv`: one row per detected AI-dialogue-bearing submission.
- `manifest.csv`: one row per copied dialogue artifact, including original
  internal path and SHA-256.
- `by_student/<student_key>/README.md`: per-submission navigation note.
- `by_student/<student_key>/dialogue/`: dialogue-facing artifacts only.
- `by_student/<student_key>/full_submission/`: full nested ZIP extraction when
  a Route-B ZIP was detected.

Detected submissions: {len(summaries)}
Extracted dialogue artifacts: {len(artifacts)}
"""
    (out_root / "README.md").write_text(readme, encoding="utf-8")


def normalize_for_match(text):
    text = re.sub(r"\\[A-Za-z]+\*?(?:\[[^\]]*\])?(?:\{([^{}]*)\})?", r" \1 ", text)
    text = re.sub(r"[^A-Za-z0-9.%^/_+-]+", " ", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def prompt_excerpt(text, limit=240):
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def assignment_tokens(assignment):
    number = int(re.search(r"\d+", assignment).group(0))
    return {
        f"hw{number}",
        f"hw{number:02d}",
        f"homework{number}",
        f"homework{number:02d}",
        f"homework {number}",
        f"homework {number:02d}",
    }


def path_mentions_assignment(path, assignment):
    text = str(path).lower().replace("_", " ").replace("-", " ")
    compact = text.replace(" ", "")
    return any(token in text or token in compact for token in assignment_tokens(assignment))


def path_mentions_other_assignment(path, assignment):
    text = str(path).lower()
    this_number = int(re.search(r"\d+", assignment).group(0))
    for match in re.finditer(r"(?:hw|homework)[_\s-]*0?(\d+)", text):
        if int(match.group(1)) != this_number:
            return True
    return False


def read_prompt_text(path):
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        pdftotext = shutil.which("pdftotext")
        if not pdftotext:
            return ""
        result = subprocess.run(
            [pdftotext, "-layout", str(path), "-"],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        return result.stdout if result.returncode == 0 else ""
    data = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("latin-1", errors="replace")


def choose_prompt_sources(student_dir, assignment):
    dialogue_dir = student_dir / "dialogue"
    candidates = []
    for path in dialogue_dir.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in PROMPT_TEXT_EXTS:
            continue
        lower = path.name.lower()
        if "template" in lower or lower == "readme.md":
            continue
        if path_mentions_other_assignment(path.relative_to(dialogue_dir), assignment):
            continue
        if not is_dialogue_artifact(path.name):
            continue
        candidates.append(path)

    if not candidates:
        return []

    buckets = [
        lambda p: p.suffix.lower() in (".txt", ".md") and path_mentions_assignment(p, assignment),
        lambda p: p.suffix.lower() in (".txt", ".md"),
        lambda p: p.suffix.lower() == ".tex" and path_mentions_assignment(p, assignment),
        lambda p: p.suffix.lower() == ".tex",
        lambda p: p.suffix.lower() == ".pdf" and path_mentions_assignment(p, assignment),
        lambda p: p.suffix.lower() == ".pdf",
    ]
    for bucket in buckets:
        picked = sorted(path for path in candidates if bucket(path))
        if picked:
            return picked
    return sorted(candidates)


USER_MARKER_RE = re.compile(
    r"^\s*(?:#+\s*)?(?:"
    r"student|user|human|me|you|user prompt|student prompt|prompt"
    r")\s*:\s*(.*)$",
    re.IGNORECASE,
)
ASSISTANT_MARKER_RE = re.compile(
    r"^\s*(?:#+\s*)?(?:"
    r"assistant|claude|chatgpt|gpt|gemini|copilot|response|ai"
    r")\s*:\s*(.*)$",
    re.IGNORECASE,
)
SPEAKER_RE = re.compile(r"\\speaker\{([^{}]+)\}")


def extract_student_prompts(text):
    prompts = []
    active = None
    buf = []

    def flush():
        nonlocal buf
        if active == "user":
            prompt = clean_prompt("\n".join(buf))
            if prompt:
                prompts.append(prompt)
        buf = []

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        speaker = SPEAKER_RE.search(line)
        if speaker:
            flush()
            role = speaker.group(1).strip().lower()
            active = "user" if role in {"user", "student", "human", "me", "you"} else "assistant"
            rest = SPEAKER_RE.sub("", line).strip()
            if rest:
                buf.append(rest)
            continue

        user_match = USER_MARKER_RE.match(line)
        assistant_match = ASSISTANT_MARKER_RE.match(line)
        if user_match:
            flush()
            active = "user"
            if user_match.group(1).strip():
                buf.append(user_match.group(1).strip())
            continue
        if assistant_match:
            flush()
            active = "assistant"
            if assistant_match.group(1).strip():
                buf.append(assistant_match.group(1).strip())
            continue

        if active == "user":
            buf.append(line)

    flush()
    return prompts


def clean_prompt(text):
    text = text.replace("\ufeff", "")
    text = re.sub(r"\\begin\{lstlisting\}|\\end\{lstlisting\}", " ", text)
    text = re.sub(r"END OF GRADED DISCOURSE", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"-{5,}", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    if not text or len(text) < 2:
        return ""
    return text


def collect_prompts(out_root, assignment):
    prompts = []
    source_rows = []
    students_root = out_root / "by_student"
    student_dirs = sorted(path for path in students_root.iterdir() if path.is_dir())
    for source_index, student_dir in enumerate(student_dirs, start=1):
        source_id = f"D{source_index:02d}"
        sources = choose_prompt_sources(student_dir, assignment)
        source_prompt_count = 0
        for source in sources:
            text = read_prompt_text(source)
            extracted = extract_student_prompts(text)
            if not extracted:
                continue
            rel_source = source.relative_to(out_root)
            for prompt in extracted:
                source_prompt_count += 1
                prompts.append(
                    {
                        "source_id": source_id,
                        "turn": source_prompt_count,
                        "student_key": student_dir.name,
                        "source_path": str(rel_source),
                        "prompt": prompt,
                    }
                )
        source_rows.append(
            {
                "source_id": source_id,
                "student_key": student_dir.name,
                "source_count": len(sources),
                "prompt_count": source_prompt_count,
            }
        )
    return prompts, source_rows


def match_theme(prompt, theme):
    normalized = normalize_for_match(prompt)
    for group in theme.get("required_any", []):
        if not any(re.search(pattern, normalized, re.IGNORECASE) for pattern in group):
            return False
    return any(re.search(pattern, normalized, re.IGNORECASE) for pattern in theme["patterns"])


def cluster_prompts(prompts):
    clusters = []
    matched_keys = set()
    for theme in THEMES:
        rows = []
        source_ids = set()
        for index, row in enumerate(prompts):
            if match_theme(row["prompt"], theme):
                rows.append(row)
                source_ids.add(row["source_id"])
                matched_keys.add(index)
        if rows:
            clusters.append({**theme, "rows": rows, "source_ids": source_ids})

    return clusters, len(matched_keys)


def write_prompt_inventory(out_root, assignment):
    inventory_dir = out_root / "prompt_inventory"
    inventory_dir.mkdir(parents=True, exist_ok=True)
    prompts, source_rows = collect_prompts(out_root, assignment)
    clusters, matched_count = cluster_prompts(prompts)

    with (inventory_dir / "anonymized_prompt_samples.csv").open(
        "w", newline="", encoding="utf-8"
    ) as fh:
        writer = csv.DictWriter(fh, fieldnames=["source_id", "turn", "prompt_excerpt"])
        writer.writeheader()
        for row in prompts:
            writer.writerow(
                {
                    "source_id": row["source_id"],
                    "turn": row["turn"],
                    "prompt_excerpt": prompt_excerpt(row["prompt"]),
                }
            )

    with (inventory_dir / "representative_prompts.csv").open(
        "w", newline="", encoding="utf-8"
    ) as fh:
        fields = [
            "id",
            "theme",
            "representative_prompt",
            "common_variations",
            "prompt_count",
            "dialogue_count",
        ]
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for cluster in clusters:
            writer.writerow(
                {
                    "id": cluster["id"],
                    "theme": cluster["theme"],
                    "representative_prompt": cluster["representative_prompt"],
                    "common_variations": cluster["common_variations"],
                    "prompt_count": len(cluster["rows"]),
                    "dialogue_count": len(cluster["source_ids"]),
                }
            )

    represented_sources = sum(1 for row in source_rows if row["prompt_count"])
    matched_rows = set()
    for cluster in clusters:
        for row in cluster["rows"]:
            matched_rows.add((row["source_id"], row["turn"]))

    lines = [
        f"# NE630 {assignment.upper()} Representative Student-to-AI Prompts\n\n",
        (
            f"This is an anonymized, generic prompt inventory built from the "
            f"{assignment.upper()} full-disclosure dialogue artifacts extracted "
            "under `extracted/ai_dialogues/by_student/`. It is meant to capture "
            "duplicate and near-duplicate student prompt patterns, not to "
            "attribute prompts to individual students.\n\n"
        ),
        "## Coverage\n\n",
        f"- Full-disclosure dialogue sources represented: {represented_sources}\n",
        f"- Extracted student-side prompt turns used for clustering: {len(prompts)}\n",
        f"- Prompt turns matched by at least one representative theme: {len(matched_rows)}\n",
        (
            "- Prompts may count in more than one theme when a single request "
            "combines physics, formatting, and submission packaging.\n"
        ),
        (
            "- Counts are directional aids for reviewing common patterns; they "
            "are not grading metrics.\n"
        ),
        (
            "- This inventory is generated by deterministic text extraction and "
            "theme matching; review source artifacts when a prompt is ambiguous.\n\n"
        ),
        "## Representative Prompt Themes\n\n",
    ]
    for cluster in clusters:
        lines.extend(
            [
                f"### {cluster['id']}. {cluster['theme']}\n\n",
                f"**Representative generic prompt:** {cluster['representative_prompt']}\n\n",
                f"**Common variations:** {cluster['common_variations']}\n\n",
                (
                    f"**Observed in:** {len(cluster['source_ids'])} dialogue source(s), "
                    f"{len(cluster['rows'])} prompt turn(s).\n\n"
                ),
            ]
        )
    if not clusters:
        lines.append("No student-side prompt turns were extracted from the available dialogue artifacts.\n")

    (inventory_dir / "representative_prompts.md").write_text(
        "".join(lines), encoding="utf-8"
    )
    return {
        "prompt_sources": represented_sources,
        "prompt_turns": len(prompts),
        "theme_count": len(clusters),
        "matched_turns": len(matched_rows),
    }


def extract(args):
    source = Path(args.source).expanduser().resolve()
    if not source.exists():
        raise SystemExit(f"source archive not found: {source}")
    assignment = assignment_label(args.assignment)
    grading_root = Path(args.grading_root).expanduser().resolve()
    assignment_root = grading_root / assignment
    raw_dir = assignment_root / "raw"
    out_root = assignment_root / "extracted" / "ai_dialogues"
    raw_dir.mkdir(parents=True, exist_ok=True)
    (out_root / "by_student").mkdir(parents=True, exist_ok=True)

    raw_name = f"{assignment}_subs.zip"
    raw_copy = raw_dir / raw_name
    if source != raw_copy:
        shutil.copy2(source, raw_copy)

    artifacts = []
    per_student = {}
    with zipfile.ZipFile(source) as outer:
        for info in outer.infolist():
            if info.is_dir():
                continue
            row = {
                "student_key": parse_canvas_key(info.filename),
                "canvas_entry": info.filename,
                "source_archive": str(source),
                "route_cue": "nested_zip" if is_zip_name(info.filename) else "top_level_dialogue",
            }
            copied = []
            has_full = False
            if is_zip_name(info.filename):
                copied, has_full = extract_nested_zip(outer, info, row, out_root)
            elif is_dialogue_artifact(info.filename):
                copied = [copy_top_level_dialogue(outer, info, row, out_root)]
            if not copied:
                continue

            key = row["student_key"]
            slot = per_student.setdefault(
                key,
                {
                    "student_key": key,
                    "canvas_entry": row["canvas_entry"],
                    "route_cue": row["route_cue"],
                    "artifact_count": 0,
                    "has_full_submission_extract": False,
                    "student_dir": str((out_root / "by_student" / key).relative_to(out_root)),
                    "artifacts": [],
                },
            )
            slot["artifact_count"] += len(copied)
            slot["has_full_submission_extract"] = (
                slot["has_full_submission_extract"] or has_full
            )
            slot["artifacts"].extend(copied)
            artifacts.extend(copied)

    summaries = []
    for slot in per_student.values():
        write_student_readme(
            out_root,
            {
                "student_key": slot["student_key"],
                "canvas_entry": slot["canvas_entry"],
                "source_archive": str(source),
                "route_cue": slot["route_cue"],
            },
            slot["artifacts"],
            slot["has_full_submission_extract"],
        )
        summaries.append(
            {
                "student_key": slot["student_key"],
                "canvas_entry": slot["canvas_entry"],
                "route_cue": slot["route_cue"],
                "artifact_count": slot["artifact_count"],
                "has_full_submission_extract": str(
                    slot["has_full_submission_extract"]
                ).lower(),
                "student_dir": slot["student_dir"],
            }
        )

    write_reports(out_root, source, raw_copy, summaries, artifacts)
    inventory = None
    if not args.no_prompt_inventory:
        inventory = write_prompt_inventory(out_root, assignment)
    print(f"assignment_root={assignment_root}")
    print(f"raw_copy={raw_copy}")
    print(f"ai_dialogues={out_root}")
    print(f"detected_submissions={len(summaries)}")
    print(f"dialogue_artifacts={len(artifacts)}")
    if inventory:
        print(f"prompt_sources={inventory['prompt_sources']}")
        print(f"prompt_turns={inventory['prompt_turns']}")
        print(f"prompt_themes={inventory['theme_count']}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--assignment", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument(
        "--grading-root",
        default="/home/robertsj/Classes/ne630_local_grading",
    )
    parser.add_argument(
        "--no-prompt-inventory",
        action="store_true",
        help="extract dialogue artifacts only; skip representative prompt inventory",
    )
    extract(parser.parse_args())


if __name__ == "__main__":
    main()
