def n(n):
    s=''
    while n>0:
        num=n%10
        s+=str(num)
        n=n//10
    return s
a=int(input())
print(n(a)) 