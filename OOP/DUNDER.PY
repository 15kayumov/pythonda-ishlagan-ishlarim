from uuid import uuid4
class Avto:     
    """Avtomobil klassi"""
    num_avto = 0
    def init(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.km = km
        self.__id = uuid4()
        Avto.num_avto +=1
    
    def __repr(self):
        return f"aAvto: {self.rang} {self.model} {self.make} {self.id}"
    
    def __eq(self, boshqa_avto):
        "Tenglik"
        return self.narh == boshqa_avto.narh
    
    def lt(self, boshqa_avto):
        "Kichik"
        return self.narh < boshqa_avto.narh
    
    def le(self, boshqa_avto):
        "Kichik yoki teng"
        return self.narh <= boshqa_avto.narh

# avto1 = Avto('gm', 'malibu','qora',2000, 20_000,50)
# avto2 = Avto('gm', 'malibu','qora',2000, 20_000,50)
# print(avto1==avto2)

# x,y=5,10
# print(x<y)

class AvtoSalon:
    """Avtosalon klassi"""
    def init(self,name):
        self.name = name
        self.avtolar = []

    def repr(self):
        return f"{self.name} avtosaloni"
    
    def len(self):
        return len(self.avtolar)
    
    def add_avto(self,*qiymat):
       for avto in qiymat:  
         if isinstance(avto,Avto):
            self.avtolar.append(avto)
         else:
            print("avto obyekt kirit")

salon1 = AvtoSalon("Maxavto: ")
avto1 = Avto('gm', 'malibu','qora',2000, 20_000,50)
avto2 = Avto('gm', 'malibu','qora',2000, 20_000,50)
avto3 = Avto('gm', 'malibu','qora',2000, 20_000,50)


salon1.add_avto(avto1,avto2,avto3)

print(salon1)


# for avto in [avto1, avto2,avto3]:
#        salon1.add_avto(avto)




# print(saalon1)


# print(isinstance('salom', str))

# print(isinstance(9.5 , float))

# print(isinstance(avto1 , Avto))