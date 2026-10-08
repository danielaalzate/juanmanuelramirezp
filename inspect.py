from html.parser import HTMLParser
from pathlib import Path
class P(HTMLParser):
 def handle_starttag(self,t,a):
  d=dict(a)
  if t in ['img','a','iframe','h4','h1','h2']: print(t,{k:v for k,v in d.items() if k in ['src','href','data-src','alt','class']})
for name in ['libros','blog']:
 print('\nPAGE',name); p=P();p.feed(Path('sources/'+name+'.html').read_text(encoding='utf-8'))
