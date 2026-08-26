# Draft Learning Objectives

> Source note: Lessons 1--29 and 31--38 are transcribed from their Markdown files. Because `pages/lesson_30.md` is absent, Lesson 30 is transcribed from the objective content in `pages/lesson_30.html`.

## Lesson 1

**Macro objective**

Determine and quantify the reactants, products, and energy inputs/outputs of nuclear reactions.

**Micro objectives**

- Compare the energy densities of different reaction types.
- Compute the total energy of a particle of (rest) mass $m_0$ with a speed $v$.
- Explain the nomenclature ${}^A_Z X$.
- Provide an example of a binary nuclear reaction of the form $A(B,C)D$.
- Compute the Q value for $A(B,C)D$.
- Provide an example of radioactive decay of the form $A \to B + C$.
- Demonstrate that the kinematics of neutrons with energies below about 10 MeV can be well approximated classically.
- Compute the mass defect of ${}^A_Z X$.
- Compute the binding energy per nucleon of ${}^A_Z X$.
- Explain how Q values relate to decay.

## Lesson 2

**Macro objective**

Characterize the neutron population and energy produced as a function of time in terms of the neutron lifetime, the energy released from fission, and the multiplication factor $k$.

**Micro objectives**

- Provide an example fission reaction and compute its Q value.
- List three forms of "nuclear" power.
- List the type and fraction of particles emitted from fission.
- Construct a mathematical model for the multiplication of neutrons.
- Explain criticality, subcriticality, and supercriticality.
- Estimate the heat generation rate of spent nuclear fuel.
- Compare fissile and fertile materials.
- List the major fissile and fertile nuclides.
- Explain why fission products are neutron rich.
- Describe the trend of stable nuclei as functions of $Z$ and $A$.

## Lesson 3

**Macro objective**

Determine the amounts of a radioactive species and its daughters at any point in time given initial amounts.

**Micro objectives**

- Convert $t_{1/2}$ to $\bar{t}$ and $\lambda$.
- Solve $N' = -\lambda N(t)$, $N(0)$ given.
- Solve $N' = -\lambda N(t) + R(t)$, $N(0)$ and $R(t)$ given.
- Convert between Ci, Bq, kg, and number (or moles).
- Describe *saturation activity* and how long it takes to achieve.
- Solve the system $N_i' = -\lambda_i N_i(t) + \lambda_{i-1} N_{i-1} + R_i(t)$ for $i = 0, 1, \ldots$, with $N_i(0)$ and $R_i(t)$ given, $\lambda_{-1} = 0$.
- Describe secular equilibrium.

## Lesson 4

**Macro objective**

Characterize the attenuation of neutrons in a parallel beam or emitted from a point source as a function of distance and material composition.

**Micro objectives**

- Describe the motion (or "transport") of neutrons through space.
- Illustrate how the microscopic cross sections of individual nuclei manifest at the macroscopic scale through attenuation.
- Explain the difference between material and geometric attenuation.
- Compute the number density of any nuclide in a chemical composition.
- Define the nuclide composition of uranium mixtures given enrichment.

## Lesson 5

**Macro objective**

For a neutron of energy $E$, determine the interactions it can undergo and compute the probability that it undergoes a particular reaction.

**Micro objectives**

- Find $\sigma_x(E)$ (i.e., the microscopic cross section for a reaction $x$) from an appropriate tabulation
- Explain how the kinetic energies of an incident neutron and the target nucleus impact $\sigma_x(E)$
- Plot tabulated cross sections over appropriate energy ranges
- For a given neutron energy $E$ and nuclide composition, determine the microscopic cross section for each nuclide and reaction.
- For a given neutron energy $E$ and nuclide composition, determine the macroscopic cross section for each reaction.

## Lesson 6

**Macro objective**

Describe the range of neutron energies typical of nuclear reactors and the likely interactions neutrons undergo throughout that range.

**Micro objectives**

- Approximate $\sigma_x(E)$ directly from resonance data
- Specify the range of energies over which neutron interactions occur in nuclear reactors
- Provide examples of threshold reactions
- List the properties of a probability density function.
- Provide examples of common distributions.
- Compute the expected value $E[f(x)]$ for $x \sim p(x)$.

## Lesson 7

**Macro objective**

Estimate the number of elastic collisions a neutron of energy $E$ must make with a nucleus of mass number $A$ to slow to an energy $E'$.

**Micro objectives**

