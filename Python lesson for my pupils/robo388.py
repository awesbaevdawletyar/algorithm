w,h,d=map(int,input().split())
if d<1 or w<1 or h<1:
    print(0)
else:
    s=(d**2)/2
    e=w/d
    t=h/d
    print("{:.4f}".format(t*e*s))