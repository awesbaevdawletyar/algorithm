# # OOP - Object orienter programming 
# # class object
# # attribut   noun  
# # methods  verb hareketler

# class Mashina:
#     def __init__(self,ati,jili,reni):
#         self.ati= ati
#         self.jili = jili
#         self.reni=reni
#     def get_name(self):
#         return self.ati
#     def get_info(self):
#         return f"Mashinin ati:{self.ati},Mashinanin jili:{self.jili},Mashinanin reni:{self.reni}"
#     def age(self):
#         return 2022-self.jili

# Spark=Mashina("Spark",2020,"Aq")
# # print(Spark.get_info())
# # print(Spark.age())
# print(Spark.get_name())
# # Matiz=Mashina("Matiz",2010,'qara')
# # Spark.jili=2011
# # Spark.reni='Qara'
# # # print(Spark.jili)
# # # print(Spark.reni)
# # print(Spark.jili)
# # print(Spark.reni)



# class Person:
#     def __init__(a,fname,lname,year):
#         a.fname=fname
#         a.lname=lname
#         a.year=year
#     def get_info(a):
#         return f"Ati:{a.fname},Familyasi:{a.lname},Jasi:{a.year}"
#     def jasi(a):
#         return 2022-a.year
# Dawlet=Person("Dawlet",'Awesbaev',1999)

# print(Dawlet.get_info())
# print(Dawlet.jasi())

class Ameller:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def qosiw(self):
        return self.a+self.b
    def aliw(self):
        return self.a-self.b
a1=int(input())
b1=int(input())
qosiw1=Ameller(a1,b1)
print(qosiw1.qosiw())