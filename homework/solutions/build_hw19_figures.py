#!/usr/bin/env python3
"""HW19 SFR enrichment study. Default: redraw saved results; --run: OpenMC.

OPENMC_CROSS_SECTIONS and PATH must point to an installed data library and
OpenMC executable for --run. No machine-specific path is stored here.
Model snapshot: hw19_sfr_model.py, unmodified Lesson 19 builder.
"""
import argparse
import hashlib
import json
from pathlib import Path
import tempfile
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT/'data/hw19_results.json'
PARTICLES, BATCHES, INACTIVE = 5000, 120, 30


def interpolate(lo, hi):
    xlo,xhi,klo,khi=lo['x'],hi['x'],lo['k'],hi['k']
    assert klo < 1 < khi and xlo < xhi
    dx,dk=xhi-xlo,khi-klo
    x=xlo+dx*(1-klo)/dk
    # First-order propagation for independent endpoint eigenvalue estimates.
    dl=dx*(1-khi)/dk**2
    dh=-dx*(1-klo)/dk**2
    sx=np.hypot(dl*lo['sigma_k'],dh*hi['sigma_k'])
    assert xlo < x < xhi
    return dict(x=float(x),sigma_x=float(sx),slope=float(dk/dx),
                lower_seed=lo['seed'],upper_seed=hi['seed'])


def run(threads):
    import openmc
    import hw19_sfr_model as m
    x0=m.LESSON16_ENRICHMENT_ATOM_FRACTION
    doc=dict(model='Lesson 19 heterogeneous reflecting SFR unit cell',
             openmc_version=openmc.__version__,
             model_sha256=hashlib.sha256((ROOT/'hw19_sfr_model.py').read_bytes()).hexdigest(),
             cross_sections_xml_sha256=hashlib.sha256(Path(m.cross_sections).read_bytes()).hexdigest(),
             data_library='ENDF/B-VIII.0 (installed HDF5 library)',
             x_definition='U235 atom fraction among uranium atoms',x0=float(x0),
             particles=PARTICLES,batches=BATCHES,inactive=INACTIVE,
             temperature_K=m.TEMPERATURE,target_k=1.,cases=[],interpolations=[])
    DATA.parent.mkdir(exist_ok=True)
    def save():
        DATA.write_text(json.dumps(doc,indent=2)+'\n')
    def case(x,seed,label):
        model=m.build_sfr_model(enrichment=x,particles=PARTICLES,batches=BATCHES,
                                inactive=INACTIVE,seed=seed)
        assert [v.density for v in model.materials]==[10.5,7.13,.837]
        assert all(v.temperature==294. for v in model.materials)
        # Retain simple source-convergence diagnostic without changing physics.
        mesh=openmc.RegularMesh()
        mesh.lower_left=(-m.PITCH/2,-m.HEX_SIDE,-.5)
        mesh.upper_right=(m.PITCH/2,m.HEX_SIDE,.5)
        mesh.dimension=(5,5,1)
        model.settings.entropy_mesh=mesh
        model.settings.output={'tallies':False}
        with tempfile.TemporaryDirectory(prefix='ne630-hw19-') as tmp:
            sp_path=model.run(cwd=tmp,threads=threads,output=False)
            with openmc.StatePoint(sp_path) as sp:
                k=sp.keff
                rates=sp.get_tally(name='regional one-group rates')
                absorption=rates.get_values(scores=['absorption']).ravel()
                production=rates.get_values(scores=['nu-fission']).ravel()
                assert np.isfinite(absorption).all() and np.all(absorption>=0)
                assert np.isfinite(production).all() and np.all(production>=0)
                generation=np.array(sp.k_generation)
                active=generation[INACTIVE:]
                assert len(active)==BATCHES-INACTIVE
                half=len(active)//2
                delta=active[half:].mean()-active[:half].mean()
                se=np.hypot(active[:half].std(ddof=1)/np.sqrt(half),
                            active[half:].std(ddof=1)/np.sqrt(len(active)-half))
                entropy=np.array(sp.entropy)
                row=dict(label=label,seed=seed,x=float(x),x_over_x0=float(x/x0),
                         weight_percent=100*m.uranium_weight_fraction_from_atom_fraction(x),
                         k=float(k.n),sigma_k=float(k.s),
                         production_by_region=production.tolist(),
                         absorption_by_region=absorption.tolist(),
                         production_over_absorption=float(production.sum()/absorption.sum()),
                         active_half_mean_difference=float(delta),active_half_difference_se=float(se),
                         active_half_z=float(delta/se),
                         k_generation=generation.tolist(),entropy=entropy.tolist())
        assert 0<row['sigma_k']<.01
        doc['cases'].append(row);save()
        print(f"{label}: x={x:.9f}, k={row['k']:.7f} +/- {row['sigma_k']:.7f}, half-z={row['active_half_z']:.2f}",flush=True)
        return row
    for j,factor in enumerate([.5,1.,1.5]):
        case(factor*x0,191901+j,f'{factor:g} x0')
    # Normally the requested points bracket one; extend only if necessary.
    for j in range(5):
        rows=sorted(doc['cases'],key=lambda z:z['x'])
        brackets=[(a,b) for a,b in zip(rows[:-1],rows[1:]) if a['k']<1<b['k']]
        if brackets:break
        trial=rows[0]['x']*.5 if rows[0]['k']>1 else min(.99,rows[-1]['x']*1.5)
        case(trial,191910+j,'extra bracket')
    else:raise RuntimeError('No bracket obtained')
    lo,hi=brackets[0]
    estimate=interpolate(lo,hi);doc['interpolations'].append(estimate);save()
    confirmed=case(estimate['x'],191920,'first interpolation check')
    # If the check lies outside two reported SE, refine locally; retain first check.
    # Endpoint noise also contributes: this is not a formal curvature test.
    for j in range(2):
        if abs(confirmed['k']-1)<=2*confirmed['sigma_k']:break
        if confirmed['k']<1:lo=confirmed
        else:hi=confirmed
        estimate=interpolate(lo,hi);doc['interpolations'].append(estimate);save()
        confirmed=case(estimate['x'],191921+j,'refined interpolation check')
    doc['final']=dict(estimate=estimate,confirmation_seed=confirmed['seed'],
                      residual_sigma=float((confirmed['k']-1)/confirmed['sigma_k']))
    save()


