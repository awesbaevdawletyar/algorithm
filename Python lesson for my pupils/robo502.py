n=int(input())
arr=[]
for i in range(n):
    s=int(input())
    arr.append(s)
u=len(arr)
for i in range(u):
    for j in range(u-1-i):
        if arr[j]<arr[j+1]: 
            arr[j],arr[j+1]=arr[j+1],arr[j]
ss=''
for k in arr:
    ss+=str(k)
ss=list(ss)
m=sorted(ss)
s2=''
for b in m:
    s2+=str(b)
print(s2[::-1])