def a(n):
    c=1
    for i in range(1,n):
        c*=i
    return c
def b(k):
    d=1
    for i in range(1,k+1):
        d*=i
    return d
def m(n,k):
    x=1
    for i in range(1,n+k-1):
        x*=i
    return x

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    result=(m(n,k)//(b(k)*a(n)))%(10**9+7)
    print(result)
