# Homework for Week 5

**Note** Homework is typically due at 1:30pm on Friday.  However, because some of this material is relevant for the 
exam, I am having this due Thursday at 11:59 pm.  But, I've converted the two more time-consuming problems into
extra credit worth 4 points each.  These can be turned in with the next homework.

 - (EXTRA CREDIT) In the last homework, you computed a spectrum $\phi(E)$ representative of a thermal-spectrum
   reactor.  As we learned (see solution), the approximations we've used make it hard to define a spectrum 
   that is "realistic" between the primary energy ranges.  I proposed an improved spectrum that I've 
   tabulated for you (first column is $E$, second is the spectrum to use; the third column applies the NR approximation).  
   Use this spectrum produce $\bar{\sigma_s}$, $\bar{\sigma_{\gamma}}$, 
   and $\bar{\sigma_f}$, and $\bar{\nu\sigma_f}$ for H-1, O-16, U-235, and U-238. 

 - (EXTRA CREDIT) For a 50-50 mixture (by volume) of UO$_2$ (10 g/cm$^3$) and H$_2$O (1 g/cm$^3$), compute $k_{\infty}$
   (using the cross sections you just computed).

 - The spectrum you just used had $1/E$ dependence through the resonance range.  How do you think $k_{\infty}$ 
   would change if the NR approximation were used in place of $1/E$?

 - Representative two-group cross sections for a pressurized-water reactor are given in the table below.  
   Use these data to compute $k_{\infty}$ and the ratio $\phi_1/\phi_2$.  Note that the *removal* cross 
   section $\Sigma_{rg}$ is $\Sigma_{tg} - \Sigma_{sg\gets g'}$ and that $\Sigma_{tg} = \Sigma_{ag} + \sum_{g'} \Sigma_{sg'\gets g}$.

|                         |   $g = 1$ | $g = 2$ |
|-------------------------|-----------|---------|
|	$\bar{\nu}\Sigma_{fg}$  | 0.008476	|	0.18514 |
|	$\Sigma_{fg}$           | 0.003320	| 0.07537 |
| $\Sigma_{ag}$         	| 0.01207	  | 0.1210 |
|	$\Sigma_{rg}$           | 0.02619   | 0.1210 |

 - Write the two-group equations *without the multiplication factor* in terms of a
   unit source in the fast group.

 - For those same equations, find $\phi_1$ and $\phi_2$.  

 - Use $\phi_1$ and $\phi_2$ to estimate $k_{\infty}$ as "gains over losses."

 - How do $\phi_1/\phi_2$ and $k_{\infty}$ from this fixed-source problem compare to 
   the eigenvalue problem discussed in class?
