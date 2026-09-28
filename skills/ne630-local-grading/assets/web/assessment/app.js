const params = new URLSearchParams(window.location.search);
let homeworkId = params.get("hw") || "hw01";
let data = null;
let scores = null;
let filter = "all";
let selected = null;
let saveTimer = null;

const EXPECTED = {
  "hw01.p01.a.q_value": { value: -6.885, tolerance: 0.02 },
  "hw01.p01.b.q_value": { value: 2.823, tolerance: 0.02 },
  "hw01.p01.c.q_value": { value: 17.346, tolerance: 0.03 },
  "hw01.p01.d.q_value": { value: 4.062, tolerance: 0.02 },
  "hw01.p02.percent_error": { value: -0.3184, tolerance: 0.05 },
  "hw01.p03.a.mass_fraction": { value: 9.1e-4, toleranceRel: 0.2 },
  "hw01.p03.b.mass_fraction": { value: 9.76e-11, toleranceRel: 0.2 },
};

const FEEDBACK = {
  pass: {
    tone: "green",
    score: 1,
    label: "Pass",
    text: "",
  },
  missing: {
    tone: "red",
    score: 0,
    label: "No usable extracted answer",
    text: "No usable answer was extracted for this part; review the original submission before assigning credit.",
  },
  p01_unit_kev: {
    tone: "yellow",
    score: 0.5,
    label: "keV/MeV unit conversion",
    text: "The Q-value appears to be in keV but was treated as MeV; convert by 1000 before reporting.",
  },
  p01_sign: {
    tone: "yellow",
    score: 0.5,
    label: "Q-value sign convention",
    text: "The Q-value magnitude is close, but the sign convention is reversed; use reactant masses minus product masses.",
  },
  p01_beta_atomic: {
    tone: "yellow",
    score: 0.5,
    label: "Beta-decay atomic masses",
    text: "For beta-minus Q-values with neutral atomic masses, do not subtract an extra electron mass; the expected value is about 2.823 MeV.",
  },
  p01_reaction_accounting: {
    tone: "red",
    score: 0,
    label: "Reaction balance or mass accounting",
    text: "The completed reaction or mass accounting is not consistent with A/Z conservation and the AME2020 masses.",
  },
  p02_sign: {
    tone: "yellow",
    score: 0.5,
    label: "Percent-error sign",
    text: "The percent-error magnitude is right, but the sign is reversed; use 100(Kapprox - Ktrue)/Ktrue, so this error is negative.",
  },
  p02_close: {
    tone: "yellow",
    score: 0.5,
    label: "Close percent error",
    text: "The percent-error calculation is close but outside tolerance; recheck the relativistic speed and avoid premature rounding.",
  },
  p02_formula: {
    tone: "red",
    score: 0,
    label: "Percent-error setup",
    text: "The percent-error result is not close to the reference; recheck the relativistic velocity and the Kapprox - Ktrue definition.",
  },
  p03_percent_fraction: {
    tone: "yellow",
    score: 0.5,
    label: "Percent vs fraction",
    text: "The result is reported as a percent or percent-scale value; convert it to the requested mass fraction.",
  },
  p03_scale: {
    tone: "red",
    score: 0,
    label: "Mass-fraction scale",
    text: "The mass-fraction scale is not close; recheck the reactant rest-mass denominator and eV/MeV conversion.",
  },
  p03c_review: {
    tone: "yellow",
    score: 0.5,
    label: "Consistency explanation review",
    text: "The consistency explanation needs review; state efficiency/composition assumptions and compare supplied energy to plant demand.",
  },
};

const els = {
  homeworkSelect: document.getElementById("homeworkSelect"),
  exportLink: document.getElementById("exportLink"),
  saveButton: document.getElementById("saveButton"),
  seedButton: document.getElementById("seedButton"),
  pathLine: document.getElementById("pathLine"),
  statusLine: document.getElementById("statusLine"),
  studentSearch: document.getElementById("studentSearch"),
  table: document.getElementById("assessmentTable"),
  detail: document.getElementById("cellDetail"),
  feedbackBank: document.getElementById("feedbackBank"),
};

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function setStatus(message) {
  els.statusLine.textContent = message;
}

function answerErrors(student, answer) {
  const suffix = answer.key.split(".").slice(1).join(".");
  return (student.errors || []).filter((error) => error.answer === suffix || error.answer === answer.key);
}

function studentAnswer(student, answer) {
  return student.answers?.[answer.key] || null;
}

