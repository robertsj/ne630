#!/usr/bin/env python3
"""Build the folded homework page and Canvas-ready assignment fragments."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from html import escape
from pathlib import Path
import re
import subprocess
import sys
from textwrap import indent

from markdown_it import MarkdownIt


ROOT = Path(__file__).resolve().parent
MARKDOWN_DIR = ROOT / "markdown"
OUTPUT = ROOT / "html" / "HW01-03.html"
CANVAS_OUTPUT_DIR = ROOT / "html"
CANVAS_CONVERTER = ROOT.parent / "build" / "convert_to_canvas.py"
CANVAS_TEMP_OUTPUT = CANVAS_CONVERTER.parent / "tmp.html"


@dataclass(frozen=True)
class Homework:
    source: str
    expected_problems: int


HOMEWORK = (
    Homework("HW01.md", 3),
    Homework("HW02.md", 3),
    Homework("HW03.md", 3),
)

HEADING_RE = re.compile(r"^##[ \t]+(.+?)[ \t]*$", re.MULTILINE)
TITLE_RE = re.compile(r"^#[ \t]+(.+?)[ \t]*$", re.MULTILINE)
SOLUTION_RE = re.compile(r"^###[ \t]+solution\b", re.IGNORECASE | re.MULTILINE)
MATH_RE = re.compile(
    r"(?<!\\)\$\$.*?(?<!\\)\$\$|(?<!\\)\$(?!\$).*?(?<!\\)\$",
    re.DOTALL,
)

MARKDOWN = MarkdownIt("commonmark", {"html": False})


def render_with_math(
    source: str,
    format_math: Callable[[str], str],
) -> str:
    """Render Markdown while shielding TeX from Markdown backslash handling."""
    math_fragments: list[str] = []

    def shield(match: re.Match[str]) -> str:
        token = f"NE630MATH{len(math_fragments):05d}PLACEHOLDER"
        math_fragments.append(match.group(0))
        return token

    rendered = MARKDOWN.render(MATH_RE.sub(shield, source))
    for index, fragment in enumerate(math_fragments):
        token = f"NE630MATH{index:05d}PLACEHOLDER"
        rendered = rendered.replace(token, format_math(fragment))
    return rendered


def render_markdown(source: str) -> str:
    """Render Markdown for the standalone page's configured MathJax."""
    return render_with_math(source, lambda fragment: fragment)


def parse_homework(
    spec: Homework,
    renderer: Callable[[str], str] = render_markdown,
) -> tuple[str, str, list[tuple[str, str]]]:
    path = MARKDOWN_DIR / spec.source
    source = path.read_text(encoding="utf-8")

    if SOLUTION_RE.search(source):
        raise ValueError(f"{path} contains a solution section")

    title_match = TITLE_RE.search(source)
    if title_match is None:
        raise ValueError(f"{path} has no level-one title")

    problem_matches = list(HEADING_RE.finditer(source))
    if len(problem_matches) != spec.expected_problems:
        raise ValueError(
            f"{path} has {len(problem_matches)} problems; "
            f"expected {spec.expected_problems}"
        )

    title = title_match.group(1)
    intro_source = source[title_match.end() : problem_matches[0].start()].strip()
    intro = renderer(intro_source) if intro_source else ""
    problems: list[tuple[str, str]] = []

    for index, match in enumerate(problem_matches):
        next_start = (
            problem_matches[index + 1].start()
            if index + 1 < len(problem_matches)
            else len(source)
        )
        problem_source = source[match.end() : next_start].strip()
        problems.append((match.group(1), renderer(problem_source)))

    return title, intro, problems


def build_canvas_fragment(source: Path, output: Path) -> None:
    """Run the course's canonical Pandoc-to-Canvas converter."""
    try:
        subprocess.run(
            [sys.executable, str(CANVAS_CONVERTER), str(source), str(output)],
            check=True,
            cwd=CANVAS_CONVERTER.parent,
        )
    finally:
        CANVAS_TEMP_OUTPUT.unlink(missing_ok=True)


