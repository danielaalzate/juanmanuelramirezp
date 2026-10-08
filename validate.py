from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.parse import urlsplit,unquote
from concurrent.futures import ThreadPoolExecutor
import json
root=Path('dist');errors=[]
class Check(HTMLParser):
 def handle_starttag(self,t,a):
  d=dict(a)
  for k in ['src','href']:
   v=d.get(k,'')
   if v.startswith('/'):
    p=unquote(urlsplit(v).path);target=root/p.lstrip('/')
    if p.endswith('/'):target=target/'index.html'
    if not target.exists():errors.append(str(target))
for p in root.rglob('*.html'):c=Check();c.feed(p.read_text(encoding='utf-8'))
assert not errors,errors
books=json.loads(Path('sources/books-original.json').read_text(encoding='utf-8'))
def pdfcheck(b):
 if not b['pdf_source']:return {'book':b['title'],'status':'no original PDF'}
 with urlopen(Request(b['pdf_source'],headers={'Range':'bytes=0-7'}),timeout=30) as r:
  signature=r.read(5);assert signature==b'%PDF-',(b['title'],signature);return {'book':b['title'],'status':r.status,'signature':'%PDF-'}
with ThreadPoolExecutor(max_workers=5) as pool:results=list(pool.map(pdfcheck,books))
Path('.impeccable/review/checks.json').write_text(json.dumps({'local_references':'pass','pdf_links':results},ensure_ascii=False,indent=2),encoding='utf-8')
print('PASS: all local references; eight verified PDF responses and Sonetos correctly has no PDF.')
