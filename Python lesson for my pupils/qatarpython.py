
qatar=input()
s=0
a=0
for i in qatar:
    if i=='U':
        s+=1
    else:
        s+=-1
    if s==0:
        a+=1
print(a-1)