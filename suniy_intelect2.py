import random as r

meni=None
uni=None

def tamini_oyin():

    print("1dan 10gacha son o'yladim ,uni topishga harakat qiling.")

    son=r.randint(1,10)
    global meni
    urunishlar=0

    while True:
        urunishlar+=1
        qanday=int(input("Sizning taxmingiz: "))
        if qanday < son:
            print("Siz o'ylagan son kichik.")
        elif qanday > son:
            print("Siz o'ylagan son katta.")
        else:
            print(f"Tabriklayman! Siz {urunishlar} urinishda to'g'ri topdingiz.")
            break
     
    meni=urunishlar




def son_taxmin():
    print("1 dan 10 gacha son o'ylang, men topishga harakat qilaman.")                                                                                  
    kichik, katta = 1, 10
    urinishlar = 0
    global uni

    
    while True:
        urinishlar += 1
        taxmin = (kichik + katta) // 2
        print(f"Menimcha, siz o'ylagan son {taxmin}.")
        javob = input("Bu son to'g'ri(T), katta(+), yoki kichik(-)? ")
        if javob == 'T':
            print(f"Men {urinishlar} urinishda topdim!")
            break
        elif javob == '+':
            kichik = taxmin + 1
        elif javob == '-':
            katta = taxmin - 1
        else:
            print("Noto'g'ri javob. Iltimos, faqat 'T', '+', yoki '-' kiriting.")
    uni=urinishlar
def funkion():
    son_taxmin()
    tamini_oyin()
    if meni<uni:
        print(f"men {uni} urinishda topdim! siz {meni} urinishda topdiz! .siz yutdiz")
    elif meni>uni:
        print(f"men {uni} urinishda topdim! siz {meni} urinishda topdiz! men yutdim")
    else:
        print(f"Men {uni} urinishda topdim! Siz {meni} urinishda topdingiz! Durrang")
funkion()