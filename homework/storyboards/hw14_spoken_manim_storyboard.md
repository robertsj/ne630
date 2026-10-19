# Homework 14 Spoken Dialogue and Manim Storyboard

Draft version: 0.1

Source solution: `homework/solutions/hw14.tex`

Working title: **Homework 14: From Cross Sections to an Infinite-Medium Check**

## Production Aim

Turn the HW14 solution into a short engineering dialogue.  The goal is not to
read the solution aloud.  The goal is to show how a seasoned analyst turns a
messy physical statement into a sequence of modeling decisions:

1. choose an energy-group structure,
2. decide how to convert tabulated data into group constants,
3. choose a downscatter closure,
4. solve the graphite fixed-source balance,
5. add uranium and derive `k_infty(R)`,
6. use OpenMC as a consistency check rather than as a replacement for the
   analytic model.

Target runtime: 8 to 10 minutes for the full HW14 video.

Prototype runtime: 4 to 5 minutes using only Scenes S00-S05, covering
Problem 1.

## Voices

**Engineer**

- Calm, practical, decision-oriented.
- Explains why each approximation is being made.
- Uses phrases like "the engineering decision is..." and "this is the closure
  we are choosing."

**Reviewer**

- Skeptical but constructive.
- Forces the Engineer to state assumptions.
- Asks what would change if a modeling choice changed.

Optional third voice later: **Narrator**, used only for scene transitions or
caption-only summaries.  For the first draft, use two voices.

## Visual Grammar

Use a consistent Manim style throughout.

- Energy axis: horizontal log axis, high energy on the left, thermal on the
  right.
- Group colors:
  - Group 1: blue
  - Group 2: teal
  - Group 3: green
- Reaction colors:
  - source: yellow
  - absorption: red
  - scattering/downscatter: cyan
  - fission production: orange
  - OpenMC/benchmark check: purple
- Material colors:
  - graphite/carbon: dark gray
  - uranium: olive or muted green
- Keep equations large and sparse.  Do not show full tables unless the table is
  being transformed into the few coefficients that matter.

## Storyboard Overview

| Scene | Time | Purpose | Spoken Beat | Manim Beat |
|---|---:|---|---|---|
| S00 | 0:00-0:25 | Hook | "What are we actually solving?" | Graphite block, 1 MeV source, question mark. |
| S01 | 0:25-1:10 | Group structure | Use FNRP Table 3.2 as the model frame. | Log-energy axis splits into groups 1, 2, 3. |
| S02 | 1:10-1:55 | Balance equation | General balance, then no fission for graphite. | Terms in the balance equation light up and simplify. |
| S03 | 1:55-2:55 | Group constants | Cross sections are constructed, not simply copied. | Table cards collapse into group data. |
| S04 | 2:55-3:55 | Downscatter closure | Only `2 <- 1` and `3 <- 2` survive. | Energy ladder arrows, blocked upscatter and `1 -> 3`. |
| S05 | 3:55-5:05 | Graphite solve | Sequential solve and balance check. | Three-node flow network and flux bars. |
| S06 | 5:05-6:15 | Add uranium | Same model, changed material and fission source. | Uranium particles appear; `R = N_C/N_U` slider. |
| S07 | 6:15-7:35 | `k_infty(R)` | Normalize by `phi_1`; derive compact expression. | Equations morph into `x(R)`, `y(R)`, boxed `k_infty`. |
| S08 | 7:35-8:50 | OpenMC check | Simulation checks the model, not the reverse. | Infinite cell, reflective boundaries, result comparison. |
| S09 | 8:50-9:20 | Close | Name the transferable method. | Four-question checklist appears. |

## Scene Details

### S00 - Cold Open: What Are We Solving?

Approximate duration: 25 seconds

**Learning move**

Separate the physical problem from the computational method.  Students should
hear immediately that this is a modeling sequence, not a formula hunt.

**Dialogue**

Reviewer: "We have a very large graphite block, a 1 MeV neutron source, and a
table of nuclear data.  What are we actually solving?"

