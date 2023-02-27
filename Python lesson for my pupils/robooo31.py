t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    for j in range(1):
        if c%(max(a,b)-min(a,b))==0:
            print('YES')
        elif a==b:
            print('NO')
        else:
            print('NO')