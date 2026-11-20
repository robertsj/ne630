#!/usr/bin/env python
"""Recompute every number quoted in the Chapter 1-7 and 10 programmed reading guides.

Run from anywhere:
    python tools/verify_examples.py            # print the table of values
    python tools/verify_examples.py --write    # also refresh figures/data/*.dat

Only NumPy and SciPy are required.  Each printed line is labelled with the guide
(ch01-ch07 or ch10; the Chapter 4 addendum uses ch04 F28 onward) and the frame that quotes it, so a reader can check a single value.
"""
import argparse
import math
import os
import sys

import numpy as np
from scipy import integrate, optimize, special

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "figures", "data")

rows = []


def rec(guide, frame, label, value, fmt="{:.4g}", unit=""):
    if isinstance(value, (list, tuple, np.ndarray)):
        text = ", ".join(fmt.format(v) for v in value)
    else:
        text = fmt.format(value)
    rows.append((guide, frame, label, text, unit))
    return value


# ----------------------------------------------------------------------------
# Shared working sets
# ----------------------------------------------------------------------------
# Toy slab set used by Lessons 33-35 and throughout both guides.
D_toy, Sa_toy, kinf_toy = 1.0, 0.10, 1.5
L2_toy = D_toy / Sa_toy
L_toy = math.sqrt(L2_toy)
# Graphite (FNRP problem 6.3) and light water (FNRP Table 7.1 L2, D = 0.16 cm).
D_gr, Sa_gr = 0.84, 2.1e-4
L_gr = math.sqrt(D_gr / Sa_gr)
D_w, L_w = 0.16, 2.85
Sa_w = D_w / L_w**2

# ----------------------------------------------------------------------------
# Chapter 6
# ----------------------------------------------------------------------------
# F5: isotropic partial current: int_0^1 mu dmu * 2pi /(4pi) = 1/4
rec("ch06", "F5", "J+ for isotropic psi, in units of phi", 2 * math.pi * 0.5 / (4 * math.pi), "{:.4f}")

# F9: dot products
rec("ch06", "F9", "(3,4).(0.6,0.8)", 3 * 0.6 + 4 * 0.8, "{:.2f}")
rec("ch06", "F9", "(3,4).(0.8,-0.6)", 3 * 0.8 - 4 * 0.6, "{:.2f}")
rec("ch06", "F9", "(3,4).(-0.6,-0.8)", -3 * 0.6 - 4 * 0.8, "{:.2f}")

# F16: diffusion coefficient from Sigma_tr (illustrative numbers)
A = 12.0
mubar = 2.0 / (3.0 * A)
St, Ss = 0.40, 0.3998
Str = St - mubar * Ss
rec("ch06", "F16", "mubar for A=12", mubar, "{:.4f}")
rec("ch06", "F16", "Sigma_tr = Sigma_t - mubar Sigma_s", Str, "{:.4f}", "1/cm")
rec("ch06", "F16", "D = 1/(3 Sigma_tr)", 1 / (3 * Str), "{:.3f}", "cm")
rec("ch06", "F16", "D if isotropic (1/(3 Sigma_t))", 1 / (3 * St), "{:.3f}", "cm")

# F17-F18: cosine flux in a slab |x|<=a/2 with the toy set, a = 10 cm, no fission
a17 = 10.0
B17 = math.pi / a17
DB2 = D_toy * B17**2
rec("ch06", "F17", "D (pi/a)^2 for a=10, D=1", DB2, "{:.4f}", "1/cm")
rec("ch06", "F17", "s'''/phi = D B^2 + Sigma_a", DB2 + Sa_toy, "{:.4f}", "1/cm")
rec("ch06", "F17", "leakage share D B^2/(D B^2+Sigma_a)", DB2 / (DB2 + Sa_toy), "{:.3f}")
int_cos = 2 * a17 / math.pi  # integral of cos(pi x/a) over |x|<a/2
rec("ch06", "F18", "int cos = 2a/pi (a=10)", int_cos, "{:.4f}", "cm")
S_tot = (DB2 + Sa_toy) * int_cos
A_tot = Sa_toy * int_cos
Lk_tot = 2 * D_toy * B17  # 2 J(a/2) with phi0 = 1
rec("ch06", "F18", "total source per phi0 (per cm^2)", S_tot, "{:.4f}")
rec("ch06", "F18", "total absorption per phi0", A_tot, "{:.4f}")
rec("ch06", "F18", "total leakage 2J(a/2) per phi0", Lk_tot, "{:.4f}")
rec("ch06", "F18", "absorption + leakage", A_tot + Lk_tot, "{:.4f}")

# F20: diffusion lengths
rec("ch06", "F20", "L toy (D=1, Sa=0.1)", L_toy, "{:.3f}", "cm")
rec("ch06", "F20", "L graphite (0.84, 2.1e-4)", L_gr, "{:.2f}", "cm")
rec("ch06", "F20", "Sigma_a water from D=0.16, L=2.85", Sa_w, "{:.4f}", "1/cm")

# F23-F24: half space
rec("ch06", "F23", "J(0)/phi0 = D/L toy", D_toy / L_toy, "{:.4f}")
rec("ch06", "F23", "Sigma_a L toy (must equal D/L)", Sa_toy * L_toy, "{:.4f}")
rec("ch06", "F24", "fraction absorbed within L, 2L, 3L (slab)", [1 - math.exp(-n) for n in (1, 2, 3)], "{:.3f}")

# F25-F26: uniform source slab |x|<=a, zero flux at +-a
for ratio in (1, 2, 5):
    rec("ch06", "F25", f"phi(0)/phi_p for a/L={ratio}", 1 - 1 / math.cosh(ratio), "{:.3f}")
    rec("ch06", "F26", f"leakage fraction (L/a)tanh(a/L), a/L={ratio}", math.tanh(ratio) / ratio, "{:.3f}")

# F28-F29: extrapolation distance and the toy slab revisited
rec("ch06", "F28", "d = 2D toy, graphite", [2 * D_toy, 2 * D_gr], "{:.2f}", "cm")
rec("ch06", "F28", "0.7104*3D toy", 0.7104 * 3 * D_toy, "{:.3f}", "cm")
a29 = 10.0
for a_eff, name in ((a29, "a=10"), (a29 + 2 * D_toy, "a~=12")):
    rec("ch06", "F29", f"phi(0)/phi_p uniform-source slab, {name}, L={L_toy:.3f}", 1 - 1 / math.cosh(a_eff / L_toy), "{:.3f}")

# F31-F32: albedo
for name, D, L in (("graphite", D_gr, L_gr), ("water", D_w, L_w), ("toy", D_toy, L_toy)):
    x = 2 * D / L
    alb = (1 - x) / (1 + x)
    rec("ch06", "F31", f"2D/L {name}", x, "{:.4f}")
    rec("ch06", "F31", f"albedo {name}", alb, "{:.3f}")
    rec("ch06", "F32", f"phi(0)/s'' = (1/4 + D/2L)^-1 {name}", 1 / (0.25 + D / (2 * L)), "{:.3f}")
    rec("ch06", "F32", f"2(1+alpha) {name}", 2 * (1 + alb), "{:.3f}")

# F33: current continuity with D1=1, D2=2
rec("ch06", "F33", "phi'_2 given phi'_1=-0.1, D1=1, D2=2", -0.1 * 1 / 2, "{:.3f}")

# F39: fraction absorbed within R for point source
for n in (1, 2, 3):
    rec("ch06", "F39", f"point-source fraction absorbed within R={n}L", 1 - math.exp(-n) * (1 + n), "{:.3f}")

# F40: two-region sphere constant C for identical media, R/L=2
x = 2.0
C = 1 / (1 + (x / math.tanh(x) - 1) / (x + 1))
rec("ch06", "F40", "C for D^=D, L^=L, R/L=2", C, "{:.3f}")
rec("ch06", "F40", "phi(R)/(s/Sa) = 1-C", 1 - C, "{:.3f}")

# F42-F44: validity
for c in (0.99, 0.9, 0.7):
    rec("ch06", "F42", f"L/lambda for c={c}", 1 / math.sqrt(3 * (1 - c)), "{:.2f}")
rec("ch06", "F43", "rms distance sqrt(6) L graphite, water", [math.sqrt(6) * L_gr, math.sqrt(6) * L_w], "{:.1f}", "cm")
St_gr = 1 / (3 * D_gr)
c_gr = 1 - Sa_gr / St_gr
alpha_gr = 1 / math.sqrt(3 * (1 - c_gr)) - 1
lam_gr = 3 * D_gr
rec("ch06", "F44", "graphite c (isotropic assumption)", c_gr, "{:.5f}")
rec("ch06", "F44", "graphite lambda=3D", lam_gr, "{:.2f}", "cm")
rec("ch06", "F44", "sqrt((1-c)/3)", math.sqrt((1 - c_gr) / 3), "{:.4f}")
rec("ch06", "F44", "alpha = [3(1-c)]^-1/2 - 1", alpha_gr, "{:.1f}")
for rL in (lam_gr / L_gr, 0.1, 0.5, 1.0):
    ratio = math.sqrt((1 - c_gr) / 3) / rL * math.exp(-alpha_gr * rL)
    rec("ch06", "F44", f"phi_u/phi at r/L={rL:.4f}", ratio, "{:.3g}")

# F45-F49: multiplying sphere, toy set
for k in (0.9,):
    rec("ch06", "F45", f"phi_p/(s/Sa)=1/(1-kinf) kinf={k}", 1 / (1 - k), "{:.2f}")
kappa = math.sqrt((1 - 0.9) / L2_toy)
Bm = math.sqrt((kinf_toy - 1) / L2_toy)
rec("ch06", "F46", "kappa for kinf=0.9", kappa, "{:.4f}", "1/cm")
rec("ch06", "F46", "B_m for kinf=1.5", Bm, "{:.4f}", "1/cm")
R47 = 20.0
kR = kappa * R47
rec("ch06", "F47", "kappa R for R=20", kR, "{:.3f}")
rec("ch06", "F47", "phi(0)/phi_p = 1 - kR/sinh(kR)", 1 - kR / math.sinh(kR), "{:.3f}")
rec("ch06", "F47", "phi(0)/(s/Sa)", (1 - kR / math.sinh(kR)) / (1 - 0.9), "{:.2f}")
R48 = 10.0
BR = Bm * R48
rec("ch06", "F48", "B R for R=10", BR, "{:.3f}")
rec("ch06", "F48", "phi(0)/phi_p = BR/sin(BR) - 1", BR / math.sin(BR) - 1, "{:.3f}")
rec("ch06", "F48", "phi(0)/(s/Sa)", (BR / math.sin(BR) - 1) / (kinf_toy - 1), "{:.2f}")
Rcrit = math.pi / Bm
rec("ch06", "F49", "critical radius pi/B_m toy", Rcrit, "{:.2f}", "cm")
rec("ch06", "F49", "P_NL at critical = 1/kinf", 1 / kinf_toy, "{:.3f}")
for R in (10.0, 20.0):
    k = kinf_toy / (1 + L2_toy * (math.pi / R) ** 2)
    rec("ch06", "F49", f"k for sphere R~={R:.0f}", k, "{:.3f}")

