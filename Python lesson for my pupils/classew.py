class Person:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
    def get_info(self):
        info=f"{self.fname} {self.lname} " 
        info+= self.age
        return info
class Insan(Person):
    def __init__(self,fname,lname,age,kurs,id,manzil):
        super().__init__(fname,lname,age)
        self.kurs=kurs
        self.id=id
        self.manzil=manzil
    def get_kurs(self):
        return self.kurs 
    def fet_id(self):
        return self.id
class Manzil:
    def __init__(self,uy,rayoni,qala):
        self.uy=uy
        self.rayoni=rayoni
        self.qala=qala
    def get_manzil(self):
        man=f"{self.uy} {self.rayoni}"
        man+=self.qala
        return man
manzil=Manzil('12','Nokis','Nokis')
Adim=Insan('Dawletyar','Awesbaev','19',"2","N000213",manzil)
print(Adim.manzil.get_manzil())