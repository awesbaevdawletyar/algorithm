a,b,c,d=map(int,input().split())
x=a**b-c
def Ekub(x,d):
    while x!=0 and d!=0:
        if x>d:
            x=x-d
        else:
            d=d-x
    return x+d
j=Ekub(x,d)
print(j)