def plot():
    d=json.loads(DATA.read_text());rows=d['cases']
    assert d.get('final'), 'Incomplete run; complete --run before rendering.'
    fig,ax=plt.subplots(figsize=(7.2,4.0),layout='constrained')
    primary=rows[:3];checks=rows[3:]
    ax.errorbar([100*r['x'] for r in primary],[r['k'] for r in primary],
                yerr=[r['sigma_k'] for r in primary],fmt='o-',capsize=4,
                color='#512888',label='Assigned cases (1 SE)')
    ax.errorbar([100*r['x'] for r in checks],[r['k'] for r in checks],
                yerr=[r['sigma_k'] for r in checks],fmt='s',capsize=4,
                color='#CA7C1B',label='Independent interpolation checks')
    ax.axhline(1,color='.3',ls='--',label=r'$k_\infty=1$')
    ax.set(xlabel='U-235 atom percent among uranium atoms',ylabel=r'$k_\infty$',
           title='Lesson 19 SFR cell: fixed geometry, densities, and 294 K')
    ax.grid(alpha=.2);ax.legend(fontsize=9)
    (ROOT/'figures').mkdir(exist_ok=True)
    fig.savefig(ROOT/'figures/hw19_enrichment.png',dpi=180);plt.close(fig)
    fig,axes=plt.subplots(2,1,figsize=(7,5.4),sharex=True,layout='constrained')
    for r in rows:
        t=np.arange(1,len(r['k_generation'])+1)
        axes[0].plot(t,r['k_generation'],lw=.7,label=r['label'])
        axes[1].plot(t,r['entropy'],lw=.7)
    for ax in axes:ax.axvline(d['inactive']+.5,color='black',ls='--');ax.grid(alpha=.2)
    axes[0].set(ylabel='Generation k');axes[0].legend(fontsize=7,ncol=2)
    axes[1].set(xlabel='Batch (one generation per batch)',ylabel='Source entropy')
    fig.savefig(ROOT/'figures/hw19_convergence.png',dpi=160);plt.close(fig)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run',action='store_true')
    parser.add_argument('--threads',type=int,default=2)
    args=parser.parse_args()
    if args.run:run(args.threads)
    plot()
