class Car:
    def __init__(self,name,year,color):
        self.name=name
        self.year=year
        self.color=color
    def _info(self):
        info=f"{self.name} -->{self.year} -->"
        info+=self.color
        return info

class Person(Car):
    def __init__(self,name,year,color,fname,lname,age,manzil):
        super().__init__(name,year,color)
        self.fname=fname
        self.lname=lname
        self.age=age
        self.manzil=manzil
    
    def first_name(self):
        return self.fname
    def last_name(self):
        return self.lname
    def age_(self):
        return self.age
class Manzil:
    def __init__(self,uy_raqam,walayat,rayon):
        self.uy_raqam=uy_raqam
        self.walayat=walayat
        self.rayon=rayon
    def get_info(self):
        return "{} {} {}".format(self.uy_raqam,self.walayat,self.rayon)
# Dawlet=Person('Spark','2022','Aq','Dawlet','Awesbaev','23')
# print(Dawlet._info())
# print(Dawlet.last_name())
manzil=Manzil('14','Xorazm','Shimbay')
Dawlet=Person('Spark','2022','Aq','Dawlet','Awesbaev','23',manzil)
print(Dawlet.manzil.get_info())