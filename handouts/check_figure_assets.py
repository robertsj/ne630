"""Validate the local, reproducible renderings used by the L25--39 drafts."""
from functools import lru_cache
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parent


def _inside_figures(path,root):
    path=path.resolve()
    if not path.is_relative_to((root/'figures').resolve()):
        raise ValueError(f'handout figure is outside handouts/figures: {path}')
    return path


@lru_cache(maxsize=None)
def catalog(root=ROOT):
    root=Path(root).resolve()
    value=json.loads((root/'figures/drafts/manifest.json').read_text())
    for entry in [{'path':value['generator'],'sha256':value['generator_sha256']}]+value['source_documents']+value.get('data_generators',[]):
        path=(root/entry['path']).resolve()
        if hashlib.sha256(path.read_bytes()).hexdigest()!=entry['sha256']:
            raise ValueError(f'figure source changed; regenerate figures: {entry["path"]}')
    if value['colors']!={'purple':'#512888','orange':'#CA7C1B'}:
        raise ValueError('draft figure palette differs from the course colors')
    for record in value['figures'].values():
        for entry in [record]+record['data']:
            path=_inside_figures(root/entry['path'],root)
            if hashlib.sha256(path.read_bytes()).hexdigest()!=entry['sha256']:
                raise ValueError(f'stale or changed handout figure/data: {entry["path"]}')
    return value


def figure_target(path,root=ROOT):
    """Map an original slide asset to its approved local rendering."""
    root=Path(root).resolve()
    path=Path(path).resolve()
    data=catalog(root)
    mapping={(root/a).resolve():(root/b).resolve() for a,b in data['replacements'].items()}
    path=mapping.get(path,path)
    return _inside_figures(path,root)


def notebook_rendering(asset,root=ROOT):
    """Keep original PNG evidence, but return the checked local vector redraw."""
    root=Path(root).resolve()
    original=_inside_figures(root/asset['path'],root)
    rendered=asset.get('rendering')
    if not rendered:return original
    data=catalog(root)
    record=data['figures'][rendered]
    return _inside_figures(root/record['path'],root)


def check_layout_and_paths(root=ROOT):
    import re
    root=Path(root).resolve()
    for n in range(25,40):
        text=(root/f'lesson_{n}_handout.tex').read_text()
        if text.count(r'\begin{handoutflow}')!=1 or text.count(r'\end{handoutflow}')!=1:
            raise ValueError(f'L{n} must use the shared two-column handoutflow environment')
        for name in re.findall(r'\\(?:includegraphics|input)(?:\[[^\]]*\])?\s*\{([^{}]*)\}',text):
            _inside_figures(root/name,root)


if __name__=='__main__':
    data=catalog()
    check_layout_and_paths()
    print(f'Verified {len(data["figures"])} local vector figures and two-column draft sources.')
