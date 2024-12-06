# car_0 = {'model':'ferari',
#           'rang':'qizil' ,
#           'yili': 2000
#           }

# print(car_0['model'])
# print(car_0['rang'])
# print(car_0['yili'])

# car_0 = {'model':'ferari',
#           'rang':'qizil' ,
#           'yili': 2000
#           }

# car_0['kurs'] = 5
# car_0['fakukltet'] = 'infarmatika'

# print(car_0)


# teelefonlar = {
#     'ali': 'iphone x',
#     'vali':'samsung',
#     'alish':'matorolla',

# }
# phone = teelefonlar['ali']
# print(f"alining telefoni {phone}")


# phone = teelefonlar.get('ali','bunday ism mavjud emas')
# print(phone)

# oilam={
#     '1-odam':'dadam',
#     '2-odam':'onam',
#     '3-odam':'opam',
#     '4-odam':'man'
# }

# malumot=oilam['1-odam']

# print(f"mening {malumot} ismlari Sayfillo.\n {malumot} 1973-yilning 13-avgustida tug'ilganlar ")

# taomlar={
#     '1-taom':'osh',
#     '2-taom':'makar on',
#     '3-taom':'shashlik',
# }

# ism1=taomlar['1-taom']
# ism2=taomlar['2-taom']
# ism3=taomlar['3-taom']


# print(f"abdulloning sevimli taomi {ism1} ")
# print(f"sadullo sevimli taomi {ism2} ")
# print(f"umid sevimli taomi {ism3} ")

# phyton={
#     '1-kod':'float',
#     '2-kod':'intijir',
#     '3-kod':'stringfy',
#     '4-kod':'if else',
# }


# kod1=phyton['1-kod']
# kod2=phyton['2-kod']
# kod3=phyton['3-kod']
# kod4=phyton['4-kod']

# print(f"{kod1} ni manosi ildizini chiqorib beradi")
# print(f"{kod2} ni manosi stringli gapni ichiga son tiqadi  ")
# print(f"{kod4} ni manosi agar bilan aksan")
                                                  
# ___________________________________________________
# oilam={
#     '1-odam':'dadam',
#     '2-odam':'onam',
#     '3-odam':'opam',

# }

# malumot1=oilam['1-odam']
# malumot2=oilam['2-odam']
# malumot3=oilam['3-odam']




# taomlar={
#     '1-taom':'osh',
#     '2-taom':'makar on',
#     '3-taom':'shashlik',
# }

# ism1=taomlar['1-taom']
# ism2=taomlar['2-taom']
# ism3=taomlar['3-taom']


# print(f"{malumot1} sevimli taomi {ism1} ")
# print(f"{malumot2} sevimli taomi {ism2} ")
# print(f"{malumot3} sevimli taomi {ism3} ")
# ___________________________________________________

# phyton={
#     '1-kod':'float',
#     '2-kod':'intijir',
#     '3-kod':'stringfy',
#     '4-kod':'if else',
# }


# kod1=phyton['1-kod']
# kod2=phyton['2-kod']
# kod3=phyton['3-kod']
# kod4=phyton['4-kod']

# print(f"{kod1} ni manosi ildizini chiqorib beradi")
# print(f"{kod2} ni manosi stringli gapni ichiga son tiqadi  ")
# print(f"{kod4} ni manosi agar bilan aksan")

# savol='kalit soz kiriting: '


# while True:
#     a=input(savol)
#     if a=={kod2}:
#         print(f'{kod2} ning manosi stringli gapni ichiga son tiqadi')
#     elif a=={kod1}:
#         print(f'{kod1} ning manosi ildizini chiqorib beradi')
#     elif a=={kod4}:
#         print(f'{kod4} ni manosi agar bilan aksan"')
#     else:
#         print('kalit soz kiritind!!')

# lugat = {
#     "Boolean": "Mantiqiy qiymat",
#     "Float": "O'nlik son",
#     "For": "Biron amalni qayta-qayta bajarish tsikli",
#     "If": "Shartlarni tekshirish operatori",
#     "Integer": "Butun son",
#     "List": "Elementlar ro'yxati",
#     "Dictionary": "Kalit-qiymat juftligi",
#     "String": "Matnli qiymat",
#     "Tuple": "O'zgarmas elementlar to'plami",
#     "Set": "Unikal elementlar to'plami"
# }

# for soz in sorted(lugat.keys()):
#     print(f"{soz} - {lugat[soz]}")



# ___________________________________________________


# davlatlar = {
#     "AQSH": "Washington D.C.",
#     "ITALIYA": "Rim",
#     "MALAYZIYA": "Kuala-Lumpur",
#     "O'ZBEKISTON": "Toshkent",
#     "QIRG'IZISTON": "Bishkek",
#     "QOZOG'ISTON": "Nursulton",
#     "ROSSIYA": "Moskva",
#     "SINGAPUR": "Sungapur",
#     "TOJIKISTON": "Dushanbe"
# }

# print("Dunyo davlatlari:")
# for davlat in sorted(davlatlar.keys()):
#     print(davlat)

# print("\nDavlatlarning poytaxtlari:")
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt)

# ___________________________________________________

# lugat={
#     'booolen':'tru fols',
#     'float':'onlik son',
#     'for':'qaytarish sikli',
#     'if':'agar aksan',
# }

# for let in sorted(lugat.keys()):
#     print(f"keys {let}")

# for let in sorted(lugat.values()):
#     print(f"keys {let}")






# davlatlar = {
#     "AQSH": "Washington D.C.",
#     "ITALIYA": "Rim",
#     "MALAYZIYA": "Kuala-Lumpur",
#     "O'ZBEKISTON": "Toshkent",
#     "QIRG'IZISTON": "Bishkek",
#     "QOZOG'ISTON": "Nursulton",
#     "ROSSIYA": "Moskva",
#     "SINGAPUR": "Sungapur",
#     "TOJIKISTON": "Dushanbe"
# }
# a=input('davlat kirit: ')
# b=davlatlar.get(a)

# if b== None:
#     print('bizda bunday davlat yoq')
# else:
#     print(f"{a} ning poytaxti {b} ")
# ____________________________________________________________________________

# menyu={
#     'osh':20000,
#     'lagman':15000,
#     'shashlik':80000,
#     'manti':43000,
#     'samsa':12000,
# }


# b=menyu.get(a)
# a=input('qaysi ovqatni tanlaysiz: ')
# if b== None:
#         print(f"kechirasiz bizda {a} yoq ")
# else:
#          print(f"{a} {b} sum ")