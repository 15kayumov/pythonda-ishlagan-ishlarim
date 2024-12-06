import uuid

# class Talaba:
#     def __init__(self,ism,familya,yil):
#         """talabaning xususiyatlari"""
#         self.ism=ism
#         self.familya=familya
#         self.yil=yil
#     def tanishtir(self):
#         print(f"mening ismim {self.ism} familyam {self.familya} yilim esa {self.yil}")
#     def nimadir(self):
#         pass
# talaba1=Talaba('abdullo',"Rajabov",2009) 
# talaba1.tanishtir()

# _________________________________________________________---------

# class Univer:
#     def __init__(self,ism,familya,yil,email):
#         """talabaning xususiyatlari"""
#         self.ism=ism
#         self.familya=familya
#         self.yil=yil
#         self.email=email
#     def tanishtir(self):
#         print(f"mening ismim {self.ism} familyam {self.familya} yilim {self.yil} email {self.email}")
#     def nimadir(self):
#         pass
# talaba1=Univer('abdullo',"Rajabov",2009,'abdullo123@gmail.com') 
# talaba1.tanishtir()
# _________________________________________________________---------
# class Univer:
#     def __init__(self,ism,familya,yil,email):
#         """talabaning xususiyatlari"""
#         self.ism=ism
#         self.familya=familya
#         self.yil=yil
#         self.email=email
#     def get_info(self):
#         print(f"mening ismim {self.ism} familyam {self.familya} yilim {self.yil} email {self.email}")
    

# talaba1=Univer('abdullo',"Rajabov",2009,'abdullo123@gmail.com')
# talaba2=Univer('umid',"qayumov",2009,'imid113@gmail.com')
# talaba3=Univer('saddulll',"Rajabov",2009,'saddullo@gmail.com')
# talaba1.get_info()
# talaba2.get_info()
# talaba3.get_info()
# _________________________________________________________---------
# class Univer:
#     def __init__(self,ism,familya,yil,email):
#         """talabaning xususiyatlari"""
#         self.ism=ism
#         self.familya=familya
#         self.yil=yil
#         self.email=email
#  _________________________________________________________---------
# vorislik va palimarfizm

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def init(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil



class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil,idraqam=uuid.uuid4()):
        super().init(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
  
    def get_id(self):
        return self.idraqam
    
    def get_bosqich(self):
        return self.bosqich

talaba = Talaba('ali','valiyev','fb12345', 2000,)
print(talaba.get_info())
print(talaba.get_id())



# print(uuid.uuid4())

