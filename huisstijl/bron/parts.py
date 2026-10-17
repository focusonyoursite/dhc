import logo, txt, json
d=logo.D(); c=logo.D(True)
parts=dict(Dbowl=d[0]+' '+d[1], Dbar=d[2], Htop='M675 0h152v320H675Z', Hbot='M675 521h152v320H675Z', Cbowl=c[0]+' '+c[1], Cbar=c[2])
def lines(layout):
    if layout=='liggend':
        cap=320; x0=1702
        b=txt.ink_bounds('DRACHTSTER','bsd900',cap); d1,_=txt.text_path('DRACHTSTER','bsd900',x0-b[0],320,cap)
        b2=txt.ink_bounds('HOBBY CLUB','bsd900',cap); tr=((b[2]-b[0])-(b2[2]-b2[0]))/(9*cap)
        d2,_=txt.text_path('HOBBY CLUB','bsd900',x0-b2[0],841,cap,tr)
        return dict(l1=d1,l2=d2,w=x0+b[2]-b[0],h=841)
    cap=128; s='DRACHTSTER HOBBY CLUB'; b=txt.ink_bounds(s,'bsd900',cap); tr=(1502-(b[2]-b[0]))/(20*cap)
    y1=841+90+cap; d1,_=txt.text_path(s,'bsd900',-b[0],y1,cap,tr)
    cap2=52; s2='WERKPLAATS SINDS 1957 · DRACHTEN'; b=txt.ink_bounds(s2,'mono500',cap2); tr2=(1502-(b[2]-b[0]))/((len(s2)-1)*cap2)
    y2=y1+60+cap2; d2,_=txt.text_path(s2,'mono500',-b[0],y2,cap2,tr2)
    return dict(l1=d1,l2=d2,w=1502,h=y2+14)
json.dump(dict(parts=parts, staand=lines('staand'), liggend=lines('liggend')), open('parts.json','w'))
