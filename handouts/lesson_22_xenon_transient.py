 import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def dNdt(t, N, phi, sig_a_Xe, Sigma_f):
  gamma_I, gamma_Xe = 0.0639, 0.00237
  lambda_I, lambda_Xe = 0.693/(6.7*3600), 0.693/(9.2*3600)
  sig_a_Xe = sig_a_Xe*1e-24
  N_I, N_Xe = N
  dN_Idt = -lambda_I*N_I + gamma_I*Sigma_f*phi(t)
  dN_Xdt = -lambda_Xe*N_Xe + lambda_I*N_I + \
            (gamma_Xe*Sigma_f-sig_a_Xe*N_Xe)*phi(t)
  return dN_Idt, dN_Xdt

hour=3600; day = 24*hour;

flux = lambda t: 2e14 if t < 3*day else 0.0

result = solve_ivp(fun=dNdt, t_span=(0.0, 5*day), 
  y0=(0, 0), args=(flux, 2.3e6, 0.16), max_step=1*hour)
t = result.t/3600; N_I, N_Xe = result.y

orange, purple = "#CA7C1B", "#512888"
plt.plot(t, N_I, color=orange, lw=1, label="I")
plt.plot(t, N_Xe, color=purple, lw=1, ls="-.", label="Xe")
plt.xlabel("$t$ (h)"); plt.ylabel("N(t) (cm$^{-3}$)")
plt.legend()
plt.show()