"""NE 630 - Point kinetics solver.

Solves Lewis 5.47 and 5.48 with no external source:

    dn/dt   = ((rho(t) - beta)/Lambda) n(t) + sum_i lambda_i C_i(t)
    dC_i/dt = -lambda_i C_i(t) + (beta_i/Lambda) n(t)

Six-group U-235 data are from Table 5.1.
"""

import numpy as np
from scipy.integrate import solve_ivp

_betas = np.array([0.00021, 0.00142, 0.00128, 0.00257, 0.00075, 0.00027])
_thalfs = np.array([56, 23, 6.2, 2.3, 0.61, 0.23])
_lambdas = np.log(2)/_thalfs
_Lambda = 5e-5


def f(t, y, rho, betas, lambdas, Lambda):
    n = y[0]           # Unpack the unknowns so that
    C = y[1:]          #   the equations are clearer.
    beta = sum(betas)  # Total delayed neutron fraction
    dndt = ((rho(t)-beta)/Lambda)*n + sum(C*lambdas)
    dCdt = -C*lambdas + betas*n/Lambda
    dydt = np.zeros(len(y))
    dydt[0] = dndt     # Collect the derivatives
    dydt[1:] = dCdt    #   into one array that we return
    return dydt


def solve(rho, times, n0, betas, lambdas, Lambda):
    """Return n(t) and C_i(t), starting critical at n0.

    rho is a function of t, and C[i] is group i+1.
    """
    y0 = np.zeros(len(betas) + 1)
    y0[0] = n0
    y0[1:] = betas * n0 / (lambdas * Lambda)
    # Limit the step to the spacing of times so that the
    # solver cannot step right over a change in rho.
    hmax = np.max(np.diff(times))
    sol = solve_ivp(f, (times[0], times[-1]), y0,
                    args=(rho, betas, lambdas, Lambda),
                    t_eval=times, max_step=hmax,
                    method="LSODA", rtol=1e-8)
    return sol.y[0], sol.y[1:]


if __name__ == "__main__":
    # Lesson 27, Example 4: rho = 0.001 for 1 <= t < 2 s.
    import matplotlib.pyplot as plt

    def rho(t):
        if 1 <= t < 2:
            return 0.001
        return 0.0

    times = np.linspace(0, 10, 10000)
    n, C = solve(rho, times, n0=1e8, betas=_betas, lambdas=_lambdas, Lambda=_Lambda)
    fig, ax1 = plt.subplots(layout="constrained")
    ax1.plot(times, n, "k", label="$n(t)$")
    ax1.set_xlabel("$t$ [s]")
    ax1.set_ylabel("$n(t)$")
    ax2 = ax1.twinx()              # Second y axis for the precursors
    for i in range(6):
        ax2.plot(times, C[i], "--", label=f"$C_{{{i+1}}}(t)$")
    ax2.set_ylabel("$C_i(t)$")
    ax2.set_yscale("log")
    fig.legend(loc="outside right upper")
    plt.show()
