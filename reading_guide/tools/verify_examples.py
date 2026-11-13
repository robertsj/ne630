#!/usr/bin/env python
"""Recompute every number quoted in the Chapter 6 and 7 programmed reading guides.

Run from anywhere:
    python tools/verify_examples.py            # print the table of values
    python tools/verify_examples.py --write    # also refresh figures/data/*.dat

Only NumPy and SciPy are required.  Each printed line is labelled with the guide
(ch06 or ch07) and the frame that quotes it, so a reader can check a single value.
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
