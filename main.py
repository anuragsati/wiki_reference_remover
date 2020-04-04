import re
from pathlib import Path


filename = input("Filename : ")
p = Path(Path.cwd() / filename)
text = p.read_text()

#actual regex 
r = re.compile(r'\[\d*\]')

ans = r.sub('', text)

p.write_text(ans)