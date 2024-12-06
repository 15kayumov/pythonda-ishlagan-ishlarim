import random

son=random.randint(1,11)

sanovchi=0

while True:
    sanovchi+=1
    taxmin=int(input("salom man son o'yladim siz shu sonni topa olasizmi?? taxminiz: "))
    if taxmin>son:
        print("kechirasiz siz o'ylagan so'z juda katta")
    elif taxmin<son:
        print("kechirasiz siz o'ylagan so'z juda kichik")
    else:
        print("tabeiklaymiz siz o'lagan son to'g'ri chiqdi :>")
        print(f"siz bu sonni {sanovchi} martada o'ylab topdiz")
        break