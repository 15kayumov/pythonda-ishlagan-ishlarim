# ismlar=[]
# print("dostiz ismini kiriting")
# n=1

# while True:
#     ism=input(f"{n}- dostingizni kiriting: ")
#     javoblar=input(ism)
#     ismlar.append(ism)
#     javob=input("dasturni toxtatish uchun (ha/yoq)")  
#     if javob=='ha':
#         n+=1
#         continue
#     else:
#         break
# print(ismlar)


# a=int(input("xoxlagan sonizni kiriting: "))


# a=0
# b=0
# c=int(input("xoxlagan sonizni kiriting: "))

# while not(c==0):
#     b+=c%10
#     c=c//10   

# print(b)   

# a=0
# b=0
# c=int(input("xoxlagan sonizni kiriting: "))

# while not(c**2):
        # _____________________________________________--
# ismlar=[]
# print("nima  zakaz  qilmoqchisiz??: ")
# n=1

# while True:
#     ism=input(f"{n}- zakazizni kiriting: ")
#     javoblar=input(ism)
#     ismlar.append(ism)
#     javob=input("dasturni toxtatish uchun (ha/yoq)")
#     if javob=='ha':
#         n+=1
#         continue
#     else:
#         break
# print(ismlar)
# _____________________________________________
# talabalar=['hasan','husan','vali','ali','bali']
# baholangan_talabalar={}

# while talabalar:
#     talaba=talabalar.pop(0)
#     baho=input(f"{talaba.title()} ning bahosini qoying: ")
#     print(f"{talaba.title} baholandi.")
#     baholangan_talabalar[talaba]=baho
# print(baholangan_talabalar)
# _____________________________________________
# e_bozor=[]
# mahsulotlar={}
# sorovnoma='burinta mahsulot kiriting: '
# while True:
#     a=input(sorovnoma)
#     e_bozor.append(a)  
#     bozor=e_bozor.pop()
#     baho=int(input(f"{bozor} ning narhini ayting")) 
#     mahsulotlar[bozor]=baho
#     print(mahsulotlar)
# _____________________________________________
# tovar=['olma','nok','banan','shaftoli',]
# mahsulot={
#     'klubnika': 20000,
#     'qaroli':22000,
#     'banan':15000,
#     'nok':12000
# }
# while tovar:
#     tovarlar=tovar.pop(0)
#     if tovarlar in mahsulot.keys():
#       print(f"bizda shu {tovarlar} bor")
#     else:
#         print(f"koechirasiz bizda {tovarlar}  yoq")
#     print(mahsulot)
