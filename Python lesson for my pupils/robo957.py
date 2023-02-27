n = int(input())
s=0
for i in range(1,n+1):
    s+=i*(i+1)//2
print(s%1000000007)