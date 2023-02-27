t=int(input())
for i in range(t):
	a,b,c=map(int,input().split())
    if a==b:
      print('NO')
    elif c%(max(a,b)-min(a,b))==0:
      print('YES')
    else:
      print('NO')