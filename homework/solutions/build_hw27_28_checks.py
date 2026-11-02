#!/usr/bin/env python3
"""Verify only HW27/HW28 source-matched solutions; build their private assets.

Source: ne630_problems/lesson_27/{statement.tex,HW27_Sol.ipynb} and
lesson_28/{statement.tex,HW28_sol.ipynb}, source HEAD 4f375f82.
No dependency on the course ne630_kinetics module or lesson notebooks.
"""
from pathlib import Path
import json
import hashlib
import numpy as np
from scipy.linalg import expm
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'data' / 'hw27_28'
OUT.mkdir(parents=True, exist_ok=True)
(ROOT / 'figures').mkdir(exist_ok=True)
HALF = np.array([56, 23, 6.2, 2.3, .61, .23])
LAM = np.log(2) / HALF
BG = np.array([.00021, .00142, .00128, .00257, .00075, .00027])
GEN = 50e-6

def matrix(rho, bg=BG, lam=LAM, gen=GEN):
    m = np.zeros((1+len(bg), 1+len(bg)))
    m[0, 0] = (rho - sum(bg)) / gen
    m[0, 1:] = lam
    m[1:, 0] = bg / gen
    m[1:, 1:] = -np.diag(lam)
    return m

beta_end = (.7*2.43*.0065 + .3*2.90*.00210)/(.7*2.43+.3*2.90)
prompt_hashes = {f'HW{n}.md': hashlib.sha256((ROOT.parent / 'markdown' / f'HW{n}.md').read_bytes()).hexdigest() for n in [27, 28]}
report = {'authoritative_markdown_sha256': prompt_hashes,
          'hw27_beta_end': beta_end,
          'hw27_beta_change_percent': 100*(beta_end/.0065-1)}
y0 = np.r_[1e6, BG/(LAM*GEN)*1e6]
np.testing.assert_allclose(matrix(0) @ y0, 0, atol=1e-7)
report['hw27_initial_precursors'] = y0[1:].tolist()
fig, ax = plt.subplots(figsize=(7, 3.5))
for sign, style in [(1, '-'), (-1, '--')]:
    current = y0.copy()
    all_t, all_y = [], []
    endpoints = {}
    for start, stop, rho in [(0, 1, 0), (1, 6, sign*.25*sum(BG)), (6, 10, 0)]:
        m = matrix(rho)
        times = np.linspace(start, stop, 251)
        exact = np.array([expm(m*(t-start))@current for t in times])
        numerical = solve_ivp(lambda t,y: m@y, (start,stop), current,
                              method='Radau', t_eval=times, rtol=2e-10, atol=1e-4)
        assert numerical.success
        np.testing.assert_allclose(numerical.y.T, exact, rtol=2e-8, atol=.002)
        assert np.all(exact > 0)
        all_t.extend(times); all_y.extend(exact)
        current = exact[-1]
        endpoints[str(stop)] = current[0]
    values = np.array(all_y)
    ax.plot(all_t, values[:,0], 'k'+style, label=f'{sign*.25:+.2f} dollars')
    np.savetxt(OUT/f'hw27_{"up" if sign>0 else "down"}.csv',
               np.column_stack([all_t, values]), delimiter=',',
               header='t_s,n_cm-3,c1,c2,c3,c4,c5,c6', comments='')
    report[f'hw27_{"up" if sign>0 else "down"}_n'] = endpoints
ax.set(xlabel='Time (s)', ylabel=r'Neutron density (cm$^{-3}$)')
ax.legend(); ax.grid(alpha=.2); fig.tight_layout()
fig.savefig(ROOT/'figures'/'hw27_neutron_density.png', dpi=180)
plt.close(fig)

report['hw28_periods'] = {}
for isotope, bg in [('U-235',BG), ('Pu-239',np.array([.00007,.00063,.00044,.00069,.00018,.00009])),
                    ('U-233',np.array([.00023,.00078,.00064,.00074,.00014,.00008]))]:
    effective = sum(bg)/sum(bg/LAM)
    period = 100/effective
    report['hw28_periods'][isotope] = {'lambda_s-1':effective, 'period_magnitude_s':period}

