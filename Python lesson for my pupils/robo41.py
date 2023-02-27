def funk(n,a):
    san=0
    for i in range(n):
        for j in range(n):
            if i<j and a[i]>2*a[j]:
                san+=1          
    return san
n1=int(input())
a1=list(map(int,input().split()))
a=funk(n1,a1)
print(a)