def homework_card(
    source_name: str,
    title: str,
    intro: str,
    problems: list[tuple[str, str]],
) -> str:
    problem_cards = []
    for problem_title, problem_body in problems:
        problem_cards.append(
            """
          <details class="problem-card">
            <summary>
              <span>{problem_title}</span>
              <span class="fold-label">Show problem</span>
            </summary>
            <div class="problem-body">
{problem_body}
            </div>
          </details>""".format(
                problem_title=escape(problem_title),
                problem_body=problem_body.rstrip(),
            )
        )

    source_href = "../markdown/" + source_name
    intro_block = (
        '<div class="homework-intro">' + intro.rstrip() + "</div>"
        if intro
        else ""
    )
    return """
      <details class="homework-card">
        <summary>
          <span class="homework-title">{title}</span>
          <span class="homework-meta">{count} problems</span>
        </summary>
        <div class="homework-body">
          <div class="source-link">
            <a href="{source_href}">View Markdown source</a>
          </div>
          {intro}
{problems}
        </div>
      </details>""".format(
        title=escape(title),
        count=len(problems),
        source_href=escape(source_href, quote=True),
        intro=intro_block,
        problems="\n".join(problem_cards),
    )


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>NE 630 Homework 01–03</title>
  <style>
    :root {
      --ksu-purple: #512888;
      --ksu-deep-purple: #3b1b64;
      --ksu-purple-soft: #f2edf8;
      --ink: #202124;
      --muted: #62636a;
      --line: #d8d1df;
      --paper: #ffffff;
      --background: #f5f3f7;
    }

    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      color: var(--ink);
      background: var(--background);
      font-family: "Myriad Pro", "Segoe UI", Arial, sans-serif;
      line-height: 1.55;
    }

    a {
      color: var(--ksu-purple);
    }

    a:hover {
      color: var(--ksu-deep-purple);
    }

    .page-header {
      color: white;
      background: var(--ksu-purple);
      border-bottom: 5px solid var(--ksu-deep-purple);
    }

    .page-header-inner,
    main {
      width: min(960px, calc(100% - 2rem));
      margin-inline: auto;
    }

    .page-header-inner {
      padding: 2.3rem 0 2rem;
    }

    .eyebrow {
      margin: 0 0 0.2rem;
      font-size: 0.9rem;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
    }

    h1 {
      margin: 0;
      font-size: clamp(2rem, 5vw, 3.2rem);
      line-height: 1.08;
    }

    .subtitle {
      max-width: 44rem;
      margin: 0.75rem 0 0;
      color: #eee7f5;
    }

    main {
      padding: 1.5rem 0 4rem;
    }

    .controls {
      display: flex;
      flex-wrap: wrap;
      gap: 0.65rem;
      margin-bottom: 1rem;
    }

    button {
      padding: 0.55rem 0.9rem;
      color: var(--ksu-purple);
      background: white;
      border: 1px solid var(--ksu-purple);
      border-radius: 0.3rem;
      font: inherit;
      font-weight: 700;
      cursor: pointer;
    }

    button:hover,
    button:focus-visible {
      color: white;
      background: var(--ksu-purple);
      outline: none;
    }

    details {
      background: var(--paper);
    }

    summary {
      display: flex;
      align-items: center;
      gap: 1rem;
      list-style: none;
      cursor: pointer;
    }

    summary::-webkit-details-marker {
      display: none;
    }

    summary::after {
      content: "+";
      display: grid;
      width: 1.6rem;
      height: 1.6rem;
      margin-left: auto;
      flex: 0 0 auto;
      place-items: center;
      border: 1px solid currentColor;
      border-radius: 50%;
      font-size: 1.1rem;
      line-height: 1;
    }

    details[open] > summary::after {
      content: "−";
    }

    summary:focus-visible {
      outline: 3px solid #b49bd0;
      outline-offset: 3px;
    }

    .homework-card {
      margin-bottom: 1rem;
      border: 1px solid var(--line);
      border-radius: 0.45rem;
      box-shadow: 0 0.2rem 0.7rem rgb(59 27 100 / 8%);
      overflow: hidden;
    }

    .homework-card > summary {
      padding: 1rem 1.15rem;
      color: white;
      background: var(--ksu-purple);
    }

    .homework-title {
      font-size: 1.25rem;
      font-weight: 700;
    }

    .homework-meta {
      color: #eee7f5;
      font-size: 0.92rem;
    }

    .homework-body {
      padding: 1rem;
    }

    .source-link {
      margin: 0 0 0.8rem;
      text-align: right;
      font-size: 0.9rem;
    }

    .homework-intro {
      margin-bottom: 1rem;
    }

    .problem-card {
      margin: 0.75rem 0;
      border: 1px solid var(--line);
      border-left: 4px solid var(--ksu-purple);
      border-radius: 0.3rem;
      overflow: hidden;
    }

    .problem-card > summary {
      padding: 0.8rem 0.9rem;
      color: var(--ksu-deep-purple);
      background: var(--ksu-purple-soft);
      font-weight: 700;
    }

    .fold-label {
      margin-left: auto;
      color: var(--muted);
      font-size: 0.82rem;
      font-weight: 400;
    }

    .problem-card[open] .fold-label {
      visibility: hidden;
    }

    .problem-body {
      padding: 0.25rem 1rem 1rem;
      overflow-x: auto;
    }

    .problem-body > :last-child {
      margin-bottom: 0;
    }

    .problem-body li + li {
      margin-top: 0.35rem;
    }

    mjx-container[display="true"] {
      overflow-x: auto;
      overflow-y: hidden;
      padding: 0.3rem 0;
    }

    @media (max-width: 620px) {
      .page-header-inner,
      main {
        width: calc(100% - 1rem);
      }

      .homework-card > summary {
        position: relative;
        align-items: flex-start;
        flex-direction: column;
        gap: 0.15rem;
        padding-right: 3.4rem;
      }

      .homework-card > summary::after {
        position: absolute;
        right: 1.3rem;
      }

      .fold-label {
        display: none;
      }
    }

    @media print {
      body {
        background: white;
      }

      .page-header {
        color: black;
        background: white;
        border-bottom-color: var(--ksu-purple);
      }

      .subtitle,
      .eyebrow {
        color: black;
      }

      .controls,
      .source-link,
      summary::after,
      .fold-label {
        display: none;
      }

      .homework-card,
      .problem-card {
        break-inside: avoid;
        box-shadow: none;
      }

      .homework-card > summary {
        color: white;
        print-color-adjust: exact;
        -webkit-print-color-adjust: exact;
      }
    }
  </style>
  <script>
    window.MathJax = {
      loader: {load: ["[tex]/cancel"]},
      tex: {
        inlineMath: [["$", "$"]],
        displayMath: [["$$", "$$"]],
        packages: {"[+]": ["cancel"]}
      },
      options: {
        skipHtmlTags: ["script", "noscript", "style", "textarea", "pre", "code"]
      }
    };
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-chtml.js"></script>
</head>
<body>
  <header class="page-header">
    <div class="page-header-inner">
      <p class="eyebrow">NE 630</p>
      <h1>Homework 01–03</h1>
      <p class="subtitle">
        Choose a homework, then open individual problems as needed.
        All sections are folded by default.
      </p>
    </div>
  </header>

  <main>
    <div class="controls" aria-label="Folding controls">
      <button id="expand-all" type="button">Expand all</button>
      <button id="collapse-all" type="button">Collapse all</button>
    </div>

