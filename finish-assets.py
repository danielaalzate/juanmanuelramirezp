from pathlib import Path
from PIL import Image
import urllib.request,re,json
src=Path(r'C:\Users\retro\.codex\generated_images\01a10872-cc25-7223-8766-536c941d16c8\exec-bc23e53f-a571-4d04-bc73-8be0b919384c.png')
im=Image.open(src);im.save('dist/assets/estudio.webp','WEBP',quality=90)
Path('sources/hero-provenance.json').write_text(json.dumps({'kind':'generated illustrative video poster','source':str(src),'description':'Juan Manuel writing in an illustrative study. Not a real recording or his verified real study.'},ensure_ascii=False,indent=2))
u='https://i.ytimg.com/vi/DTZzfXQgzh8/hqdefault.jpg'
data=urllib.request.urlopen(u,timeout=25).read();Path('sources/entrevista.jpg').write_bytes(data);Image.open('sources/entrevista.jpg').save('dist/assets/entrevista.webp','WEBP',quality=90)
html=urllib.request.urlopen('https://juanmanuelramirezescritor.com/inicio').read().decode();Path('sources/inicio.html').write_text(html,encoding='utf-8')
pos=html.find('Inscríbete');ids=re.findall(r'id="([^"]+)"',html[:pos]);print('SUBSCRIBE',ids[-8:]);print('Hero size',im.size)
