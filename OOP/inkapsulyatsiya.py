from uuid import uuid4
class Avto:
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
       
    
    def get_km(self):
        return self.__km
    
    def add_km(self,km):
        if km>=0:
            self.__km += km
        else:
            print("mashinani km kamaytirib bulmaydi")


avto1 = Avto("gm",'malibu','qora',2000, 20000, 50)
avto1.add_km(20)

print(avto1.get_km())
