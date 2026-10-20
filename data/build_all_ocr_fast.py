import fitz,pytesseract,json,re,os
from PIL import Image,ImageOps
from concurrent.futures import ProcessPoolExecutor,as_completed
from pathlib import Path
root=Path('/mnt/data/miftah_sources')
S={'bourda':root/'AL-Bourda_Cheikh Samba Diagne.pdf','idrissiya':next(root.glob('34832145*.pdf')),'barhout':root/'Livre Barhout(1).pdf'}
def one(a):
 b,p,path=a; doc=fitz.open(str(path)); pix=doc[p].get_pixmap(dpi=130,colorspace=fitz.csGRAY,alpha=False); im=Image.frombytes('L',[pix.width,pix.height],pix.samples); im=ImageOps.autocontrast(im)
 t=pytesseract.image_to_string(im,lang='Arabic',config='--psm 11').replace('\u200f','').replace('\u200e','').strip()
 return {'book':b,'page':p+1,'text':t,'letters':len(re.findall(r'[\u0600-\u06ff]',t))}
J=[]
for b,p in S.items():
 d=fitz.open(str(p))
 for i in range(len(d)):J.append((b,i,p))
out=[]
with ProcessPoolExecutor(max_workers=8) as ex:
 fs=[ex.submit(one,j) for j in J]
 for i,f in enumerate(as_completed(fs),1):
  try:out.append(f.result())
  except Exception as e: print('err',e)
  if i%20==0: print(i,flush=True)
out.sort(key=lambda x:(x['book'],x['page']))
Path('/mnt/data/miftah_app/data/ocr-all.json').write_text(json.dumps(out,ensure_ascii=False),encoding='utf8')
print('done',len(out))
