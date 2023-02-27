class New():
    def __init__(self,name):
        self.name=name

    def __str__(self):  #__repr__(self)
        return self.name
new_obj=New('Dawka')
print(new_obj)