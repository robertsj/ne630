# Course Introduction

Welcome to NE 630 - Nuclear Reactor Theory!  What is "nuclear reactor theory?"  Good question.  Nuclear reactor theory is all about the physics of systems that use neutrons to produce fissions in a self-sustaining, chain reaction.  Often, this discipline is called **reactor physics**, a term I'll use often. 

In a nutshell, reactor physics combines all the basics from NE 495 (reactions, cross sections, fluxes) to produce a mathematical model that describes the neutron population in a reactor.  For us, that model will be the *neutron diffusion equation* that describes the neutron density in space, energy, and time:

$$
\frac{1}{v} \frac{\partial \phi}{\partial t}
 - \nabla D(\mathbf{r}, E) \nabla \phi 
  + \Sigma_t(\mathbf{r}, E) \phi(\mathbf{r}, E, t) 
  = \int^{\infty}_0 \Sigma_s(\mathbf{r}, E'\to E) \phi(\mathbf{r}, E', t) dE'
   + \frac{\chi(E)}{k_{\text{eff}}} \int^{\infty}_0 \bar{\nu}(\mathbf{r}, E')\Sigma_f(\mathbf{r}, E') \phi(\mathbf{r}, E', t) dE' + S(\mathbf{r}, E, t) \, .
$$

Whoa!  That's a bit overwhelming, no?  Don't worry!  While some of the symbols may look familiar (e.g., $\phi$ is the neutron flux and $\Sigma_t$ is the total, macroscopic cross section), some of them are likely new to you.  


The same goes for the math involved: as written, the equation is an integro-differential equation, which means there are both derivatives and integrals of the unknown flux.  Again, don't worry!  A big part of learning and using reactor physics is to reduce the governing equations to the simplest possible form that captures the physics of interest.  An example I always include in NE 495 is the four-factor formula ($k_{\text{eff}} = f p \eta \epsilon)$), which one can derive from the diffusion equation by ignoring space and time and by separating neutron energies into "thermal" and "fast."  If that looks Greek to you, don't worry: we'll be doing that derivation later in class!


During the course, we'll follow the textbook pretty closely and cover the majority of its content.  A detailed lesson schedule will be provided elsewhere, but the coarse-grained structure is as follows:

  - Nuclear reactions, radioactive decay, and neutron interactions [2-3 weeks]
  - Neutron energy distributions, and energy-integrated, steady-state reaction rates, and the multigroup method (no space, no time) [2-3 weeks]
  - Reactor kinetics, dynamics, and depletion (i.e., time-dependent reaction rates) (no space, no energy) [4-5 weeks]
  - Neutron spatial distributions for source-driven and critical systems (no time, either no energy or multigroup) [4-5 weeks]


Finally, I believe it's important for students to be able to use computers both to solve problems and to perform "experiments" (i.e., simulations) that reinforce all the "theory."  For solving problems, I will often use Jupyter, a browser-based tool that lets one combine code and words in an online "notebook."  For experiements, we'll use the free and open-source Monte Carlo code OpenMC, which will be available on a remote cluster (e.g., Beocat).  How much we use either tool for in-class activities and homework assignments will depend on your previous experience and interests.
