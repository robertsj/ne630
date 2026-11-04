"""Refresh the two embedded plot tables in lesson_29_handout.tex.

Run this script beside the handout and lesson_29_feedback.py before rebuilding
with latexmk -xelatex lesson_29_handout.tex. Numerical annotations and prose
are for the supplied cases and must be revised when the constants change.
"""
from pathlib import Path
import re
import numpy as np

base = Path(__file__).resolve().parent
from lesson_29_feedback import solve, alpha, beta, n0

def table(times, external, states, tscale):
    data = [tscale*times]
    for y in states:
        data.extend([y[0]/n0, (external + alpha*y[2])/beta])
    rows = ['t fixedn fixedr An Ar Bn Br']
    rows.extend(' '.join(f'{v:.8g}' for v in row) for row in zip(*data))
    return '\n'.join(rows)

t1 = np.unique(np.r_[0, np.geomspace(.001, .5, 38), np.linspace(.5, 5, 31)])
t2 = 5 + t1
step = np.r_[np.full_like(t1, .003), np.zeros_like(t2)]
tp = np.linspace(0, .2, 121)
states, prompt = [], []
for model in ('fixed', 'A', 'B'):
    y1 = solve(.003, t1, model)
    y2 = solve(0., t2, model, y1[:, -1])
    states.append(np.hstack((y1, y2)))
    prompt.append(solve(1.5*beta, tp, model))
path = base / "lesson_29_handout.tex"
source = path.read_text(encoding="utf-8")
for key, args in [('mild', (np.r_[t1, t2], step, states, 1)),
                  ('prompt', (tp, 1.5*beta, prompt, 1000))]:
    tex = '\\pgfplotstableread{\n' + table(*args) + '\n}\\' + key + 'data\n'
    pattern = r'\\pgfplotstableread\{[^{}]*\}\\' + key + r'data\n'
    source, count = re.subn(pattern, lambda _: tex, source)
    if count != 1:
        raise ValueError(f"Expected exactly one {key} table, found {count}")
path.write_text(source, encoding="utf-8")