Engineer: "Not transport in full detail.  First we are building a three-group
engineering model: enough physics to estimate the spectrum, then enough
structure to test it with OpenMC."

Reviewer: "So the answer depends on the choices we make before the arithmetic."

Engineer: "Exactly.  HW14 is mostly about making those choices explicit."

**Manim choreography**

- Fade in title: `HW14: From Cross Sections to k_infty`.
- Show a large graphite block as a rectangle with subtle texture.
- Drop in a yellow source marker labeled `1 MeV source`.
- Add three floating labels:
  - `data`
  - `assumptions`
  - `group balance`
- Pull those labels into a single flow arrow labeled `model`.

**On-screen text**

`The solution is a sequence of modeling decisions.`

### S01 - Choose the Energy Groups

Approximate duration: 45 seconds

**Learning move**

Make the group structure concrete before any cross-section algebra appears.

**Dialogue**

Reviewer: "Why three groups?"

Engineer: "Because the data in FNRP Table 3.2 already suggests a coarse
structure: fast, intermediate, and thermal.  We use that structure instead of
pretending we know the detailed energy dependence."

Reviewer: "And the 1 MeV source?"

Engineer: "It enters group 1.  So `S_1 = s_0`, while `S_2` and `S_3` start at
zero."

**Manim choreography**

- Draw a horizontal log-energy axis.
- Mark:
  - `10^6 eV`
  - `10^5 eV`
  - `1 eV`
  - `thermal`
- Shade regions:
  - `g = 1: 10^5 < E <= 10^6 eV`
  - `g = 2: 1 < E <= 10^5 eV`
  - `g = 3: E <= 1 eV`
- Animate a yellow source arrow landing in group 1.
- Show:
  ```tex
  S_1=s_0,\qquad S_2=S_3=0
  ```

**Manim notes**

Use one reusable energy-axis object for the whole video.  It should be
possible to dim or highlight groups without rebuilding the axis in later
scenes.

### S02 - Write the Group Balance, Then Simplify

Approximate duration: 45 seconds

**Learning move**

Show the general balance once, then strip it down for Problem 1.

**Dialogue**

Engineer: "The model starts with a group balance.  Removal from a group is
balanced by source, scattering into the group, and possibly fission."

Reviewer: "Possibly?"

Engineer: "For pure graphite, there is no fission source.  That term is kept in
the framework because we will need it later, but for Problem 1 it vanishes."

Reviewer: "So the same equation carries all three problems, but different terms
are active."

Engineer: "That is the point."

**Manim choreography**

- Show the full balance:
  ```tex
  \Sigma_{r,g}\phi_g
  = S_g
  + \sum_{h\ne g}\Sigma_{s,g\leftarrow h}\phi_h
  + \frac{\chi_g}{k_\infty}s_f'''
  ```
- Highlight terms:
  - left side: `removal`
  - `S_g`: external source
  - scattering sum: in-scatter
  - fission term: inactive for Problem 1
- Cross out or fade the fission term for graphite.
- Replace `\Sigma_{r,g}` with:
  ```tex
  \Sigma_{r,g}=\Sigma_{a,g}+\sum_{h\ne g}\Sigma_{s,h\leftarrow g}
  ```

**On-screen text**

`Problem 1: graphite only -> no fission source`

### S03 - Build the Group Constants

Approximate duration: 60 seconds

**Learning move**

Show that the group constants are constructed from assumptions about weighting.

**Dialogue**

Reviewer: "Can we just copy the numbers from the table?"

Engineer: "For thermal and fast averages, mostly yes, if we respect what the
table means.  But the intermediate group is built from resonance integrals, so
we divide by the lethargy width."

Reviewer: "That is the `ln(10^5)` factor?"

Engineer: "Right.  The group-2 average is an integral quantity converted into a
group average."

**Manim choreography**

- Show three small data cards:
  - thermal average
  - resonance integral
  - fission-spectrum fast average
