"""Recover numerical line data for handout figures from the original notebooks.

Writes only under this directory. Ordinary figure builds use the saved NPZ/JSON
and do not require detran. Use the scientific Python environment for --refresh.
The two historical two-group illustrations are digitized separately, not solved
with guessed material data. Notebook code/content itself is never modified.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
DATA = ROOT / 'drafts' / 'data'


def capture():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np

    DATA.mkdir(parents=True, exist_ok=True)

    def notebook(name):
        p = REPO / 'notebooks' / name
        return json.loads(p.read_text()), hashlib.sha256(p.read_bytes()).hexdigest()

    def save(fig, name, source, digest, cells, note=''):
        arrays, axes = {}, []
        for a, ax in enumerate(fig.axes):
            lines = []
            for i, line in enumerate(ax.lines):
                x, y = np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float)
                key = f'a{a}_line{i}'
                arrays[key+'_x'], arrays[key+'_y'] = x, y
                lines.append({'key':key, 'label':line.get_label(), 'linestyle':line.get_linestyle(), 'marker':line.get_marker()})
            axes.append({'lines':lines, 'xlabel':ax.get_xlabel(), 'ylabel':ax.get_ylabel(), 'title':ax.get_title(), 'xlim':ax.get_xlim(), 'ylim':ax.get_ylim(), 'xscale':ax.get_xscale(), 'yscale':ax.get_yscale()})
        np.savez_compressed(DATA/(name+'.npz'), **arrays)
        (DATA/(name+'.json')).write_text(json.dumps({'source':source, 'source_sha256':digest, 'cells':cells, 'note':note, 'axes':axes},indent=2)+'\n')
        plt.close(fig)

    nb, digest = notebook('lesson_38.ipynb')
    scope = {'__name__':'__handout_recovery__'}
    for index, cell in enumerate(nb['cells']):
        if cell['cell_type'] != 'code' or not ''.join(cell['source']).strip():
            continue
        exec(compile(''.join(cell['source']),f'lesson_38.ipynb:cell{index}','exec'),scope)
        if index in (46,50):
            save(plt.gcf(),f'lesson38_cell{index}','../notebooks/lesson_38.ipynb',digest,list(range(index+1)),
                 'Original source recomputed; the handout retains its original listings and historical stored text results.')
        plt.close('all')

    nb,digest = notebook('lesson_39.ipynb')
    scope = {'__name__':'__handout_recovery__'}
    for index in (19,21):
        exec(compile(''.join(nb['cells'][index]['source']),f'lesson_39.ipynb:cell{index}','exec'),scope)
        if index==19:
            save(plt.gcf(),'lesson39_cell19','../notebooks/lesson_39.ipynb',digest,[19])
        plt.close('all')
    # Suppress progress logging while leaving the original equations/settings.
    original_input=scope['get_input']
    def quiet_input():
        inp=original_input()
        inp.put_int('inner_print_level',0)
        inp.put_int('outer_print_level',0)
        return inp
    scope['get_input']=quiet_input
    for index in (22,24,25,27,28,30,31):
        if index==27:
            # The stored plot is a left-edge 1-cm source, not the stale uniform
            # source_map left in the notebook. This reproduces the stated example.
            scope['source_map']=[1]+[0]*19
        exec(compile(''.join(nb['cells'][index]['source']),f'lesson_39.ipynb:cell{index}','exec'),scope)
        save(plt.gcf(),f'lesson39_cell{index}','../notebooks/lesson_39.ipynb',digest,[19,21,index],
             'For cells27/28, source_map=[1]+[0]*19 reproduces the stored localized-source illustration; notebook code is unchanged.' if index in (27,28) else '')
        plt.close('all')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh',action='store_true',help='execute source notebook code to recover line data')
    parser.add_argument('--detran-python',default='/home/robertsj/Research/detran/pydetran/build')
    parser.add_argument('--detran-lib',default='/home/robertsj/Research/detran/install/lib')
    parser.add_argument('--worker',action='store_true',help=argparse.SUPPRESS)
    args=parser.parse_args()
    if args.worker:
        capture()
    elif args.refresh:
        env=os.environ.copy()
        env['PYTHONPATH']=args.detran_python+os.pathsep+env.get('PYTHONPATH','')
        env['LD_LIBRARY_PATH']=args.detran_lib+os.pathsep+env.get('LD_LIBRARY_PATH','')
        env['MPLCONFIGDIR']=str(ROOT/'.mplconfig')
        subprocess.run([sys.executable,str(Path(__file__).resolve()),'--worker'],env=env,cwd=ROOT,check=True)
    else:
        parser.error('use --refresh to explicitly recover data; normal builds use build_draft_figures.py')


if __name__=='__main__':main()
