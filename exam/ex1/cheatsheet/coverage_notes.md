# Instructor coverage notes

These notes are not part of the two-page student reference.

## Source basis

The working sources were the uploaded `chapter1.tex`, `chapter2.tex`,
`chapter3.tex`; `hw01.tex` through `hw13.tex`, including their solutions;
and the lesson-handout bodies for Lessons 1–10 and 12–14. The archive did
not contain a separate Lesson 11 handout. Its thermal-neutron material is
represented using HW11 and Chapter 3. The supplied `ne630boardhandout.cls`
provides the page geometry, color palette, typography conventions, and columns.

## Assessment-to-reference alignment

| Assessed work | Reference sections | Material retained |
|---|---|---|
| HW1; Lessons 1–2; Chapter 1 reaction/energy examples | 1, 8; constants | Reaction conservation, Q and binding energy, atomic-mass beta-minus convention, classical/relativistic kinetic energy, atom counting, mass-to-energy conversion, thermal/electric power, useful atomic masses. |
| HW2; Lesson 2 | 1–2 | Prompt versus delayed fission emissions, neutron-rich products, fissile/fertile distinctions, idealized generations, criticality classification, Wigner–Way decay heat and its time convention. |
| HW3; Lesson 3; Chapter 1 decay/production examples | 2, 8 | Half-life/activity/inventory conversion; decay with constant production; general chain balance and integrating-factor solution; unforced two-member chain; secular equilibrium; uranium isotope-ratio evolution and the assigned half-lives. |
| HW4–5; Lessons 4–5; Chapter 2 composition/cross-section example | 3 | Atom, mass, and volume fractions; compound stoichiometry; density-to-number-density conversion; macroscopic mixture cross sections; partial and conditional reaction probabilities; fission-rate-weighted multiplicity; exponential first flights, attenuation, and point-source geometry. |
| HW6; Lesson 6 | 4, 6–7 | Cross-section shapes and principal MT identifiers, single-level Breit–Wigner capture, resonance tails and Doppler trends, distribution normalization, the assigned Watt birth spectrum. |
| HW7–8; Lessons 7–8; Chapter 2 scattering material | 3, 5–6, 8–9 | Elastic energy/angle relations and their assumptions, support-limited probabilities, mixture collision weighting, expectations and Jacobians, logarithmic energy loss, collision-count estimate, moderator power/ratio, fuel reproduction. |
| HW9–10; Lessons 9–10; Chapter 3 slowing-down material | 6–7, 9 | Energy/lethargy transformation, scattering-only balance, 1/(Sigma_s E) versus 1/E flux, slowing-down density, NR/WR spectra and their assumptions, self-shielding and consistent normalization. |
| HW11; Chapter 3 thermal-spectrum material | 6, 9 | Maxwellian number density versus flux, mean speed and energy, energy associated with mean speed, bin-integrated flux versus spectral density, Maxwellian averaging of a 1/v cross section. |
| HW12; Lesson 12; Chapter 3 averaged-rate examples | 8–9 | Flux-weighted constants, resonance integrals and their group-width denominator, NR versus 1/E weights, selected course fuel data with their averaging conventions. |
| HW13; Lessons 13–14 | 9–11 | Reaction-rate-preserving collapse, group normalization, incident-to-outgoing elastic transfers, transfer-column conservation/cutoff loss, general multigroup balance, removal versus absorption, fission production, fixed-source versus eigenvalue equations, and one-/two-group scalar formulas. |

## Editorial choices and assumptions

**Reference rather than worked answers.** The sheet supplies reusable principles,
relations, and selected course data. It does not repeat completed homework
calculations, figures, numerical flux solutions, plotting instructions, or Python
/OpenMC application workflows. A general integrating-factor expression supports
both the constant-production daughter problem and more general decay chains
without reproducing every specialized solved case.

**Numerical inputs.** The atomic masses are retained to the digits supplied for
the HW1 reactions. The uranium half-lives are the assigned HW3 values, rather
than replacements drawn from an external evaluation. Moderator data come from
Chapter 3, Table 3.1. Fuel cross sections/integrals come from Table 3.2, with the
thermal multiplicities used in HW9 / the associated book problem. U-238 thermal
fission is shown as approximately zero, matching the simplified course treatment.
The data table distinguishes Maxwellian flux averages from cross sections at
0.0253 eV and distinguishes a resonance integral from a group-average cross
section. The course uses the intermediate interval 1–100,000 eV; the tabulated
resonance integrals are reference values used with that interval, not newly
processed data.

A particular exam composition, density, resonance-parameter set, or multigroup
coefficient table should accompany its problem. Copying every such homework
input would displace generally useful equations and would not supply data for a
new examination material. In particular, the sheet does not mix the rounded HW13
production coefficients with the more explicit Lesson 14 values.

**Model distinctions.** The sheet preserves the distinction between neutron
number-density and flux spectra; capture and absorption; removal and absorption;
source shape and flux shape; averaging a ratio and taking a ratio of averages;
and a fixed-source solution and an eigenvector normalization. In the scattering
kinematics section E is incident and E-prime outgoing, as in Lesson 7. The
slowing-down integral and group-transfer section explicitly relabel E-prime as
incident, as used in those course balances.

The stationary-target elastic kernel is not applied to thermal upscatter.
NR and WR are labeled approximations; the WR expression cancels same-energy
fuel scattering instead of counting it as removal. No universal claim is made
about which approximation must produce a deeper flux depression. Group-transfer
columns close only when outgoing energies are fully covered. Only fission is
scaled by 1/k. The simple two-group 1/(1-k) source multiplier is conditional on
its stated source, fission-spectrum, and no-upscatter assumptions.

**Scope of data and source dependence.** The sheet uses the supplied course
conventions, not a newly evaluated nuclear-data library. Special-purpose data
and code-dependent details remain the responsibility of the corresponding
problem statement. The coverage tags identify lessons; the eleven numbered
reference sections are organizational groupings, not a renumbering of lessons.
