"""One-group, source-free point kinetics with fuel-temperature feedback."""
import numpy as np
from scipy.integrate import solve_ivp

beta, Lambda = 0.0065, 1e-4            # Lambda in s
lam = np.log(2) / 5.0                  # 1/s
alpha = -3e-5                          # 1/K
A, B = 100.0, 240.0                    # K, K/s
n0 = 1e9                               # 1/cm^3
y0 = [n0, beta*n0/(lam*Lambda), 0.0]  # n, C, theta

def f(t, y, rho_ext, model):
    n, C, theta = y
    rho = rho_ext + alpha*theta
    dn = (rho - beta)*n/Lambda + lam*C
    dC = beta*n/Lambda - lam*C
    if model == "A":
        dT = A*dn/n0
    elif model == "B":
        dT = B*n/n0
    elif model == "fixed":
        dT = 0.0
    else:
        raise ValueError("Use A, B, or fixed")
    return dn, dC, dT

def solve(rho_ext, times, model, start=y0):
    sol = solve_ivp(f, (times[0], times[-1]), start,
                    args=(rho_ext, model), t_eval=times,
                    method="LSODA", rtol=1e-8, atol=1e-9)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.y

# A 300 pcm insertion is withdrawn at 5 s.
if __name__ == "__main__":
    import matplotlib.pyplot as plt

    t1 = np.linspace(0, 5, 1001)
    t2 = np.linspace(5, 10, 1001)
    tp = np.linspace(0, 0.20, 501)
    fig, axes = plt.subplots(2, 2, figsize=(10, 7), layout="constrained")
    styles = {"fixed": ("0.3", "--"), "A": ("#512888", "-"),
              "B": ("#ba6710", "-.")}

    for model, (color, style) in styles.items():
        one = solve(0.003, t1, model)
        two = solve(0.0, t2, model, one[:, -1])
        pulse = solve(1.5*beta, tp, model)
        t = np.r_[t1, t2]
        state = np.hstack((one, two))
        inserted = np.r_[np.full_like(t1, 0.003), np.zeros_like(t2)]
        values = (state[0]/n0, (inserted + alpha*state[2])/beta,
                  pulse[0]/n0, (1.5*beta + alpha*pulse[2])/beta)
        for ax, x, y in zip(axes.flat, (t, t, 1000*tp, 1000*tp), values):
            ax.plot(x, y, color=color, ls=style, label=model, lw=2)

    for ax in axes[0]:
        ax.set_xlabel("Time (s)")
        ax.axvline(5, color="0.75", lw=0.8, zorder=0)
    for ax in axes[1]:
        ax.set_xlabel("Time (ms)")
    for ax in axes[:, 0]:
        ax.set_ylabel("Relative neutron density, n/n0")
    for ax in axes[:, 1]:
        ax.set_ylabel("Net reactivity, rho/beta")
    axes[1, 0].set_ylim(0, 15)
    axes[1, 1].axhline(1, color="0.65", lw=0.8, zorder=0)
    axes[0, 0].legend()
    plt.show()
