a=int(input())
b=int(input())
c=int(input())
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i!=j and j!=k and k!=i:
                print(d[i],d[j],d[k])