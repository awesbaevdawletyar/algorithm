n=int(input())
m=[]
for i in range(1, n + 1):
    m.append(int(input()))
for k in m:
    s = 0
    for j in range(2, k+1, 2):
        if k%j == 0:
            s+= 1
            j+=j*2
    print(s)