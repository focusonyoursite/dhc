import logo, txt, os
OUT='out'; os.makedirs(OUT,exist_ok=True)
ZW='#2B2828'; WIT='#FFFFFF'; GEEL='#F2B705'; GROEN='#2D6A52'
P=logo.PATH
def svg(w,h,body,title='Drachtster Hobby Club'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {h:g}" width="{w:g}" height="{h:g}" role="img" aria-label="{title}"><title>{title}</title>{body}</svg>\n'
def mark(fill,tx=0,ty=0,s=1):
    t='' if (tx,ty,s)==(0,0,1) else f' transform="translate({tx:g} {ty:g}) scale({s:g})"'
    return f'<path fill="{fill}" fill-rule="evenodd"{t} d="{P}"/>'
def fit(s,fn,cap,width):
    # tracking zodat de tekst precies 'width' breed is (inktbreedte)
    b=txt.ink_bounds(s,fn,cap,0); n=len(s)-1
    return (width-(b[2]-b[0]))/(n*cap), b[0]
files={}
# 1. beeldmerk
for naam,kl in [('zwart',ZW),('wit',WIT),('geel',GEEL),('groen',GROEN)]:
    files[f'dhc-logo-{naam}.svg']=svg(1502,841,mark(kl))
# 2. liggend: tekstregels lijnen uit met de H-blokken (0-320 en 521-841)
def liggend(kl,txtkl=None):
    txtkl=txtkl or kl; cap=320; gap=200; x0=1502+gap
    d1,w1=txt.text_path('DRACHTSTER','bsd900',x0,320,cap,0.0)
    b=txt.ink_bounds('DRACHTSTER','bsd900',cap); d1,w1=txt.text_path('DRACHTSTER','bsd900',x0-b[0],320,cap)
    b2=txt.ink_bounds('HOBBY CLUB','bsd900',cap); tr=((b[2]-b[0])-(b2[2]-b2[0]))/(9*cap)
    d2,_=txt.text_path('HOBBY CLUB','bsd900',x0-b2[0],841,cap,tr)
    W=x0+(b[2]-b[0])
    return svg(W,841,mark(kl)+f'<path fill="{txtkl}" d="{d1} {d2}"/>')
files['dhc-logo-liggend-zwart.svg']=liggend(ZW)
files['dhc-logo-liggend-wit.svg']=liggend(WIT)
# 3. staand: naam op logobreedte + regel eronder
def staand(kl,sub=None):
    sub=sub or kl
    cap=128; tr,bx=fit('DRACHTSTER HOBBY CLUB','bsd900',cap,1502)
    y1=841+90+cap
    d1,_=txt.text_path('DRACHTSTER HOBBY CLUB','bsd900',-bx,y1,cap,tr)
    cap2=52; s2='WERKPLAATS SINDS 1957 · DRACHTEN'
    tr2,bx2=fit(s2,'mono500',cap2,1502)
    y2=y1+60+cap2
    d2,_=txt.text_path(s2,'mono500',-bx2,y2,cap2,tr2)
    return svg(1502,y2+14,mark(kl)+f'<path fill="{kl}" d="{d1}"/><path fill="{sub}" d="{d2}"/>')
files['dhc-logo-staand-zwart.svg']=staand(ZW)
files['dhc-logo-staand-wit.svg']=staand(WIT)
# 4. icoon / avatar (vierkant, ook rond veilig)
def icoon(bg,kl,S=1024,frac=0.62,rond=False,rx=0):
    s=S*frac/1502; h=841*s
    bgel=f'<circle cx="{S/2}" cy="{S/2}" r="{S/2}" fill="{bg}"/>' if rond else f'<rect width="{S}" height="{S}" rx="{rx}" fill="{bg}"/>'
    return svg(S,S,bgel+mark(kl,(S-1502*s)/2,(S-h)/2,round(s,5)))
files['dhc-icoon-zwart.svg']=icoon(ZW,WIT,rx=0)
files['dhc-icoon-geel.svg']=icoon(GEEL,ZW)
files['dhc-icoon-groen.svg']=icoon(GROEN,WIT)
files['dhc-favicon.svg']=icoon(ZW,WIT,S=64,frac=0.84,rx=10)
for k,v in files.items(): open(os.path.join(OUT,k),'w').write(v)
print(len(files))