# ----------------------------------------------------------------------------
# Chapter 7
# ----------------------------------------------------------------------------
# F4-F5: slab k with toy set
for a in (14.05, 20.0, 10.0):
    k = kinf_toy / (1 + L2_toy * (math.pi / a) ** 2)
    rec("ch07", "F4", f"slab k for a={a}", k, "{:.3f}")
rec("ch07", "F5", "kinf for critical slab a=20", 1 + L2_toy * (math.pi / 20) ** 2, "{:.3f}")

# F8: Bessel values
j01 = special.jn_zeros(0, 1)[0]
rec("ch07", "F8", "first zero of J0", j01, "{:.4f}")
rec("ch07", "F8", "J0(2.405/2)", special.j0(j01 / 2), "{:.3f}")
xs = 1.2025
series = 1 - xs**2 / 4 + xs**4 / 64 - xs**6 / 2304
rec("ch07", "F8", "J0 series to x^6 at 1.2025", series, "{:.4f}")
rec("ch07", "F8", "J1(2.405)", special.j1(j01), "{:.3f}")

# F9-F10: PWR-size core
Rt, Ht = 150.0, 360.0
Br2 = (j01 / Rt) ** 2
Bz2 = (math.pi / Ht) ** 2
B2 = Br2 + Bz2
rec("ch07", "F9", "B_r^2 (R~=150)", Br2, "{:.4e}", "1/cm^2")
rec("ch07", "F9", "B_z^2 (H~=360)", Bz2, "{:.4e}", "1/cm^2")
rec("ch07", "F9", "B^2", B2, "{:.4e}", "1/cm^2")
rec("ch07", "F9", "radial share of B^2", Br2 / B2, "{:.3f}")
M_pwr = 7.62
M2 = M_pwr**2
rec("ch07", "F10", "M^2 B^2", M2 * B2, "{:.5f}")
PNL = 1 / (1 + M2 * B2)
rec("ch07", "F10", "P_NL", PNL, "{:.4f}")
kinf_crit = 1 / PNL
rec("ch07", "F10", "kinf for k=1", kinf_crit, "{:.4f}")
k105 = 1.05 * PNL
rec("ch07", "F10", "k for kinf=1.05", k105, "{:.4f}")
rec("ch07", "F10", "rho for kinf=1.05", (k105 - 1) / k105, "{:.4f}")

# F11-F12: power normalization
peak_r = j01 / (2 * special.j1(j01))
peak_z = math.pi / 2
rec("ch07", "F11", "radial peak/avg 2.405/(2 J1)", peak_r, "{:.3f}")
rec("ch07", "F11", "axial peak/avg pi/2", peak_z, "{:.3f}")
rec("ch07", "F11", "total peak/avg", peak_r * peak_z, "{:.3f}")
P = 3000e6
V = math.pi * Rt**2 * Ht
rec("ch07", "F12", "V = pi R^2 H", V, "{:.3e}", "cm^3")
Pavg = P / V
rec("ch07", "F12", "average power density", Pavg, "{:.1f}", "W/cm^3")
rec("ch07", "F12", "peak power density", Pavg * peak_r * peak_z, "{:.0f}", "W/cm^3")
gamma, Sf = 3.1e-11, 0.0100
rec("ch07", "F12", "average flux P'''/(gamma Sigma_f)", Pavg / (gamma * Sf), "{:.3e}", "1/cm^2-s")
rec("ch07", "F12", "peak flux", Pavg * peak_r * peak_z / (gamma * Sf), "{:.3e}", "1/cm^2-s")

# F13: H=D buckling coefficient and optimum
rec("ch07", "F13", "2.405^2 + (pi/2)^2", j01**2 + (math.pi / 2) ** 2, "{:.3f}")
rec("ch07", "F13", "4*(2.405^2) + pi^2  (=33.0)", 4 * j01**2 + math.pi**2, "{:.2f}")


def vol_hd(hd):
    # cylinder with H = hd * D, fixed buckling B^2 = 1 -> minimize volume
    # B^2 = (j01/R)^2 + (pi/H)^2, H = 2 hd R  => B^2 = [j01^2 + (pi/(2hd))^2]/R^2
    R = math.sqrt(j01**2 + (math.pi / (2 * hd)) ** 2)  # for B = 1
    H = 2 * hd * R
    return math.pi * R**2 * H


opt = optimize.minimize_scalar(vol_hd, bounds=(0.3, 3), method="bounded")
rec("ch07", "F13", "H/D minimizing critical volume", opt.x, "{:.3f}")
rec("ch07", "F13", "H/R at optimum", 2 * opt.x, "{:.3f}")

# F15: collisions to thermalize in water
n_w = math.log(2.0e6 / 0.0253) / 0.92
rec("ch07", "F15", "ln(E1/E2)", math.log(2.0e6 / 0.0253), "{:.2f}")
rec("ch07", "F15", "n for water (xi=0.92)", n_w, "{:.1f}")

# F16-F17: two-group vs migration area
L1, L2 = 7.36, 1.96
f1, f2 = 1 + L1**2 * B2, 1 + L2**2 * B2
rec("ch07", "F16", "1+L1^2 B^2, 1+L2^2 B^2", [f1, f2], "{:.5f}")
rec("ch07", "F16", "two-group P_NL", 1 / (f1 * f2), "{:.5f}")
rec("ch07", "F17", "M^2 = L1^2+L2^2", L1**2 + L2**2, "{:.2f}", "cm^2")
rec("ch07", "F17", "M", math.sqrt(L1**2 + L2**2), "{:.3f}", "cm")
rec("ch07", "F17", "M^2 approx P_NL", 1 / (1 + (L1**2 + L2**2) * B2), "{:.5f}")
B2_small = 0.33 / (L1**2 + L2**2)
rec("ch07", "F17", "H~/M=10: M^2B^2", 0.33, "{:.2f}")
rec("ch07", "F17", "H~/M=10: P_NL (M^2)", 1 / 1.33, "{:.3f}")
rec("ch07", "F17", "H~/M=10: P_NL two-group", 1 / ((1 + L1**2 * B2_small) * (1 + L2**2 * B2_small)), "{:.3f}")

# F19: design chain
for Pw, label in ((3000e6, "3000 MW"), (300e6, "300 MW")):
    Vd = Pw / 100.0  # cm^3 at 100 W/cm^3
    Hd = (4 * Vd / math.pi) ** (1 / 3)
    term = 33.0 * (M_pwr / Hd) ** 2
    rec("ch07", "F19", f"{label}: V at 100 W/cm^3", Vd / 1e6, "{:.2f}", "m^3")
    rec("ch07", "F19", f"{label}: H~ = (4V/pi)^(1/3)", Hd, "{:.1f}", "cm")
    rec("ch07", "F19", f"{label}: 33 (M/H~)^2", term, "{:.4f}")
    rec("ch07", "F19", f"{label}: P_NL", 1 / (1 + term), "{:.3f}")

# F24: axial reflector savings for the PWR-size core with a water reflector
Mhat = 5.84
alpha2 = Br2 + 1 / Mhat**2
alpha = math.sqrt(alpha2)
Bz = math.pi / Ht
rec("ch07", "F24", "1/M^2 reflector (water)", 1 / Mhat**2, "{:.5f}", "1/cm^2")
rec("ch07", "F24", "alpha^2 = B_r^2 + 1/M^2", alpha2, "{:.5f}", "1/cm^2")
rec("ch07", "F24", "alpha", alpha, "{:.4f}", "1/cm")
rec("ch07", "F24", "B_z = pi/H~", Bz, "{:.6f}", "1/cm")
for ratio, name in ((1.0, "D^/D=1"), (0.16 / 1.383, "D^/D=0.16/1.383")):
    arg = alpha * ratio / Bz
    Hp = (2 / Bz) * math.atan(arg)
    rec("ch07", "F24", f"{name}: alpha D^/(B_z D)", arg, "{:.2f}")
    rec("ch07", "F24", f"{name}: H'", Hp, "{:.1f}", "cm")
    rec("ch07", "F24", f"{name}: s_z = (H~-H')/2", (Ht - Hp) / 2, "{:.2f}", "cm")
    rec("ch07", "F24", f"{name}: thick-reflector estimate M^ D/D^", Mhat / ratio, "{:.2f}", "cm")

# F26: savings as a fraction of half height
for HM in (10, 50):
    rec("ch07", "F26", f"s/(H/2) with s=M, H/M={HM}", 2 / HM, "{:.2f}")

# F29: uniform poison worth with the one-group PWR set
nuSf = 2.43 * Sf
Sa_pwr = nuSf / kinf_crit
D_pwr = M2 * Sa_pwr
rec("ch07", "F29", "nu Sigma_f (nu=2.43, Sf=0.01)", nuSf, "{:.4f}", "1/cm")
rec("ch07", "F29", "Sigma_a = nuSf/kinf", Sa_pwr, "{:.5f}", "1/cm")
rec("ch07", "F29", "D = M^2 Sigma_a", D_pwr, "{:.3f}", "cm")
rho_u = -0.01 * Sa_pwr / nuSf
rec("ch07", "F29", "rho for dSa/Sa = 1% (exact formula)", rho_u, "{:.5f}")
kprime = nuSf / (Sa_pwr * 1.01 + D_pwr * B2)
rec("ch07", "F29", "k' by direct recalculation", kprime, "{:.5f}")
rec("ch07", "F29", "rho = (k'-1)/k' direct", (kprime - 1) / kprime, "{:.5f}")

# F30-F32: rods
rec("ch07", "F30", "J0^2(2.405/2)", special.j0(j01 / 2) ** 2, "{:.3f}")
for xf in (0.25, 0.5, 0.75):
    rec("ch07", "F31", f"normalized rod worth at x/H={xf}", xf - math.sin(2 * math.pi * xf) / (2 * math.pi), "{:.4f}")
J1sq = special.j1(j01) ** 2
rec("ch07", "F32", "J1^2(2.405)", J1sq, "{:.4f}")
acSac = 2.0
rho_rod = -acSac / (J1sq * nuSf * math.pi * Rt**2)
rec("ch07", "F32", "central full-length rod worth, a_c Sigma_ac = 2 cm", rho_rod, "{:.5f}")
rec("ch07", "F32", "same in pcm", rho_rod * 1e5, "{:.0f}", "pcm")
rec("ch07", "F32", "rod at R/2 (x J0^2)", rho_rod * special.j0(j01 / 2) ** 2 * 1e5, "{:.0f}", "pcm")
rec("ch07", "F32", "central rod half inserted", rho_rod * 0.5 * 1e5, "{:.0f}", "pcm")
# cross-check the rod-worth denominator numerically: int nuSf phi^2 dV with phi = J0 cos
num = integrate.quad(lambda r: special.j0(j01 * r / Rt) ** 2 * r, 0, Rt)[0] * 2 * math.pi * (Ht / 2)
den_check = acSac * (Ht / 2) / (nuSf * num)
rec("ch07", "F32", "numerical check of |rho| central rod", den_check, "{:.5f}")

