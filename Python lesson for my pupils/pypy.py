def algorithms_uz(n):
    i = 1
    answer = 0
    while n>=0:
        n-=i
        i += 1
        answer += 1
    print(answer - 1)
n = int(input())
algorithms_uz(n)