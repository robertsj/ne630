# Homework 32

Almost everyone got to the right set of equations from the boundary conditions but a few folks didn't get that $C_1=C_2=0$.


# Homework 33

For 33.1, most folks did well.  Some botched the boundary conditions.  Write these out by hand!  SymPy is good for double checking (and for nice looking math), but you need to be able to set these up on paper.  When plotting multiple-region fluxes, be sure not to plot the flux for one region over x values that belong to another region! 

For 33.2, a few folks were concerned by the "messy" results.  Recall that, for a single-region slab, we will always have a system like $aC_1 + bC_2 = s_1$ and $cC_1 + dC_2 = s_2$ from the boundary conditions. Yes, the $a, b, c, d$ and maybe $s_1$ and $s_2$ depend on $D$, $\Sigma_a$, or $L$, but we don't have to write all that out!   So, as long as you can get to, e.g., $C_1 = (d s_2 -b s_2)/(a d - bc)$, then you can can do integration, differention, numerical substitution, etc., all using the basic form $\phi(x) = C_1 e^{x/L} + C_2 e^{-a/L} + \phi_p(x)$.  In other words, you can evaluate $J_{\mp}(x) = \phi(x)/4 \pm (D/2)d\phi/dx$.

A handful of folks used $\alpha = (1-2D/L)/(1+2D/L)$ as defined by Eq. (6.41) in the text for $R$.  Recall, though, Eq. (6.40) is for an *infinite* half space (Eq. 6.40 is the general definition for the albedo which is equivalent to the reflection coefficient).  For our problem, we'd get $R \to \alpha$ in the limit that $a \to \infty$.  

