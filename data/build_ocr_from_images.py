from pathlib import Path
import pytesseract,json,re
from PIL import Image,ImageOps
from concurrent.futures import ThreadPoolExecutor,as_completed
ROOT=Path('/mnt/data/miftah_app/assets')
J=[]
for book in ['bourda','idrissiya','barhout']:
 for p in sorted((ROOT/book).glob('*.jpg')):
  try: num=int(p.stem)
  except: continue
  J.append((book,num,p))
def one(x):
 b,n,p=x
 im=Image.open(p).convert('L'); im=ImageOps.autocontrast(im)
 t=pytesseract.image_to_string(im,lang='Arabic',config='--psm 11').replace('\u200f','').replace('\u200e','').strip()
 return {'book':b,'page':n,'text':t,'letters':len(re.findall(r'[\u0600-\u06ff]',t))}
out=[]
with ThreadPoolExecutor(max_workers=12) as ex:
 fs=[ex.submit(one,x) for x in J]
 for i,f in enumerate(as_completed(fs),1):
  try:out.append(f.result())
  except Exception as e: print('err',e)
  if i%30==0: print(i,flush=True)
out.sort(key=lambda x:(x['book'],x['page']))
Path(ROOT.parent/'data'/'ocr-all.json').write_text(json.dumps(out,ensure_ascii=False),encoding='utf8')
print('done',len(out))
