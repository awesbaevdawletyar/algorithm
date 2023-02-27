n=int(input())
m=str(n//1000)
m1=str(n%1000)
uz=len(m)
s=0
s1=0
for i in m:
    s+=int(i)
for j in m1:
    s1+=int(j)
if s==s1:
    print('YES')
else:
    print('NO')