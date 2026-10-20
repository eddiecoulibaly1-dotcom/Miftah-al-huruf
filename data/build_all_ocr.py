import fitz, pytesseract, json, re, sys, os
from PIL import Image, ImageOps
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

ROOT=Path('/mnt/data/miftah_app')
SOURCES={
 'bourda':'/mnt/data/miftah_sources/AL-Bourda_Cheikh Samba Diagne.pdf',
 'idrissiya':'/mnt/data/miftah_sources/34832145-الروضة-السندسية-في-الاسماء-الادريسية-السهرورية.pdf',
 'barhout':'/mnt/data/miftah_sources/Livre Barhout(1).pdf',
}
OUT=ROOT/'data'/'ocr-all.json'

def process(args):
    book,pno,pdfpath=args
    doc=fitz.open(pdfpath)
    page=doc[pno]
    pix=page.get_pixmap(dpi=160, colorspace=fitz.csGRAY, alpha=False)
    im=Image.frombytes('L',[pix.width,pix.height],pix.samples)
    im=ImageOps.autocontrast(im)
    results=[]
    for psm in (6,11):
        txt=pytesseract.image_to_string(im,lang='Arabic',config=f'--psm {psm}')
        txt=txt.replace('\u200f','').replace('\u200e','').strip()
        # confidence
        data=pytesseract.image_to_data(im,lang='Arabic',config=f'--psm {psm}',output_type=pytesseract.Output.DICT)
        cs=[]
        for c in data.get('conf',[]):
            try:
                c=float(c)
                if c>=0: cs.append(c)
            except: pass
        conf=sum(cs)/len(cs) if cs else 0
        letters=len(re.findall(r'[\u0600-\u06ff]',txt))
        results.append((conf,letters,txt,psm))
    results.sort(key=lambda x:(x[0],x[1]),reverse=True)
    best=results[0]
    return {'book':book,'page':pno+1,'text':best[2],'confidence':round(best[0],1),'letters':best[1], 'alternatives':[{'psm':r[3],'confidence':round(r[0],1),'text':r[2]} for r in results[1:]]}

def main():
    jobs=[]
    for book,pdf in SOURCES.items():
        doc=fitz.open(pdf)
        for pno in range(len(doc)): jobs.append((book,pno,pdf))
    out=[]
    workers=min(4,os.cpu_count() or 2)
    print('jobs',len(jobs),'workers',workers,flush=True)
    with ProcessPoolExecutor(max_workers=workers) as ex:
        futs=[ex.submit(process,j) for j in jobs]
        for i,f in enumerate(as_completed(futs),1):
            try: out.append(f.result())
            except Exception as e: print('ERR',e,file=sys.stderr)
            if i%10==0: print(i,flush=True)
    out.sort(key=lambda x:(x['book'],x['page']))
    OUT.write_text(json.dumps(out,ensure_ascii=False),encoding='utf-8')
    print('wrote',OUT,len(out))

if __name__=='__main__': main()