- Animate the group-2 formula:
  ```tex
  \bar{\sigma}_{x,2}
  = \frac{I_x}{\int_1^{10^5}dE/E}
  = \frac{I_x}{\ln(10^5)}
  ```
- Table cards collapse into a compact list:
  ```tex
  \sigma_{a,g}^{(i)},\quad
  \sigma_{f,g}^{(i)},\quad
  \sigma_{s,g}^{(i)}
  ```
- Show the microscopic-to-macroscopic conversion:
  ```tex
  \Sigma_{x,g}=\sum_i N^{(i)}\sigma_{x,g}^{(i)}10^{-24}
  ```

**Implementation notes**

Avoid rendering the full cross-section table from the solution.  Use a short
animated table with one row each for carbon, U-235, and U-238, then collapse
the table into the symbols needed downstream.

### S04 - Decide the Scattering Transfer Model

Approximate duration: 60 seconds

**Learning move**

Make the downscatter approximation visible and defendable.

**Dialogue**

Reviewer: "The table gives scattering, but not exactly the group-to-group
transfer we need.  Where does that come from?"

Engineer: "We choose an elastic downscatter closure.  A collision changes the
neutron energy within a range set by the mass of the nucleus.  In this model,
upscatter is neglected, and one collision does not jump directly from group 1
to group 3."

Reviewer: "So only two transfer paths remain."

Engineer: "`2 <- 1` and `3 <- 2`.  That is the structural assumption that turns
the system into a sequential solve."

**Manim choreography**

- Show energy ladder with three boxes: `g1`, `g2`, `g3`.
- Draw cyan arrows:
  - `g1 -> g2`
  - `g2 -> g3`
- Briefly draw faded rejected arrows:
  - `g2 -> g1` labeled `upscatter neglected`
  - `g1 -> g3` labeled `not one collision`
- Show:
  ```tex
  \alpha^{(i)}=\left(\frac{A^{(i)}-1}{A^{(i)}+1}\right)^2
  ```
  then:
  ```tex
  \sigma_{s,g+1\leftarrow g}^{(i)}
  \simeq \sigma_{s,g}^{(i)}\frac{\xi^{(i)}}{\Delta u_g}
  ```

**On-screen text**

`Closure: elastic downscatter with 1/E weighting inside each slowing-down group`

### S05 - Solve the Pure Graphite Balance

Approximate duration: 70 seconds

**Learning move**

Show why the fixed-source equations are sequential and how the flux shape
emerges.

**Dialogue**

Engineer: "For pure graphite, all macroscopic coefficients come from carbon.
Once those are assembled, the balance equations solve from high energy to low
energy."

Reviewer: "Because the source starts in group 1 and scattering only moves
downward."

Engineer: "Exactly.  Group 1 gets the source.  Group 2 gets what scatters from
group 1.  Group 3 gets what scatters from group 2."

Reviewer: "And the large thermal flux is not magic; it is the consequence of
slow absorption in the moderator."

Engineer: "Yes.  The final balance check is that all absorption adds back up to
the original source."

**Manim choreography**

- Show a three-node directed graph:
  - node `1`: source `s_0`, absorption sink
  - node `2`: downscatter input, absorption sink
  - node `3`: downscatter input, absorption sink
- Display the reduced balances:
  ```tex
  (\Sigma_{a,1}+\Sigma_{s,2\leftarrow1})\phi_1=s_0
  ```
  ```tex
  (\Sigma_{a,2}+\Sigma_{s,3\leftarrow2})\phi_2
  =\Sigma_{s,2\leftarrow1}\phi_1
  ```
  ```tex
  \Sigma_{a,3}\phi_3=\Sigma_{s,3\leftarrow2}\phi_2
  ```
- Solve them in sequence and reveal:
  ```tex
  \phi_1=54.1144s_0,\quad
  \phi_2=132.488s_0,\quad
  \phi_3=2910.95s_0
  ```
- Animate bars for `phi_1`, `phi_2`, `phi_3`, with group 3 largest.
- Close with:
  ```tex
  \Sigma_{a,1}\phi_1+\Sigma_{a,2}\phi_2+\Sigma_{a,3}\phi_3=s_0
  ```

