"""Portable static Sites archive, for Windows hosts without Bash."""
import io, json, sys, tarfile
from pathlib import Path
root = Path(__file__).resolve().parent
manifest = json.loads((root / '.openai/hosting.json').read_text(encoding='utf-8'))
manifest['static']['directory'] = 'dist'
with tarfile.open(sys.argv[1], 'w:gz') as archive:
    for path in (root / 'dist').rglob('*'):
        if path.is_file():
            archive.add(path, arcname='dist/' + path.relative_to(root / 'dist').as_posix())
    data = (json.dumps(manifest) + '\n').encode()
    info = tarfile.TarInfo('dist/.openai/hosting.json')
    info.size = len(data)
    archive.addfile(info, io.BytesIO(data))
print('Static archive prepared.')
