"""Build all L25--39 draft plots inside handouts/figures using course colors.

Numerical formulas are retained from the cited notebooks. Recovered notebook
line data live beside this script under drafts/data; see their JSON provenance.
Normal builds need NumPy, SciPy, and Matplotlib, not the external detran solver.
"""
from pathlib import Path
import hashlib
import json
import re
import textwrap
import os
os.environ.setdefault("MPLCONFIGDIR",str(Path(__file__).resolve().parent/".mplconfig"))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'drafts'
DATA=OUT/'data'
def course_color(name):
    source=(ROOT.parent/'ne630handout.cls').read_text()
    match=re.search(r'\\definecolor\{'+name+r'\}\{RGB\}\{([0-9,]+)\}',source)
    if match is None:raise ValueError('Missing shared course color '+name)
    return '#'+''.join(f'{int(part):02X}' for part in match[1].split(','))

PURPLE=course_color('wcprimary')
ORANGE=course_color('wcalerted')
GRAY='#777777'
COLORS=[PURPLE,ORANGE,'#9271B6','#8D5713','#3B1B64','#DAB784','#B9A4D0']
STYLES=['-','--','-.',':',(0,(5,1)),(0,(3,1,1,1)),(0,(1,1))]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8,'axes.labelsize':8,
 'xtick.labelsize':7,'ytick.labelsize':7,'legend.fontsize':7,'axes.titlesize':8,
 'lines.linewidth':1.15,'pdf.fonttype':42,'savefig.bbox':'tight'})
RECORDS={}


