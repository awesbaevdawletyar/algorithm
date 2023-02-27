w,h,d=map(int,input().split())
san=w/d*h/d
S=w*h
s=d**2/2*san
ss=S-s
print("%.4f"%ss)