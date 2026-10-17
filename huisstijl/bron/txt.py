from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
import os
D=os.path.join(os.path.dirname(__file__),'fonts')
_c={}
def font(n):
    if n not in _c: _c[n]=TTFont(os.path.join(D,n+'.ttf'))
    return _c[n]
def capH(n):
    f=font(n); return f['OS/2'].sCapHeight
def text_path(s, fname, x, y, cap, track=0.0):
    """baseline at y, cap = desired cap height in px; track as fraction of cap. returns (d, width)"""
    f=font(fname); gs=f.getGlyphSet(); cmap=f.getBestCmap(); hm=f['hmtx']
    sc=cap/capH(fname); pen=SVGPathPen(gs); cx=0
    for i,ch in enumerate(s):
        g=cmap.get(ord(ch)); 
        if g is None: continue
        tp=TransformPen(pen,(sc,0,0,-sc,x+cx,y)); gs[g].draw(tp)
        cx+=hm[g][0]*sc + (track*cap if i<len(s)-1 else 0)
    return pen.getCommands(), cx
def width(s,fname,cap,track=0.0): return text_path(s,fname,0,0,cap,track)[1]
def ink_bounds(s,fname,cap,track=0.0):
    f=font(fname); gs=f.getGlyphSet(); cmap=f.getBestCmap(); hm=f['hmtx']; sc=cap/capH(fname)
    bp=BoundsPen(gs); cx=0
    for i,ch in enumerate(s):
        g=cmap[ord(ch)]; gs[g].draw(TransformPen(bp,(sc,0,0,-sc,cx,0))); cx+=hm[g][0]*sc+(track*cap if i<len(s)-1 else 0)
    return bp.bounds
