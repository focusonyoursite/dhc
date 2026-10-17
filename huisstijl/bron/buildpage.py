import json, os, urllib.parse, logo
s=open('page.src.html').read()
parts=open('parts.json').read()
anim=open('logo-anim.js').read().split('\n',1)[1]  # zonder eigen DHC_PARTS-regel
pat=open('patterns.js').read()
V={f:open('out/'+f).read().strip() for f in os.listdir('out') if f.endswith('.svg')}
fav='data:image/svg+xml,'+urllib.parse.quote(V['dhc-favicon.svg'])
s=s.replace('/*FAVICON*/',fav).replace('/*PATH*/',logo.PATH).replace('/*PARTS*/','const DHC_PARTS = '+parts+';').replace('/*ANIM*/',anim).replace('/*PAT*/',pat).replace('/*VARIANTS*/',json.dumps(V))
os.makedirs('page',exist_ok=True); open('page/dhc-huisstijl.html','w').write(s); print(len(s))
