n = int(input())
m = list(map(int,input().split()))

for i in m:
    for j in m:
        if abs(i - j) == 1:
            m.remove(i)
            m.remove(j)

for a in m:
    print(a,end=' ')