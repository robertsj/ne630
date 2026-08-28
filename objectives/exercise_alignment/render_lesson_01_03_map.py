#!/usr/bin/env python3
"""Render a self-contained graphical view of the Lesson 01-03 mapping."""

from __future__ import annotations

import csv
import html
import json
from pathlib import Path


BASE = Path(__file__).resolve().parent
CATALOG_PATH = BASE / "lesson_01_03_catalog.yml"
EDGES_PATH = BASE / "lesson_01_03_exercise_edges.psv"
OUTPUT_PATH = BASE / "lesson_01_03_map.html"


def parse_catalog(path: Path) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    objectives: list[dict[str, str]] = []
    orthogonal: list[dict[str, str]] = []
    section: str | None = None
    current: dict[str, str] | None = None

    def finish_current() -> None:
        nonlocal current
        if current is None:
            return
        if section == "objectives":
            objectives.append(current)
        elif section == "orthogonal_objectives":
            orthogonal.append(current)
        current = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if line == "objectives:":
            finish_current()
            section = "objectives"
            continue
        if line == "orthogonal_objectives:":
            finish_current()
            section = "orthogonal_objectives"
            continue
        if section not in {"objectives", "orthogonal_objectives"}:
            continue

        stripped = line.strip()
        if stripped.startswith("- id: "):
            finish_current()
            current = {"id": stripped.split(": ", 1)[1]}
        elif current is not None and ": " in stripped:
            key, value = stripped.split(": ", 1)
            current[key] = value

    finish_current()
    return objectives, orthogonal


def parse_edges(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream, delimiter="|"))


def esc_script_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False).replace("</", "<\\/")


