n = int(input())
s = str(input())
k,q,t = 0,0,0
for i in s:
    t += 1
    if i == "U":
        k+=1
    else:
        k-=1
    if k==0 and s[t-1] == "U":
        q+=1
print(q)