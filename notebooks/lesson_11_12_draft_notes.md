# Lessons 11 and 12 — instructor review

These are separate, executable drafts. The existing `lesson_10.ipynb` and
`lesson_12.ipynb` have not been replaced.

- [Lesson 11 draft](lesson_11_draft.ipynb): extend Lesson 10 through the thermal
  range using the ideas in
  [`NeutronThermalization.ipynb`](../../xfnrp/Chapter3/NeutronThermalization.ipynb).
  Includes thermal balance, detailed balance, bound-hydrogen scattering,
  Maxwellian **flux** versus neutron number density, temperature comparisons,
  uranium absorption, and correct per-source flux normalization.
- [Lesson 12 draft](lesson_12_draft.ipynb): add energy-resolved and all-energy
  `nu-fission`, `absorption`, and `flux` tallies; derive effective macroscopic
  cross sections; scan and refine H/U; check a rate ratio with independent
  replicas; and run the same material as a k-eigenvalue problem.

## Modeling choices to review

- H/U means hydrogen **atoms per total uranium atom**. H2O/U is half that value.
- Natural uranium, water oxygen only, 294 K, prescribed density 1 g/cm³,
  reflecting sphere, no artificial 1 eV neutron-energy cutoff. This is the
  homogeneous pedagogical material from Lesson 10, not a UO2 lattice.
- Lesson 11 suppresses fission descendants to isolate thermalization of the
  imposed 1 MeV source. Lesson 12 explicitly transports descendants in the
  main fixed-source scan, then compares a descendants-suppressed calculation.
  Fixed-source mode alone does not determine this choice.
- The moderation curve uses **mixture absorption** in its denominator:
  `eta_mix = P/A_mix`. Conventional fuel-only reproduction is `eta_fuel = P/A_U`.
  Both are displayed, with `eta_mix = eta_fuel * (A_U/A_mix)`.
  Here the absorption fractions are all-energy quantities, not a claim that
  these are separately the thermal factors in a four-factor decomposition.
- The requested value near 0.85 is a qualitative expectation, not a fitted
  target. The notebook reports the computed value and the sampled H/U maximum.
  Independent replicas check the winning point; establishing a precise optimal
  H/U would also require more statistics at neighboring points.
- In eigenvalue mode, the 1 MeV distribution is only an initial source-bank
  guess. Later generations use fission distributions from the evaluated data.
  Inactive generations, a generation trace, and normalized spectral comparisons
  make that change visible.
- The optional neutron-balance check includes the small excess from non-fission
  neutron-producing reactions. It uses an analog `scatter`/`nu-scatter` tally;
  the main flux and reaction-rate tallies use the track-length estimator.

## Running the drafts

Use a Jupyter kernel in an environment containing OpenMC, its executable,
NumPy, pandas, and Matplotlib. Set `OPENMC_CROSS_SECTIONS` to a continuous-energy
data library with natural-U isotopes, H-1, O-16, and `c_H_in_H2O` data. Lesson 11
also uses 600 K data. The drafts were checked using the existing `openmc` conda
environment and the local ENDF/B-VIII.0 library.

Run cells from top to bottom. By default, output XML/HDF5 files go under
`.ne630_draft_runs/lesson_11` or `.ne630_draft_runs/lesson_12` in the notebook
working directory; this directory is git-ignored. Set `NE630_RUN_DIR` before
starting the kernel to redirect scratch files. Every calculation gets a new
case directory, so repeated cells cannot silently consume old statepoints.

Lesson 12 saves `coarse_scan.csv`, `fine_scan.csv`, `replicas.csv`, and
`validation_summary.json` in its scratch directory. Seeds and calculation
settings are retained in the result records. Monte Carlo outputs can vary
slightly with version, library, and parallel reduction order.

The course pages, published site, and original source notebooks are unchanged.

## Executed draft results (21 September 2026)

Both notebooks executed from a fresh kernel with OpenMC 0.16.0 and the local
ENDF/B-VIII.0 data. Their plots and output tables are saved in the notebooks.
Lesson 11 took approximately 34 seconds; Lesson 12 took approximately
7 minutes on four threads. All code cells completed without an error.

The multiplying fixed-source scan covered H/U = 0.25–300 and refined 3–5
in increments of 0.5. The largest refined sampled value was at H/U = 3.5
(H2O/U = 1.75); the statistically unresolved broad optimum is around 3–4.
Five fresh, equal-size independent-seed runs at H/U = 3.5 gave:

| Calculation at H/U = 3.5 | Result |
|---|---:|
| Multiplying 1 MeV fixed source, mixture production/absorption | η_mix = 0.88016 ± 0.00042 |
| 1 MeV fixed source, fission descendants suppressed | η_mix = 0.81730 |
| Eigenvalue calculation | k∞ = 0.88954 ± 0.00164 |
| P/A using the eigenvalue spectrum | 0.88831 |
| Eigenvalue neutron-balance ratio P/(A − G_s) | 0.89003 |

The quoted ± values are estimated **one-standard-error** uncertainties, not
confidence limits on the optimum's location. The first uses covariance across
five independent replicas; the eigenvalue uncertainty is OpenMC's estimate.
The fixed-source reference at H/U = 5 gave A − P − G_s = 1.00528, consistent
with approximately one external neutron per history. The eigenvalue balance
agrees with the separately reported k within its sampling uncertainty.

Thus the requested “0.85 or so” is best presented as **roughly 0.88 for this
explicit model and source treatment**, not as an exact maximum of 0.85.
Suppressing fission descendants changes the weighting spectrum and the ratio;
conventional fuel-only η is a different denominator again.

Verification artifacts and standalone HTML review copies are in
`/home/robertsj/Classes/ne630/review/lesson11-12/`; the case files and CSV/JSON
results are under its `executed_runs/` directory. Nothing was published.
