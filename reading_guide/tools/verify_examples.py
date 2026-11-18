#!/usr/bin/env python
"""Recompute every number quoted in the Chapter 1-4, 6, and 7 programmed reading guides.

Run from anywhere:
    python tools/verify_examples.py            # print the table of values
    python tools/verify_examples.py --write    # also refresh figures/data/*.dat

Only NumPy and SciPy are required.  Each printed line is labelled with the guide
(ch01-ch04, ch06, or ch07) and the frame that quotes it, so a reader can check a single value.
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
    return 0


if __name__ == "__main__":
    sys.exit(main())
