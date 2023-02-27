a=[[1,2,3],[1,2,3],[1,2,3]]
b=[[3,2,1],[3,2,1],[3,2,1]]
c=[]
aa=len(a)
bb=len(b)
for i in range(aa):
    d=[]
    for j in range(aa):
        d.append(a[i][j]-b[i][j])
    c.append(d)
for i in c:
    print(i)        
