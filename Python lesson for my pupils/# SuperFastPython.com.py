n=int(input())
triangle=[]
def paskal(n):
    for i in range(n+1):
        triangle.append([1]+[0]*n)
# for i in triangle:
#     print(i)
    san=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            triangle[i][j]=triangle[i-1][j]+triangle[i-1][j-1]
            if triangle[i][j]%2==0:
                san+=1
    return san
a=paskal(n)
print(a)