from pathlib import Path
import json,re
root=Path('/mnt/data/miftah_app')
out=root/'data'
books={'bourda':87,'idrissiya':66,'barhout':34}
idx=[]
for book,n in books.items():
  for p in range(1,n+1):
    f=out/'ocr'/book/f'{p:03d}.txt'
    text=f.read_text(errors='ignore') if f.exists() else ''
    text=re.sub(r'\s+',' ',text).strip()
    idx.append({'book':book,'page':p,'text':text,'source':'OCR arabe — uniquement pour La Bourdah' if book=='bourda' and text else ('source PDF textuelle' if book=='barhout' and text else '')})
(out/'ocr-index.json').write_text(json.dumps(idx,ensure_ascii=False,separators=(',',':')))
print('index',len(idx), 'chars',sum(len(x['text']) for x in idx))
