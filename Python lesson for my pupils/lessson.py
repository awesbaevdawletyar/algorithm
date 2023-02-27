# lists=[1,2,3,4,5,6,10,123]
# print(sum(lists))
# s=0
# for i in lists:
#     if i%2==1:
#         s+=i
# print(s)
# import math
# print(math.log(math.e))
# x=float(input())

# if x<1:
#     print("%.2f"%(1/(x*x)))
# elif x>=-1 and x<-2:
#     print("%.2f"%(x*x))
# elif x>=2:
#     print(4)

# from math import *
# a,b,c,d,x=map(float,input().split())
# a=int(a)
# b=int(b)
# c=int(c)
# d=int(d)
# e=a*x**2+b*x+c
# f=x*a**3+a**2+a**(b-c)
# g=cos(abs((a*x+b)/(c*x+d+2**c)))
# y2=e/f+g
# print("%.2f"%y2)

# a=int(input())
# print(f'The next number for the number {a} is {a+1}.')
# print(f'The previous number for the number {a} is {a-1}.')
a,b=map(int,input().split())
print(10-a,abs(a-b))