def save(fig,name,sources,data=(),note=''):
    OUT.mkdir(parents=True,exist_ok=True)
    path=OUT/(name+'.pdf')
    pages=fig if isinstance(fig,list) else [fig]
    from matplotlib.backends.backend_pdf import PdfPages
    with PdfPages(path,metadata={'CreationDate':None,'ModDate':None}) as pdf:
        for page in pages:
            pdf.savefig(page,bbox_inches='tight')
            plt.close(page)
    RECORDS[name]={'pages':len(pages),'path':'figures/drafts/'+path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
      'sources':sources,'data':[{'path':'figures/drafts/data/'+p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in data],
      'palette':[PURPLE,ORANGE],'note':note}


def base(size=(3.45,2.35)):
    fig,ax=plt.subplots(figsize=size,layout='constrained')
    ax.spines[['top','right']].set_visible(False)
    return fig,ax


def solve_one_group(rho,beta=.0065,Lambda=5e-5,decay=.0766,n0=1):
    c0=beta*n0/(decay*Lambda)
    b=decay-(rho-beta)/Lambda
    c=-(decay*(rho-beta)/Lambda+decay*beta/Lambda)
    d=np.sqrt(b*b-4*c)
    w1,w2=(-b+d)/2,(-b-d)/2
    a1=(rho*n0/Lambda-n0*w2)/(w1-w2)
    a2=n0-a1
    return a1,a2,w1,w2


def legacy():
    fig,ax=base()
    t=np.linspace(0,10,10000)
    for i,k in enumerate((.5,.9,.99)):
        n=.01/(k-1)*np.expm1((k-1)*t/.01)
        ax.plot(t,n,color=COLORS[i],ls=STYLES[i],label=rf'$k_\infty={k:g}$')
    ax.set(xlabel='$t$ [s]',ylabel='$n(t)/S_0$');ax.legend()
    save(fig,'subcrit_mult',['notebooks/lesson_26.ipynb, cells24–26'])

    beta=np.array([.00021,.00142,.00128,.00257,.00075,.00027])
    decay=np.log(2)/np.array([56,23,6.2,2.3,.61,.23]);Lambda=5e-5
    def rhs(y,t):
        rho=.001 if 1<=t<=2 else 0
        return np.r_[((rho-beta.sum())/Lambda)*y[0]+np.sum(decay*y[1:]),-decay*y[1:]+beta*y[0]/Lambda]
    y0=np.r_[1e8,beta*1e8/(decay*Lambda)]
    values=odeint(rhs,y0,t)
    fig,ax=base((3.45,2.7))
    for i in range(7):ax.plot(t,values[:,i],color=COLORS[i],ls=STYLES[i],label='$n(t)$' if i==0 else rf'$C_{i}(t)$')
    ax.set(xlabel='$t$ [s]',yscale='log');ax.legend(ncol=2)
    save(fig,'example_kinetics',['notebooks/lesson_27.ipynb, cells39,49–60'])

    pages=[]
    for end,height in ((.1,3.4),(10,2.5)):
        fig,axes=plt.subplots(2,1,figsize=(3.45,height),layout='constrained')
        for row,sign in enumerate((1,-1)):
            tt=np.linspace(0,end,1000)
            for i,fraction in enumerate((.05,.1,.15,.2)):
                a1,a2,w1,w2=solve_one_group(sign*fraction*.0065)
                label=(r'$\rho_A$' if sign>0 else r'$\rho_B$') if i==2 else rf'$\rho={sign*fraction:g}\beta$'+('\n'+rf'$\omega_1={w1:.4f},\ \omega_2={w2:.1f}$' if end==.1 else '')
                axes[row].plot(tt,a1*np.exp(w1*tt)+a2*np.exp(w2*tt),color=COLORS[i],ls=STYLES[i],label=label)
            axes[row].set(xlabel='$t$ [s]',ylabel='$n(t)/n_0$')
            axes[row].legend(ncol=2,fontsize=6,loc='upper center',bbox_to_anchor=(.5,1.58 if end==.1 else 1.35),handlelength=1.3,columnspacing=.7)
            axes[row].spines[['top','right']].set_visible(False)
        if end==.1:
            # Reserve separate space for both two-line frequency legends and
            # the first subplot's x label, including at printed column size.
            fig.set_layout_engine(None)
            axes[0].set_position([.16,.63,.82,.23])
            axes[1].set_position([.16,.13,.82,.23])
        pages.append(fig)
    save(pages,'traces',['notebooks/lesson_28.ipynb, cell15'],note='Same four trace panels, in two separately flowing column-sized parts; original unknown step labels and frequency annotations retained.')

    a1,a2,w1,w2=solve_one_group(-.5*.0065)
    tt=np.linspace(0,.2,1000)
    fig,ax=base()
    for y,c,ls,label in [(a1*np.exp(w1*tt),PURPLE,':',r'$a_1e^{\omega_1t}$'),(a2*np.exp(w2*tt),ORANGE,'--',r'$a_2e^{\omega_2t}$'),(a1*np.exp(w1*tt)+a2*np.exp(w2*tt),GRAY,'-',r'$n(t)$')]:ax.plot(tt,y,color=c,ls=ls,label=label)
    ax.set(xlabel='$t$ [s]',ylabel='$n(t)/n_0$');ax.legend()
    save(fig,'prompt_drop_illustration',['notebooks/lesson_28.ipynb, cells14,22'],note='Analytic two-exponential solution for rho=-0.5 beta and Lambda=5e-5, redrawn instead of a raster attachment.')

    x=np.linspace(0,10,1000);L=np.sqrt(10)
    zf=10*(1-np.cosh(x/L)/np.cosh(10/L))
    vac=10*(1-np.cosh(x/L)/(np.cosh(10/L)+(2/L)*np.sinh(10/L)))
    fig,ax=base()
    ax.plot(x,zf,color=PURPLE,label='zero flux');ax.plot(x,vac,color=ORANGE,ls='--',label='zero partial current')
    ax.set(xlabel='$x$',ylabel=r'$\phi(x)$');ax.legend(fontsize=6.7)
    save(fig,'slab_bc',['slides/lecture_33.tex','slides/lecture_34.tex'])

    fig,ax=base((3.45,3.1));x=np.linspace(-5,5,1000);D=.5;Sa=.2;L=np.sqrt(D/Sa)
    ks=[0,.25,.5,.75,.9,.99,1.05,1.1,1.15,1.2,1.25]
    for i,k in enumerate(ks):
        if k<=1:
            alpha=np.sqrt((1-k)/L**2);y=(1-np.cosh(alpha*x)/np.cosh(alpha*5))/(D*alpha**2)
        else:
            B=np.sqrt((k-1)/L**2);y=(np.cos(B*x)/np.cos(B*5)-1)/(D*B**2)
        ax.plot(x,y,color=COLORS[i%len(COLORS)],ls=STYLES[i%len(STYLES)],label=rf'${k:g}$')
    ax.set(xlabel='$x$',ylabel=r'$\phi(x)$');ax.legend(title=r'$k_\infty$',ncol=3,fontsize=6,handlelength=1.4,columnspacing=.7)
    save(fig,'multiplying_slab',['notebooks/Lesson_33_and_34_examples.ipynb, cells45–48'])


def captured():
    for meta_path in sorted(DATA.glob('*.json')):
        name=meta_path.stem
        meta=json.loads(meta_path.read_text());arrays=np.load(meta_path.with_suffix('.npz'))
        for a,axis in enumerate(meta['axes']):
            fig,ax=base((3.45,2.55))
            lines=axis['lines']
            for i,line in enumerate(lines):
                color=PURPLE if i==0 else ORANGE
                if line.get('role'):color=PURPLE if line['role']=='fast' else ORANGE
                if name=='lesson38_cell50' and i==2:color=ORANGE
                if name=='lesson39_cell22':color=[GRAY,PURPLE,ORANGE][i]
                label=line['label'];style=line['linestyle'];marker=line.get('marker','None')
                if name=='lesson38_cell46':label=['LHS','RHS',rf'$k_1={arrays[line["key"]+"_x"][0]:.5f}$'][i]
                elif name=='lesson38_cell50':label=['unperturbed','perturbed','_nolegend_'][i]
                elif name in ('lesson39_cell24','lesson39_cell27','lesson39_cell30'):label=['diffusion: vacuum' if name.endswith('24') else 'diffusion','transport'][i]
                if name=='lesson39_cell22' and i==0:style='--'
                ax.plot(arrays[line['key']+'_x'],arrays[line['key']+'_y'],color=color,ls=style,marker=marker,label=label,markersize=3)
            ax.set(xlabel=axis['xlabel'],ylabel=axis['ylabel'],xlim=axis['xlim'],ylim=axis['ylim'],xscale=axis['xscale'],yscale=axis['yscale'])
            if axis['title']:ax.set_title(textwrap.fill(axis['title'],48))
            handles,labels=ax.get_legend_handles_labels()
            if labels:ax.legend(fontsize=6.7)
            save(fig,name,[meta['source']+': cells '+','.join(map(str,meta['cells']))],
                 [meta_path,meta_path.with_suffix('.npz')],meta.get('note',meta.get('method','')))


def main():
    legacy();captured()
    replacements={f'../slides/figures/generated/{name}.pgf':'figures/drafts/'+name+'.pdf' for name in ('subcrit_mult','example_kinetics','traces','prompt_drop_illustration','slab_bc','multiplying_slab')}
    replacements['../slides/figures/generated/prompt_drop_illustration.png']='figures/drafts/prompt_drop_illustration.pdf'
    documents=[]
    for name in ('lesson_26.ipynb','lesson_27.ipynb','lesson_28.ipynb','Lesson_33_and_34_examples.ipynb','lesson_38.ipynb','lesson_39.ipynb'):
        p=ROOT.parents[1]/'notebooks'/name
        documents.append({'path':'../notebooks/'+name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    data_generators=[{'path':'figures/'+name,'sha256':hashlib.sha256((ROOT/name).read_bytes()).hexdigest()} for name in ('capture_notebook_plot_data.py','digitize_two_group_illustrations.py')]
    class_path=ROOT.parent/'ne630handout.cls'
    documents.append({'path':'ne630handout.cls','sha256':hashlib.sha256(class_path.read_bytes()).hexdigest()})
    payload={'data_generators':data_generators,'replacements':replacements,'source_documents':documents,'generator':'figures/build_draft_figures.py','generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'colors':{'purple':PURPLE,'orange':ORANGE},'figures':RECORDS}
    (OUT/'manifest.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
    print(f'Built {len(RECORDS)} vector figures under {OUT}')


if __name__=='__main__':main()
