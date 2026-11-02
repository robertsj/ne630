#!/usr/bin/env python3
"""Reproduce/verify HW20--24 and 27--28 solution numbers and figures.

Inputs: ne630_problems at 9c3dc61; current HW20--23 Markdown governs.
No transport runs: HW21 bonus uses explicitly identified legacy tally data.
Outputs remain instructor-only. Run with NumPy, SciPy, and Matplotlib.
"""
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm
from scipy.optimize import minimize_scalar

ROOT = Path(__file__).resolve().parent
FIG = ROOT / "figures"
PURPLE, ORANGE = "#512888", "#CA7C1B"


def close(a, b, **kw):
    np.testing.assert_allclose(a, b, rtol=kw.pop("rtol", 2e-8), atol=kw.pop("atol", 1e-10), **kw)


def main():
    FIG.mkdir(exist_ok=True)
    # Preserve the rounded textbook inputs used in the legacy HW20--22 chain.
    NA, e, nu, eps, zeta, ratio, pnl = 6.022e23, .03, 2.43, 1.24, 1.16, 2., .95
    nf, nm = 11 * NA / 270, NA / 18
    af = nf * (e * 591 + (1-e) * 2.42) * 1e-24
    sf = nf * e * 505e-24
    am = nm * (2 * .295 + 1.69e-4) * 1e-24
    I0 = 4.45 + 26.6 * np.sqrt(4 / (11 * 1.1))
    gamma = .0061 + .0047 * 4 / 11

    def p(tf, density):
        I = I0 * (1 + gamma * (np.sqrt(tf) - np.sqrt(300)))
        return np.exp(-nf * (1-e) * I * 1e-24 / (ratio * 1.28 * density))

    def C(tf, density):
        return nu * sf * eps * pnl * p(tf, density)

    def D(density):
        return af + zeta * ratio * density * am

    rho = lambda k: 1 - 1 / k
    rod = 1.04 * C(300, 1) - D(1)
    x = lambda tf, d: (C(tf, d) - D(d)) / rod
    cc, hzp, fp = x(300, 1), x(600, .66), x(1200, .66)
    for tf, d, frac in [(300, 1, cc), (600, .66, hzp), (1200, .66, fp)]:
        close(C(tf, d) / (D(d) + frac * rod), 1)
    close(rho(C(300, 1) / (D(1) + rod)), -.04)
    hw20 = dict(reactivity=rho(1.00234), eta=nu*sf/af, f=af/D(1), p=p(300,1),
                epsilon=eps, k_cold=C(300,1)/D(1), excess=rho(C(300,1)/D(1)),
                fuel_absorption=af, fuel_fission=sf, water_absorption=am,
                resonance_integral=I0, gamma=gamma, rod_cross_section=rod,
                x_cc=cc, x_hzp=hzp, x_fp=fp, p_hzp=p(600,.66), p_fp=p(1200,.66),
                temperature_defect=rho(C(600,.66)/(D(.66)+cc*rod)),
                power_defect=rho(C(1200,.66)/(D(.66)+hzp*rod)),
                hot_excess=rho(C(1200,.66)/D(.66)), C_fp=C(1200,.66))

    # Number-ratio ppm is not mass ppm; distinguish logarithmic and rho derivatives.
    ab_ref = (C(1200,.66)-af)/(zeta*ratio*.66) - am
    nb_ref = ab_ref / 3409e-24
    ppm_atom = nb_ref/nm * 1e6
    ppm_b10_mass = ppm_atom * 10/18
    ppm_nat_mass_ratio = ppm_atom/.2 * 10.8/18
    hw21 = dict(boron_absorption_ref=ab_ref, B10_density_hot=.66*nb_ref,
                B10_per_million_water=ppm_atom, B10_mass_ppm_water=ppm_b10_mass,
                natB_mass_ppm_water=ppm_nat_mass_ratio,
                natB_mass_ppm_solution=1e6*ppm_nat_mass_ratio/(1e6+ppm_nat_mass_ratio))
    for label, ab in [("unborated", 0), ("borated", ab_ref)]:
        def k(d):
            return C(1200,d)/(af + zeta*ratio*d*(am+ab))
        f = af/(af+zeta*ratio*.66*(am+ab))
        a_log = -.004*(np.log(1/p(1200,.66))-(1-f))
        h = .001
        dplus, dminus = .66*np.exp(-.004*h), .66*np.exp(.004*h)
        close((np.log(k(dplus))-np.log(k(dminus)))/(2*h), a_log)
        a_rho = a_log/k(.66)
        close((rho(k(dplus))-rho(k(dminus)))/(2*h), a_rho)
        hw21[label] = dict(f=f, k=k(.66), alpha_log_pcm=1e5*a_log, alpha_rho_pcm=1e5*a_rho)
    gamma21 = .0061 + .0047*4/(11*1.1)
    tf = np.linspace(300,1000,300)
    afunc = lambda t: -gamma21*np.log(1/.63)/(2*np.sqrt(t))
    fig, ax = plt.subplots(figsize=(6.4,3.3))
    ax.plot(tf, 1e5*afunc(tf), color=PURPLE)
    ax.set(xlabel="Fuel temperature (K)", ylabel=r"$10^5\,d\ln k/dT_f$ (K$^{-1}$)")
    ax.grid(alpha=.2);fig.tight_layout();fig.savefig(FIG/'hw21_fuel_coefficient.png',dpi=180);plt.close(fig)
    hw21['fuel_alpha_log_pcm']={str(t):float(1e5*afunc(t)) for t in [300,600,1000,1200]}
    legacy=[(0,1200,600,1.28397,.00096),(0,900,600,1.29557,.00112),
            (0,1200,610,1.27228,.00096),(4800,1200,600,1.05104,.00097),
            (4800,900,600,1.05924,.00090),(4800,1200,610,1.05259,.00094)]
    hw21['legacy_coefficients']={}
    for name,lo,hi,dt in [('fuel_0',1,0,300),('moderator_0',0,2,10),('fuel_4800',4,3,300),('moderator_4800',3,5,10)]:
        k0,s0=legacy[lo][3:];k1,s1=legacy[hi][3:]
        hw21['legacy_coefficients'][name]=dict(log_pcm=1e5*np.log(k1/k0)/dt,
            log_sd_pcm=1e5*np.hypot(s1/k1,s0/k0)/dt,
            rho_pcm=1e5*(rho(pnl*k1)-rho(pnl*k0))/dt,
            rho_sd_pcm=1e5*np.hypot(s1/(pnl*k1*k1),s0/(pnl*k0*k0))/dt)

    phi, li, lx, yi, yx, sx = 3e13, np.log(2)/(6.7*3600), np.log(2)/(9.2*3600), .0639, .00237, 2.64e-18
    fission = sf*phi
    ieq, xeq = yi*fission/li, (yi+yx)*fission/(lx+sx*phi)
    def xenon(t):
        return xeq*np.exp(-lx*t)+li*ieq/(li-lx)*(np.exp(-lx*t)-np.exp(-li*t))
    peak=minimize_scalar(lambda t:-xenon(t),bounds=(0,36*3600),method='bounded').x
    times=np.linspace(0,48*3600,600)
    sol=solve_ivp(lambda t,y:[-li*y[0],li*y[0]-lx*y[1]],(0,times[-1]),[ieq,xeq],t_eval=times,rtol=1e-10,atol=1.)
    assert sol.success;close(sol.y[1],xenon(times),rtol=3e-9)
    close(li*ieq*np.exp(-li*peak),lx*xenon(peak),rtol=1e-7)
    worth=lambda X:-sx*X/C(1200,.66)
    hw22=dict(i_eq=ieq,x_eq=xeq,absorption=sx*xeq,equilibrium_worth=worth(xeq),
              peak_hours=peak/3600,x_at_11p3=xenon(11.3*3600),x_peak=xenon(peak),
              worth_11p3=worth(xenon(11.3*3600)),peak_worth=worth(xenon(peak)),
              withdrawn_peak=rho(C(1200,.66)/(D(.66)+sx*xenon(peak))))
    fig,axs=plt.subplots(1,2,figsize=(10,3.4))
    axs[0].plot(times/3600,xenon(times)/1e15,color=PURPLE)
    axs[0].set(ylabel=r"Xe density ($10^{15}$ cm$^{-3}$ of fuel)")
    axs[1].plot(times/3600,1e5*worth(xenon(times)),color=ORANGE)
    axs[1].set(ylabel="Xenon worth (pcm; fixed hot conditions)")
    for ax in axs:ax.set(xlabel="Time after shutdown (h)");ax.grid(alpha=.2)
    fig.tight_layout();fig.savefig(FIG/'hw22_xenon.png',dpi=180);plt.close(fig)

    fluence=np.log(2)/591e-24
    pu=(2.42/973)*.96*(-np.expm1(-973e-24*fluence))
    hw23=dict(fluence_half=fluence,pu_fraction=pu,CR0=2.42*.96/(591*.04),
              CR_half=2.42*.96/(591*.02+973*pu),pu_power=698*pu/(505*.02+698*pu))
    # Dimensionless manufactured checks of Pa/U solution, including equal rates.
    for a,b in [(1.2,.3),(1.2,1.2),(1.2,0.)]:
        rate,decay=2.,.7; t=np.linspace(0,12,301)
        pa=rate/a*(-np.expm1(-a*t))
        first=t if b==0 else -np.expm1(-b*t)/b
        second=t*np.exp(-a*t) if a==b else (np.exp(-a*t)-np.exp(-b*t))/(b-a)
        u=decay*rate/a*(first-second)
        q=solve_ivp(lambda t,y:[rate-a*y[0],decay*y[0]-b*y[1]],(0,12),[0,0],t_eval=t,rtol=2e-11,atol=1e-12)
        assert q.success;close(q.y,np.array([pa,u]),atol=5e-11)

    ns=np.arange(1,6);bc=2*(.243-.05)/(.00664*(ns+1))
    powers=np.array([1.3,.9,.8]);bc3=3*(.243-.05)/(.00664*(powers@np.cumsum(powers)))
    close(np.mean(powers*(.243-.00664*bc3*np.cumsum(powers)))-.05,0)
    hw24=dict(cycle=bc.tolist(),discharge=(ns*bc).tolist(),limit=2*(.243-.05)/.00664,
              unequal_cycle=bc3,unequal_discharge=3*bc3)

    lam=np.log(2)/np.array([56,23,6.2,2.3,.61,.23])
    bet=np.array([.00021,.00142,.00128,.00257,.00075,.00027]);L=50e-6;n0=1e6
    y0=np.r_[n0,bet*n0/(L*lam)]
    def matrix(r):
        A=np.zeros((7,7));A[0,0]=(r-bet.sum())/L;A[0,1:]=lam
        A[1:,0]=bet/L;A[1:,1:]=-np.diag(lam);return A
    close(matrix(0)@y0,np.zeros(7),atol=2e-8)
    hw27=dict(beta_boc=.0065,beta_eoc=(.7*2.43*.0065+.3*2.9*.0021)/(.7*2.43+.3*2.9),precursors=y0[1:].tolist())
    fig,ax=plt.subplots(figsize=(7,3.6))
    for sign,color in [(1,PURPLE),(-1,ORANGE)]:
        state=y0.copy();ts=[];ys=[];checkpoints={}
        for lo,hi,r in [(0,1,0),(1,6,sign*.25*bet.sum()),(6,10,0)]:
            A=matrix(r);t=np.linspace(lo,hi,401)
            q=solve_ivp(lambda t,y:A@y,(lo,hi),state,method='Radau',t_eval=t,rtol=2e-10,atol=1e-3)
            assert q.success
            exact=expm(A*(hi-lo))@state;close(q.y[:,-1],exact,rtol=1e-8)
            state=q.y[:,-1];checkpoints[str(hi)]=float(state[0]);ts.extend(t);ys.extend(q.y[0])
        hw27[str(sign)]=checkpoints
        ax.plot(ts,np.array(ys)/1e6,label=f'{sign*.25:+.2f} dollars, 1–6 s',color=color)
    ax.set(xlabel='Time (s)',ylabel=r'$n(t)$ ($10^6$ cm$^{-3}$)');ax.legend();ax.grid(alpha=.2)
    fig.tight_layout();fig.savefig(FIG/'hw27_six_group.png',dpi=180);plt.close(fig)
    hw28={}
    for label,bv in [('U233',[.00023,.00078,.00064,.00074,.00014,.00008]),('U235',bet),('Pu239',[.00007,.00063,.00044,.00069,.00018,.00009])]:
        bv=np.array(bv);le=bv.sum()/np.sum(bv/lam);hw28[label]=dict(lambda_eff=le,period_small_cent=100/le)
    beta,lamb=.0065,.08
    for sign in [1,-1]:
        r=sign*.2*beta;B=lamb+(beta-r)/L;C0=-lamb*r/L
        w=np.sort(np.roots([1,B,C0]))[::-1]
        aa=np.array([n0*(r/L-w[1])/(w[0]-w[1]),0.]);aa[1]=n0-aa[0]
        bb=beta*aa/(L*(w+lamb))
        A=np.array([[(r-beta)/L,lamb],[beta/L,-lamb]])
        initial=np.array([n0,beta*n0/(L*lamb)])
        vals=[]
        for t in [0,.1,10]:
            v=np.array([aa@np.exp(w*t),bb@np.exp(w*t)])
            close(v,expm(A*t)@initial,rtol=2e-10);vals.append(v.tolist())
        hw28[str(sign)]=dict(B=B,C=C0,roots=w.tolist(),a=aa.tolist(),b=bb.tolist(),values=vals)
    result=dict(hw20=hw20,hw21=hw21,hw22=hw22,hw23=hw23,hw24=hw24,hw27=hw27,hw28=hw28)
    print(json.dumps(result,indent=2))
    print('PASS: critical states, finite-difference coefficients, Xe ODE/peak, Pa/U limits, batch balance, six-group IVP/expm, and one-group roots/expm.')


if __name__ == '__main__':
    main()