function scoreObject(studentGroup, answerKey) {
  scores.scores[studentGroup] ||= {};
  scores.scores[studentGroup][answerKey] ||= {
    score: null,
    max_score: 1,
    notes: "",
    feedback_key: "",
  };
  scores.scores[studentGroup][answerKey].max_score ??= 1;
  return scores.scores[studentGroup][answerKey];
}

function numericValue(extracted) {
  const value = extracted?.row?.value?.value ?? extracted?.value?.value;
  return typeof value === "number" ? value : null;
}

function near(value, expected, tolerance) {
  return Math.abs(value - expected) <= tolerance;
}

function nearRel(value, expected, toleranceRel) {
  return Math.abs(value - expected) / Math.max(Math.abs(expected), 1e-300) <= toleranceRel;
}

function feedbackFor(student, answer) {
  const extracted = studentAnswer(student, answer);
  const errors = answerErrors(student, answer);
  if (!extracted) {
    return FEEDBACK.missing;
  }

  const status = extracted.comparison?.status;
  if (status === "match") return FEEDBACK.pass;
  if (answer.key === "hw01.p03.c.sanity_check_claim") return FEEDBACK.p03c_review;

  const spec = EXPECTED[answer.key];
  const value = numericValue(extracted);
  if (!spec || value === null || errors.length) {
    return FEEDBACK.p01_reaction_accounting;
  }

  if (answer.key.startsWith("hw01.p01.")) {
    if (Math.abs(value) > 100 && near(value / 1000, spec.value, Math.max(spec.tolerance * 2, 0.05))) {
      return FEEDBACK.p01_unit_kev;
    }
    if (near(value, -spec.value, Math.max(spec.tolerance * 8, 0.15))) {
      return FEEDBACK.p01_sign;
    }
    if (answer.key === "hw01.p01.b.q_value" && value > 2.2 && value < 2.4) {
      return FEEDBACK.p01_beta_atomic;
    }
    return FEEDBACK.p01_reaction_accounting;
  }

  if (answer.key === "hw01.p02.percent_error") {
    if (value > 0 && near(value, Math.abs(spec.value), 0.08)) return FEEDBACK.p02_sign;
    if (value < 0 && near(value, spec.value, 0.12)) return FEEDBACK.p02_close;
    return FEEDBACK.p02_formula;
  }

  if (answer.key.startsWith("hw01.p03.")) {
    if (nearRel(value / 100, spec.value, 0.25) || nearRel(value * 100, spec.value, 0.25)) {
      return FEEDBACK.p03_percent_fraction;
    }
    return FEEDBACK.p03_scale;
  }

  return FEEDBACK.p01_reaction_accounting;
}

function effectiveScore(student, answer) {
  const item = scoreObject(student.student_group, answer.key);
  if (item.score !== null && item.score !== "") {
    return {
      score: Number(item.score),
      feedback: FEEDBACK[item.feedback_key] || feedbackFor(student, answer),
      manual: true,
    };
  }
  return { score: feedbackFor(student, answer).score, feedback: feedbackFor(student, answer), manual: false };
}

function seedScores(overwrite = false) {
  let changed = false;
  for (const student of data.students) {
    for (const answer of data.answers) {
      const suggestion = feedbackFor(student, answer);
      const item = scoreObject(student.student_group, answer.key);
      if (overwrite || item.score === null || item.score === "") {
        item.score = suggestion.score;
        item.max_score = 1;
        item.feedback_key = Object.keys(FEEDBACK).find((key) => FEEDBACK[key] === suggestion) || "";
        item.notes = suggestion.text;
        changed = true;
      } else if (!item.notes && suggestion.text) {
        item.notes = suggestion.text;
        item.feedback_key ||= Object.keys(FEEDBACK).find((key) => FEEDBACK[key] === suggestion) || "";
        changed = true;
      }
    }
  }
  return changed;
}

function studentTotals(student) {
  let total = 0;
  let max = 0;
  let yellow = 0;
  let red = 0;
  let review = 0;
  for (const answer of data.answers) {
    const cell = effectiveScore(student, answer);
    total += cell.score;
    max += 1;
    if (cell.score === 0.5) yellow += 1;
    if (cell.score === 0) red += 1;
    if (studentAnswer(student, answer)?.extraction?.needs_review || answer.key === "hw01.p03.c.sanity_check_claim") review += 1;
  }
  return { total, max, yellow, red, review };
}

function filteredStudents() {
  const query = els.studentSearch.value.trim().toLowerCase();
  return data.students.filter((student) => {
    if (query && !student.student_group.toLowerCase().includes(query)) return false;
    const totals = studentTotals(student);
    if (filter === "yellow") return totals.yellow > 0;
    if (filter === "red") return totals.red > 0;
    if (filter === "review") return totals.review > 0 || (student.errors || []).length > 0;
    return true;
  });
}

