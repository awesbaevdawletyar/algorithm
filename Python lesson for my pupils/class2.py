class VkAccountInWebSite():
    def __init__(self,name,login_id,password):
        self.__name=name
        self.__login_id=login_id
        self.__password=password
    
    def publicLogin(self):
        self.__loginVk()


    def __loginVk(self):
        if self.__login_id == 123 and self.__password == 456:
            print('Hello '+self.__name)
        return True

vakk=VkAccountInWebSite('Dawlet',123,456)
vakk.publicLogin()
# print(vakk.__name)