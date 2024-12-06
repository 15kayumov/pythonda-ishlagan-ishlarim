def avto_info(komponiya,model,rangi,korobka,yili,narhi=None):
    avto = {
        'komponiya':komponiya,
        'model':model,
        'rang':rangi,
        'korobka':korobka,
        'yil':yili,
        'narh':narhi
    }
    return avto


print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat

def avto_kirit():
    """foydalanuvchi kiritgan avmatlani birbalo qiladi"""
    while True:
        print("\n Quyidagi ma'lumotlarni kiriting",end='')
        kompaniya=input("Ishlab chiqaruvchi: ")
        model=input("Modeli: ")
        rangi=input("Rangi: ")
        korobka=input("Korobka: ")
        yili=input("Ishlab chiqarilgan yili: ")
        narhi=input("Narhi: ")
        

        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
        
        
        javob = input("Yana avto qo'shasizmi? (yes/no): ")
        if javob=='no':
            break
        return avtolar


def info_print(avto_info):
    """dsffdfqwefsdf"""
    print(f"{avto_info["rang"].title()} {avto_info['komponiya'].upper()}"
          f"{avto_info["model"].upper()} {avto_info['korobka']} korobka"
          f"{avto_info["yil"]}-yil {avto_info['narh']}$")
    