#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const readline = require('readline/promises');
const { chromium } = require('playwright');

const PROJECT_ROOT = path.resolve(__dirname, '..');
const HOMEWORK_ID = process.env.HOMEWORK_ID || 'hw01';
const START_INDEX = Number.parseInt(process.env.START_INDEX || process.env.ROW_INDEX || '0', 10);
const STUDENT_COUNT = Number.parseInt(process.env.STUDENT_COUNT || '1', 10);
const STUDENT_OPTION_OFFSET = Number.parseInt(process.env.STUDENT_OPTION_OFFSET || '1', 10);
const CANVAS_SCORE = process.env.CANVAS_SCORE || '1';
const SPEEDGRADER_URL = process.env.SPEEDGRADER_URL || '';

const PROFILE_DIR = path.join(PROJECT_ROOT, 'canvas-browser-profile');
const DEFAULT_FEEDBACK_CSV = path.join(PROJECT_ROOT, HOMEWORK_ID, 'assessment', 'canvas_feedback.csv');
const DEFAULT_QUEUE_CSV = path.join(PROJECT_ROOT, HOMEWORK_ID, 'assessment', 'speedgrader_queue.csv');
const CSV_PATH = process.env.QUEUE_CSV || (fs.existsSync(DEFAULT_QUEUE_CSV) ? DEFAULT_QUEUE_CSV : DEFAULT_FEEDBACK_CSV);

const COMMENT_FRAME =
  'iframe[title="Rich Text Area. Press ALT+F8 for Rich Content Editor shortcuts."]';
const COMMENT_EDITOR_LABEL = 'Rich Text Area. Press ALT-0';

function parseCsv(text) {
  const rows = [];
  let row = [];
  let field = '';
  let inQuotes = false;

  for (let i = 0; i < text.length; i += 1) {
    const char = text[i];
    const next = text[i + 1];

    if (char === '"') {
      if (inQuotes && next === '"') {
        field += '"';
        i += 1;
      } else {
        inQuotes = !inQuotes;
      }
      continue;
    }

    if (!inQuotes && char === ',') {
      row.push(field);
      field = '';
      continue;
    }

    if (!inQuotes && (char === '\n' || char === '\r')) {
      if (char === '\r' && next === '\n') {
        i += 1;
      }
      row.push(field);
      rows.push(row);
      row = [];
      field = '';
      continue;
    }

    field += char;
  }

  if (field.length > 0 || row.length > 0) {
    row.push(field);
    rows.push(row);
  }

  return rows.filter((csvRow) => csvRow.some((value) => value.length > 0));
}

function readFeedbackRows(csvPath) {
  const csv = fs.readFileSync(csvPath, 'utf8');
  const [headers, ...records] = parseCsv(csv);

  return records.map((record) =>
    Object.fromEntries(headers.map((header, index) => [header, record[index] || ''])),
  );
}

function previewFeedback(row, rowIndex) {
  const internalScore = row.internal_total_score || row.total_score || '';
  const internalMax = row.internal_total_max || row.total_max || '';
  const submissionStatus = row.submission_status || 'submitted';
  const bodyPreview = row.feedback_text
    .split(/\r?\n/)
    .filter(Boolean)
    .slice(0, 4)
    .join('\n');

  console.log(`CSV row: ${rowIndex + 1}`);
  console.log(`Student/group: ${row.student_group}`);
  console.log(`Submission status: ${submissionStatus}`);
  if (internalScore || internalMax) {
    console.log(`Internal score: ${internalScore || '?'} / ${internalMax || '?'}`);
  }
  console.log(`Canvas score to fill: ${canvasScoreForRow(row)}`);
  console.log('Feedback preview:');
  console.log(bodyPreview);
  console.log('');
}

function canvasScoreForRow(row) {
  return row.canvas_score || CANVAS_SCORE;
}

