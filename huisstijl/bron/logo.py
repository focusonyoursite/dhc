import math
W,H=1502,841
r=420.5; cx=100; cy=420.5
dy=math.sqrt(r*r-(482-cx)**2); y1=round(cy-dy,2); y2=round(cy+dy,2)
def D(m=False):
    X=(lambda x: round(W-x,2)) if m else (lambda x:x)
    s=0 if m else 1
    o=f"M{X(0)} 0H{X(100)}A{r} {r} 0 0 {s} {X(482)} {y1}V{y2}A{r} {r} 0 0 {s} {X(100)} {H}H{X(0)}Z"
    h=f"M{X(0)} 199H{X(126)}A203 203 0 0 {s} {X(126)} 605H{X(0)}Z"
    bx=X(521) if m else 482
    b=f"M{bx} 0h39V{H}h-39Z"
    return o,h,b
d=D(); c=D(True)
HH="M675 0h152v320H675ZM675 521h152v320H675Z"
PATH=" ".join([d[0],d[1],d[2],HH,c[0],c[1],c[2]])
if __name__=="__main__": print(PATH)