# F33: coupling ratios
rec("ch07", "F33", "H~/M PWR 360/7.62", 360 / 7.62, "{:.1f}")
rec("ch07", "F33", "H~/M small fast core 100/19.2", 100 / 19.2, "{:.1f}")

# ----------------------------------------------------------------------------
# Chapter 1
# ----------------------------------------------------------------------------
U_MEV = 931.5          # MeV per u, as in Lesson 1
NA = 6.022e23
MEV_J = 1.602e-13
YEAR = 3.156e7         # s

rec("ch01", "F1", "energy ratio 200 MeV / 4 eV", 200e6 / 4.0, "{:.2g}")
rec("ch01", "F1", "mass fraction converted, fission", 200 / (236 * U_MEV), "{:.2e}")
rec("ch01", "F1", "mass fraction converted, combustion", 4e-6 / (44 * U_MEV), "{:.2e}")
e_nuc = 1e9 / 0.30 * 5 * 365 * 24 / 100e3      # Wh/kg
e_coal = 1e9 / 0.40 * 24 / 10000e3
rec("ch01", "F2", "nuclear plant energy per kg fuel", e_nuc / 1e9, "{:.2f}", "GWh/kg")
rec("ch01", "F2", "coal plant energy per kg fuel", e_coal / 1e3, "{:.1f}", "kWh/kg")
rec("ch01", "F2", "ratio", e_nuc / e_coal, "{:.2e}")
rec("ch01", "F2", "c^2", (2.9979e8) ** 2 / 3.6e12, "{:.0f}", "GWh/kg")

mn_c2 = 939.57
for K in (2.0, 6.3, 10.0):
    b2 = 1 - (mn_c2 / (K + mn_c2)) ** 2
    Kc = 0.5 * mn_c2 * b2
    rec("ch01", "F6", f"K={K} MeV: beta^2, v (m/s), K_classical, % error",
        (b2, math.sqrt(b2) * 2.9979e8, Kc, 100 * (Kc - K) / K), "{:.4g}")

m = {"H1": 1.007825031898, "He4": 4.00260325413, "Li7": 7.01600343426, "Be9": 9.012183062,
     "B10": 10.012936862, "B12": 12.014352638, "C13": 13.00335483534, "Co60": 59.933815536,
     "Ni60": 59.930785129, "n": 1.008664}
rec("ch01", "F8", "Q 9Be(a,p)12B", (m["Be9"] + m["He4"] - m["B12"] - m["H1"]) * U_MEV, "{:.3f}", "MeV")
rec("ch01", "F8", "Q 60Co beta-", (m["Co60"] - m["Ni60"]) * U_MEV, "{:.3f}", "MeV")
rec("ch01", "F8", "Q 7Li(p,a)4He", (m["Li7"] + m["H1"] - 2 * m["He4"]) * U_MEV, "{:.2f}", "MeV")
rec("ch01", "F8", "Q 10B(a,p)13C", (m["B10"] + m["He4"] - m["C13"] - m["H1"]) * U_MEV, "{:.3f}", "MeV")
d_he = 2 * m["H1"] + 2 * m["n"] - m["He4"]
rec("ch01", "F9", "He-4 mass defect (u), B (MeV), B/A", (d_he, d_he * U_MEV, d_he * U_MEV / 4), "{:.5g}")
# D-T Q from binding energies per nucleon 1.112, 2.827, 7.074 MeV
rec("ch01", "F11", "D-T Q from B/A values", 4 * 7.074 - 2 * 1.112 - 3 * 2.827, "{:.2f}", "MeV")
VC = 1.44 / 4.0
rec("ch01", "F11", "Coulomb energy at 4 fm (MeV), T (K)", (VC, VC * 1e6 / 8.617e-5), "{:.3g}")


def semf(A):
    """Semi-empirical binding energy per nucleon along the line of stability (figure only)."""
    Z = A / (2 + 0.015 * A ** (2.0 / 3.0))
    return 15.75 - 17.8 * A ** (-1.0 / 3.0) - 0.711 * Z**2 / A ** (4.0 / 3.0) - 23.7 * (A - 2 * Z) ** 2 / A**2


rec("ch01", "F10", "SEMF B/A at A=56, 117, 235", (semf(56), semf(117), semf(235)), "{:.2f}", "MeV")
rec("ch01", "F10", "fission estimate 235*(B/A_117 - B/A_235)", 235 * (semf(117) - semf(235)), "{:.0f}", "MeV")

gam = 3.1e-11
rec("ch01", "F12", "recoverable MeV per fission", gam / MEV_J, "{:.0f}", "MeV")
frate = 3000e6 / gam
rec("ch01", "F13", "fissions/s at 3000 MW", frate, "{:.2e}")
rec("ch01", "F13", "U-235 fissioned per day", frate * 86400 * 235 / NA / 1e3, "{:.2f}", "kg")
rec("ch01", "F13", "U-235 fissioned per year", frate * 86400 * 365 * 235 / NA / 1e6, "{:.2f}", "t")
rec("ch01", "F14", "Q prompt symmetric fission", (235.043928 - 2 * 116.917956 - 1.0086649) * U_MEV, "{:.1f}", "MeV")
rec("ch01", "F14", "Q total after beta chains", (235.043928 - 2 * 116.902955 - 1.0086649) * U_MEV, "{:.1f}", "MeV")
rec("ch01", "F15", "generations to double at k=1.1", math.log(2) / math.log(1.1), "{:.2f}")
rec("ch01", "F16", "k^(t/l) and exp((k-1)t/l), k=1.001, l=1e-4 s, t=1 s", (1.001**1e4, math.exp(10)), "{:.4g}")
rec("ch01", "F16", "k=0.999 after 1 s", 0.999**1e4, "{:.2e}")
for tt, name in ((1, "1 s"), (3600, "1 h"), (86400, "1 d"), (30 * 86400, "30 d"), (YEAR, "1 y")):
    rec("ch01", "F18", f"Wigner-Way Pd/P0, t0=1 y, t={name}",
        0.0622 * (tt**-0.2 - (YEAR + tt) ** -0.2), "{:.4f}")
rec("ch01", "F18", "same for t0=30 d, t=1 d", 0.0622 * (86400**-0.2 - (31 * 86400) ** -0.2), "{:.4f}")

lam_I = math.log(2) / 8.05
lam_Sr = math.log(2) / 10628
rec("ch01", "F22", "lambda I-131 (1/d), Sr-90 (1/d)", (lam_I, lam_Sr), "{:.3g}")
rec("ch01", "F23", "1 g Ra-226 activity", math.log(2) / (1600 * YEAR) * NA / 226, "{:.3g}", "Bq")
AI, ASr = 0.85e18 / 3.7e10, 1.63e18 / 3.7e10
rec("ch01", "F25", "saturation activities I, Sr (Ci)", (AI, ASr), "{:.3g}")
for tt in (7, 30, 365.25):
    rec("ch01", "F25", f"activities at {tt} d: I, Sr (Ci)",
        (AI * (1 - math.exp(-lam_I * tt)), ASr * (1 - math.exp(-lam_Sr * tt))), "{:.3g}")
rec("ch01", "F24", "1-2^-n for n=1,3,5,7", [1 - 2.0**-n for n in (1, 3, 5, 7)], "{:.3f}")
rec("ch01", "F24", "half-lives to 90, 99 % of saturation", (math.log(10) / math.log(2), math.log(100) / math.log(2)), "{:.2f}")
lS, lY = math.log(2) / 75.0, math.log(2) / (18.7 * 60)
tt = 3600.0
nS = math.exp(-lS * tt)
nY = lS / (lY - lS) * (math.exp(-lS * tt) - math.exp(-lY * tt))
rec("ch01", "F27", "A=94 chain at 1 h: Sr, Y, Zr fractions", (nS, nY, 1 - nS - nY), "{:.3g}")
tmax = math.log(lS / lY) / (lS - lY)
rec("ch01", "F27", "time of maximum Y-94 (s), value", (tmax, lS / (lY - lS) * (math.exp(-lS * tmax) - math.exp(-lY * tmax))), "{:.3g}")
rec("ch01", "F28", "N_Y90/N_Sr90 in secular equilibrium (64.1 h / 28.8 y)", 64.1 / (28.8 * 365.25 * 24), "{:.2e}")

# ----------------------------------------------------------------------------
# Chapter 2
# ----------------------------------------------------------------------------
N0 = 0.6023  # 1e24 per mol, Lewis's value
nAl = 2.70 * 6.022e23 / 26.98
nW = 1.00 * 6.022e23 / 18.015
rec("ch02", "F3", "n_Al, n_H2O (1/cm3)", (nAl, nW), "{:.3e}")
Sal = -math.log(0.9949) / 0.050
rec("ch02", "F4", "Al: Sigma (1/cm), sigma (b)", (Sal, Sal / nAl * 1e24), "{:.3g}")
Sw = nW * (2 * 20 + 3.8) * 1e-24
rec("ch02", "F6", "water Sigma_s epithermal (1/cm), mfp (cm), P(no collision in 2 cm)", (Sw, 1 / Sw, math.exp(-2 * Sw)), "{:.3g}")
rec("ch02", "F5", "survive 1 mfp, collide within 1 mfp", (math.exp(-1), 1 - math.exp(-1)), "{:.3f}")
rec("ch02", "F6", "Sigma=0.8: thickness for 5% (cm), first collision within 2 cm", (math.log(20) / 0.8, 1 - math.exp(-1.6)), "{:.3g}")
rec("ch02", "F7", "point source 1e6 n/s at 1 m in vacuum", 1e6 / (4 * math.pi * 100**2), "{:.2f}", "n/cm2/s")
rec("ch02", "F7", "Sigma for a tenfold cut over 50 cm", math.log(10) / 50, "{:.4f}", "1/cm")
S_st, S_liq = (rho * 6.022e23 / 18.015 * (2 * 21.8 + 3.8) * 1e-24 for rho in (0.036, 0.74))
rec("ch02", "F8", "steam, liquid at 1000 psi, 40% void mixture (1/cm)", (S_st, S_liq, 0.4 * S_st + 0.6 * S_liq), "{:.3g}")
sU = 0.08 * 607.5 + 0.92 * 11.8
SUO2 = 11 * N0 / 270 * (sU + 7.0)
SC = 1.6 * N0 / 12 * 4.9
rec("ch02", "F10", "sigma_U, sigma_UO2 (b), Sigma_UO2, Sigma_C, mixture (1/cm)", (sU, sU + 7, SUO2, SC, 0.25 * SUO2 + 0.75 * SC), "{:.3g}")
ea = (0.04 / 235) / (0.04 / 235 + 0.96 / 238)
rec("ch02", "F9", "4 w/o -> a/o", ea, "{:.4f}")
rec("ch02", "F9", "Lewis (2.24) at 0.04 and 0.007", (1.0128 * 0.04 / (1 + 0.0128 * 0.04), 1.0128 * 0.007 / (1 + 0.0128 * 0.007)), "{:.5f}")
Re_, Ra_ = 2 * 20 + 4 + 15, 2 * 0.1 + 600
rec("ch02", "F12", "mixture strengths e, a, t (b)", (Re_, Ra_, Re_ + Ra_), "{:.1f}")
rec("ch02", "F12", "P(e), P(H el), P(U abs), P(f|abs)", (Re_ / (Re_ + Ra_), 40 / (Re_ + Ra_), 600 / (Re_ + Ra_), 500 / Ra_), "{:.4f}")
rec("ch02", "F12", "P(first interaction is fission within one mfp)", 500 / (Re_ + Ra_) * (1 - math.exp(-1)), "{:.3f}")


