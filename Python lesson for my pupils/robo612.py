a,b = map(str,input().split())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum = 0
for i in alphabet:
    if i == a and i == b:
        sum += (alphabet.index(i)+1)*2
    elif i == a or i == b:
        sum += (alphabet.index(i)+1)
print(sum)