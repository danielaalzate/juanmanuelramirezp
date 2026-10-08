import urllib.request,re,json
from pathlib import Path
from PIL import Image
Path('dist/assets/fonts').mkdir(exist_ok=True)
for key,url in [('display','https://fonts.googleapis.com/css2?family=Libre+Caslon+Display&display=swap'),('body','https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap')]:
 css=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})).read().decode();Path('sources/'+key+'-font.css').write_text(css)
 urls=re.findall(r'url\((https[^)]+)\)',css)
 for i,u in enumerate(dict.fromkeys(urls)):
  ext='woff2' if '.woff2' in u else 'ttf';Path('dist/assets/fonts/'+key+'-'+str(i)+'.'+ext).write_bytes(urllib.request.urlopen(u).read())
 print(key,len(urls),[u.split('.')[-1] for u in urls])
books=json.loads(Path('sources/books-original.json').read_text(encoding='utf-8'))
for b in books:
 im=Image.open('dist/'+b['cover']); bbox=im.getbbox();b['bounds']=bbox;b['size']=im.size
Path('sources/books-original.json').write_text(json.dumps(books,ensure_ascii=False,indent=2),encoding='utf-8')