def chi(E):
    return 0.453 * math.exp(-1.036 * E) * math.sinh(math.sqrt(2.29 * E))


rec("ch02", "F13", "norm of chi", integrate.quad(chi, 0, 60)[0], "{:.4f}")
rec("ch02", "F13", "mean fission energy", integrate.quad(lambda E: E * chi(E), 0, 60)[0], "{:.2f}", "MeV")
rec("ch02", "F13", "most probable fission energy", optimize.minimize_scalar(lambda E: -chi(E), bounds=(0.1, 3), method="bounded").x, "{:.2f}", "MeV")
rec("ch02", "F13", "fraction below 0.1 MeV", integrate.quad(chi, 0, 0.1)[0], "{:.4f}")
rec("ch02", "F13", "fraction above 10 MeV", integrate.quad(chi, 10, 60)[0], "{:.1e}")
kB = 8.617065e-5
kT0 = kB * 293.61
rec("ch02", "F14", "kT and 1.5 kT at 293.61 K (eV)", (kT0, 1.5 * kT0), "{:.4f}")
vfac = math.sqrt(2 * 1.602e-19 / 1.6749e-27)
rec("ch02", "F14", "v at 0.0253 eV, 1 eV, 2 MeV (m/s, classical)", (vfac * math.sqrt(0.0253), vfac, vfac * math.sqrt(2e6)), "{:.3g}")
rec("ch02", "F14", "E ratio 2 MeV / 0.0253 eV", 2e6 / 0.0253, "{:.2g}")
rec("ch02", "F16", "H capture at 1 eV, 100 eV from 0.333 b", (0.333 * math.sqrt(0.0253), 0.333 * math.sqrt(0.0253 / 100)), "{:.3g}", "b")
R238 = 1.25e-13 * 238 ** (1 / 3)
rec("ch02", "F17", "R (cm) and 4 pi R^2 (b) for U-238", (R238, 4 * math.pi * R238**2 * 1e24), "{:.3g}")
rec("ch02", "F18", "E_cm/E for A=1, 12, 238", [A_ / (1 + A_) for A_ in (1, 12, 238)], "{:.3f}")
Er, Gam, s0, gg = 6.67, 0.027, 2.0e4, 0.95


def bw(E):
    return s0 * gg * math.sqrt(Er / E) / (1 + 4 * (E - Er) ** 2 / Gam**2)


rec("ch02", "F20", "illustrative BW capture at Er, Er+G/2, Er+10G, 0.0253 eV (b)",
    (bw(Er), bw(Er + Gam / 2), bw(Er + 10 * Gam), bw(0.0253)), "{:.3g}")


def alpha(A_):
    return ((A_ - 1) / (A_ + 1)) ** 2


def xi(A_):
    a = alpha(A_)
    return 1.0 if a == 0 else 1 + a / (1 - a) * math.log(a)


for A_, name in ((1, "H"), (2, "D"), (12, "C"), (16, "O"), (56, "Fe"), (238, "U-238")):
    a = alpha(A_)
    nmin = float("inf") if a == 0 else math.log(1e6) / math.log(1 / a)
    rec("ch02", "F23/F28", f"{name}: alpha, xi, 2/(A+2/3), n(2 MeV->0.025 eV), n_min(1 MeV->1 eV), mu_L",
        (a, xi(A_), 2 / (A_ + 2 / 3), math.log(2e6 / 0.025) / xi(A_), nmin, 2 / (3 * A_)), "{:.4g}")
rec("ch02", "F24", "E'/E at mu_c=0 for A=12", (144 + 1) / 169, "{:.3f}")
rec("ch02", "F26", "fraction below E/2 after one collision: D, C", ((0.5 - alpha(2)) / (1 - alpha(2)), max(0.0, (0.5 - alpha(12)) / (1 - alpha(12)))), "{:.4f}")
rec("ch02", "F25", "mean E'/E: H, D, C, U", [(1 + alpha(A_)) / 2 for A_ in (1, 2, 12, 238)], "{:.4f}")
rec("ch02", "F28", "ln(2e6/0.025)", math.log(2e6 / 0.025), "{:.2f}")
xiO = 2 / (16 + 2 / 3)
rec("ch02", "F29", "xi-bar water (Lewis 2.62)", (2 * 20 + xiO * 3.8) / (2 * 20 + 3.8), "{:.3f}")
rec("ch02", "F29", "collisions 2 MeV -> 1 eV in water, xi=0.93", math.log(2e6) / 0.93, "{:.1f}")
SsU, SsO = 9.37, 4.01   # illustrative: Table 3.2 thermal scattering, b
rec("ch02", "F29", "xi-bar for UO2 with sigma_s 9.37 and 4.01 b; U alone",
    ((xi(238) * SsU + 2 * xi(16) * SsO) / (SsU + 2 * SsO), xi(238)), "{:.4f}")

# ----------------------------------------------------------------------------
# Chapter 3
# ----------------------------------------------------------------------------
for e in (0.007, 0.03, 0.05, 0.20, 1.0):
    rec("ch03", "F3", f"thermal eta at enrichment {e}", e * 2.43 * 505 / (e * 591 + (1 - e) * 2.42), "{:.3f}")
mods = {"H2O": (0.93, 1.28, 58.0), "D2O": (0.51, 0.18, 21000.0), "C": (0.158, 0.056, 200.0)}
for name, (x_, sdp, sdr) in mods.items():
    rec("ch03", "F5", f"{name}: implied Sigma_a (1/cm), Sigma_s (1/cm), collisions for ln=18.2", (sdp / sdr, sdp / x_, 18.2 / x_), "{:.3g}")
sdp_mix = 0.99 * 0.18 + 0.01 * 1.28
Sa_mix = 0.99 * 0.18 / 21000 + 0.01 * 1.28 / 58
Ss_mix = 0.99 * 0.18 / 0.51 + 0.01 * 1.28 / 0.93
rec("ch03", "F6", "D2O + 1% H2O: xi, power, Sigma_a, ratio", (sdp_mix / Ss_mix, sdp_mix, Sa_mix, sdp_mix / Sa_mix), "{:.4g}")
rec("ch03", "F6", "percent changes: xi, power, ratio",
    (100 * (sdp_mix / Ss_mix / 0.51 - 1), 100 * (sdp_mix / 0.18 - 1), 100 * (sdp_mix / Sa_mix / 21000 - 1)), "{:.1f}")
fr = 100 / 3.1e-11
sf = 2.43 * fr
rec("ch03", "F12", "fission rate, s_f at 100 W/cm3", (fr, sf), "{:.3g}")
rec("ch03", "F12", "E phi = q/(xi Sigma_s), water", sf / 1.28, "{:.3g}")
rec("ch03", "F12", "phi_I = (q/xi Sigma_s) ln(1e5)", sf / 1.28 * math.log(1e5), "{:.3g}")
rec("ch03", "F13", "(1-alpha)E_r at 10 eV: U-238, H", ((1 - alpha(238)) * 10, 10.0), "{:.3g}", "eV")
rec("ch03", "F15", "resonance escape, x=9, Delta=0.5 eV, E_r=10 eV, xi=0.9: shielded, unshielded",
    (math.exp(-0.9 * 0.5 / (0.9 * 10)), math.exp(-9 * 0.5 / (0.9 * 10))), "{:.3f}")
rec("ch03", "F16", "mean energy of phi_M in kT; density-weighted mean in kT", (2.0, 1.5), "{:.1f}")
rec("ch03", "F16", "kT at 293.61 K and 573.15 K (eV)", (kB * 293.61, kB * 573.15), "{:.4f}")
rec("ch03", "F21", "1/ln(1e5)", 1 / math.log(1e5), "{:.4f}")
rec("ch03", "F21", "U-238 capture: 0.0869 * 278", 278 / math.log(1e5), "{:.1f}", "b")
rec("ch03", "F21", "sqrt(pi)/2", math.sqrt(math.pi) / 2, "{:.4f}")
rec("ch03", "F21", "H: 0.295/0.8862", 0.295 / (math.sqrt(math.pi) / 2), "{:.3f}", "b")
rec("ch03", "F21", "H thermal average at 573.15 K", 0.295 * math.sqrt(293.61 / 573.15), "{:.3f}", "b")
sw_T = 2 * 0.295 + 1.69e-4
rec("ch03", "F21", "water sigma_aT at 293 K and 573 K (b)", (sw_T, sw_T * math.sqrt(293.61 / 573.15)), "{:.3f}")
sw_I = (2 * 0.149 + 8.53e-5) / math.log(1e5)
sw_F = 2 * 3.92e-5 + 1.20e-2
sw = (sw_T + sw_I + sw_F) / 3
nW3 = 1.0 * 6.022e23 / 18.015
rec("ch03", "F22", "water sigma_a: T, I, F, equal-flux mean (b)", (sw_T, sw_I, sw_F, sw), "{:.4g}")
rec("ch03", "F22", "Sigma_a (1/cm), phi_tot for s=10", (nW3 * sw * 1e-24, 10 / (nW3 * sw * 1e-24)), "{:.4g}")
sfU = (505 + 272 / math.log(1e5) + 1.22) / 3
saU = (591 + 404 / math.log(1e5) + 1.29) / 3
rec("ch03", "F23", "U-235 equal-flux sigma_f, sigma_a (b)", (sfU, saU), "{:.4g}")
rec("ch03", "F23", "critical r = N_U/N_w; k_inf as r->inf", (sw / (2.43 * sfU - saU), 2.43 * sfU / saU), "{:.4g}")
for r in (5e-4, 2e-3):
    rec("ch03", "F23", f"k_inf at r={r}", r * 2.43 * sfU / (sw + r * saU), "{:.3f}")