**Prototype endpoint**

This is the natural endpoint for a first 4 to 5 minute prototype.  End with
the balance check and a title card:

`Next: same model, new material, fission feedback.`

### S06 - Add Uranium Without Rebuilding the Model

Approximate duration: 70 seconds

**Learning move**

Show that Problem 2 reuses the same machinery but changes the material and
turns on fission.

**Dialogue**

Reviewer: "Now uranium is dispersed in the graphite.  Do we start over?"

Engineer: "No.  We keep the group structure and transfer model.  The material
composition changes, and fission production becomes active."

Reviewer: "The control variable is the carbon-to-uranium atom ratio?"

Engineer: "Yes.  `R = N_C/N_U`.  Once `R` is specified, the uranium atom density
and enrichment split are fixed."

**Manim choreography**

- Start from the graphite block.
- Add sparse green uranium dots.
- Introduce a slider labeled `R = N_C/N_U`.
- Show:
  ```tex
  N_U=\frac{N_C}{R},\qquad
  N^{(235)}=0.02\frac{N_C}{R},\qquad
  N^{(238)}=0.98\frac{N_C}{R}
  ```
- Transform microscopic uranium data into enrichment-averaged coefficients:
  ```tex
  u_{x,g}=0.02\sigma_{x,g}^{(235)}
  +0.98\sigma_{x,g}^{(238)}
  ```
- Add orange fission loop arrows to the group network.

**On-screen text**

`Same model. New material. Fission source active.`

### S07 - Derive the Compact `k_infty(R)` Expression

Approximate duration: 80 seconds

**Learning move**

Avoid drowning students in algebra.  Show the normalization trick and the
interpretation of the final expression.

**Dialogue**

Engineer: "For an infinite multiplying medium, the external source disappears.
The source is now fission production divided by `k_infty`."

Reviewer: "That sounds like an eigenvalue problem."

Engineer: "It is.  But because the transfer model is still one-way in energy,
we can normalize by `phi_1` and express the lower groups as ratios."

Reviewer: "`x(R)` and `y(R)` are the spectral shape relative to group 1."

Engineer: "Then `k_infty` is fission production divided by absorption, weighted
by that shape."

**Manim choreography**

- Show source-free balances with fission source:
  ```tex
  (\Sigma_{a,1}+\Sigma_{s,2\leftarrow1})\phi_1
  =\frac{s_f'''}{k_\infty}
  ```
- Define:
  ```tex
  x(R)=\frac{\phi_2}{\phi_1},\qquad
  y(R)=\frac{\phi_3}{\phi_1}
  ```
- Animate the ratio expressions:
  ```tex
  x(R)=
  \frac{\Sigma_{s,2\leftarrow1}(R)}
  {\Sigma_{a,2}(R)+\Sigma_{s,3\leftarrow2}(R)}
  ```
  ```tex
  y(R)=
  \frac{\Sigma_{s,3\leftarrow2}(R)x(R)}
  {\Sigma_{a,3}(R)}
  ```
- Collapse numerator and denominator into the boxed result:
  ```tex
  k_\infty(R)=
  \frac{\nu\Sigma_{f,1}
  +\nu\Sigma_{f,2}x
  +\nu\Sigma_{f,3}y}
  {\Sigma_{a,1}+\Sigma_{a,2}x+\Sigma_{a,3}y}
  ```
- Use color coding:
  - orange numerator: production
  - red denominator: absorption

**On-screen text**

`k_infty = production / loss for the assumed spectrum`

### S08 - Translate to OpenMC for `R = 1000`

Approximate duration: 75 seconds

**Learning move**

Frame OpenMC as an independent continuous-energy check of the assumptions.

**Dialogue**

Reviewer: "Problem 3 asks for OpenMC.  Is that replacing the three-group
model?"

