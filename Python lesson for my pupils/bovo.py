n,m=map(int,input().split())
if n>1 and m<100 and (m+j)<100:
    j=n-2*m
    print()
else:
    print(-1)