# Lesson 27

## Learning Objectives

### Macro Objectives

Students will be able to write down, to explain each term of a system of, and to solve numerically the system of first-order, ordinary differential 
equations that model the neutron density and the densities of delayed neutron precursors in time.

### Micro Objectives

 - Explain how neutrons can be produced relatively long after a fission has occured.
 - Show how a delayed neutron precursor concentration $C_i(t)$ is related to the physical concentration of a fission product and its daughters. 
 - Provide representative values for the delayed neutron fraction of different fissile nuclides.
 - Show that, in the one-group approximation, the inclusion of delayed-neutron precursors does not impact a steady-state system.
 - Quantify how delayed neutrons impact the neutron lifetime.
 - Use `odeint` or similar tools to solve numerically
   systems of first-order differential equations.

## Key Terms


 - delayed neutron precursor concentration $C_i$
 - delayed neutron fraction $\beta_i$
 - precursor group (indexed by the $i$ in $C_i$ and $\beta_i$)
 - average delayed neutron lifetime $l_d$
 - average neutron lifetime $\bar{l}$


## Before Lecture

  - Read Section 5.4.
  - Read [these notes](https://robertsj.github.io/me400_notes/lectures/Systems_Of_IVPs.html#SciPy's-odeint) on use of `odeint` for solving systems of initial-value problems.

## After Lecture

### Homework

  - [27.1] Problem 5.2 from the text.
  - [27.2] Like Problem 5.16 from the text, but set
    $\rho(t) = 0$ for $0 \leq t < 1$, 
    $\rho(t) \pm 0.25\beta$ (i.e., 0.25 dollars) for $1 \leq t < 6$, and $\rho(t) = 0$ for 
    $6 \leq t \leq 10$ s.  By adding a second of $\rho(t) = 0$ at the beginning, we can verify that the
    system remains in steady state.  Remember, you need
    to find the appropriate precursor concentrations
    for steady state to use for initial conditions.
    You may assume that $n(0) = 1$ for simplicity.