- For a given target nuclide and neutron energy, predict whether elastic or inelastic scattering dominates the slowing of neutrons.
- Compute the minimum, maximum, and expected outgoing energy of a neutron of energy $E$ after it scatters elastically (and isotropically) off of a given target nucleus.
- Compute the probability that a neutron of energy $E$ loses a given fraction of its energy following an elastic collision.
- Derive the slowing down decrement $\xi$ for a material with multiple nuclides.

## Lesson 8

**Macro objective**

Explain in a "big picture" sense what the goals of thermal and fast reactor designs are and how they differ based on $\eta(E)$, $\xi$, $\Sigma_s$ and $\Sigma_a$.

**Micro objectives**

- Compute the slowing down decrement, power, and ratio of a moderator.
- Explain what features make a moderator a "good" one.
- Compute, visualize, and characterize the ratio $\eta(E)$.
- Compute $\Sigma_a$.
- List the assumptions and simplifications required to analyze a steady-state, infinite, homogeneous reactor.

## Lesson 9

**Macro objective**

Students will be able to approximate the flux spectra $\phi(E)$ of fast neutrons and epithermal neutrons subject to elastic collisions in the absence of resonance absorption in infinite, homogeneous systems.

**Micro objectives**

- *Recall* $\Sigma_x$, $\chi(E)$, $p(E'\to E)$, $\xi$, $\alpha$, $1$ eV and $0.1$ MeV as "cutoffs"
- Explain the differences and relationships between the neutron density distribution $\tilde{n}'''(E)$, the neutron density $n'''$, and the neutron flux distribution $\phi(E)$ (the book uses $\varphi(E)$, but I'll stick with $\phi(E)$ because that's how I write it by hand.)
- Explain the neutron flux in terms of neutron path lengths.
- Describe mathematically the volumetric rate $R_x$ [1/cm$^3$-s] of some reaction $x$.
- Write down and explain the terms of the neutron slowing-down equation (SDE).
- Explain the difference between the collision rate $R_s(E)=\Sigma_S(E)\phi(E)$ and the slowing-down density $q(E)$.
- Verify that the solution to the SDE for purely-scattering media satisfies $\Sigma_S\phi(E) \propto E^{-1}$.

## Lesson 10

**Macro objective**

Students will be able to approximate the flux spectra $\phi(E)$ of epithermal neutrons subject to elastic collisions and resonance absorption in infinite, homogeneous systems.

**Micro objectives**

- Write down the slowing-down equation for a system with a moderator and fuel.
- Explain what a "narrow" resonance is in terms of the width $\Gamma$ and the mass number $A$ of the resonant nucleus.
- Use the narrow resonance (NR) approximation to define an intermediate flux spectrum.
- Describe the impact of a resonance located at $E_r$ on the neutron flux spectrum near that energy.
- Estimate the fraction of neutrons that pass by one or more resonances.

## Lesson 11

**Macro objective**

Students will be able to approximate the flux distribution of thermal neutrons in a thermal-spectrum reactor.

**Micro objectives**

- Write down the balance equation for thermal neutrons of energy below $E_{th} = 1$ eV.
- Explain the idea of detailed balance.
- State the Maxwell-Boltzmann distribution, i.e., $\phi_{MB}(E) \propto E e^{-E/kT}$.
- Describe the impact of absorption and temperature on the thermal spectrum.
- Describe why the free-gas approximation may be unsuitable for real materials.

## Lesson 12

**Macro objective**

Students will be able to compute effective cross sections and reaction rates averaged over the entire energy range of interest in order to estimate the multiplication factor of an infinite, homogeneous system.

**Micro objectives**

- Write down a mathematical expression for an effective cross section.
- Use integration to convert the spectrum (slowing-down) equation into an algebraic expression of single, integrated reaction rates.
- Express the infinite-medium multiplication factor in terms of effective cross sections.
- Numerically compute an effective cross section over any desired energy interval from tabulated data.

## Lesson 13

**Macro objective**

Students will be able to express the multiplication factor, thermal flux, and fast flux in the two-group formalism for an infinite, homogeneous system.

**Micro objectives**

- Describe the relationship between a *resonance integral* and *effective cross section*.
- Compute two-group cross sections from tabulated data using appropriate spectra.
- Express the balance of neutrons in a source-driven, infinite, homogeneous medium in terms of two-group fluxes and data.
- Express the balance of neutrons in a multiplication-driven, infinite, homogeneous medium in terms of two-group fluxes and data.
- Use OpenMC to produce multi-group cross sections from an infinite-homogeneous model.

## Lesson 14

**Macro objective**

Students will be able to express the multiplication factor, thermal flux, and fast flux in the multi-group formalism for an infinite, homogeneous system.

**Micro objectives**

- Describe the spectrum equation as linear system of equations (i.e., $\mathbf{Ax}=\mathbf{b}$)
- Describe the spectrum equation as an eigenvalue problem (i.e., $\mathbf{Ax}=\lambda\mathbf{x}$)
- Plot multigroup functions (e.g., cross sections and fluxes) as functions of energy and lethargy.

## Lesson 15

**Macro objective**

Students will be able to describe the constraints on and general features of common power reactor core configurations.

**Micro objectives**

- Explain the importance of criticality and the safe removal of heat to reactor core designs.
- Describe the basic "unit cell" common to most power reactors.
- Explain how the use of light water (over other moderators) impacts core size and fuel enrichment.

## Lesson 16

**Macro objective**

Students will be able to determine the flux spectra and multiplication factors for typical fast-spectrum reactors based on unit-cell analysis.

**Micro objectives**

- Define the geometry of a typical, fast-spectrum reactor unit cell.
- Define the material composition of a typical, fast-spectrum reactor unit cell.
- Explain the dominant features of a fast reactor's flux spectrum $\phi(E)$.

## Lesson 17

**Macro objective**

Students will be able to use the four-factor formula to characterize (quantitatively and qualitatively) the multiplication factor of a thermal-spectrum reactor based on unit-cell quantities.

**Micro objectives**

- Define the geometry of a typical, pressurized-water reactor (PWR) unit cell.
- Define the material composition of a typical, PWR unit cell.
- Explain what each term of the four-factor formula describes about the neutron lifecycle in a thermal-spectrum nuclear reactor.
- Numerically evaluate each term of the four-factor formula given two-group, unit-cell values of cross sections and fluxes.
- Show that the product of the two-group, two-region definitions for the four factors simplifies to the ratio of gains to losses.

## Lesson 18

**Macro objective**

Students will be able to run OpenMC models of typical SFR and PWR unit cells and to extract the results of these simulations for further analysis.

**Micro objectives**

- Have an account on and be able to access [ondemand.beocat.ksu.edu](ondemand.beocat.ksu.edu).
- Access the terminal through the browser.
- Execute a sequence of short commands to install OpenMC and related packages.
- Request a Jupyter instance with $N$ cores and $M$ GB of memory.
- Use the online interface to transfer files to and from Beocat.
- Create and run Jupyter notebooks that use OpenMC and related packages.

## Lesson 19

**Macro objective**

Students will be able to design unit cells that meet target objectives within given constraints.

**Micro objectives**

- Apply minimization to a function $f(x)$ to obtain optimum values of $x$
- Explain how changes in $P/D$ effect $f$, $p$, and $k_{\infty}$ of a PWR unit cell.
- Explain how changes in the Pu fraction impact $k_{\infty}$ of a SFR unit cell.
- Fit data points to a polynomial.

## Lesson 20

**Macro objective**

Students will be able to quantify the step changes in reactivity as a reactor is brought to power from cold, shutdown conditions.

**Micro objectives**

- Explain the relationship between reactivity and the multiplication factor.
- Represent reactivity in accepted units.
- List the integral reactivity changes observed when a reactor is brought to full power from cold, shutdown conditions.
- Describe how excess reactivity is balanced by the introduction of control (i.e., neutron "poisons")

## Lesson 21

**Macro objective**

Students will be able to quantify the impact of temperature, density, and other factors on reactivity.

**Micro objectives**

- Explain why the fuel temperature coefficient (FTC) is usually strongly negative.
- Explain how the moderator (or coolant) temperature coefficient (MTC) depends on geometry.
- Explain how the fuel and coolant temperature coefficients for a sodium-cooled fast reactor differ from those of a light-water reactor.

## Lesson 22

**Macro objective**

Students will be able to quantify the impact of xenon buildup on reactivity.

**Micro objectives**

- Model the impact of reactivity control, fission products, and depletion by proper adjustments to the four-factor formula.
- Quantify how the addition of chemical shim impacts the moderator temperature coefficient.
- List the primary long-term changes in a nuclear reactor core

## Lesson 23

**Macro objective**

Students will be able to quantify how fuel nuclides and core reactivity evolve as functions of burnup.

**Micro objectives**

- Define the differential equations needed to compute the concentrations of U-235, U-238, and Pu-239 in time.
- Write a general expression for $k$ (or $\rho$) that accounts for the transmutation of uranium nuclides.
- Convert between units of time and burnup.
- Quantify what fraction of power comes from the fission of Pu-239 as a function of time or burnup.
- Describe how, as a function of burnup, the power changes for a fixed flux and how the flux changes for a fixed power.
- Explain how a reactor with a large conversion ratio can, theoretically, produce more energy than a reactor with a small conversion ratio.
- Describe how burnable absorbers mixed with the fuel impact reactivity and why that impact is sometimes required.

## Lesson 24

**Macro objective**

Students will be able to explain cycle lengths and refueling strategies using the linear reactivity model.

**Micro objectives**

- Provide a typical discharge burnup range for light-water reactor fuel.
- Demonstrate that a fuel's reactivity is approximately linear with burnup
- Estimate how much more burnup can be accumulated by fuel if it is divided into $N$ equal batches.

## Lesson 25

**Macro objective**

Students will be able to write down, to solve, and to explain each term of a first-order, ordinary differential equation that models the neutron flux, the neutron density, or the number of neutrons in a non-multiplying system as a function of time.

**Micro objectives**

- Explain how the neutron kinetics equation is derived.
- Write an expression for the effective speed of neutrons in a given energy group.
- Identify the similarities between the neutron lifetime and the neutron mean-free path.
- Predict the neutron density as a function of time in an infinite, non-multiplying system.
- Estimate the lifetime of a thermal neutron from appropriate nuclear data.

## Lesson 26

**Macro objective**

Students will be able to write down, to solve, and to explain each term of a first-order, ordinary differential equation that models the neutron flux, the neutron density, or the number of neutrons a multiplying system in the absence of delayed neutron precursors.

**Micro objectives**

- Explain how changes in the neutron population with time depend on the system's multiplication factor (or reactivity).
- Show by how much a source of neutrons is amplified in a subcritical system.

## Lesson 27

**Macro objective**

Students will be able to write down, to explain each term of a system of, and to solve numerically the system of first-order, ordinary differential equations that model the neutron density and the densities of delayed neutron precursors in time.

**Micro objectives**

- Explain how neutrons can be produced relatively long after a fission has occured.
- Show how a delayed neutron precursor concentration $C_i(t)$ is related to the physical concentration of a fission product and its daughters.
- Provide representative values for the delayed neutron fraction of different fissile nuclides.
- Show that, in the one-group approximation, the inclusion of delayed-neutron precursors does not impact a steady-state system.
- Quantify how delayed neutrons impact the neutron lifetime.
- Use `odeint` or similar tools to solve numerically systems of first-order differential equations.

## Lesson 28

**Macro objective**

Students will be able to solve the kinetics equations subject to step insertions of reactivity and to predict neutron and precursor densities and reactor periods from those solutions and approximations thereof.

**Micro objectives**

- Explain how and why the solution to the kinetics equations fundamentally changes when $\rho$ exceeds $\beta$.
- Approximate the neutron density immediately following a step insertion of reactivity.
- Explain why the reactor power can never be reduced to zero immediately.
- Explain how an image like Figure 5.3 in the text can be used to predict $T$ given $\rho$ and vice versa for a given reactor.
- Explain how an image like Figure 5.4 in the text can be used to predict $T$ given $\rho$ and vice versa for various reactors.
- Solve by hand the kinetics equations with a single precursor group.

## Lesson 29

**Macro objective**

Students will be able to predict how feedback from temperature changes impacts the solution of the kinetics equations.

**Micro objectives**

- Describe the terms in the model (provided in class) that relates the neutron density and the fuel and coolant temperatures.

## Lesson 30

**Macro objective**

Students will be able to show that neutrons are conserved (or not) in a spatial volume given the neutron flux and appropriate cross-section data.

**Micro objectives**

- Write down, in plain English, a statement that describes neutron balance in a control volume.
- Explain what the neutron current $\vec{J}$ represents. Note that a vector $\vec{x}$ can also be written $\mathbf{x}$.
- Given a neutron flux $\phi(\vec{r})$ and a diffusion coefficient $D(\mathbf{r})$, compute the neutron current.
- Integrate the neutron continuity equation (Lewis, Eq. (6.10)) or the neutron diffusion equation (Lewis, Eq. (6.12)) over a control volume.
- Describe how the neutron diffusion equation is similar to and different from other conservation equations in engineering.

## Lesson 31

**Macro objective**

Students will be able to show that neutrons are conserved (or not) in a spatial volume given the neutron flux and appropriate cross-section data.

**Micro objectives**

- Write down, in plain English, a statement that describes neutron balance in a control volume.
- Explain what the neutron current $\vec{J}$ represents. Note that a vector $\vec{x}$ can also be written $\mathbf{x}$.
- Given a neutron flux $\phi(\vec{r})$ and a diffusion coefficient $D(\mathbf{r})$, compute the neutron current.
- Integrate the neutron continuity equation (Lewis, Eq. (6.10)) or the neutron diffusion equation (Lewis, Eq. (6.12)) over a control volume.
- Describe how the neutron diffusion equation is similar to and different from other conservation equations in engineering.

## Lesson 32

**Macro objective**

Students will be able to develop solutions for the one-speed diffusion equation in slab geometry for single-region systems with constant $D$, constant $\Sigma_a$, and an arbitrary volumetric source term $s(x)$.

**Micro objectives**

- Explain what is meant by "slab" geometry and under which conditions such a model is of use.
- Describe what "homogeneous" and "particular" solutions are and the basic techniques used to find them.
- Verify that a solution $\phi(x)$ satisfies the diffusion equation.
- Verify that a solution $\phi(x)$ preserves neutron balance over an arbitrary volume.

## Lesson 33

**Macro objective**

Students will be able to define and solve the equations representing multi-region, source-driven, slab systems subject to vacuum and reflecting boundary conditions.

**Micro objectives**

- Explain in plain English what is meant by "partial current."
- List the quantities involved in the diffusion equation that must be continuous throughout the domain.
- For a homogeneous region within a slab system of one or more regions, determine the particular solution given the source term $s(x)$ in that region.
- Given the homogeneous and particular solutions for each of $N$ regions of a heterogeneous slab and the boundary conditions at the left and ride surfaces of the slab, write down the system of $2N$ equations needed to determine each constant of integration.
- Use `numpy.linalg.solve` or other tools (perhaps from MATH 551) to solve linear systems.

## Lesson 34

**Macro objective**

Students will be able to define and solve the equations representing multi-region, source-driven, slab systems with multiplication subject to vacuum and reflecting boundary conditions.

**Micro objectives**

- Explain how the inclusion of multiplication can fundamentally change the solution of the diffusion equation.
- Explain how an increasing $k_{\infty}$ impacts the flux magnitude in a subcritical system.

## Lesson 35

**Macro objective**

Students will be able to define and evaluate criticality conditions for slab and cylindrical systems.

**Micro objectives**

- Explain how the material and geometric buckling are used to define criticality.
- Explain why the solution to the diffusion eigenvalue problem is unique only to within a multiplicative constant.
- Explain why one might choose hyperbolic sines and cosines over standard exponential functions.
- Describe the process of using series expansions to solve differential equations.

## Lesson 36

**Macro objective**

Students will be able to write down the equations necessary to model multi-region reactors using the two-group approximation and to solve such equations numerically.

**Micro objectives**

- Explain what the *removal cross section* $\Sigma_r$ represents.
- Explain what the scattering cross section $\Sigma_{s_{2\gets 1}}$ represents. (Pay attention to the arrow, which I use to make explicit how the indices are ordered!)
- Explain why the "right-hand sides" of the two-group equations (in Eq. (7-40) of Duderstadt and Hamilton; see reading below) are the appropriate "gains" terms for each energy group.
- Explain what the migration area is as it relates to a neutron's life.
- Determine $k$ for a bare, homogeneous reactor in 1-D slab or 1-D cylindrical coordinates subject to zero-flux boundary conditions.
- Describe why one would use $M^2$ in place of $L_1^2$ in the modified one-group diffusion.

## Lesson 37

**Macro objective**

Students will be able to characterize both quantitatively and qualitatively the impact of a reflector region on an otherwise bare reactor core using diffusion theory.

**Micro objectives**

- Explain why reflectors are used in reactor systems.
- Estimate by how much a reflector reduces leakage losses from a reactor core.
- Describe the properties needed by a good neutron reflector.
- Compute the reflector savings for a slab reactor using one-group diffusion theory.
- Sketch the flux profile through a core and reflector region in both the one- and two-group approximations.

## Lesson 38

**Macro objective**

Students will be able to use the one-group diffusion approximation to estimate how a small and localized perturbation in a reactor core changes the reactivity of the system.

**Micro objectives**

- Explain how the first-order perturbation estimate for $\Delta \rho$ is obtained using one-group diffusion theory.
- Explain why perturbation theory is accurate only for "small" changes in system properties (e.g., an absorption cross section).

