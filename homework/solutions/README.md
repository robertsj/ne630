# Fall 2026 NE 630 solution manual

This directory builds one instructor-only PDF covering Homework 01 through
Homework 28, including the current local four-part depletion/Gd Homework 24:

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

Homework 24 is included in the canonical manual and also has a standalone instructor review packet:

```bash
make hw24_review.pdf PYTHON=/path/to/scientific/python
```

The [review PDF](hw24_review.pdf) contains the written solution, generated
tables and plots, and the disposition of the invalid
infinite-dilution cycle model. Its section source is [hw24.tex](hw24.tex);
both PDFs now use the same section and numerical assets in the full HW01--28 manual.

The solution follows the current local `../markdown/HW24.md`, confirmed by the instructor on November 2, 2026, with four required parts. Part (2) plots
spectrum-averaged macroscopic Gd-157 and Xe-135 absorption in cm⁻¹ for
the Gd-bearing case during the first 30 days; its samples and endpoints
are retained in the `poison_absorption_*.csv` files. The cross-section
mistake is part (4) and reruns only the non-Gd case with infinite-dilution data.
The earlier 10 MWd/kg core
comparison is retained as an optional verification appendix.

[build_hw24_solution.py](build_hw24_solution.py) reruns the three calculations
and fails if any numerical verification check fails. It requires NumPy,
SciPy, pandas, and Matplotlib. The checks include independent power,
burnup, heavy-metal mass and neutron balances; analytic Gd depletion;
solver convergence with BDF and Radau; sampling sensitivity; and EOC
interpolation bounds. [data/hw24/](data/hw24/) retains summary, financial
arithmetic, verification and core-history CSV files, complete inventory
histories compressed as `.csv.gz`, and source hashes/package versions in
`provenance.json`. pandas reads the compressed CSV files directly.

The executed [solution notebook](hw24_solution.ipynb) embeds the same
numerical source, including the verification checks. Run it from inside
this checkout. To regenerate its source after changing the builder, run
`python build_hw24_solution.py --notebook` (also requires nbformat), then
execute all cells with Jupyter or nbclient. Regeneration clears previous
outputs; execute the notebook before presenting it as verified.

This solution uses a finer grid than the starter to resolve startup; the
retained starter-grid comparison quantifies the small difference. Both
shielded limiting discharge burnups exceed the simulated history. Every
nonlinear EOC residual at a fitted limiting cycle is therefore explicitly
unsupported. The approximately $43.70 million figure is formal
arithmetic from an invalid altered cycle model, not established losses.


## Homeworks 27 and 28

The existing manual now includes `hw27.tex` (two problems) and `hw28.tex`
(three current problems, with Problem 3 no longer labeled bonus). Source provenance, numbering,
limited prompt corrections, and unresolved source limitations are documented
in `../README.md`. Matching worked solutions are adapted from source Lessons
27–28 and checked against their notebooks. Problem 3 has no worked source solution. The qualified new derivation from
upstream `232ceea` is included, together with its additional scale-separation
restriction and the counterexample to the unchanged student hypotheses.

Run only the new numerical checks/assets with:

    /home/robertsj/miniforge3/bin/python build_hw27_28_checks.py

This checks HW27 critical equilibrium and each piecewise transient against
independent Radau integration, and HW28 two-mode analytical coefficients and
densities against both matrix exponentials and Radau. Data and check values
are retained in `data/hw27_28/`; the missing legacy HW27 solution plot is
regenerated as `figures/hw27_neutron_density.png`. None of this uses or repairs
the unrelated course `ne630_kinetics.py` API mismatch.

Build the complete canonical manual without a figure override:

    PATH=/home/robertsj/miniforge3/bin:$PATH make PYTHON=/home/robertsj/miniforge3/bin/python

HW24 tables and figures are explicit prerequisites; its builder tracks the
authoritative Markdown and local `code/ne630_depletion.py`. The existing
executed HW24 notebook embeds the identical builder source and is retained.

## HW19–24 working-tree reconciliation (November 2, 2026)

The remote was fetched and `origin/Fall2026` remained at `232ceea`. Only
missing HW19–23 manual sources/dependencies and the qualified HW28 solution
were initially imported from upstream. The November 3 commit is based on
that history and retains its HW19 statement and transport provenance.
Current student Markdown/HTML, the local depletion module, and notebook
inputs are unchanged. The conflicting upstream HW24 statement was rejected.
The local HW24 derivation and numerical builder already matched all four
parts; the solution now includes the common inputs and fuller problem
statements, and its three cases and 42 checks have been rerun locally.
The former legacy-HW24 block was removed from the imported multi-homework
checker so it cannot be mistaken for the current assignment.

