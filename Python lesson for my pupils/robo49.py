import math
def istrue(array):
    i = 1
    while True:
        s = i * (i+1) //2
        array.append(s)
        if s > max(arr):
            break
        i+=1
    return array
t = int(input())
arr = list(map(int,input().split()))
m = []
a = istrue(m)
result = ""
uz=len(arr)
for i in arr:
    if i in a or i==0:
        result+='1'
    else:
        result+='0'
print(result)