def a(n):
    if n<2:
        return 0
    elif n%2==0:
        return 3*a(n/2)+n/4*(n/2-1)
    else:
        return 2*a((n-1)/2)+a((n+1)/2)+((n-1)/4)*((n+1)/2)
n=int(input())
print(int(a(n+1)))