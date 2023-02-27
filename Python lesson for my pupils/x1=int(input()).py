qatar=int(input())
bagana=int(input())
a=[]
for i in range(qatar):
    b=[]
    for j in range(bagana):
        b.append(int(input()))
    a.append(b)
s=0
for i in a:
    print(i)
for i in range(qatar):
    for j in range(bagana):
        s+=a[i][j]
    print(s)   