async function fillCurrentStudent(page, row) {
  await page.getByTestId('grade-input').fill(canvasScoreForRow(row));
  await page.frameLocator(COMMENT_FRAME).getByLabel(COMMENT_EDITOR_LABEL).fill(row.feedback_text);
}

async function advanceToCsvRow(page, rowIndex) {
  const optionId = rowIndex + STUDENT_OPTION_OFFSET;
  await page.getByTestId('student-select-trigger').click();
  await page.getByTestId(`student-option-${optionId}`).click();
  await page.waitForLoadState('domcontentloaded', { timeout: 10000 }).catch(() => {});
  await page.getByTestId('grade-input').waitFor({ timeout: 15000 });
}

async function main() {
  if (!fs.existsSync(CSV_PATH)) {
    throw new Error(`Cannot find feedback/queue CSV: ${CSV_PATH}`);
  }

  const rows = readFeedbackRows(CSV_PATH);
  const selectedRows = rows.slice(START_INDEX, START_INDEX + STUDENT_COUNT);

  if (!Number.isInteger(START_INDEX) || START_INDEX < 0) {
    throw new Error(`START_INDEX must be a non-negative integer; got ${process.env.START_INDEX || process.env.ROW_INDEX}.`);
  }

  if (!Number.isInteger(STUDENT_COUNT) || STUDENT_COUNT < 1) {
    throw new Error(`STUDENT_COUNT must be a positive integer; got ${process.env.STUDENT_COUNT}.`);
  }

  if (selectedRows.length !== STUDENT_COUNT) {
    throw new Error(
      `Requested ${STUDENT_COUNT} row(s) starting at ${START_INDEX}, but only ${selectedRows.length} are available.`,
    );
  }

  if (process.env.PREVIEW_ONLY === '1') {
    selectedRows.forEach((row, offset) => previewFeedback(row, START_INDEX + offset));
    return;
  }

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  let context;

  try {
    context = await chromium.launchPersistentContext(PROFILE_DIR, {
      headless: false,
    });

    const page = context.pages()[0] || (await context.newPage());
    console.log(`Using CSV: ${CSV_PATH}`);

    if (!SPEEDGRADER_URL) {
      console.log('No SPEEDGRADER_URL configured; use the browser to navigate manually.');
    } else {
      await page.goto(SPEEDGRADER_URL);
    }

    await rl.question(
      `Log in/navigate to CSV row ${START_INDEX + 1}, then press Enter to begin. `,
    );

    for (let offset = 0; offset < selectedRows.length; offset += 1) {
      const rowIndex = START_INDEX + offset;
      const row = selectedRows[offset];

      previewFeedback(row, rowIndex);

      if (offset > 0) {
        await rl.question('Verify Canvas is on this student, then press Enter to fill only. ');
      }

      await fillCurrentStudent(page, row);

      console.log('Filled score and comment. Nothing has been submitted yet.');
      const answer = await rl.question('After reviewing Canvas, type y then Enter to submit: ');

      if (answer.trim().toLowerCase() !== 'y') {
        console.log('Stopped before submitting. Canvas was left filled for manual review.');
        break;
      }

      await page.getByTestId('submit-comment-button').click();
      console.log(`Submitted CSV row ${rowIndex + 1}.`);

      if (offset >= selectedRows.length - 1) {
        break;
      }

      const nextRowIndex = rowIndex + 1;
      const nextRow = selectedRows[offset + 1];
      const moveAnswer = await rl.question(
        `Type n then Enter to advance Canvas to CSV row ${nextRowIndex + 1} (${nextRow.student_group}), or press Enter to stop: `,
      );

      if (moveAnswer.trim().toLowerCase() !== 'n') {
        console.log('Stopped after submit; Canvas was not advanced.');
        break;
      }

      await advanceToCsvRow(page, nextRowIndex);
    }

    await rl.question('Press Enter to close the Playwright browser. ');
  } finally {
    rl.close();
    if (context) {
      await context.close();
    }
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
