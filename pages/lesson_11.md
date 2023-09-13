# Lesson 11

## Learning Objectives

Students will be able to approximate the flux distribution of thermal neutrons in a thermal-spectrum reactor.

### Macro Objectives

Students will be able to approximate the flux distribution of thermal neutrons in a thermal-spectrum reactor.


### Micro Objectives

 - Write down the balance equation for thermal neutrons of energy below $E_{th} = 1$ eV.
 - Explain the idea of detailed balance.
 - State the Maxwell-Boltzmann distribution, i.e., $\phi_{MB}(E) \propto E e^{-E/kT}$.
 - Describe the impact of absorption and temperature on the thermal spectrum.
 - Describe why the free-gas approximation may be unsuitable for real materials.

## Key Terms

 - (principle of) detailed balance
 - upscatter
 - thermal equilibrium
 - free-gas approximation
 - spectral hardening
 

## Before Lecture

  - Read section 3.4, focusing on the last two subsections.

## After Lecture

### Homework

 - For this problem, you will define and plot a complete spectrum for an infinite, homogeneous system 
 using the simple approximations we've examined.  Let 
 
$$
\phi_{\infty}(E) =
  \begin{cases}
    \frac{\chi(E)}{\Sigma_t(E)}      & \quad  10^{5} < E < 10^7 (eV) \\
    \frac{C_I}{E}                   & \quad  1 < E  \leq 10^{5} \\
    C_T E e^{-E/kT}                 & \quad  10^{-3} \leq 1 \, , \\
  \end{cases}
$$

where $C_I$ and $C_T$ are constants,  $k = 8.617 \cdot 10^{-5}$ [eV/K], and T = 300 K.
Because our fast spectrum ignores scattering, *all* neutrons born 
from fission must cross the energy $E=0.1$ MeV barrier.  You can use this fact to define $C_I$.
To define $C_T$, we shall assume that the half of the neutron flux is thermal (i.e., $E < 1$ eV).
This 1-to-1 ratio of the integrated thermal and non-thermal fluxes is reasonably 
typical of a thermal-spectrum reactor.  Is the flux continuous at 1 eV?