def render_html(objectives: list[dict[str, str]], orthogonal: list[dict[str, str]], edges: list[dict[str, str]]) -> str:
    data = {
        "objectives": objectives,
        "orthogonal": orthogonal,
        "edges": edges,
    }
    page_title = "NE 630 Objective Mapping: Lessons 01-03"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(page_title)}</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f7f7f4;
      --panel: #ffffff;
      --ink: #202124;
      --muted: #61666c;
      --line: #d9dedb;
      --line-strong: #aeb8b3;
      --accent: #176b70;
      --accent-soft: #d8eeee;
      --accent-mid: #87c5c2;
      --book-lewis: #2d6cdf;
      --book-dhnra: #b35f00;
      --book-lamarsh: #6f4bb2;
      --warn: #bc6c25;
      --shadow: 0 8px 24px rgba(22, 32, 38, 0.08);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}

    * {{ box-sizing: border-box; }}

    body {{
      margin: 0;
      background: var(--bg);
      color: var(--ink);
    }}

    header {{
      border-bottom: 1px solid var(--line);
      background: #fbfbf9;
    }}

    .wrap {{
      width: min(1420px, calc(100vw - 40px));
      margin: 0 auto;
    }}

    .top {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto;
      gap: 20px;
      align-items: end;
      padding: 24px 0 18px;
    }}

    h1 {{
      margin: 0 0 6px;
      font-size: 28px;
      line-height: 1.15;
      letter-spacing: 0;
    }}

    .subtitle {{
      margin: 0;
      color: var(--muted);
      font-size: 14px;
    }}

    .stats {{
      display: grid;
      grid-template-columns: repeat(4, minmax(92px, 1fr));
      gap: 8px;
      min-width: 420px;
    }}

    .stat {{
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
      padding: 9px 10px;
      box-shadow: var(--shadow);
    }}

    .stat strong {{
      display: block;
      font-size: 20px;
      line-height: 1;
    }}

    .stat span {{
      display: block;
      margin-top: 4px;
      color: var(--muted);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    main {{
      padding: 18px 0 30px;
    }}

    .toolbar {{
      display: grid;
      grid-template-columns: auto auto minmax(240px, 1fr) auto;
      gap: 10px;
      align-items: center;
      margin-bottom: 14px;
    }}

    .segmented, .search {{
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
      min-height: 38px;
    }}

    .segmented {{
      display: inline-flex;
      padding: 3px;
      gap: 3px;
    }}

    button {{
      appearance: none;
      border: 0;
      border-radius: 6px;
      background: transparent;
      color: var(--muted);
      cursor: pointer;
      font: inherit;
      min-height: 30px;
      padding: 0 10px;
    }}

    button.active {{
      background: var(--accent);
      color: white;
    }}

    .search {{
      display: flex;
      align-items: center;
      padding: 0 10px;
      gap: 8px;
    }}

    .search span {{
      color: var(--muted);
      font-size: 14px;
    }}

    input {{
      width: 100%;
      border: 0;
      outline: 0;
      background: transparent;
      color: var(--ink);
      font: inherit;
    }}

    .layout {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) 360px;
      gap: 14px;
      align-items: start;
    }}

    .panel {{
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
      box-shadow: var(--shadow);
      overflow: hidden;
    }}

    .panel-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      padding: 12px 14px;
      border-bottom: 1px solid var(--line);
      background: #fbfbf9;
    }}

    .panel-head h2 {{
      margin: 0;
      font-size: 15px;
      letter-spacing: 0;
    }}

    .small {{
      color: var(--muted);
      font-size: 12px;
    }}

    .matrix-wrap {{
      overflow: auto;
      max-height: calc(100vh - 205px);
    }}

    table {{
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      min-width: 880px;
    }}

    th, td {{
      border-bottom: 1px solid var(--line);
      vertical-align: top;
      text-align: left;
    }}

    th {{
      position: sticky;
      top: 0;
      z-index: 2;
      background: #fbfbf9;
      padding: 10px 12px;
      color: var(--muted);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    td {{
      padding: 8px;
    }}

    .objective-cell {{
      width: 34%;
      min-width: 290px;
      padding: 10px 12px;
      cursor: pointer;
    }}

    .objective-id {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-weight: 700;
      font-size: 13px;
    }}

    .lesson-pill {{
      border-radius: 5px;
      background: var(--accent-soft);
      color: #174f52;
      padding: 2px 6px;
      font-weight: 700;
      font-size: 11px;
    }}

    .objective-text {{
      margin-top: 6px;
      color: #33383d;
      font-size: 13px;
      line-height: 1.35;
    }}

    tr.selected .objective-cell {{
      background: #eef7f6;
      box-shadow: inset 4px 0 0 var(--accent);
    }}

    .book-cell {{
      width: 22%;
      min-width: 170px;
    }}

    .heat {{
      min-height: 52px;
      border-radius: 7px;
      border: 1px solid transparent;
      padding: 7px;
      cursor: pointer;
    }}

    .heat:hover {{
      border-color: var(--line-strong);
    }}

    .count {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 24px;
      height: 24px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.8);
      color: var(--ink);
      font-weight: 700;
      font-size: 12px;
    }}

    .exercise-list {{
      display: flex;
      flex-wrap: wrap;
      gap: 4px;
      margin-top: 6px;
    }}

    .chip {{
      display: inline-flex;
      align-items: center;
      max-width: 100%;
      border-radius: 5px;
      background: rgba(255, 255, 255, 0.76);
      border: 1px solid rgba(0, 0, 0, 0.07);
      padding: 2px 5px;
      font-size: 11px;
      line-height: 1.2;
      white-space: nowrap;
    }}

    .empty {{
      color: #a0a6a8;
      font-size: 13px;
      padding: 8px;
    }}

    .detail {{
      position: sticky;
      top: 14px;
    }}

    .detail-body {{
      padding: 14px;
    }}

    .detail-title {{
      margin: 0 0 8px;
      font-size: 16px;
      line-height: 1.25;
    }}

    .detail-text {{
      color: #343a3f;
      font-size: 13px;
      line-height: 1.45;
      margin-bottom: 12px;
    }}

    .detail-section {{
      border-top: 1px solid var(--line);
      padding-top: 12px;
      margin-top: 12px;
    }}

    .detail-section h3 {{
      margin: 0 0 8px;
      color: var(--muted);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    .edge-card {{
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 9px;
      margin-bottom: 8px;
    }}

    .edge-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
      margin-bottom: 6px;
      font-size: 12px;
      font-weight: 700;
    }}

    .basis {{
      color: #3c4248;
      font-size: 12px;
      line-height: 1.35;
    }}

    .tag-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
      margin-top: 7px;
    }}

    .tag {{
      border-radius: 5px;
      background: #f1eee8;
      color: #59432b;
      padding: 2px 5px;
      font-size: 10px;
      line-height: 1.2;
    }}

    .network {{
      display: none;
      min-height: 680px;
      overflow: auto;
    }}

    svg {{
      display: block;
      min-width: 1000px;
      width: 100%;
      height: auto;
      background: #ffffff;
    }}

    .node rect {{
      rx: 7;
      ry: 7;
      stroke: var(--line-strong);
    }}

    .node text {{
      fill: var(--ink);
      font-size: 12px;
      dominant-baseline: middle;
    }}

    .node .sub {{
      fill: var(--muted);
      font-size: 10px;
    }}

    .edge {{
      fill: none;
      stroke: rgba(33, 72, 86, 0.22);
      stroke-width: 1.4;
    }}

    .edge.highlight {{
      stroke: var(--accent);
      stroke-width: 2.4;
    }}

    .legend {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      align-items: center;
      padding: 10px 14px;
      border-top: 1px solid var(--line);
      color: var(--muted);
      font-size: 12px;
    }}

    .swatch {{
      width: 13px;
      height: 13px;
      border-radius: 4px;
      display: inline-block;
      vertical-align: -2px;
      margin-right: 4px;
    }}

    .source-note {{
      margin-top: 12px;
      color: var(--muted);
      font-size: 12px;
    }}

    @media (max-width: 980px) {{
      .top, .toolbar, .layout {{
        grid-template-columns: 1fr;
      }}
      .stats {{
        min-width: 0;
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }}
      .detail {{
        position: static;
      }}
      .matrix-wrap {{
        max-height: none;
      }}
      .wrap {{
        width: min(100vw - 24px, 1420px);
      }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="wrap top">
      <div>
        <h1>{html.escape(page_title)}</h1>
        <p class="subtitle">Direct exercise alignments, coverage density, and reusable orthogonal tags.</p>
      </div>
      <div class="stats" aria-label="Mapping statistics">
        <div class="stat"><strong id="stat-objectives">0</strong><span>Objectives</span></div>
        <div class="stat"><strong id="stat-exercises">0</strong><span>Exercises</span></div>
        <div class="stat"><strong id="stat-edges">0</strong><span>Edges</span></div>
        <div class="stat"><strong id="stat-tags">0</strong><span>Tags</span></div>
      </div>
    </div>
  </header>
  <main>
    <div class="wrap">
      <div class="toolbar">
        <div class="segmented" id="lesson-controls" aria-label="Lesson filter"></div>
        <div class="segmented" id="view-controls" aria-label="View selector">
          <button type="button" data-view="matrix" class="active">Matrix</button>
          <button type="button" data-view="network">Network</button>
        </div>
        <label class="search" for="search-box"><span>Search</span><input id="search-box" type="search" placeholder="objective, exercise, book, tag"></label>
        <div class="segmented" id="book-controls" aria-label="Book filter"></div>
      </div>

      <div class="layout">
        <section class="panel">
          <div class="panel-head">
            <h2 id="primary-title">Coverage Matrix</h2>
            <span class="small" id="visible-count"></span>
          </div>
          <div class="matrix-wrap" id="matrix-wrap">
            <table id="matrix-table"></table>
          </div>
          <div class="network" id="network-wrap">
            <svg id="network-svg" role="img" aria-label="Objective to exercise network"></svg>
          </div>
          <div class="legend">
            <span><span class="swatch" style="background:#e8f5f4"></span>Light coverage</span>
            <span><span class="swatch" style="background:#87c5c2"></span>Moderate coverage</span>
            <span><span class="swatch" style="background:#176b70"></span>Dense coverage</span>
            <span><span class="swatch" style="background:#f1eee8"></span>Orthogonal tag</span>
          </div>
        </section>

        <aside class="panel detail">
          <div class="panel-head">
            <h2>Selected Objective</h2>
            <span class="small" id="detail-count"></span>
          </div>
          <div class="detail-body" id="detail-body"></div>
        </aside>
      </div>
      <p class="source-note">Generated from <code>lesson_01_03_catalog.yml</code> and <code>lesson_01_03_exercise_edges.psv</code>.</p>
    </div>
  </main>
  <script id="mapping-data" type="application/json">{esc_script_json(data)}</script>
  <script>
    const DATA = JSON.parse(document.getElementById("mapping-data").textContent);
    const BOOKS = ["Lewis", "DHNRA", "Lamarsh"];
    const LESSONS = ["All", "L01", "L02", "L03"];
    const state = {{ lesson: "All", book: "All", view: "matrix", query: "", selected: null }};

    const objectivesById = new Map(DATA.objectives.map((objective) => [objective.id, objective]));
    const orthogonalById = new Map(DATA.orthogonal.map((tag) => [tag.id, tag]));
    const exerciseKey = (edge) => `${{edge.book}} ${{edge.exercise_id}}`;
    const objectiveSort = (a, b) => a.id.localeCompare(b.id, undefined, {{ numeric: true }});
    const edgeSort = (a, b) => {{
      const byBook = BOOKS.indexOf(a.book) - BOOKS.indexOf(b.book);
      return byBook || a.exercise_id.localeCompare(b.exercise_id, undefined, {{ numeric: true }});
    }};

    function init() {{
      state.selected = DATA.objectives[0]?.id ?? null;
      renderControls();
      bindControls();
      renderAll();
    }}

    function renderControls() {{
      const lessonControls = document.getElementById("lesson-controls");
      lessonControls.innerHTML = LESSONS.map((lesson) => `<button type="button" data-lesson="${{lesson}}" class="${{lesson === state.lesson ? "active" : ""}}">${{lesson}}</button>`).join("");

      const bookControls = document.getElementById("book-controls");
      bookControls.innerHTML = ["All", ...BOOKS].map((book) => `<button type="button" data-book="${{book}}" class="${{book === state.book ? "active" : ""}}">${{book}}</button>`).join("");
    }}

    function bindControls() {{
      document.getElementById("lesson-controls").addEventListener("click", (event) => {{
        const button = event.target.closest("button[data-lesson]");
        if (!button) return;
        state.lesson = button.dataset.lesson;
        renderControls();
        ensureSelectedVisible();
        renderAll();
      }});

      document.getElementById("book-controls").addEventListener("click", (event) => {{
        const button = event.target.closest("button[data-book]");
        if (!button) return;
        state.book = button.dataset.book;
        renderControls();
        ensureSelectedVisible();
        renderAll();
      }});

      document.getElementById("view-controls").addEventListener("click", (event) => {{
        const button = event.target.closest("button[data-view]");
        if (!button) return;
        state.view = button.dataset.view;
        document.querySelectorAll("#view-controls button").forEach((node) => node.classList.toggle("active", node.dataset.view === state.view));
        renderAll();
      }});

      document.getElementById("search-box").addEventListener("input", (event) => {{
        state.query = event.target.value.trim().toLowerCase();
        ensureSelectedVisible();
        renderAll();
      }});
    }}

    function filteredObjectives() {{
      return DATA.objectives.filter((objective) => {{
        if (state.lesson !== "All" && objective.lesson !== state.lesson) return false;
        if (!state.query) return true;
        const edges = edgesForObjective(objective.id);
        const text = [
          objective.id,
          objective.text,
          ...edges.flatMap((edge) => [
            edge.book,
            edge.exercise_id,
            edge.problem_path,
            edge.direct_basis,
            edge.orthogonal_objectives,
          ]),
        ].join(" ").toLowerCase();
        return text.includes(state.query);
      }}).sort(objectiveSort);
    }}

    function filteredEdges() {{
      return DATA.edges.filter((edge) => {{
        const objective = objectivesById.get(edge.objective_id);
        if (!objective) return false;
        if (state.lesson !== "All" && objective.lesson !== state.lesson) return false;
        if (state.book !== "All" && edge.book !== state.book) return false;
        if (!state.query) return true;
        const text = [
          edge.objective_id,
          objective.text,
          edge.book,
          edge.exercise_id,
          edge.problem_path,
          edge.direct_basis,
          edge.orthogonal_objectives,
        ].join(" ").toLowerCase();
        return text.includes(state.query);
      }}).sort(edgeSort);
    }}

    function edgesForObjective(objectiveId) {{
      return filteredEdges().filter((edge) => edge.objective_id === objectiveId);
    }}

    function rawEdgesForObjective(objectiveId) {{
      return DATA.edges.filter((edge) => edge.objective_id === objectiveId).sort(edgeSort);
    }}

    function ensureSelectedVisible() {{
      const visible = filteredObjectives();
      if (!visible.some((objective) => objective.id === state.selected)) {{
        state.selected = visible[0]?.id ?? null;
      }}
    }}

    function renderAll() {{
      const visibleObjectives = filteredObjectives();
      const visibleEdges = filteredEdges();
      const visibleExercises = new Set(visibleEdges.map(exerciseKey));
      const visibleTags = new Set(visibleEdges.flatMap(splitTags));

      document.getElementById("stat-objectives").textContent = visibleObjectives.length;
      document.getElementById("stat-exercises").textContent = visibleExercises.size;
      document.getElementById("stat-edges").textContent = visibleEdges.length;
      document.getElementById("stat-tags").textContent = visibleTags.size;
      document.getElementById("visible-count").textContent = `${{visibleObjectives.length}} rows, ${{visibleEdges.length}} edges`;

      document.getElementById("matrix-wrap").style.display = state.view === "matrix" ? "block" : "none";
      document.getElementById("network-wrap").style.display = state.view === "network" ? "block" : "none";
      document.getElementById("primary-title").textContent = state.view === "matrix" ? "Coverage Matrix" : "Objective-Exercise Network";

      renderMatrix(visibleObjectives);
      renderNetwork(visibleObjectives, visibleEdges);
      renderDetail();
    }}

    function renderMatrix(objectives) {{
      const table = document.getElementById("matrix-table");
      const maxCount = Math.max(1, ...objectives.flatMap((objective) => BOOKS.map((book) => edgesForObjective(objective.id).filter((edge) => edge.book === book).length)));

      table.innerHTML = `
        <thead>
          <tr>
            <th>Objective</th>
            ${{BOOKS.map((book) => `<th>${{book}}</th>`).join("")}}
          </tr>
        </thead>
        <tbody>
          ${{objectives.map((objective) => renderObjectiveRow(objective, maxCount)).join("")}}
        </tbody>
      `;
    }}

    function renderObjectiveRow(objective, maxCount) {{
      const selected = objective.id === state.selected ? "selected" : "";
      return `
        <tr class="${{selected}}" data-objective="${{objective.id}}">
          <td class="objective-cell" onclick="selectObjective('${{objective.id}}')">
            <div class="objective-id"><span class="lesson-pill">${{objective.lesson}}</span>${{objective.id}}</div>
            <div class="objective-text">${{escapeHtml(objective.text)}}</div>
          </td>
          ${{BOOKS.map((book) => renderBookCell(objective.id, book, maxCount)).join("")}}
        </tr>
      `;
    }}

    function renderBookCell(objectiveId, book, maxCount) {{
      const edges = edgesForObjective(objectiveId).filter((edge) => edge.book === book);
      if (!edges.length) {{
        return `<td class="book-cell"><div class="empty">-</div></td>`;
      }}
      const intensity = edges.length / maxCount;
      const bg = heatColor(book, intensity);
      return `
        <td class="book-cell">
          <div class="heat" style="background:${{bg}}" onclick="selectObjective('${{objectiveId}}')" title="${{escapeAttr(edges.map((edge) => `${{edge.book}} ${{edge.exercise_id}}: ${{edge.direct_basis}}`).join("\\n"))}}">
            <span class="count">${{edges.length}}</span>
            <div class="exercise-list">
              ${{edges.map((edge) => `<span class="chip">${{escapeHtml(edge.exercise_id)}}</span>`).join("")}}
            </div>
          </div>
        </td>
      `;
    }}

    function heatColor(book, intensity) {{
      const base = {{
        Lewis: [45, 108, 223],
        DHNRA: [179, 95, 0],
        Lamarsh: [111, 75, 178],
      }}[book];
      const alpha = 0.16 + Math.min(0.62, intensity * 0.62);
      return `rgba(${{base[0]}}, ${{base[1]}}, ${{base[2]}}, ${{alpha.toFixed(3)}})`;
    }}

    function renderNetwork(objectives, edges) {{
      const svg = document.getElementById("network-svg");
      const objectiveIds = objectives.map((objective) => objective.id);
      const exerciseGroups = new Map();
      for (const edge of edges) {{
        const key = exerciseKey(edge);
        if (!exerciseGroups.has(key)) {{
          exerciseGroups.set(key, {{ key, book: edge.book, exercise_id: edge.exercise_id, path: edge.problem_path, objectives: new Set() }});
        }}
        exerciseGroups.get(key).objectives.add(edge.objective_id);
      }}
      const exercises = Array.from(exerciseGroups.values()).sort((a, b) => {{
        const byBook = BOOKS.indexOf(a.book) - BOOKS.indexOf(b.book);
        return byBook || a.exercise_id.localeCompare(b.exercise_id, undefined, {{ numeric: true }});
      }});

      const rowHeight = 58;
      const width = 1120;
      const height = Math.max(680, Math.max(objectiveIds.length, exercises.length) * rowHeight + 80);
      const leftX = 36;
      const rightX = 728;
      const nodeWidth = 324;
      const nodeHeight = 38;
      const top = 42;
      const objectiveY = new Map(objectiveIds.map((id, index) => [id, top + index * rowHeight]));
      const exerciseY = new Map(exercises.map((exercise, index) => [exercise.key, top + index * rowHeight]));

      const edgeLines = edges.map((edge) => {{
        const y1 = objectiveY.get(edge.objective_id) + nodeHeight / 2;
        const y2 = exerciseY.get(exerciseKey(edge)) + nodeHeight / 2;
        const highlight = edge.objective_id === state.selected ? "highlight" : "";
        return `<path class="edge ${{highlight}}" d="M ${{leftX + nodeWidth}} ${{y1}} C 520 ${{y1}}, 610 ${{y2}}, ${{rightX}} ${{y2}}"></path>`;
      }}).join("");

      const objectiveNodes = objectives.map((objective) => nodeTemplate(leftX, objectiveY.get(objective.id), nodeWidth, nodeHeight, objective.id, objective.text, "objective", objective.id === state.selected)).join("");
      const exerciseNodes = exercises.map((exercise) => nodeTemplate(rightX, exerciseY.get(exercise.key), nodeWidth, nodeHeight, `${{exercise.book}} ${{exercise.exercise_id}}`, exercise.path.replace("books/", ""), "exercise", exercise.objectives.has(state.selected))).join("");

      svg.setAttribute("viewBox", `0 0 ${{width}} ${{height}}`);
      svg.innerHTML = `
        <text x="${{leftX}}" y="22" fill="#61666c" font-size="12" font-weight="700">Objectives</text>
        <text x="${{rightX}}" y="22" fill="#61666c" font-size="12" font-weight="700">Exercises</text>
        ${{edgeLines}}
        ${{objectiveNodes}}
        ${{exerciseNodes}}
      `;
    }}

    function nodeTemplate(x, y, width, height, label, sublabel, kind, active) {{
      const fill = active ? "#e1f1f0" : "#ffffff";
      const stroke = kind === "objective" ? "#176b70" : "#aeb8b3";
      const clippedSub = sublabel.length > 52 ? `${{sublabel.slice(0, 49)}}...` : sublabel;
      return `
        <g class="node" onclick="selectObjective('${{kind === "objective" ? label : state.selected}}')" style="cursor:${{kind === "objective" ? "pointer" : "default"}}">
          <rect x="${{x}}" y="${{y}}" width="${{width}}" height="${{height}}" fill="${{fill}}" stroke="${{stroke}}"></rect>
          <text x="${{x + 12}}" y="${{y + 14}}" font-weight="700">${{escapeSvg(label)}}</text>
          <text class="sub" x="${{x + 12}}" y="${{y + 29}}">${{escapeSvg(clippedSub)}}</text>
        </g>
      `;
    }}

    function renderDetail() {{
      const body = document.getElementById("detail-body");
      const count = document.getElementById("detail-count");
      if (!state.selected) {{
        count.textContent = "";
        body.innerHTML = `<p class="detail-text">No objective selected.</p>`;
        return;
      }}
      const objective = objectivesById.get(state.selected);
      const edges = edgesForObjective(state.selected);
      const allEdges = rawEdgesForObjective(state.selected);
      const tags = Array.from(new Set(edges.flatMap(splitTags)));
      count.textContent = `${{edges.length}} visible / ${{allEdges.length}} total`;
      body.innerHTML = `
        <h2 class="detail-title">${{objective.id}}</h2>
        <div class="detail-text">${{escapeHtml(objective.text)}}</div>
        <div class="detail-section">
          <h3>Exercises</h3>
          ${{edges.length ? edges.map(renderEdgeCard).join("") : `<div class="small">No visible exercises under the current filters.</div>`}}
        </div>
        <div class="detail-section">
          <h3>Orthogonal Tags</h3>
          ${{tags.length ? `<div class="tag-row">${{tags.map(renderTag).join("")}}</div>` : `<div class="small">No visible orthogonal tags.</div>`}}
        </div>
      `;
    }}

    function renderEdgeCard(edge) {{
      return `
        <div class="edge-card">
          <div class="edge-meta">
            <span>${{escapeHtml(edge.book)}} ${{escapeHtml(edge.exercise_id)}}</span>
            <span class="small">${{escapeHtml(edge.review_status)}}</span>
          </div>
          <div class="basis">${{escapeHtml(edge.direct_basis)}}</div>
          ${{splitTags(edge).length ? `<div class="tag-row">${{splitTags(edge).map(renderTag).join("")}}</div>` : ""}}
        </div>
      `;
    }}

    function renderTag(tagId) {{
      const tag = orthogonalById.get(tagId);
      const label = tagId.replace(/^ORTHO_/, "").replaceAll("_", " ").toLowerCase();
      return `<span class="tag" title="${{escapeAttr(tag?.text ?? tagId)}}">${{escapeHtml(label)}}</span>`;
    }}

    function splitTags(edge) {{
      const value = typeof edge === "string" ? edge : edge.orthogonal_objectives;
      return value ? value.split(";").map((tag) => tag.trim()).filter(Boolean) : [];
    }}

    function selectObjective(id) {{
      if (!id) return;
      state.selected = id;
      renderAll();
    }}

    function escapeHtml(value) {{
      return String(value ?? "").replace(/[&<>"']/g, (char) => ({{ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }}[char]));
    }}

    function escapeAttr(value) {{
      return escapeHtml(value).replace(/\\n/g, "&#10;");
    }}

    function escapeSvg(value) {{
      return escapeHtml(value);
    }}

    window.selectObjective = selectObjective;
    init();
  </script>
</body>
</html>
"""


def main() -> None:
    objectives, orthogonal = parse_catalog(CATALOG_PATH)
    edges = parse_edges(EDGES_PATH)
    OUTPUT_PATH.write_text(render_html(objectives, orthogonal, edges), encoding="utf-8")
    print(OUTPUT_PATH)


if __name__ == "__main__":
    main()
