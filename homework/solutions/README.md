# Fall 2026 NE 630 solution manual

This directory builds one instructor-only PDF covering Homework 01 through
Homework 18:

```bash
make
```

The canonical entry point is `fall_2026_ne630_solution_manual.tex`; the
`hwNN.tex` files are its section-level inputs.  Each homework problem starts
on a fresh page, followed immediately by its solution, for grading and
exam-design use. Existing solution language is
drawn from the matching LaTeX sources in
`/home/robertsj/Classes/ne630_problems` at commit `e1fba66`. Problem 1 of the
source Lesson 16 assignment supplies Homework 15; source Lesson 16 Problems 2
and 3 supply Homework 16. Lessons 17 and 18 retain their matching homework
numbers. New or materially adapted material is labeled in the PDF and
documented in source comments.

The figure files used by the manual are retained in `figures/`.  The Homework
05 plots are embedded outputs from `notebooks/lesson_05.ipynb`.  To extract
those outputs again and regenerate the Homework 06 plots from an OpenMC U-238
data file, run

```bash
python build_figures.py --u238-h5 /path/to/neutron/U238.h5
```

`build_figures.py` requires NumPy, Matplotlib, and h5py.  It uses the 294 K
MT-102 data and the corrected Fall 2026 value
`Gamma_n(80.75 eV) = 1.874e-3 eV`.

The Homework 18 plots are rebuilt automatically by `make` from
`data/hw18_p_over_d.csv` through `build_hw18_figures.py`. The retained data are
adapted from `ne630_problems/lesson_18/p_over_d.csv`; one plainly inconsistent
epsilon entry at `P/D=2.5` is corrected and documented in `hw18.tex`.
The figure builder requires NumPy and Matplotlib. To select a scientific
Python environment explicitly, run `make PYTHON=/path/to/environment/bin/python`.

This manual contains solutions and must not be added to the student-facing
Sphinx or `gh-pages` publication pipeline.