# multigroup: hydrogen scattering out of group 2 (Lesson 13)
E0g, E1g, E2g, E3g = 1e7, 1e5, 1.0, 1e-3
Lg = math.log(E1g / E2g)
s22 = 20 * (Lg + E2g / E1g - 1) / Lg
s32 = 20 * (E2g - E3g) * (1 / E2g - 1 / E1g) / Lg
slost = 20 * E3g * (1 / E2g - 1 / E1g) / Lg
rec("ch03", "F31", "H: sigma_s 2<-2, 3<-2, below E3, sum (b)", (s22, s32, slost, s22 + s32 + slost), "{:.5f}")
rec("ch03", "F31", "fraction of group-2 collisions entering group 3", s32 / 20, "{:.4f}")
num22 = integrate.quad(lambda E: (E - E2g) / E**2, E2g, E1g)[0] * 20 / Lg
rec("ch03", "F31", "numerical check of 2<-2", num22, "{:.5f}")
# illustrative three-group water tank (Lesson 13 structure; removal data are illustrative)
Sr1, Sr2, Sa3 = 0.10, 0.12, 0.0197
s21, s31, s32m = 0.099, 0.0009, 0.1195
p1 = 10 / Sr1
p2 = s21 * p1 / Sr2
p3 = (s31 * p1 + s32m * p2) / Sa3
Sa1, Sa2 = Sr1 - s21 - s31, Sr2 - s32m
rec("ch03", "F29", "3-group tank fluxes", (p1, p2, p3), "{:.4g}")
rec("ch03", "F29", "absorption audit (should be 10)", Sa1 * p1 + Sa2 * p2 + Sa3 * p3, "{:.4f}")
# two-group multiplying system (Lesson 14)
Sg = (2.04e-3, 1.91e-2)
Sf2g = (2.96e-4, 1.38e-2)
nub = (2.49, 2.43)
d = 4.27e-2
Sa = [Sg[i] + Sf2g[i] for i in range(2)]
f = [nub[i] * Sf2g[i] for i in range(2)]
Sr1 = Sa[0] + d
Rr = d / Sa[1]
den = Sr1 - f[0] - f[1] * Rr
ph1 = 1 / den
ph2 = Rr * ph1
kinf2 = (f[0] + f[1] * Rr) / Sr1
rec("ch03", "F32", "Sigma_a1, Sigma_a2, Sigma_r1, f1, f2", (Sa[0], Sa[1], Sr1, f[0], f[1]), "{:.6g}")
rec("ch03", "F33", "R, denominator, phi1, phi2", (Rr, den, ph1, ph2), "{:.8g}")
rec("ch03", "F33", "R_a, production, difference", (Sa[0] * ph1 + Sa[1] * ph2, f[0] * ph1 + f[1] * ph2, Sa[0] * ph1 + Sa[1] * ph2 - f[0] * ph1 - f[1] * ph2), "{:.7g}")
rec("ch03", "F33", "n2/n1", Rr * 1e5 / 2e3, "{:.4f}")
rec("ch03", "F34", "k_inf two-group", kinf2, "{:.8f}")
rec("ch03", "F34", "pieces: f1/Sr1, d/Sr1, f2/Sa2", (f[0] / Sr1, d / Sr1, f[1] / Sa[1]), "{:.4f}")
M = np.array([[Sr1, 0.0], [-d, Sa[1]]])
F = np.array([[f[0], f[1]], [0.0, 0.0]])
ev, evec = np.linalg.eig(np.linalg.solve(M, F))
i = int(np.argmax(ev.real))
vec = np.abs(evec[:, i].real)
rec("ch03", "F35", "largest eigenvalue of M^-1 F; normalized eigenvector", (ev[i].real, vec[0] / vec.sum(), vec[1] / vec.sum()), "{:.6f}")
rec("ch03", "F36", "one-group collapse k = sum f phi / sum Sa phi", (f[0] + f[1] * Rr) / (Sa[0] + Sa[1] * Rr), "{:.6f}")
rec("ch03", "F37", "source multiplication 1/(1-k)", 1 / (1 - kinf2), "{:.5f}")
rec("ch03", "F37", "phi1 without fission; ratio", (1 / Sr1, ph1 * Sr1), "{:.5g}")
f2crit = (Sr1 - f[0]) / Rr
rec("ch03", "F37", "f2 for k=1 and percent increase", (f2crit, 100 * (f2crit / f[1] - 1)), "{:.5g}")

# ----------------------------------------------------------------------------
# Chapter 4
# ----------------------------------------------------------------------------
rec("ch04", "F2", "pins for 3000 MW at 17.5 kW/m, 3.66 m", 3000e6 / (17.5e3 * 3.66), "{:.0f}")
for name, pd in (("PWR", 102), ("BWR", 56), ("PHWR", 7.7), ("HTGR", 6.6), ("SFR", 217)):
    rec("ch04", "F2", f"{name} volume for 3000 MW", 3000 / pd, "{:.1f}", "m3")
rec("ch04", "F2", "pin power (kW) and power density check 17.5 kW/m in a 1.26 cm square cell (W/cm3)", (17.5 * 3.66, 175 / 1.26**2), "{:.3g}")
rf = 0.6
rec("ch04", "F4", "pitch for Vm/Vf=2, D=1.2 cm: square, hex", (math.sqrt(3 * math.pi * rf**2), math.sqrt(2 * 3 * math.pi * rf**2 / math.sqrt(3))), "{:.3f}", "cm")
rec("ch04", "F4", "minimum coolant/fuel: square, hex", (4 / math.pi - 1, 2 * math.sqrt(3) / math.pi - 1), "{:.3f}")
rec("ch04", "F4", "hex fuel fraction pi/(2 sqrt3) at P=D", math.pi / (2 * math.sqrt(3)), "{:.3f}")
NH, NUm = 2 * 1.0 * 6.022e23 / 18.015, 19.1 * 6.022e23 / 238.03
rec("ch04", "F5", "N_H, N_U metal", (NH, NUm), "{:.3e}")
rec("ch04", "F5", "r_U/R for H/U = 10, 100", [(NH / (NH + h * NUm)) ** (1 / 3) for h in (10, 100)], "{:.3f}")
NPu, NUO, NNa, NFe = 11.0 * N0 / 271, 11.0 * N0 / 270, 0.97 * N0 / 23, 7.87 * N0 / 55.85
rec("ch04", "F6", "N PuO2, UO2, Na, Fe (1e24/cm3)", (NPu, NUO, NNa, NFe), "{:.4f}")
St_f = 0.15 * NPu * 8.6 + 0.85 * NUO * 8.2
rec("ch04", "F6", "fuel Sigma_t (1/cm), mfp (cm), Na mfp (cm)", (St_f, 1 / St_f, 1 / (NNa * 3.7)), "{:.3g}")


def kfast(x):
    prod = 0.3 * (x * NPu * 2.98 * 1.95 + (1 - x) * NUO * 2.47 * 0.05)
    absf = 0.3 * (x * NPu * 2.40 + (1 - x) * NUO * 0.404)
    return prod, absf, 0.5 * NNa * 0.0018, 0.2 * NFe * 0.0087


pr, af, ac, ast = kfast(0.15)
rec("ch04", "F8", "production, fuel abs, Na abs, Fe abs (1/cm)", (pr, af, ac, ast), "{:.4g}")
rec("ch04", "F8", "k_inf problem 4.3", pr / (af + ac + ast), "{:.3f}")
rec("ch04", "F8", "fraction of absorptions outside fuel", (ac + ast) / (af + ac + ast), "{:.4f}")
mass = (0.3 * 11.0, 0.5 * 0.97, 0.2 * 7.87)
rec("ch04", "F8", "fuel mass fraction", mass[0] / sum(mass), "{:.3f}")
xs = optimize.brentq(lambda x: kfast(x)[0] / sum(kfast(x)[1:]) - 1 / 0.9, 0.01, 0.5)
rec("ch04", "F9", "PuO2 volume fraction for k_inf = 1/0.9", xs, "{:.4f}")
a_fi, a_fe, b_fi, b_fe = 2.40, 0.404, 2.98 * 1.95, 2.47 * 0.05
C = (ac + ast) / (0.3 * NUO)
rec("ch04", "F9", "C (b) and Lesson 16 closed form e*", (C, ((1 / 0.9) * (a_fe + C) - b_fe) / ((b_fi - b_fe) - (1 / 0.9) * (a_fi - a_fe))), "{:.4f}")
for name, v in (("PWR", (1.27, 0.63, 0.94, 1.89)), ("BWR", (1.28, 0.63, 0.94, 1.89)), ("PHWR", (1.08, 0.84, 0.97, 1.31)), ("HTGR", (1.20, 0.62, 0.98, 2.02))):
    rec("ch04", "F13", f"{name} four-factor product", v[0] * v[1] * v[2] * v[3], "{:.3f}")
BT, BF, ATf, ATm, AIf = 1000.0, 270.0, 529.0, 34.0, 331.0
rec("ch04", "F15", "eps, p, f, eta_T, product, B/A", ((BT + BF) / BT, (ATf + ATm) / (ATf + ATm + AIf), ATf / (ATf + ATm), BT / ATf,
    (BT + BF) / BT * (ATf + ATm) / (ATf + ATm + AIf) * ATf / (ATf + ATm) * BT / ATf, (BT + BF) / (ATf + ATm + AIf)), "{:.4f}")
rec("ch04", "F13", "100 neutrons: after eps, p, f, eta", (127, 127 * 0.63, 127 * 0.63 * 0.94, 127 * 0.63 * 0.94 * 1.89), "{:.1f}")
# PWR example (FNRP problem 4.6)
e4 = 0.03
saf = e4 * 591 + (1 - e4) * 2.42
etaT = e4 * 2.43 * 505 / saf
NUO2 = 11.0 * N0 / 270
I46 = 4.45 + 26.6 * math.sqrt(4 / (11.0 * 1.1))
xsS = 1.28
expo = (1 - e4) * NUO2 * I46 / xsS          # times Vf/Vm
p46 = math.exp(-expo / 2)
Sam = 1.0 * 6.022e23 / 18.015 * (2 * 0.295 + 1.69e-4) * 1e-24
Saf = NUO2 * saf
cz = 1.16 * Sam / Saf
f46 = 1 / (1 + 2 * cz)
rec("ch04", "F19", "sigma_aT fuel (b), eta_T at 3%", (saf, etaT), "{:.4g}")
rec("ch04", "F19", "eta_T fissile alone and the bracket of (4.53)", (2.43 * 505 / 591, 1 + (1 - e4) * 2.42 / (e4 * 591)), "{:.4f}")
rec("ch04", "F19", "eta_T for 2% U-235, 1% Pu-239 (problem 4.12)", (0.02 * 2.43 * 505 + 0.01 * 2.90 * 698) / (0.02 * 591 + 0.01 * 973 + 0.97 * 2.42), "{:.3f}")
rec("ch04", "F18", "I for D=1.0 cm with and without Dancoff (b)", (I46, 4.45 + 26.6 * math.sqrt(4 / 11.0)), "{:.2f}")
rec("ch04", "F18", "I for D=0.8, 1.2 cm (rho=11)", (4.45 + 26.6 * math.sqrt(4 / 8.8), 4.45 + 26.6 * math.sqrt(4 / 13.2)), "{:.2f}")
rec("ch04", "F18", "infinitely dilute I_a of U-238", 278, "{:.0f}", "b")
rec("ch04", "F20", "N_UO2 (1e24), exponent coefficient, exponent at Vm/Vf=2, p", (NUO2, expo, expo / 2, p46), "{:.4f}")
rec("ch04", "F20", "p with the dilute I=278 b", math.exp(-(1 - e4) * NUO2 * 278 / xsS / 2), "{:.3f}")
rec("ch04", "F21", "Sigma_aT water, fuel (1/cm), zeta ratio c, f", (Sam, Saf, cz, f46), "{:.4f}")
rec("ch04", "F21", "f with zeta = 1", 1 / (1 + 2 * Sam / Saf), "{:.4f}")
rec("ch04", "F21", "k_inf = 1.24 p f eta_T", 1.24 * p46 * f46 * etaT, "{:.3f}")