Engineer: "No.  It checks the model.  For `R = 1000`, we translate the atom
densities into one infinite homogeneous material, use reflective or periodic
boundaries, and run a `k`-eigenvalue calculation."

Reviewer: "So the OpenMC answer should be compared to the analytic result, but
not forced to match it."

Engineer: "Correct.  The three-group model gives a consistency check:
`k_infty` is about `1.04793` for `nu = 2.43` under the same closure."

**Manim choreography**

- Show a square cell with reflective boundary indicators.
- Fill it with graphite and sparse uranium dots.
- Show density cards:
  ```tex
  N_C=1.13416984\times10^{23}\ \mathrm{cm^{-3}}
  ```
  ```tex
  N_U=1.13416984\times10^{20}\ \mathrm{cm^{-3}}
  ```
- Animate an OpenMC workflow:
  `material -> cell -> settings -> k estimate`
- Show comparison board:
  ```text
  Three-group check: k_infty = 1.04793
  OpenMC result: mean +/- uncertainty
  ```

**Implementation notes**

Do not invent a numerical OpenMC result unless an actual OpenMC run is added
later.  Use a placeholder result card or show the analytic check only.

### S09 - Closing: Transferable Questions

Approximate duration: 30 seconds

**Learning move**

Leave students with a reusable analysis checklist.

**Dialogue**

Reviewer: "So what should a student remember from HW14?"

Engineer: "Not just the number.  Remember the questions: What group structure
am I using?  How did I average the data?  What transfer paths did I allow?
And what does the simulation check?"

Reviewer: "That is the difference between calculating and modeling."

Engineer: "Exactly."

**Manim choreography**

- Fade out equations.
- Show checklist:
  1. `What groups define the model?`
  2. `How are cross sections averaged?`
  3. `Which transfers are allowed?`
  4. `What does OpenMC check?`
- End on:
  `HW14: state the assumptions before trusting the number.`

## Suggested Manim File Structure

Initial implementation can be one file:

```text
homework/videos/hw14_manim/hw14_story.py
```

Suggested classes:

```python
class HW14Intro(Scene): ...
class EnergyGroups(Scene): ...
class GroupBalance(Scene): ...
class CrossSectionData(Scene): ...
class DownscatterClosure(Scene): ...
class GraphiteSolve(Scene): ...
class UraniumEigenvalue(Scene): ...
class OpenMCCheck(Scene): ...
```

Reusable helper objects:

- `make_energy_axis()`
- `make_group_boxes()`
- `make_three_group_network(fission=False)`
- `reaction_arrow(kind="scatter"|"absorb"|"fission"|"source")`
- `equation_card(tex, title=None, color=None)`
- `density_card(label, value)`

## Audio and Caption Notes

- Record Engineer and Reviewer separately, even if generated text-to-speech is
  used.  This makes pacing and revisions easier.
- Use captions matching the spoken dialogue, but keep equations as on-screen
  math rather than caption text.
- Avoid long spoken strings of symbols.  Say "group-one absorption" while the
  visual shows `\Sigma_{a,1}`.
- Use short pauses before and after each modeling decision.  The pauses matter
  more than extra explanation.

## First Production Pass

Recommended first pass: build only S00-S05.

Deliverable:

- 4 to 5 minute Problem 1 prototype.
- Two voices.
- Energy-axis visual grammar finalized.
- Three-node balance network finalized.
- No OpenMC scene yet.

Why start here:

- Problem 1 establishes almost every visual primitive needed for Problems 2
  and 3.
- It tests whether the dialogue style is useful before building the longer
  eigenvalue and OpenMC sections.
- It keeps the first production review small enough to revise quickly.

## Open Questions for Jeremy

These can wait until after a prototype storyboard read-through.

1. Should the voices feel like "instructor and student" or "engineer and
   reviewer"?
2. Should the video include derivation pauses where students are invited to
   stop and solve one step?
3. Should the OpenMC segment show actual code snippets, or only the modeling
   translation?
4. Should the tone be solution-review focused, or should it be reusable as a
   lesson on multigroup modeling?

