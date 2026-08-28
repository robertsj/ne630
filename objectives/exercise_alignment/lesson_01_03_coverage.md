# Lesson 01-03 Exercise Coverage

This is a compact review view of `lesson_01_03_exercise_edges.psv`.  The edge
table is the source of truth; this file is just an index for scanning.

## Lesson 01

| Objective | Lewis | DHNRA | Lamarsh |
|---|---|---|---|
| L01.MACRO | 1.3 | 2.1 | 1.11, 2.29 |
| L01.M01 energy densities | 1.6 | - | 3.11, 3.12 |
| L01.M02 relativistic energy | 1.5 | - | 1.6 |
| L01.M03 nuclide notation | 1.1, 1.2, 1.3, 1.4, 1.7 | 2.1 | 1.11 |
| L01.M04 binary reactions | 1.3, 1.4, 1.12 | 2.1 | 1.11, 1.15, 2.13, 2.15, 2.16, 2.29 |
| L01.M05 Q values | - | - | 1.11, 2.10, 2.13, 2.15, 2.16, 2.29, 3.2 |
| L01.M06 radioactive decay examples | 1.2, 1.3, 1.7, 1.12, 1.19 | 2.2, 2.8, 2.19 | 1.13, 1.15, 1.17, 2.7 |
| L01.M07 classical neutron kinematics | 1.5 | - | 1.6 |
| L01.M08 mass defect | 1.6 | - | 1.9, 1.10, 1.11, 2.29 |
| L01.M09 binding energy per nucleon | - | - | 1.10 |
| L01.M10 Q values and decay | 1.19 | - | 1.11, 2.29, 3.2 |

## Lesson 02

| Objective | Lewis | DHNRA | Lamarsh |
|---|---|---|---|
| L02.MACRO | 1.9, 5.4 | 2.20, 3.9 | 3.11, 12.1, 12.2, 12.18 |
| L02.M01 fission reaction Q | - | - | 3.2 |
| L02.M02 forms of nuclear power | - | 3.7 | - |
| L02.M03 fission emitted particles | 2.5 | 2.19 | 3.7, 3.8, 3.10 |
| L02.M04 multiplication model | 5.3, 5.4, 5.5 | 3.1, 3.2, 3.9 | 12.7, 12.13, 12.18 |
| L02.M05 critical/subcritical/supercritical | 5.3, 5.17 | 3.3, 3.8, 3.9, 15.11 | 12.4, 12.5, 12.12, 12.18 |
| L02.M06 spent-fuel heat | 1.9 | 15.1, 15.21 | 3.4, 3.5, 3.6 |
| L02.M07 fissile versus fertile | 1.7, 10.13, 10.14 | 3.4, 7.13, 15.14, 15.15, 15.18, 15.19, 15.22 | 4.4, 4.5, 13.28, 13.34 |
| L02.M08 major fissile/fertile nuclides | 10.14 | 15.18, 15.19, 15.22 | 13.28 |
| L02.M09 neutron-rich fission products | - | 2.19 | - |
| L02.M10 Z-A stability trend | - | 2.19 | - |

Note: L02.M02 has a weak proxy match rather than an exact "list three forms"
exercise.  DHNRA 3.7 compares several plant types, including LWR, HTGR, LMFBR,
and fusion, but it does not include the nuclear-battery thread from the NE 630
lesson page.

## Lesson 03

| Objective | Lewis | DHNRA | Lamarsh |
|---|---|---|---|
| L03.MACRO | 1.10, 1.20 | 2.3, 2.4 | 1.17, 13.28 |
| L03.M01 half-life to lambda/mean life | 1.10, 1.11, 1.14, 1.16, 1.17, 1.18, 1.19 | 2.2, 2.3, 2.8, 2.21 | 1.13, 1.15, 1.17, 2.7, 12.7 |
| L03.M02 pure decay ODE | 1.11, 1.14, 1.16, 1.18, 1.19 | 2.2, 2.8, 2.21 | 1.13, 1.15, 2.7 |
| L03.M03 production plus decay ODE | 1.13, 1.14, 1.16, 1.17, 1.20, 10.12 | 2.4, 14.9, 15.4, 15.8 | 1.14, 1.15, 1.16, 2.1, 2.3, 13.20, 13.23, 13.33 |
| L03.M04 activity/mass/number conversions | 1.12, 1.13, 1.15, 1.17, 1.19 | 2.20, 2.21 | 1.1, 1.2, 1.3, 1.4, 1.5, 1.13, 1.15, 2.1, 2.3, 3.11 |
| L03.M05 saturation activity | 1.10, 1.13, 1.14, 1.16, 1.17 | 2.4, 15.3, 15.4 | 1.13, 1.15, 1.16, 1.17, 2.1, 13.11, 13.12, 13.14, 13.20, 13.22 |
| L03.M06 chain systems | 1.10, 1.17, 1.20, 10.1, 10.10, 10.11, 10.12, 10.13, 10.14 | 2.3, 2.4, 6.14, 15.2, 15.5, 15.6, 15.7, 15.10, 15.13, 15.15, 15.16, 15.17, 15.19, 15.22 | 1.17, 12.3, 12.10, 12.16, 13.13, 13.14, 13.15, 13.16, 13.17, 13.18, 13.19, 13.28, 13.31, 13.33, 13.35 |
| L03.M07 secular equilibrium | 1.10, 1.17, 1.20 | 2.3, 15.3, 15.9, 15.16 | 1.17, 13.11, 13.12, 13.20, 13.21, 13.22 |

## Orthogonal Tagging

Orthogonal objectives are stored in `lesson_01_03_catalog.yml` and attached to
individual rows in the edge table.  The most common tags in this seed pass are:

- `ORTHO_FISSION_PRODUCT_POISONS`
- `ORTHO_FUEL_CYCLE_BURNUP`
- `ORTHO_REACTIVITY_CONTROL`
- `ORTHO_CROSS_SECTIONS_REACTION_RATES`
- `ORTHO_UNIT_CONVERSIONS`
- `ORTHO_DELAYED_NEUTRON_KINETICS`
- `ORTHO_REACTOR_POWER_CONVERSION`

These should be treated as reusable latent objectives, not final course
objectives.