def k46(x, c=cz):
    return 1.24 * etaT * math.exp(-expo / x) / (1 + c * x)


for x in (1.0, 2.0, 3.0, 4.0):
    rec("ch04", "F22", f"Vm/Vf={x}: p, f, k", (math.exp(-expo / x), 1 / (1 + cz * x), k46(x)), "{:.3f}")
xo = optimize.minimize_scalar(lambda x: -k46(x), bounds=(0.5, 8), method="bounded").x
rec("ch04", "F22", "optimum Vm/Vf and k_max", (xo, k46(xo)), "{:.3f}")
rec("ch04", "F22", "closed form optimum", (expo * cz + math.sqrt((expo * cz) ** 2 + 4 * cz * expo)) / (2 * cz), "{:.3f}")
NB = 1e-3 * 1.0 * 6.022e23 / 10.81
SaB = NB * 0.199 * 3409e-24
cb = 1.16 * (Sam + SaB) / Saf
xb = optimize.minimize_scalar(lambda x: -k46(x, cb), bounds=(0.5, 8), method="bounded").x
rec("ch04", "F24", "1000 ppm B: Sigma_a boron (1/cm), f at 2, k at 2, optimum, k at optimum", (SaB, 1 / (1 + 2 * cb), k46(2, cb), xb, k46(xb, cb)), "{:.4f}")
rec("ch04", "F24", "dk/dx sign at x=2: no boron, 1000 ppm", (k46(2.05) - k46(1.95), k46(2.05, cb) - k46(1.95, cb)), "{:.4f}")
I0 = 4.45 + 26.6 * math.sqrt(4 / 11.0)
rec("ch04", "F25", "D2O Vm/Vf for same p (no Dancoff)", (1 - e4) * NUO2 * I0 / (0.18 * expo / 2), "{:.1f}")
rec("ch04", "F25", "D2O Vm/Vf for same f", 2 * Sam / (0.18 / 21000), "{:.0f}")

# ----------------------------------------------------------------------------
# Chapter 4 addendum: reactivity feedback (FNRP 9.1-9.4; Lessons 20-21)
# ----------------------------------------------------------------------------
beta5 = 0.0065                      # U-235 delayed fraction (Table 5.1)
k28 = 1.0065
rho28 = (k28 - 1) / k28
rec("ch04", "F28", "k=1.0065: rho, pcm, dollars (beta=0.0065)", (rho28, 1e5 * rho28, rho28 / beta5), "{:.4g}")
rec("ch04", "F28", "worth of k 1.02 -> 1.00: exact 1/k1-1/k2, and dk/k", (1 / 1.02 - 1.0, (1.0 - 1.02) / 1.02), "{:.5f}")
# F29: additive form with the Chain 6 lattice
kinf46 = 1.24 * p46 * f46 * etaT
rec("ch04", "F29", "k_inf of Chain 6", kinf46, "{:.3f}")
p_hot = 0.812
rec("ch04", "F29", "p 0.832 -> 0.812: d ln p, exact drho with k_inf=1.73 (pcm)",
    (1e5 * math.log(p_hot / p46), 1e5 * (1 / kinf46 - 1 / (kinf46 * p_hot / p46))), "{:.0f}")
rec("ch04", "F29", "leakage term P_L=0.03, dM2/M2=+0.02 (pcm)", -1e5 * 0.03 * 0.02, "{:.0f}")
# F30: temperature dependence of the resonance integral, Eq. (9.13)-(9.14), Table 9.1
def gtilde(C1, C2, rho_f, D):
    return C1 + C2 * 4 / (rho_f * D)
g_ox = gtilde(0.0061, 0.0047, 11.0, 1.0)
g_met = gtilde(0.0048, 0.0064, 19.1, 1.0)
rec("ch04", "F30", "gamma-tilde UO2 (rho=11, D=1) and U metal (rho=19.1, D=1)", (g_ox, g_met), "{:.5f}", "K^-1/2")
for T in (600.0, 1200.0):
    r_ox = 1 + g_ox * (math.sqrt(T) - math.sqrt(300))
    rec("ch04", "F30", f"I(T)/I(300) UO2 at {T:.0f} K, and I (b) from 19.7", (r_ox, I46 * r_ox), "{:.4g}")
I_met = 2.95 + 25.8 * math.sqrt(4 / 19.1)
rec("ch04", "F30", "U metal I(300) (b), I(1200)/I(300)", (I_met, 1 + g_met * (math.sqrt(1200) - math.sqrt(300))), "{:.4g}")
lnp0 = expo / 2                      # ln(1/p) for the oxide lattice, Vm/Vf = 2
expo_met = (NUm * 1e-24 / NUO2) * (I_met / I46) * lnp0   # same Vm/Vf, metal rod of the same size
# NUm is in 1/cm^3; NUO2 in 1e24/cm^3
rec("ch04", "F30", "metal rod: N_U ratio, exponent ln(1/p), p", (NUm * 1e-24 / NUO2, expo_met, math.exp(-expo_met)), "{:.4g}")
# F31: fuel temperature coefficient (9.16) and Doppler defect
def alpha_f(g, lnp, T, exact=False):
    a = -g * lnp / (2 * math.sqrt(T))
    if exact:
        a /= 1 + g * (math.sqrt(T) - math.sqrt(300))
    return a
for T in (600.0, 1200.0):
    rec("ch04", "F31", f"alpha_f UO2 at {T:.0f} K (pcm/K): (9.16), with I(T0)/I(T)",
        (1e5 * alpha_f(g_ox, lnp0, T), 1e5 * alpha_f(g_ox, lnp0, T, True)), "{:.3f}")
rec("ch04", "F31", "alpha_f U metal at 1200 K (pcm/K)", 1e5 * alpha_f(g_met, expo_met, 1200.0), "{:.3f}")
rec("ch04", "F31", "Doppler defect 300->600 and 600->1200 K (pcm)",
    (-1e5 * g_ox * lnp0 * (math.sqrt(600) - math.sqrt(300)), -1e5 * g_ox * lnp0 * (math.sqrt(1200) - math.sqrt(600))), "{:.0f}")
rec("ch04", "F31", "Lesson 21 check: p0=0.8, rho=10, D=1, T=1200 (pcm/K)", 1e5 * alpha_f(gtilde(0.0061, 0.0047, 10.0, 1.0), math.log(1 / 0.8), 1200.0), "{:.3f}")
# F32: moderator temperature coefficient (9.24)
bm = 2.9e-4
for name, p_, f_ in (("cold Chain 6", p46, f46), ("Table 4.2 PWR", 0.63, 0.94), ("1000 ppm boron", p46, 1 / (1 + 2 * cb))):
    rec("ch04", "F32", f"alpha_m {name}: ln(1/p), 1-f, pcm/K", (math.log(1 / p_), 1 - f_, -1e5 * bm * (math.log(1 / p_) - (1 - f_))), "{:.4g}")
# F34: composite coefficients (illustrative plant data, unlike problem 9.3)
af, ac = -2.5e-5, -1.0e-5
Rf = 0.4                                  # K/MW
Wcp = 1.5e4 * 5500 / 1e6                  # MW/K
inv2W = 1 / (2 * Wcp)
rec("ch04", "F34", "W c_p (MW/K), 1/(2 W c_p) (K/MW)", (Wcp, inv2W), "{:.4g}")
alphaT = af + ac
alphaP = (Rf + inv2W) * af + inv2W * ac
rec("ch04", "F34", "isothermal coefficient (pcm/K), power coefficient (pcm/MW)", (1e5 * alphaT, 1e5 * alphaP), "{:.3f}")
rec("ch04", "F34", "temperature defect 300->560 K (pcm), power defect 0->3000 MW (pcm)", (1e5 * alphaT * 260, 1e5 * alphaP * 3000), "{:.0f}")
rec("ch04", "F34", "fuel and coolant temperature rise at 3000 MW (K)", ((Rf + inv2W) * 3000, inv2W * 3000), "{:.0f}")
# F35: startup budget
rho_ex = 0.15
rec("ch04", "F35", "rod worth for SDM -0.04; rho_ex at HZP; at HFP", (rho_ex + 0.04, rho_ex + alphaT * 260, rho_ex + alphaT * 260 + alphaP * 3000), "{:.4f}")

# ----------------------------------------------------------------------------
# Chapter 5
# ----------------------------------------------------------------------------
vE = lambda E: 1.384e6 * math.sqrt(E)      # cm/s, E in eV
rec("ch05", "F2", "v(0.0253 eV) (cm/s)", vE(0.0253), "{:.3g}")
l_water = 1 / (Sam * vE(0.0253))
rec("ch05", "F2", "l_inf thermal water (Sigma_a=0.0197) (s)", l_water, "{:.3g}")
rec("ch05", "F2", "l_inf fast lattice (Sigma_a=0.00534, v=1e9) (s)", 1 / (0.00534 * 1e9), "{:.3g}")
rec("ch05", "F2", "lambda_a water (cm) = l v", 1 / Sam, "{:.1f}")
rec("ch05", "F3", "n(inf) = l S0 for S0=1e8/s; 3 l (ms)", (l_water * 1e8, 3e3 * l_water), "{:.3g}")
rec("ch05", "F3", "fraction of n(inf) at t = l, 2l, 3l", [1 - math.exp(-n) for n in (1, 2, 3)], "{:.3f}")
rec("ch05", "F5", "Gamma=0.1: P_L, P_NL", (0.1 / 1.1, 1 / 1.1), "{:.4f}")
l6 = 1e-4
for k in (1.001, 0.999):
    r = (k - 1) / l6
    rec("ch05", "F6", f"k={k}: (k-1)/l (1/s), e-fold (s), doubling/halving (s), factor in 1 s", (r, 1 / abs(r), math.log(2) / abs(r), math.exp(r)), "{:.4g}")
rec("ch05", "F6", "k=1.001, l=1e-7: e-fold (s)", 1e-7 / 0.001, "{:.1e}")
T7 = 20 / math.log(2)
k7 = 1 + 0.001 / T7
rec("ch05", "F7", "double in 20 s, l=1e-3: T (s), k-1, rho", (T7, k7 - 1, (k7 - 1) / k7), "{:.4g}")
for k in (0.9, 0.99):
    rec("ch05", "F8", f"k={k}, l=1e-4, S0=1e8: n(inf), tau (s)", (l6 * 1e8 / (1 - k), l6 / (1 - k)), "{:.3g}")
rec("ch05", "F8", "critical: n after 60 s at S0=1e8", 1e8 * 60, "{:.1e}")
# Delayed neutron data, Table 5.1
thalf = np.array([56, 23, 6.2, 2.3, 0.61, 0.23])
lam = np.log(2) / thalf
bi = {"U235": np.array([0.00021, 0.00142, 0.00128, 0.00257, 0.00075, 0.00027]),
      "Pu239": np.array([0.00007, 0.00063, 0.00044, 0.00069, 0.00018, 0.00009]),
      "U233": np.array([0.00023, 0.00078, 0.00064, 0.00074, 0.00014, 0.00008])}