report['hw28_step'] = {}
for sign in [1,-1]:
    beta, lam, gen, n0 = .0065, .08, 5e-5, 1e6
    rho = sign*.2*beta
    c0 = beta*n0/(lam*gen)
    B = lam-(rho-beta)/gen
    C = -lam*rho/gen
    w2 = (-B-np.sqrt(B*B-4*C))/2
    w1 = C/w2  # avoid cancellation in the slow eigenvalue
    a1 = n0*(rho/gen-w2)/(w1-w2); a2 = n0-a1
    b1 = -c0*w2/(w1-w2); b2 = c0-b1
    times = np.array([0.,.1,10.])
    analytical = np.array([[a1*np.exp(w1*t)+a2*np.exp(w2*t),
                            b1*np.exp(w1*t)+b2*np.exp(w2*t)] for t in times])
    m = matrix(rho, np.array([beta]),np.array([lam]),gen)
    exact = np.array([expm(m*t)@np.array([n0,c0]) for t in times])
    numerical = solve_ivp(lambda t,y:m@y,(0,10),[n0,c0],method='Radau',
                          t_eval=times,rtol=2e-10,atol=1e-4)
    assert numerical.success
    np.testing.assert_allclose(analytical,exact,rtol=2e-11)
    np.testing.assert_allclose(analytical,numerical.y.T,rtol=2e-9)
    np.testing.assert_allclose(m@np.array([n0,c0]), [rho/gen*n0,0],atol=1e-7)
    report['hw28_step'][str(sign*.2)] = dict(B=B,C=C,w1=w1,w2=w2,a1=a1,a2=a2,
                                           b1=b1,b2=b2,times=times.tolist(),values=analytical.tolist())
# Current Problem 3 is no longer labeled bonus; its conditions still do not imply separated roots.
beta, lam, gen, rho = .0065, .08, 5e-5, .0065-1e-4
delta = beta-rho
report['hw28_problem3_caveat'] = {
    'beta_over_lambda_Lambda': beta/(lam*gen),
    'abs_beta_minus_rho_over_lambda_Lambda':delta/(lam*gen),
    'root_separation_parameter':4*lam*abs(rho)*gen/delta**2,
    'note':'Current Problem 3 retains insufficient hypotheses near prompt criticality. No worked source solution; retain authoritative prompt and flag privately for instructor review.'}
# Asymptotic counterexample: both supplied ratios diverge, but roots do not separate.
family = []
for epsilon in [1e-4, 1e-8, 1e-12]:
    delta = beta*epsilon**.75
    gen = beta*epsilon/lam
    rho = beta-delta
    separation = 4*lam*rho*gen/delta**2
    actual_rate = max(np.linalg.eigvals(matrix(rho, np.array([beta]), np.array([lam]), gen)))
    claimed_rate = lam*rho/delta
    assert beta/(lam*gen) >= 1e4-1
    assert delta/(lam*gen) >= 10-1e-9
    assert separation > 100
    assert claimed_rate/actual_rate > 5
    family.append(dict(epsilon=epsilon, beta_over_lambda_Lambda=beta/(lam*gen),
                       delta_over_lambda_Lambda=delta/(lam*gen),
                       root_separation_parameter=separation,
                       exact_positive_rate=float(actual_rate),
                       claimed_positive_rate=claimed_rate))
report['hw28_problem3_caveat']['asymptotic_counterexample'] = family
assert prompt_hashes == {f'HW{n}.md': hashlib.sha256((ROOT.parent / 'markdown' / f'HW{n}.md').read_bytes()).hexdigest() for n in [27, 28]}
(OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
print('PASS: equilibrium; piecewise matrix exponential vs Radau; analytic two-mode vs expm and Radau.')
