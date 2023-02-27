a=[[4,-5,8],[1,3,-1]]
b=[[-1,5],[-2,-3],[3,4]]
#a+b
#a-b
c=[]
c1=[]
aa=len(a)
s=[]
for i in range(aa):
    d=[]
    d1=[]
    for j in range(aa):
        s[i][j]=0
        s+=a[i][j]*b[j][i]
        d.append(s)
    c.append(d)
    s=0
for i in c:
    print(i)

