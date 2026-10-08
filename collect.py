from html.parser import HTMLParser
from pathlib import Path
import json,urllib.request,concurrent.futures,re
class Parser(HTMLParser):
 def __init__(self): super().__init__(); self.items=[]; self.capture=None; self.buf=[]; self.depth=0
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=='img': self.items.append({'type':'img','src':d.get('src','')})
  if t=='a' and '.pdf' in d.get('href',''): self.items.append({'type':'pdf','url':'https:'+d['href'] if d['href'].startswith('//') else d['href']})
  if t in ['h4','p'] and not self.capture:self.capture=t;self.buf=[]
 def handle_data(self,d):
  if self.capture:self.buf.append(d)
 def handle_endtag(self,t):
  if t==self.capture:
   self.items.append({'type':t,'text':' '.join(''.join(self.buf).split())});self.capture=None
p=Parser();p.feed(Path('sources/libros.html').read_text(encoding='utf-8'))
books=[];img=None
for v in p.items:
 if v['type']=='img':img=v['src']
 if v['type']=='h4' and img:
  books.append({'title':v['text'],'cover_source':'https:'+img if img.startswith('//') else img,'paragraphs':[]});img=None
 if v['type']=='p' and books: books[-1]['paragraphs'].append(v['text'])
pdfs=[x['url'] for x in p.items if x['type']=='pdf']
for i,b in enumerate(books):
 b['slug']=['venezuela-bajo-el-sol','el-ingenioso-hidalgo','una-ronda-del-tiempo','cuentos-impertinentes','la-tienda-de-los-muertos','huellas-cifradas','sonetos','ileso-albedrio','reforma-electoral'][i]
 b['pdf_source']=pdfs[i if i<6 else i-1] if i!=6 else None
 b['cover']='assets/covers/'+b['slug']+'.png'
Path('sources/books-original.json').write_text(json.dumps(books,ensure_ascii=False,indent=2),encoding='utf-8')
Path('dist/assets/covers').mkdir(exist_ok=True)
def download(b):
 # The original CDN's crop removes scan margins without changing the real cover.
 data=urllib.request.urlopen(b['cover_source'],timeout=30).read();Path('dist/'+b['cover']).write_bytes(data);return (b['title'],len(data))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
 for x in pool.map(download,books):print(x)
print('PDFS',len(pdfs),'BOOKS',len(books))