Lam = 5e-5
for nm, b in bi.items():
    rec("ch05", "F9", f"beta {nm}", b.sum(), "{:.5f}")
rec("ch05", "F9", "beta_eff 80% U-235, 20% Pu-239 fissions; fractional drop", (0.8 * 0.0065 + 0.2 * 0.0021, 1 - (0.8 * 0.0065 + 0.2 * 0.0021) / 0.0065), "{:.4g}")
b = bi["U235"]
beta = b.sum()
tbar = (b * thalf).sum() / beta
lbar = beta / (b / lam).sum()
rec("ch05", "F10", "U-235: average half-life (5.32) (s), 1/lambda-bar (5.34) (s), lambda-bar (1/s)", (tbar, 1 / lbar, lbar), "{:.4g}")
rec("ch05", "F10", "l_d = l + 1/lambda (s), lbar = l + beta/lambda (s), lbar/l", (Lam + 1 / lbar, Lam + beta / lbar, (Lam + beta / lbar) / Lam), "{:.4g}")
rec("ch05", "F12", "C_1/n and sum C_i/n at critical, Lambda=5e-5", (b[0] / (lam[0] * Lam), (b / (lam * Lam)).sum()), "{:.4g}")
rec("ch05", "F13", "one cent in pcm: U-235, Pu-239", (1e5 * 0.01 * 0.0065, 1e5 * 0.01 * 0.0021), "{:.2f}")
rec("ch05", "F13", "rho=(k-1)/k and Lambda=l/k for k=1.0065, l=5e-5", ((k28 - 1) / k28, 5e-5 / k28), "{:.4g}")


def inhour(omega, b=b, lam=lam, Lam=Lam):
    return omega * (Lam + (b / (omega + lam)).sum())


def period(rho, b=b, lam=lam, Lam=Lam):
    """Dominant root of the inhour equation."""
    if rho > 0:
        w = optimize.brentq(lambda w: inhour(w, b, lam, Lam) - rho, 1e-12, 1e6)
    else:
        w = optimize.brentq(lambda w: inhour(w, b, lam, Lam) - rho, -lam[0] * (1 - 1e-12), -1e-12)
    return 1 / w


inhour_T7 = inhour(1 / T7)
rows.insert(next(i for i, r in enumerate(rows) if r[:2] == ("ch05", "F8")),
            ("ch05", "F7", "same T=28.9 s with six delayed groups: rho (pcm), ratio to prompt-only",
             f"{1e5 * inhour_T7:.3g}, {inhour_T7 / ((k7 - 1) / k7):.3g}", ""))
rec("ch05", "F16", "T for rho=+0.1 beta: exact, small-rho (5.56), (s)", (period(0.1 * beta), (Lam + beta / lbar) / (0.1 * beta)), "{:.1f}")
rec("ch05", "F16", "T for rho=-0.1 beta: exact, small-rho (s); limit -1/lambda_1 (s)", (period(-0.1 * beta), -(Lam + beta / lbar) / (0.1 * beta), -1 / lam[0]), "{:.1f}")
rec("ch05", "F16", "T for rho=0.02, 0.2, 0.5 beta (s)", [period(x * beta) for x in (0.02, 0.2, 0.5)], "{:.1f}")
rec("ch05", "F16", "T for rho=1.1 beta: exact, Lambda/(rho-beta) (s)", (period(1.1 * beta), Lam / (0.1 * beta)), "{:.4f}")
T17 = 7200 / math.log(1000)
rho17 = inhour(1 / T17)
rec("ch05", "F17", "1 W -> 1 kW in 2 h: T (s), rho (pcm), cents", (T17, 1e5 * rho17, 100 * rho17 / beta), "{:.4g}")
rec("ch05", "F17", "15 min period, 1 W -> 1 MW: time (s), (h)", (900 * math.log(1e6), 900 * math.log(1e6) / 3600), "{:.4g}")
rec("ch05", "F17", "T for +10 cents: U-235, Pu-239, U-233 (s)", [period(0.1 * bi[n].sum(), bi[n], lam, Lam) for n in ("U235", "Pu239", "U233")], "{:.1f}")
rec("ch05", "F17", "T for -10 cents: U-235, Pu-239, U-233 (s)", [period(-0.1 * bi[n].sum(), bi[n], lam, Lam) for n in ("U235", "Pu239", "U233")], "{:.1f}")
rec("ch05", "F18", "T above prompt critical: 1.5 dollars (s)", Lam / (0.5 * beta), "{:.4f}")
rec("ch05", "F19", "rod drop 100 W -> 70 W: dollars; fast time constant Lambda/(beta+|rho|) (ms)", (100 / 70 - 1, 1e3 * Lam / (beta * (1 + 100 / 70 - 1))), "{:.3g}")
rec("ch05", "F19", "prompt jump for +0.1, +0.2, +0.5 beta; drop for -0.1 beta", [1 / (1 - x) for x in (0.1, 0.2, 0.5, -0.1)], "{:.3f}")
# One delayed group (problem 5.10) versus six
def one_group_roots(rho, beta=beta, lam1=lbar, Lam=Lam):
    a, bq, c = Lam, beta - rho + lam1 * Lam, -lam1 * rho
    d = math.sqrt(bq * bq - 4 * a * c)
    return (-bq + d) / (2 * a), (-bq - d) / (2 * a)
for x in (0.02, 0.2):
    ws, wf = one_group_roots(x * beta)
    rec("ch05", "F20", f"rho={x} beta one group: omega_s, omega_f (1/s), T_1g, T_6g (s)", (ws, wf, 1 / ws, period(x * beta)), "{:.4g}")
rec("ch05", "F20", "one-group amplitudes for 0.2 beta: A_s/n0, A_f/n0", (lambda ws, wf: ((0.2 * beta / Lam - wf) / (ws - wf), 1 - (0.2 * beta / Lam - wf) / (ws - wf)))(*one_group_roots(0.2 * beta)), "{:.4f}")
# Feedback (Lesson 29 models)
alpha29, A29 = -3e-5, 100.0
rec("ch05", "F21", "temperature rise cancelling 300 pcm (K)", 0.003 / abs(alpha29), "{:.0f}")
rec("ch05", "F21", "Model A steady p for 300 pcm and 1.5 dollars (beta=0.0065)", (1 + 0.003 / (abs(alpha29) * A29), 1 + 1.5 * beta / (abs(alpha29) * A29)), "{:.3f}")
rec("ch05", "F22", "Model B: rise to prompt critical at 1.5 dollars (K)", 0.5 * beta / abs(alpha29), "{:.0f}")
# Six-group step response (Fig. 1 of the Chapter 5 guide)
def step_response(rho, times, b=b, lam=lam, Lam=Lam):
    G = len(b)
    A = np.zeros((G + 1, G + 1))
    A[0, 0] = (rho - b.sum()) / Lam
    A[0, 1:] = lam
    A[1:, 0] = b / Lam
    A[1:, 1:] = -np.diag(lam)
    y0 = np.concatenate([[1.0], b / (lam * Lam)])
    w, V = np.linalg.eig(A)
    c = np.linalg.solve(V, y0)
    return np.real(np.array([(V[0] * c * np.exp(w * t)).sum() for t in times]))
t_fig = np.concatenate([np.linspace(0, 0.05, 51), np.linspace(0.06, 2, 98), np.linspace(2.5, 100, 196)])
n_plus = step_response(0.1 * beta, t_fig)
n_minus = step_response(-0.1 * beta, t_fig)
rec("ch05", "F14", "six-group n/n0 at t=0.5 s and 100 s for +0.1 beta", (step_response(0.1 * beta, [0.5])[0], n_plus[-1]), "{:.3f}")
rec("ch05", "F14", "six-group n/n0 at t=0.5 s and 100 s for -0.1 beta", (step_response(-0.1 * beta, [0.5])[0], n_minus[-1]), "{:.3f}")

# ----------------------------------------------------------------------------
# Chapter 10
# ----------------------------------------------------------------------------
kPWR = 1.27 * 0.63 * 0.94 * 1.89 * 0.97
rec("ch10", "F3", "Table 4.2 PWR with P_NL=0.97: k, rho_ex", (kPWR, (kPWR - 1) / kPWR), "{:.4f}")
f_need = 0.94 / kPWR
Acon = 1 / f_need - 1 - 0.06 / 0.94
rec("ch10", "F3", "f needed, A_con/A_f, control share of thermal absorptions", (f_need, Acon, Acon / (1 + 0.06 / 0.94 + Acon)), "{:.4f}")
lam131 = math.log(2) / (8.02 * 86400)
lam137 = math.log(2) / (30.2 * 365.25 * 86400)
rec("ch10", "F5", "I-131: lambda (1/s), 5 half-lives (d)", (lam131, 5 * 8.02), "{:.3g}")
rec("ch10", "F5", "Cs-137: lambda t after 3 y; 1-exp(-x) over x", (lam137 * 3 * 365.25 * 86400, (1 - math.exp(-lam137 * 3 * 365.25 * 86400)) / (lam137 * 3 * 365.25 * 86400)), "{:.4f}")
gI, gX, gP = 0.0639, 0.00237, 0.01071
lamI, lamX, lamP = math.log(2) / (6.7 * 3600), math.log(2) / (9.2 * 3600), math.log(2) / (53 * 3600)
sX, sS = 2.65e6 * 1e-24, 41000e-24
rec("ch10", "F6", "lambda_I, lambda_X (1/s)", (lamI, lamX), "{:.3e}")
rec("ch10", "F6", "flux where sigma_X phi = lambda_X", lamX / sX, "{:.2e}", "1/cm2/s")
Sf22, phi22, Sa22 = 0.16, 2e14, 0.34
rec("ch10", "F6", "X_max = (gI+gX) Sigma_f/sigma_X for Sigma_f=0.16", (gI + gX) * Sf22 / sX, "{:.2e}", "1/cm3")
def xe_eq(phi, Sf=Sf22):
    I0 = gI * Sf * phi / lamI
    X0 = (gI + gX) * Sf * phi / (lamX + sX * phi)
    return I0, X0
for phi in (2e13, phi22):
    I0, X0 = xe_eq(phi)
    rec("ch10", "F7", f"phi={phi:.0e}: I_eq, X_eq (1/cm3), Sigma_aX (1/cm), worth -Sigma_aX/0.34", (I0, X0, sX * X0, -sX * X0 / Sa22), "{:.3g}")
rec("ch10", "F7", "worth limit at infinite flux", -(gI + gX) * Sf22 / Sa22, "{:.4f}")
rec("ch10", "F8", "flux above which xenon rises after shutdown", lamX * gX / (sX * gI), "{:.2e}", "1/cm2/s")
tpk = math.log(lamI / lamX) / (lamI - lamX)
rec("ch10", "F8", "high-flux peak time (s), (h)", (tpk, tpk / 3600), "{:.4g}")
def xe_after(t, phi, Sf=Sf22):
    I0, X0 = xe_eq(phi, Sf)
    return X0 * np.exp(-lamX * t) + lamI / (lamI - lamX) * I0 * (np.exp(-lamX * t) - np.exp(-lamI * t))
