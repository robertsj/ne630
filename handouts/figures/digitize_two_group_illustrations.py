"""Trace the two historical two-group curve illustrations into numerical tables.

The original notebook contains only PNG attachments, not their generating data.
This reads their curve pixels without modifying either source image. Axis
calibration and the approximately one-pixel tracing precision are recorded beside
the data; the new handout plots are vector renderings of those same curves.
"""
from pathlib import Path
from io import BytesIO
import base64
import hashlib
import json
import numpy as np
from PIL import Image

ROOT=Path(__file__).resolve().parent
NOTEBOOK=ROOT.parents[1]/'notebooks/lesson_39.ipynb'
DATA=ROOT/'drafts/data'


def main():
    nb=json.loads(NOTEBOOK.read_text())
    DATA.mkdir(parents=True,exist_ok=True)
    for cell in (10,11):
        name=next(iter(nb['cells'][cell]['attachments']))
        raw=base64.b64decode(nb['cells'][cell]['attachments'][name]['image/png'])
        pixels=np.asarray(Image.open(BytesIO(raw)).convert('RGB')).astype(float)
        h,w=pixels.shape[:2]
        if cell==10:
            x0,x40,y0,y1=107,730,224,88
            ranges=[(107,436,'black',r'$\phi_1^{I}$','-'),(107,436,'red',r'$\phi_2^{I}$','-.'),(438,748,'black',r'$\phi_1^{II}$','--'),(437,748,'red',r'$\phi_2^{II}$',':')]
        else:
            x0,x40,y0,y1=156,1090,330,134
            ranges=[(164,1117,'black','fast','-'),(157,1117,'red','thermal','--')]
        arrays,lines={},[]
        for index,(left,right,color,label,style) in enumerate(ranges):
            r,g,b=pixels[:,:,0],pixels[:,:,1],pixels[:,:,2]
            mask=(np.maximum.reduce([r,g,b])<100) if color=='black' else ((r>160)&(r>g*1.4)&(r>b*1.4))
            mask[:10]=False
            mask[y0+1:]=False
            if cell==10:
                # Exclude labels in the upper-right legend and frame.
                mask[:120,650:]=False
                if color=='black':mask[:80]=False
            else:
                mask[:110,990:]=False
                if color=='black':mask[:120]=False
            xp,yp=[],[]
            previous=134 if cell==11 and color=='black' else None
            for x in range(left,right+1):
                rows=np.flatnonzero(mask[:,x])
                if cell==10 and index==1:rows=rows[rows>195]
                if color=='black' and previous is not None:
                    rows=rows[np.abs(rows-previous)<12]
                if not len(rows):continue
                y=float(np.median(rows))
                xp.append(x);yp.append(y)
                if color=='black':previous=y
            x=(np.array(xp)-x0)/((x40-x0)/40)
            y=(y0-np.array(yp))/(y0-y1)
            key=f'a0_line{index}'
            arrays[key+'_x'],arrays[key+'_y']=x,y
            lines.append({'key':key,'label':label,'linestyle':style,'marker':'None','role':'fast' if color=='black' else 'thermal'})
        name=f'lesson39_cell{cell}'
        np.savez_compressed(DATA/(name+'.npz'),**arrays)
        metadata={'source':'../notebooks/lesson_39.ipynb','source_sha256':hashlib.sha256(NOTEBOOK.read_bytes()).hexdigest(),'cells':[cell],
          'embedded_image_sha256':hashlib.sha256(raw).hexdigest(),'method':'Digitized original curve pixels; source PNG is unchanged.',
          'precision':{'x_cm_per_pixel':40/(x40-x0),'flux_per_pixel':1/(y0-y1),'curve_location_uncertainty_pixels':1},
          'axes':[{'lines':lines,'xlabel':'$x$ [cm]','ylabel':r'$\phi(x)$','title':'','xlim':[-2,43],'ylim':[-0.05,1.58],'xscale':'linear','yscale':'linear'}]}
        (DATA/(name+'.json')).write_text(json.dumps(metadata,indent=2)+'\n')


if __name__=='__main__':main()
