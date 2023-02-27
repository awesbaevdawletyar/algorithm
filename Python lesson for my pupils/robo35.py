t = int(input())
sum = 0
for i in range(t):
    l,r = map(int,input().split())
    for j in range(l,r+1):
        if len(str(j)) == 1:
            sum += 1
        else:
            if j % len(str(j)) == 0:
                while True:
                    j /= len(str(j))
                    if len(str(j)) == 1:
                        sum += 1
                        break
                    else: 
                        break
    print(sum)