function cellTone(score) {
  if (score >= 0.999) return "green";
  if (score > 0) return "yellow";
  return "red";
}

function displayValue(student, answer) {
  const extracted = studentAnswer(student, answer);
  if (!extracted) return "missing";
  return extracted.display || extracted.row?.value?.display || "";
}

function compactValue(value) {
  return String(value || "")
    .replaceAll("\\mathrm", "")
    .replaceAll("\\text", "")
    .replace(/[{}]/g, "")
    .replace(/\s+/g, " ")
    .slice(0, 42);
}

function renderTable() {
  const students = filteredStudents();
  const header = `
    <thead>
      <tr>
        <th class="student-col">Student</th>
        ${data.answers.map((answer) => `<th title="${escapeHtml(answer.label)}">${escapeHtml(answer.label.replace(" q value", ""))}</th>`).join("")}
        <th>Total</th>
      </tr>
    </thead>
  `;
  const body = students.map((student) => {
    const totals = studentTotals(student);
    const cells = data.answers.map((answer) => {
      const result = effectiveScore(student, answer);
      const tone = cellTone(result.score);
      const extracted = studentAnswer(student, answer);
      const review = extracted?.extraction?.needs_review ? " review" : "";
      const selectedClass = selected?.student === student.student_group && selected?.answer === answer.key ? " selected" : "";
      return `
        <td>
          <button class="score-cell ${tone}${review}${selectedClass}" data-student="${escapeHtml(student.student_group)}" data-answer="${escapeHtml(answer.key)}" type="button">
            <span class="cell-score">${result.score}</span>
            <span class="cell-value">${escapeHtml(compactValue(displayValue(student, answer)))}</span>
          </button>
        </td>
      `;
    }).join("");
    return `
      <tr>
        <th class="student-col" title="${escapeHtml(student.student_group)}">
          <span>${escapeHtml(student.student_group)}</span>
          <small>${totals.yellow} yellow · ${totals.red} red</small>
        </th>
        ${cells}
        <td class="total-cell">${totals.total.toFixed(1)} / ${totals.max}</td>
      </tr>
    `;
  }).join("");
  els.table.innerHTML = `${header}<tbody>${body}</tbody>`;
  els.table.querySelectorAll(".score-cell").forEach((button) => {
    button.addEventListener("click", () => {
      selected = { student: button.dataset.student, answer: button.dataset.answer };
      render();
    });
  });
}

function selectedStudentAndAnswer() {
  if (!selected && data.students[0] && data.answers[0]) {
    selected = { student: data.students[0].student_group, answer: data.answers[0].key };
  }
  return {
    student: data.students.find((item) => item.student_group === selected?.student),
    answer: data.answers.find((item) => item.key === selected?.answer),
  };
}

function renderDetail() {
  const { student, answer } = selectedStudentAndAnswer();
  if (!student || !answer) {
    els.detail.innerHTML = "<h2>No cell selected</h2>";
    return;
  }
  const extracted = studentAnswer(student, answer);
  const item = scoreObject(student.student_group, answer.key);
  const result = effectiveScore(student, answer);
  const feedback = result.feedback;
  const pdfLink = student.solution_pdf_url ? `<a class="button secondary" href="${student.solution_pdf_url}" target="_blank" rel="noreferrer">PDF</a>` : "";
  const textLink = extracted?.locator_url ? `<a class="button secondary" href="${extracted.locator_url}" target="_blank" rel="noreferrer">Text</a>` : "";
  els.detail.innerHTML = `
    <div class="detail-head">
      <div>
        <h2>${escapeHtml(student.student_group)}</h2>
        <p>${escapeHtml(answer.label)}</p>
      </div>
      <div class="detail-links">${pdfLink}${textLink}</div>
    </div>
    <div class="score-buttons" role="group" aria-label="Score">
      ${[1, 0.5, 0].map((score) => `<button class="${Number(item.score) === score ? "active" : ""}" data-score="${score}" type="button">${score}</button>`).join("")}
    </div>
    <div class="feedback-choice">
      <label>Feedback</label>
      <select id="feedbackSelect">
        ${Object.entries(FEEDBACK).filter(([key]) => key !== "pass").map(([key, value]) => `<option value="${key}"${(item.feedback_key || feedbackKey(feedback)) === key ? " selected" : ""}>${escapeHtml(value.label)}</option>`).join("")}
      </select>
    </div>
    <div class="detail-grid">
      <section>
        <h3>Expected</h3>
        <p>${escapeHtml(answer.expected_display)}</p>
        <pre>${escapeHtml(answer.expected_evidence || "")}</pre>
      </section>
      <section>
        <h3>Student</h3>
        <p>${escapeHtml(displayValue(student, answer))}</p>
        <pre>${escapeHtml(extracted?.evidence || answerErrors(student, answer).map((e) => e.reason).join("; "))}</pre>
      </section>
    </div>
    <label class="notes-label">Shared feedback / notes</label>
    <textarea id="notesInput">${escapeHtml(item.notes || feedback.text || "")}</textarea>
  `;

  els.detail.querySelectorAll(".score-buttons button").forEach((button) => {
    button.addEventListener("click", () => {
      const score = Number(button.dataset.score);
      item.score = score;
      item.max_score = 1;
      if (score === 1) {
        item.feedback_key = "pass";
        item.notes = "";
      } else if (!item.feedback_key || item.feedback_key === "pass") {
        const suggestion = feedbackFor(student, answer);
        item.feedback_key = feedbackKey(suggestion);
        item.notes = suggestion.text;
      }
      scheduleSave();
      render();
    });
  });

  const feedbackSelect = document.getElementById("feedbackSelect");
  feedbackSelect.addEventListener("change", () => {
    const selectedFeedback = FEEDBACK[feedbackSelect.value];
    item.feedback_key = feedbackSelect.value;
    item.score = selectedFeedback.score;
    item.notes = selectedFeedback.text;
    scheduleSave();
    render();
  });

  document.getElementById("notesInput").addEventListener("input", (event) => {
    item.notes = event.target.value;
    scheduleSave();
  });
}

