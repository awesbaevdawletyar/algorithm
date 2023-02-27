import random
n=int(input())
list=[]
for i in range(n):
    list.append(random.randint(1,100))
print(list)
for i in range(n-1):
    for j in range(n-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print(list)