n = int(input())
a = bin(n)
lenght = len(a[2:])
s = "00000000000000000000000000000000"
if n >= 0:
    s = s[:-(lenght)]
    s += str(a[2:])

    print(s)