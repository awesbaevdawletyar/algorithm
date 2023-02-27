n = int(input())
even = 0
for i in range(n+2):
      C = 1
      for j in range(1, i+1):
         C = C * (i - j) // j
         if C%2==0 and C!=0:
            even+=1
print(even)