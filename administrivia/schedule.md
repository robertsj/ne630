# NE 630 Detailed Schedule

This file documents the detailed schedule workflow. It is intentionally
separate from the syllabus because the syllabus should carry only the
CourseDog-required general roadmap and major graded-component timing.

The dated Canvas schedule source is `schedule-source.psv`. The Canvas HTML
snippet is produced by `tool/build_canvas_schedule.py`.

Term: Fall 2026

Meeting pattern: MWF, 1:30-2:20 p.m.

Location: Ward 135

Detailed dates should be synchronized with Canvas before the first class
session and updated there as the semester evolves.

## Term Anchors

- First day of Fall 2026 classes: Monday, August 24, 2026.
- No class: Monday, September 7, 2026, for Labor Day.
- No class: Friday, October 9, 2026, for Fall break / Wildcat Pause Day.
- No class: Monday, November 23, Wednesday, November 25, and Friday, November
  27, 2026, for Fall break. Thanksgiving Holiday is observed Thursday-Friday,
  November 26-27.
- Final exams: Monday, December 14, 2026 through Friday, December 18, 2026.
- Planned Exam 1: Friday, October 2, 2026.
- Planned Exam 2: Friday, November 6, 2026.
- Planned Exam 3: Friday, December 18, 2026, 11:50 a.m.-1:40 p.m., based on
  the MWF 1:30 p.m. meeting pattern.

## Canvas Schedule Printer

To rebuild the Canvas schedule snippet:

```bash
/home/robertsj/miniforge3/bin/python administrivia/tool/build_canvas_schedule.py
```

The generated copy/paste target is `generated/schedule-canvas.html`.

To print the snippet directly to the terminal:

```bash
/home/robertsj/miniforge3/bin/python administrivia/tool/build_canvas_schedule.py --stdout
```

The builder validates that the Fall 2026 no-class dates and major exam dates
are present before writing the Canvas HTML.

The official K-State 2026-2027 academic calendar lists Fall 2026 semester
dates as August 24-December 18, Labor Day on September 7, Wildcat Pause Day on
October 9, Fall Break on November 22-29, Thanksgiving Holiday observed on
November 26-27, and final examinations on December 14-18.

## Fall 2026 Topic Roadmap

The day-by-day schedule in `schedule-source.psv` follows the prior NE 630
schedule while shifting around Fall 2026 no-class days.

| Weeks | Dates | Main Topics | Major Items |
| --- | --- | --- | --- |
| 1-2 | Aug 24-Sep 4 | Nuclear reactions, fission, radioactive decay, neutron attenuation, and cross-section data | Homework begins |
| 3 | Sep 7-11 | Labor Day; scattering kinematics; eta and moderators | No class Sep 7 |
| 4-5 | Sep 14-25 | Fast and thermal spectra, resonance absorption, effective cross sections, multigroup equations, and k-eigenvalue problems |  |
| 6 | Sep 28-Oct 2 | Reactor core survey and fast reactor unit-cell analysis | Exam 1 on Oct 2 |
| 7 | Oct 5-9 | Thermal unit cells and OpenMC modeling | No class Oct 9 |
| 8-10 | Oct 12-30 | Unit-cell design, reactivity, feedback, poisons, depletion, and point kinetics |  |
| 11 | Nov 2-6 | Step reactivity changes and feedback | Exam 2 on Nov 6 |
| 12-13 | Nov 9-20 | Diffusion equation and one-speed diffusion models |  |
| 14 | Nov 23-27 | Fall break and Thanksgiving holiday | No class all scheduled meetings |
| 15-16 | Nov 30-Dec 11 | Criticality, reflected reactors, perturbation theory, transport preview, and review | Prep week |
| Finals | Dec 14-18 | Final exam period | Exam 3 on Dec 18 |

## Schedule Maintenance Rules

- Keep `schedule-source.psv`, the generated Canvas snippet, and Canvas aligned,
  but let Canvas be the student-facing operational schedule during the term.
- Do not paste this full table into `syllabus.md`.
- If an exam date changes after the CourseDog submission, use
  `templates/syllabus-addendum.md` and announce the addendum in Canvas.
- Minor reading swaps, pacing changes, and homework-detail changes can be
  announced in Canvas without a formal syllabus addendum.
