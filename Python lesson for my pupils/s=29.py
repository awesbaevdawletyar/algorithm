s=int(input())
uz=len(str(s))
birlik=''
onliq=''
juzlik=''
if uz==2:
    ss=s-9
    birlik+=str(ss)
    ss=s-8
    onliq+=str(ss)
    ss=s-7
    juzlik+=str(ss)
print(juzlik+onliq+birlik)
