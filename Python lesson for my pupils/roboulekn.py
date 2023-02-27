s=input()
q=int(input())
x=0
y=0
for i in range(q):
    l,r=map(int,input().split())
    for j in s[l-1:r]:
        print(ord(j),end= " ")
        if ord(j)>=65 and ord(j)>=90:
            x+=1
        elif ord(j)>=97 and ord(j)>=108:
            y+=1
    if x>y:
        print("Katta hariflar")
    else:
        print("Kishik hariflar")