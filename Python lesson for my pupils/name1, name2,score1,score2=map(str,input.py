name1, name2,score1,score2=map(str,input().split())
m=int(input())
s=0
if name1=="Real_Madrid":
    if int(score1)>int(score2):
        s+=int(score1)+m+10
    elif int(score1)==int(score2):
        s+=int(score1)+m+5
    else:
        s+=int(score1)+m+2
else:
    if int(score1)>int(score2):
        s+=int(score1)+m+10
    elif int(score1)==int(score2):
        s+=int(score1)+m+5
    else:
        s+=int(score1)+m+2
print(s)