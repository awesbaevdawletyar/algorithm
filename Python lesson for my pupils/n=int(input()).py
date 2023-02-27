n=int(input())
x=list(map(int,input().split()))
uz=len(x)
count=0
for i in n:
    for j in n:
        if x[i] ==x[j]:
            count+=1
    if count == 1:
         