HW19 uses the instructor-supplied Canvas statement retained in `hw19.tex`,
with upstream OpenMC results in `data/hw19_results.json`. These are retained
transport calculations, not newly run calculations in this reconciliation.
`build_hw19_figures.py` redraws these results without OpenMC; only explicit
`--run` launches transport. `hw19_sfr_model.py` retains the Lesson 19 model.
The input is U-235 atom fraction among uranium: the default 15 wt% converts
to 0.1516279521. The initial interpolated 9.02404 atom% gives
1.015286 ± 0.000954; the refined 8.75096 atom% gives 0.999839 ± 0.000886.
Do not interpret the cell threshold as finite-core criticality.

`build_hw20_28_figures.py` checks HW20–23 and HW27–28 with NumPy, SciPy,
and Matplotlib. It verifies control balances, temperature derivatives,
Xe against an independent ODE/peak condition, Pa/U equal-rate and
zero-removal limits, and kinetic modes against matrix exponentials.
It regenerates the HW21, HW22, and independent HW27 figures; it does not
use or repair the unrelated course kinetics module.

Inherited qualifications are retained, not resolved by changing prompts:

- HW20 uses the stated rounded 270 g/mol and slowing-down power 1.28 cm⁻¹;
  direct hot-excess evaluation avoids adding defects from different states.
- HW21 distinguishes number-ratio, B-10 mass, and natural-boron mass ppm;
  historical transport coefficients are labeled, not newly simulated.
- HW22 retains the requested 11.3-hour evaluation and the computed actual
  peak of 8.51278 hours; the discrepancy remains an instructor decision.
- HW23 follows current atom-fraction and constant-U-238 assumptions, with
  corrected initial-condition signs and time factors plus limiting cases.
- HW24 has four required parts, not the legacy batch-algebra problems.
  The optional 10 MWd/kg core comparison is not a fifth assigned problem.
- HW28 Problem 3 remains conditional on additional scale separation.

The corrected source and supporting assets are committed on Fall2026.
Generated solution PDFs remain ignored and local-only; no Sphinx, gh-pages,
or Canvas publication is part of this source update.

The startup/extrema table uses explicit pandas column access and a
regression assertion requiring both shielded rows and their exact reference
values. The executed notebook embeds the same corrected source.


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


### Deviations and grading decisions

| HW | Treatment |
| --- | --- |
| 19 | Canvas statement recovered. Uses U-235 atom fraction among uranium atoms, converting the default 15 wt% first. Targets k-infinity = 1, not the notebook's illustrative 1/0.90 finite-core target. Reports the first interpolation and its independent check even when refinement is needed. |
| 20 | Preserves legacy rounded 270 g/mol and table slowing-down power 1.28 cm⁻¹, explicitly distinguished from HW17's microscopic estimate. Repairs missing rod-cross-section divisor; replaces invalid addition of defects from different control states with direct hot-excess evaluation. |
| 21 | Separates number-ratio ppm, B-10 mass ppm, and natural-boron mass ppm; OpenMC accepts elemental-boron mass ppm. Separates d(log k)/dT from dρ/dT away from criticality. Retains labeled historical transport data, fixes cell/effective-k terminology, and propagates tally errors consistently. 4800 ppm is a near-critical historical estimate, not a newly fitted root. |
| 22 | Current statement says the peak is 11.3 h; given half-lives/yields/flux imply 8.51278 h. Supplies both 11.3-h requested evaluation and actual peak; recommends correcting the statement before requiring one unique answer. Fixed hot-state, fuel-volume worth convention retained. |
| 23 | Matches current atom-fraction/constant-inventory assumptions; corrects sign on a general initial-condition term and missing time factors in legacy integrating factors. Adds equal-rate and zero-removal limits without importing unneeded example material data. |
| 24 | Current four-part depletion/Gd assignment replaces the legacy batch-algebra sheet. The infinite-dilution cycle is invalid; its revenue difference is formal arithmetic only. The optional 10-MWd/kg check is not a fifth assigned problem. |
| 27 | Uses current remote student statement and its checked solution/figure. Follows signed reactivity histories rather than ambiguous insertion/removal wording. Distinguishes production-weighted beta from true importance-weighted beta_eff. Uses segmented stiff integration at 1 and 6 s; all precursor inventories retained. |
| 28 | Restores missing n in neutron equation; distinguishes modal rates from time constants. Preserves small-reactivity period approximation because generation time is unspecified in Problem 1. Uses current Problem 3 (no longer bonus), preserves the remote validity warning and asymptotic counterexample, and supplies a labeled new derivation under the additional scale-separation restriction. The student prompt remains unchanged and requires instructor review. |

OpenMC concentration convention checked against the
[official API documentation](https://docs.openmc.org/en/stable/pythonapi/generated/openmc.model.borated_water.html).
The source problem repository and existing student assignments were not modified.
The missing HW19 student statement was recovered from the supplied Canvas text.
These solutions and plots are instructor-only and are not part of gh-pages.
