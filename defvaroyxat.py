# def oraliq(min,max):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min+=1
#     return sonlar

# print(oraliq(0,10))
# print(oraliq(10,20))

    

# def avto_info(komponiya,model,rangi,korobka,yili,narhi=None):
#     avto = {
#         'komponiya':komponiya,
#         'model':model,
#         'rang':rangi,
#         'korobka':korobka,
#         'yil':yili,
#         'narh':narhi
#     }
#     return avto


# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\n Quyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    

#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
   
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break

# print(avtolar)


# def uquvchilar(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop(0)
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting")
#         baholar[ism] = baho
#     return baholar

# talabalar = ['ali','vali','hasan','sali']
# baholar = uquvchilar(talabalar)

# print(baholar)   

# arr=[109,11000000]
# def sonlar(son):
#     print(f"kichik son={min(son)}\n katta son={max(son)}")

# sonlar(son=arr)
# __________________________________

# def min4(a,b,c,d):
#     print(min(a,b,c,d))
# min4(a=4,b=6,c=11,d=141)
# __________________________________
# def akslantiruvchi_son(son):
#     teskari_son = str(son)[::-1]
#     return int(teskari_son)


# son = 123
# print(akslantiruvchi_son(son))  