function feedbackKey(feedback) {
  return Object.keys(FEEDBACK).find((key) => FEEDBACK[key] === feedback) || "";
}

function renderFeedbackBank() {
  els.feedbackBank.innerHTML = Object.entries(FEEDBACK)
    .filter(([key, item]) => key !== "pass")
    .map(([, item]) => `
      <article class="feedback-item ${item.tone}">
        <strong>${escapeHtml(item.score)} · ${escapeHtml(item.label)}</strong>
        <p>${escapeHtml(item.text)}</p>
      </article>
    `)
    .join("");
}

function render() {
  renderTable();
  renderDetail();
  renderFeedbackBank();
}

async function loadHomeworks() {
  const response = await fetch("/api/homeworks");
  const payload = await response.json();
  els.homeworkSelect.innerHTML = payload.homeworks
    .map((hw) => `<option value="${escapeHtml(hw)}"${hw === homeworkId ? " selected" : ""}>${escapeHtml(hw.toUpperCase())}</option>`)
    .join("");
}

async function loadData() {
  setStatus("Loading assessment data...");
  const response = await fetch(`/api/hw/${homeworkId}/data`);
  if (!response.ok) throw new Error(await response.text());
  data = await response.json();
  scores = data.scores;
  els.exportLink.href = `/api/hw/${homeworkId}/export.csv`;
  els.pathLine.textContent = `${data.paths.table} -> ${data.paths.scores}`;
  const seeded = seedScores(false);
  render();
  setStatus(`Loaded ${data.students.length} submissions. Draft scores ${seeded ? "prepared" : "already present"}.`);
  if (seeded) await saveNow();
}

async function saveNow() {
  clearTimeout(saveTimer);
  saveTimer = null;
  setStatus("Saving...");
  const response = await fetch(`/api/hw/${homeworkId}/scores`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(scores),
  });
  if (!response.ok) throw new Error(await response.text());
  scores = await response.json();
  setStatus(`Saved ${scores.updated_at}`);
}

function scheduleSave() {
  setStatus("Unsaved changes...");
  clearTimeout(saveTimer);
  saveTimer = setTimeout(() => saveNow().catch((error) => setStatus(`Save failed: ${error.message}`)), 600);
}

els.saveButton.addEventListener("click", () => saveNow().catch((error) => setStatus(`Save failed: ${error.message}`)));
els.seedButton.addEventListener("click", () => {
  seedScores(true);
  scheduleSave();
  render();
});
els.studentSearch.addEventListener("input", render);
document.querySelectorAll(".filter").forEach((button) => {
  button.addEventListener("click", () => {
    filter = button.dataset.filter;
    document.querySelectorAll(".filter").forEach((item) => item.classList.toggle("active", item === button));
    render();
  });
});
els.homeworkSelect.addEventListener("change", async () => {
  homeworkId = els.homeworkSelect.value;
  selected = null;
  history.replaceState(null, "", `/assessment/?hw=${homeworkId}`);
  await loadData();
});

(async function init() {
  try {
    await loadHomeworks();
    await loadData();
  } catch (error) {
    setStatus(`Load failed: ${error.message}`);
  }
})();
