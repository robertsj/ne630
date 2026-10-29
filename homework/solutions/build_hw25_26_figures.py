#!/usr/bin/env python3
"""Verify HW25/26 numbers and regenerate the instructor-only HW26 plots.

Legacy inputs: ne630_problems/lesson_25 and lesson_26, commit 9c3dc61.
Uses the stated downscatter cross section 0.0427 cm^-1 consistently.
The accelerator example is new, hypothetical Fall 2026 material.
"""

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


ROOT = Path(__file__).resolve().parent
PURPLE = "#512888"
ORANGE = "#CA7C1B"


def checked_close(actual, expected, **kwargs):
    np.testing.assert_allclose(actual, expected, rtol=2e-9, atol=1e-10, **kwargs)


def main():
    output = ROOT / "figures"
    output.mkdir(exist_ok=True)
    v_fe = 2.2e5 * np.sqrt(1e6 / 0.0253)
    batches = np.arange(1, 6)
    cycle = 2 * (0.243 - 0.05) / (0.00664 * (batches + 1))
    # End-of-cycle reactivity, using all N batch burnups directly.
    for n, increment in zip(batches, cycle):
        checked_close(np.mean(0.243 - 0.00664 * increment * np.arange(1, n + 1)) - 0.05, 0)

    period = 10 / np.log(3)
    k_step = 1 + 0.002 / period
    checked_close(np.exp((k_step - 1) * 10 / 0.002), 3)

    absorption = np.array([2.04e-3 + 2.96e-4, 1.91e-2 + 1.38e-2])
    production = np.array([7.38e-4, 3.36e-2])
    down = 4.27e-2
    speeds = np.array([1e8, 2.2e5])  # cm/s
    shape = np.array([absorption[1] / down, 1.0])
    weights = shape / shape.sum()
    sigma_a = absorption @ weights
    nu_sigma_f = production @ weights
    speed = 1 / np.sum(weights / speeds)
    lifetime = 1 / (sigma_a * speed)
    multiplication = nu_sigma_f / sigma_a
    reactivity = (multiplication - 1) / multiplication
    tau = lifetime / (1 - multiplication)
    source = 100.0  # neutrons/cm^3/s
    steady_absorption = source / (1 - multiplication)

    # Independent steady two-group solve, with fast-only production/source.
    matrix = np.array([[absorption[0] + down - production[0], -production[1]],
                       [-down, absorption[1]]])
    flux = np.linalg.solve(matrix, np.array([source, 0.0]))
    checked_close(absorption @ flux, steady_absorption)
    two_group_k = (production[0] + production[1] * down / absorption[1]) / (absorption[0] + down)
    checked_close(two_group_k, multiplication)

    times = np.linspace(0, 0.1, 501)
    density = source * tau * (-np.expm1(-times / tau))
    numeric = solve_ivp(lambda t, y: [source - y[0] / tau], (0, 0.1), [0.0],
                        t_eval=times, rtol=1e-11, atol=1e-13)
    assert numeric.success
    checked_close(numeric.y[0], density)
    rate = sigma_a * speed * density
    fig, ax = plt.subplots(figsize=(6.4, 3.3))
    ax.plot(times, rate, color=PURPLE, label="One-group transient")
    ax.axhline(steady_absorption, color=ORANGE, ls="--", label="Two-group steady balance")
    ax.set(xlabel="Time (s)", ylabel=r"Absorption rate (cm$^{-3}$ s$^{-1}$)", xlim=(0, .1), ylim=(0, 7000))
    ax.grid(color="0.9")
    ax.legend(loc="lower right")
    fig.tight_layout()
    fig.savefig(output / "hw26_absorption_rate.png", dpi=180)
    plt.close(fig)

    charge = 1.602176634e-19
    current = 10e-3
    yield_per_proton = 20.0
    ton, cycle_time = 1e-3, 10e-3
    duty = ton / cycle_time
    k, ell, nu = 0.95, 1e-4, 2.5
    ef = 200e6 * charge
    beam_energy = 1e9 * charge
    source_on = yield_per_proton * current / charge
    source_avg = duty * source_on
    pulse_tau = ell / (1 - k)
    mean_n = pulse_tau * source_avg
    fissions_avg = k * mean_n / (nu * ell)
    thermal_avg = ef * fissions_avg
    electrical_avg = duty * 25e6
    beam_on = current / charge * beam_energy
    # Exact periodic pulse endpoints, retaining the off-time neutron tail.
    a = np.exp(-ton / pulse_tau)
    b = np.exp(-(cycle_time - ton) / pulse_tau)
    saturated = source_on * pulse_tau
    n_max = saturated * (1 - a) / (1 - a * b)
    n_min = b * n_max
    checked_close(saturated + (n_min - saturated) * a, n_max)

    # Independent dimensionless ODE integration, accumulating integral x du.
    on = solve_ivp(lambda u, y: [1 - y[0], y[0]], (0, ton / pulse_tau),
                   [n_min / saturated, 0], rtol=1e-12, atol=1e-14)
    off = solve_ivp(lambda u, y: [-y[0], y[0]], (ton / pulse_tau, cycle_time / pulse_tau),
                    on.y[:, -1], rtol=1e-12, atol=1e-14)
    assert on.success and off.success
    checked_close(off.y[0, -1] * saturated, n_min)
    integrated_n = off.y[1, -1] * saturated * pulse_tau
    checked_close(integrated_n / cycle_time, mean_n)
    checked_close(thermal_avg / 1e6, 30.4)
    checked_close(ef * k / (nu * ell) * integrated_n, thermal_avg * cycle_time)

    t = np.unique(np.r_[np.linspace(0, cycle_time, 1001), ton])
    n = np.where(t <= ton, saturated + (n_min - saturated) * np.exp(-t / pulse_tau),
                 n_max * np.exp(-(t - ton) / pulse_tau))
    fig, ax = plt.subplots(figsize=(6.4, 3.3))
    ax.axvspan(0, ton * 1e3, color=ORANGE, alpha=.18, label="Beam on")
    ax.plot(t * 1e3, ef * k * n / (nu * ell) / 1e6, color=PURPLE, label="Periodic fission power")
    ax.axhline(thermal_avg / 1e6, color=ORANGE, ls="--", label="Cycle average")
    ax.set(xlabel="Time within one cycle (ms)", ylabel="Fission thermal power (MW)", xlim=(0, 10), ylim=(0, None))
    ax.grid(color="0.9")
    ax.legend(loc="upper right")
    fig.tight_layout()
    fig.savefig(output / "hw26_pulse_power.png", dpi=180)
    plt.close(fig)

    results = {
        "hw25": {"graphite_lifetime_s": 1 / (2.2e5 * .273e-3),
                  "iron_speed_cm_s": float(v_fe), "iron_lifetime_s": 1 / (v_fe * .738e-3),
                  "cycle_burnup_MWd_kg": cycle.tolist(), "discharge_burnup_MWd_kg": (batches * cycle).tolist(),
                  "limiting_discharge_burnup_MWd_kg": 2 * (.243 - .05) / .00664},
        "hw26_p1": {"period_s": float(period), "k": float(k_step), "rho": float((k_step - 1) / k_step)},
        "hw26_p2": {"flux_ratio": float(shape[0]), "absorption_cm_inverse": float(sigma_a),
                     "production_cm_inverse": float(nu_sigma_f), "speed_cm_s": float(speed),
                     "lifetime_s": float(lifetime), "k": float(multiplication), "rho": float(reactivity),
                     "relaxation_s": float(tau), "density_ss_cm_inverse3": float(source * tau),
                     "absorption_ss_cm_inverse3_s_inverse": float(steady_absorption),
                     "absorption_at_01s": float(rate[-1]), "steady_two_group_fluxes": flux.tolist()},
        "hw26_p3": {"source_on_s_inverse": source_on, "source_avg_s_inverse": source_avg,
                     "mean_neutrons": mean_n, "mean_fissions_s_inverse": fissions_avg,
                     "mean_thermal_MW": thermal_avg / 1e6, "thermal_energy_cycle_MJ": thermal_avg * cycle_time / 1e6,
                     "beam_on_MW": beam_on / 1e6, "mean_beam_MW": duty * beam_on / 1e6,
                     "mean_electric_MW": electrical_avg / 1e6, "thermal_to_electric_ratio": thermal_avg / electrical_avg,
                     "pulse_start_neutrons": float(n_min), "pulse_end_neutrons": float(n_max)},
    }
    print(json.dumps(results, indent=2))
    print("PASS: batch criticality, source-free growth, steady two-group balance, transient ODE, and periodic-cycle integration.")


if __name__ == "__main__":
    main()
