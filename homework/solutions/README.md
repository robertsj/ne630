# Fall 2026 NE 630 solution manual

This directory builds one instructor-only PDF covering Homework 01 through
Homework 28.
HW24, HW27, and HW28 are source-based drafts pending assignment confirmation:

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

Homeworks 25 and 26 retain the three Lesson 25 problems and two Lesson 26
problems from `ne630_problems` at `9c3dc61`. Homework 26 adds a new pulsed
accelerator-driven reactor exercise as Problem 3. The statements match the
student Markdown drafts, and the new exercise's solution is labeled DRAFT.
The adapted solutions correct the legacy fast-neutron description, missing
integration differential, flux-ratio orientation, source units, and inconsistent
downscatter/rounded-removal data. The stated `0.0427 cm^-1` downscatter value
is used consistently; the resulting one-group and two-group steady balances agree.

`build_hw25_26_figures.py` verifies the numerical answers, checks the steady
two-group balance and both transient models independently, and regenerates the
two Homework 26 solution plots. It requires NumPy, SciPy, and Matplotlib:

```bash
python build_hw25_26_figures.py
make PYTHON=/path/to/environment/bin/python
```

The pulsed-source solution integrates over a complete periodic cycle, including
the neutron tail after beam shutoff. Its thermal/electrical power comparison is
not a claim of net electrical production. The optional waveform plot is an
instructor check, not an additional student requirement.

This manual contains solutions and must not be added to the student-facing
Sphinx or `gh-pages` publication pipeline.


## HW19–24 and HW27–28 additions (2026-11-02)

HW20–23 statements match the current student Markdown (converted with Pandoc).
HW24, HW27, and HW28 use `ne630_problems` at `9c3dc61` because no current
assignment files were found. HW19 uses the Canvas statement supplied by Jeremy
on November 2, 2026, now archived in `../markdown/HW19.md` and `../html/HW19.html`.
Its solution is new and uses actual OpenMC runs of the Lesson 19 cell.

The new verification/figure builder requires NumPy, SciPy, and Matplotlib:

```bash
python build_hw20_28_figures.py
make PYTHON=/home/robertsj/opt/miniforge3/bin/python
```

It checks control criticality, analytic temperature derivatives against finite
differences, xenon decay against an independent ODE and its peak condition,
Pa/U formulas including coincident-rate and zero-U-removal limits, unequal-batch
criticality, six-group `solve_ivp` against matrix exponentials on each interval,
and the one-group modal solution against a matrix exponential. It regenerates
three instructor-only figures. This builder does not run OpenMC; the separate
HW19 study below does.

### Deviations and grading decisions

| HW | Treatment |
| --- | --- |
| 19 | Canvas statement recovered. Uses U-235 atom fraction among uranium atoms, converting the default 15 wt% first. Targets k-infinity = 1, not the notebook's illustrative 1/0.90 finite-core target. Reports the first interpolation and its independent check even when refinement is needed. |
| 20 | Preserves legacy rounded 270 g/mol and table slowing-down power 1.28 cm⁻¹, explicitly distinguished from HW17's microscopic estimate. Repairs missing rod-cross-section divisor; replaces invalid addition of defects from different control states with direct hot-excess evaluation. |
| 21 | Separates number-ratio ppm, B-10 mass ppm, and natural-boron mass ppm; OpenMC accepts elemental-boron mass ppm. Separates d(log k)/dT from dρ/dT away from criticality. Retains labeled historical transport data, fixes cell/effective-k terminology, and propagates tally errors consistently. 4800 ppm is a near-critical historical estimate, not a newly fitted root. |
| 22 | Current statement says the peak is 11.3 h; given half-lives/yields/flux imply 8.51278 h. Supplies both 11.3-h requested evaluation and actual peak; recommends correcting the statement before requiring one unique answer. Fixed hot-state, fuel-volume worth convention retained. |
| 23 | Matches current atom-fraction/constant-inventory assumptions; corrects sign on a general initial-condition term and missing time factors in legacy integrating factors. Adds equal-rate and zero-removal limits without importing unneeded example material data. |
| 24 | Source Problem 1 duplicates current HW25 Problem 3; retained explicitly rather than silently renumbered. Includes unequal-power three-batch bonus. |
| 27 | Follows signed reactivity histories rather than ambiguous insertion/removal wording. Distinguishes production-weighted beta from true importance-weighted beta_eff. Uses segmented stiff integration at 1 and 6 s; all precursor inventories retained. |
| 28 | Restores missing n in neutron equation; distinguishes modal rates from time constants. Preserves small-reactivity period approximation because generation time is unspecified in Problem 1. Supplies missing bonus derivation and adds the scale-separation condition absent from the source near prompt criticality. |

OpenMC concentration convention checked against the
[official API documentation](https://docs.openmc.org/en/stable/pythonapi/generated/openmc.model.borated_water.html).
The source problem repository and existing student assignments were not modified.
The missing HW19 student statement was recovered from the supplied Canvas text.
These solutions and plots are instructor-only and are not part of gh-pages.


### HW19 reproducible transport study

`hw19_sfr_model.py` retains the constants and `build_sfr_model` implementation
from `notebooks/lesson_19.ipynb` (notebook SHA256
`d51136a6fe47be0817432889df3160342f567c3c43b496b0603b0ce8717ffabb`).
The original notebook is unchanged. `build_hw19_figures.py --run` uses OpenMC
0.16.0 and the installed ENDF/B-VIII.0 HDF5 library, with 5000 particles per
batch, 120 batches, and 30 inactive batches. It retains independent seeds,
reported eigenvalue standard errors, regional reaction rates, generation
estimates, source entropy, and hashes of the model and library manifest in
`data/hw19_results.json`. Statepoint scratch files are temporary.

The fissile-content input is **U-235 atom fraction among uranium atoms**;
`x0 = 0.15162795205640187` is the atom-fraction equivalent of 15 wt% U-235.
The prescribed cases multiply that atom fraction, not the weight percentage.
All geometry, densities, coolant, and temperatures remain those of Lesson 19.
The reflecting-cell eigenvalue is interpreted as k-infinity, not a finite-core
criticality prediction. The first interpolation is always checked independently;
if the check is outside two reported standard errors of one, up to two local
bracket refinements are also checked. This is a refinement heuristic, not a
statistical test of curvature: endpoint noise also affects the estimate.

Regenerate figures from the saved results (no transport calculation):

```bash
python build_hw19_figures.py
```

Recompute the study using an environment with OpenMC and its executable on PATH:

```bash
OPENMC_CROSS_SECTIONS=/path/to/cross_sections.xml python build_hw19_figures.py --run --threads 2
```

A normal `make` only redraws saved data, never launches OpenMC. After a new
transport run, update the rounded numerical table and interpolation values in
`hw19.tex` to match the saved results. Reported Monte Carlo standard errors are
not nuclear-data, geometry, or model uncertainties. Source-entropy and generation
histories are retained as diagnostics; naive half-run comparisons are not a
formal independent convergence proof. See the [OpenMC execution-settings guide](https://docs.openmc.org/en/stable/usersguide/settings.html)
for inactive batches and source convergence.

The saved five-run reference study gives a first estimate of 9.02404 atom%
(check: 1.015286 ± 0.000954), then a locally refined estimate of 8.75096 atom%
(check: 0.999839 ± 0.000886). The first result is retained explicitly rather
than replaced silently by the refined result.
