# n,m=map(int,input().split(':'))
# d=int(input())
# s=n*60+m+d
# h=s//60%24
# m=s%60
# print(('0'+str(h))[-2:]+':'+('0'+str(m))[-2:])

# n,m=input().split(':')
# s = int(input())
# h = (60 * int(n))
# m = int(m)
# x = (h + m + s)%1440
# h1 = x//60
# m1 = x%60
# print(str(h1).rjust(2,"0")+':'+str(m1).rjust(2,"0"))

s=input()

for i in s:
    if i.isdigit():
        print(i,end=" ")