__HOMEWORK_CARDS__
  </main>

  <script>
    const details = Array.from(document.querySelectorAll("details"));
    const originalPrintState = new Map();

    document.getElementById("expand-all").addEventListener("click", () => {
      details.forEach((item) => {
        item.open = true;
      });
    });

    document.getElementById("collapse-all").addEventListener("click", () => {
      details.slice().reverse().forEach((item) => {
        item.open = false;
      });
    });

    window.addEventListener("beforeprint", () => {
      details.forEach((item) => {
        originalPrintState.set(item, item.open);
        item.open = true;
      });
    });

    window.addEventListener("afterprint", () => {
      details.forEach((item) => {
        item.open = originalPrintState.get(item);
      });
      originalPrintState.clear();
    });
  </script>
</body>
</html>
"""


def main() -> None:
    cards: list[str] = []
    canvas_outputs: list[Path] = []
    total_problems = 0
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    for spec in HOMEWORK:
        title, intro, problems = parse_homework(spec)
        cards.append(homework_card(spec.source, title, intro, problems))
        total_problems += len(problems)

        canvas_output = CANVAS_OUTPUT_DIR / Path(spec.source).with_suffix(
            ".html"
        ).name
        build_canvas_fragment(
            MARKDOWN_DIR / spec.source,
            canvas_output,
        )
        canvas_outputs.append(canvas_output)

    document = TEMPLATE.replace("__HOMEWORK_CARDS__", "\n".join(cards))
    OUTPUT.write_text(document, encoding="utf-8")
    print(
        f"Wrote {OUTPUT} with {len(HOMEWORK)} homework sections "
        f"and {total_problems} problems."
    )
    print(
        "Wrote Canvas fragments: "
        + ", ".join(str(path.relative_to(ROOT)) for path in canvas_outputs)
    )


if __name__ == "__main__":
    main()