I0, X0 = xe_eq(phi22)
tmax = optimize.minimize_scalar(lambda t: -xe_after(t, phi22), bounds=(0, 1e5), method="bounded").x
rec("ch10", "F8", "phi=2e14: peak time (h), X_peak/X_eq, peak worth", (tmax / 3600, xe_after(tmax, phi22) / X0, -sX * xe_after(tmax, phi22) / Sa22), "{:.3g}")
reserve = 0.05
t1 = optimize.brentq(lambda t: sX * xe_after(t, phi22) / Sa22 - reserve, 0, tmax)
t2 = optimize.brentq(lambda t: sX * xe_after(t, phi22) / Sa22 - reserve, tmax, 1e6)
rec("ch10", "F8", "dead time for a 0.05 reserve: start, end (h), length (h)", (t1 / 3600, t2 / 3600, (t2 - t1) / 3600), "{:.3g}")
I0b, X0b = xe_eq(2e13)
tmaxb = optimize.minimize_scalar(lambda t: -xe_after(t, 2e13), bounds=(0, 1e5), method="bounded").x
rec("ch10", "F8", "phi=2e13: peak time (h), X_peak/X_eq", (tmaxb / 3600, xe_after(tmaxb, 2e13) / X0b), "{:.3g}")
rec("ch10", "F9", "lambda_P (1/s); S_eq = gP Sigma_f/sigma_S (1/cm3); Sigma_aS = gP Sigma_f; worth", (lamP, gP * Sf22 / sS, gP * Sf22, -gP * Sf22 / Sa22), "{:.3g}")
rec("ch10", "F9", "1/(sigma_S phi) at 2e14 (d); P_o/S_o = sigma_S phi/lambda_P at 2e14, 1.3e13", (1 / (sS * phi22) / 86400, sS * phi22 / lamP, sS * 1.3e13 / lamP), "{:.3g}")
rec("ch10", "F9", "Table 3.2 Sm-149 thermal average (b)", 61500, "{:.0f}")
# Depletion: Lesson 23 one-group data, 3% enrichment, phi = 2e14
sa25, sf25, sa28, sf28, sa49, sf49 = 57.20, 46.89, 1.02, 0.11, 195.10, 124.41
sg28 = sa28 - sf28
phi23 = 2e14
rec("ch10", "F10", "U-238 captured per year at 2e14 (sigma_a=1.02 b)", sa28 * 1e-24 * phi23 * 365.25 * 86400, "{:.4f}")
Phi_half = math.log(2) / (sa25 * 1e-24)
rec("ch10", "F11", "fluence for half the U-235 (1/cm2), time at 2e14 (s), (y)", (Phi_half, Phi_half / phi23, Phi_half / phi23 / (365.25 * 86400)), "{:.3g}")
rec("ch10", "F11", "N49(inf)/N28 = sg28/sa49; 1/(sa49 phi) (s), (y)", (sg28 / sa49, 1 / (sa49 * 1e-24 * phi23), 1 / (sa49 * 1e-24 * phi23) / (365.25 * 86400)), "{:.3g}")
e10 = 0.03
rec("ch10", "F11", "N49(inf)/N25(0) at 3%", sg28 / sa49 * (1 - e10) / e10, "{:.3f}")
N25_0, N28_0 = e10, 1 - e10
N25_h = 0.5 * N25_0
N49_h = sg28 / sa49 * N28_0 * (1 - math.exp(-sa49 * 1e-24 * Phi_half))
rec("ch10", "F12", "CR(0) at 3%", sg28 * N28_0 / (sa25 * N25_0), "{:.3f}")
rec("ch10", "F12", "half burned: N49/N_U, CR, Pu power fraction", (N49_h, sg28 * N28_0 / (sa25 * N25_h + sa49 * N49_h), sf49 * N49_h / (sf25 * N25_h + sf49 * N49_h)), "{:.3f}")
rec("ch10", "F12", "CR(0) at 4% (for comparison)", sg28 * 0.96 / (sa25 * 0.04), "{:.3f}")
# k(t) with Lesson 23 thermal data
NU23 = 10.4 * N0 / 270                     # 1e24/cm3
sa25T, sf25T, nu25, sa28T, sa49T, sf49T, nu49 = 297.40, 253.09, 2.43, 1.32, 1146.51, 732.22, 2.90
zeta, vmvf, p23, eps23, pnl23, Sam23 = 1.1, 1.0, 0.6, 1.3, 0.95, 0.007
def k23(n25, n49):
    num = nu25 * sf25T * n25 + nu49 * sf49T * n49
    den = sa25T * n25 + sa49T * n49 + sa28T * N28_0 * NU23 + zeta * vmvf * Sam23
    return num / den * eps23 * p23 * pnl23
k0 = k23(N25_0 * NU23, 0.0)
kh = k23(N25_h * NU23, N49_h * NU23)
rec("ch10", "F13", "N_U (1e24/cm3), N25(0), N28(0)", (NU23, N25_0 * NU23, N28_0 * NU23), "{:.4g}")
rec("ch10", "F13", "k(0), rho(0)", (k0, (k0 - 1) / k0), "{:.3f}")
rec("ch10", "F13", "k, rho at half U-235 (Pu, no FP)", (kh, (kh - 1) / kh), "{:.3f}")
rec("ch10", "F13", "k at half U-235 if Pu-239 ignored", k23(N25_h * NU23, 0.0), "{:.3f}")
# burnup to the half-burned point at constant flux
kappa = 3.2e-11
t_h = Phi_half / phi23
tt = np.linspace(0, t_h, 2001)
n25 = N25_0 * NU23 * 1e24 * np.exp(-sa25 * 1e-24 * phi23 * tt)
n49 = sg28 / sa49 * N28_0 * NU23 * 1e24 * (1 - np.exp(-sa49 * 1e-24 * phi23 * tt))
Pd = kappa * phi23 * 1e-24 * (sf25 * n25 + sf49 * n49)
Q = integrate.trapezoid(Pd, tt)
m0 = 10.4e-3 * 238 / 270                   # kg heavy metal per cm3
rec("ch10", "F13", "P''' at t=0 and at half-burned (W/cm3)", (Pd[0], Pd[-1]), "{:.0f}")
rec("ch10", "F13", "energy per cm3 (J), heavy-metal mass (kg/cm3), burnup (MWd/kg)", (Q, m0, Q / m0 / 8.64e10), "{:.3g}")
rec("ch10", "F14", "1 full-power day at 100 W/cm3, UO2 10.4 g/cm3: MWd/kg; 3 y", (100 * 86400 / m0 / 8.64e10, 3 * 365.25 * 100 * 86400 / m0 / 8.64e10), "{:.3g}")
fima = 8.64e10 / kappa / (6.022e26 / 238)
rec("ch10", "F14", "fissions per kg per MWd/kg; % of heavy atoms per MWd/kg; at 50 MWd/kg", (8.64e10 / kappa, 100 * fima, 50 * 100 * fima), "{:.3g}")
phiT = 4e13
for name, s in (("B-10", 3409.0), ("Gd-157", 254000.0), ("U-235", 591.0)):
    rec("ch10", "F15", f"{name}: sigma phi_T (1/s), half-life in flux (d)", (s * 1e-24 * phiT, math.log(2) / (s * 1e-24 * phiT) / 86400), "{:.3g}")
Rfis = 3000e6 / 3.1e-11
rec("ch10", "F16", "fission rate at 3000 MW (1/s)", Rfis, "{:.3g}")
rec("ch10", "F16", "I-131 saturation activity (Bq), (Ci)", (0.029 * Rfis, 0.029 * Rfis / 3.7e10), "{:.3g}")
N137 = 0.063 * Rfis * 3 * 365.25 * 86400
rec("ch10", "F16", "Cs-137 after 3 y: atoms, kg, Bq, Ci", (N137, N137 * 137 / 6.022e23 / 1e3, lam137 * N137, lam137 * N137 / 3.7e10), "{:.3g}")
rho0, aL, rhoL = 0.25, 0.15 / 35, 0.05
rec("ch10", "F18", "LRM slope a (per MWd/kg)", aL, "{:.5f}")
for N in (1, 2, 3, 4):
    Bc = 2 * (rho0 - rhoL) / (aL * (N + 1))
    rec("ch10", "F18", f"N={N}: B_c, B_d (MWd/kg)", (Bc, N * Bc), "{:.1f}")
rec("ch10", "F18", "limit N->inf: B_d (MWd/kg)", 2 * (rho0 - rhoL) / aL, "{:.1f}")
# Data for the figures
t_xe = np.linspace(0, 72 * 3600, 289)
xe_lo = xe_after(t_xe, 2e13) / xe_eq(2e13)[1]
xe_hi = xe_after(t_xe, phi22) / X0
sm_hi = 1 + (sS * phi22 / lamP) * (1 - np.exp(-lamP * t_xe))
sm_lo = 1 + (sS * 2e13 / lamP) * (1 - np.exp(-lamP * t_xe))
Phi_fig = np.linspace(0, 4e22, 201)
n25_fig = np.exp(-sa25 * 1e-24 * Phi_fig)
n49_fig = sg28 / sa49 * (N28_0 / N25_0) * (1 - np.exp(-sa49 * 1e-24 * Phi_fig))

# ----------------------------------------------------------------------------
# Output
# ----------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="refresh figures/data/*.dat tables")
    args = ap.parse_args()
    w = max(len(r[2]) for r in rows)
    for g, f, label, text, unit in rows:
        print(f"{g} {f:>4}  {label:<{w}}  {text} {unit}")
    if args.write:
        os.makedirs(DATA, exist_ok=True)
        x = np.linspace(0.0, 10.0, 401)
        with open(os.path.join(DATA, "bessel.dat"), "w") as fh:
            fh.write("x J0 J1 Y0\n")
            for xi in x:
                y0 = special.y0(xi) if xi > 0 else float("nan")
                fh.write(f"{xi:.4f} {special.j0(xi):.6f} {special.j1(xi):.6f} {y0:.6f}\n")
        print(f"wrote {os.path.join(DATA, 'bessel.dat')}")
        with open(os.path.join(DATA, "kinetics_step.dat"), "w") as fh:
            fh.write("t nplus nminus\n")
            for ti, a, c in zip(t_fig, n_plus, n_minus):
                fh.write(f"{ti:.4f} {a:.6f} {c:.6f}\n")
        with open(os.path.join(DATA, "xenon_shutdown.dat"), "w") as fh:
            fh.write("th xelo xehi smlo smhi\n")
            for ti, a, c, d, e in zip(t_xe / 3600, xe_lo, xe_hi, sm_lo, sm_hi):
                fh.write(f"{ti:.3f} {a:.5f} {c:.5f} {d:.5f} {e:.5f}\n")
        with open(os.path.join(DATA, "depletion.dat"), "w") as fh:
            fh.write("fluence n25 n49\n")
            for ti, a, c in zip(Phi_fig / 1e21, n25_fig, n49_fig):
                fh.write(f"{ti:.3f} {a:.6f} {c:.6f}\n")
        print(f"wrote kinetics_step.dat, xenon_shutdown.dat, depletion.dat in {DATA}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
