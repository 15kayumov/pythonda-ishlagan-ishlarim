# narh = 15000
# choy = True
# salat = fal

# if choy and salat:
#     narh = narh + 10_000
# elif choy or salat:
#     narh = narh + 5000
# print(narh)


# narh = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
# if choy:
#     print("mijoz choy oldi")
#     narh = narh + 2000
# if salat:
#     print("mijoz salat oldi")
#     narh = narh + 3000
# if non:
#     print("mijoz non oldi")
#     narh = narh + 4000
# if kompot:
#     print("mijoz kompot oldi")
#     narh = narh + 10000
# if assorti:
#     print("mijoz assorti oldi")
#     narh = narh + 40_000
# print(f"jami {narh} sum")


# menu = ['manti', 'osh', 'somsa','shurva','tarvuz']
# ovqat = input('Nima ovqat yeysiz: ')

# if ovqat.lower() not in menu:
#     print('bizda bunday taom yoq')
# else:
#     print('buyurtma qabul qilindi ')



# menu = ['manti', 'osh', 'somsa','shurva','tarvuz']
# buyurtmalar = ['shashlik','norin','somsa','osh']

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"menuda {taom} bor")
#     else:
#         print(f"menuda bunday {taom} yoq")



# menu = ['manti', 'osh', 'somsa','shurva','tarvuz']
# buyurtmalar = ['shashlik','norin','somsa','osh']


# if buyurtmalar:
#     for taom in buyurtmalar:
#       if taom in menu:
#           print(f"menuda {taom} bor")
#       else:
#           print(f"menuda bunday {taom} yoq")
# else:
#     print('savatingiz bush')
# _________________________________________________________________________________
# menu=['anor','un','sok','kola','rolton','non','qatiq','kifir','gazirifka']
# savat=[]

# for zakaz in range(5):
#     savat.append(input(f"saavatga {zakaz+1}-maxsulotni qo'shing: "))

# if savat:
#     for zakaz in savat:
#         if zakaz in menu:
#             print(f"menuda {zakaz } bor")
#         else:
#             print(f"menuda bunday {zakaz } yoq")
# else:
#     print('savatingiz bush ')

# ____________________________________________________________________________
# menu=['anor','un','sok','kola','rolton','non','qatiq','kifir','gazirifka']
# savat=[]

# for zakaz in range(5):
#     savat.append(input(f"saavatga {zakaz+1}-maxsulotni qo'shing: "))

# if savat:
#     for zakaz in savat:
#         if zakaz in menu:
#             print(f"menuda {zakaz } bor")
#         else:
#             print(f"do'konimizda  bunday {zakaz } yoq")
# else:
#     print('savatingiz bush ')


# ____________________________________________________________________________
# menu=['anor','un','sok','kola','rolton','non','qatiq','kifir','gazirifka']
# savat=[]
# bor_maxsulot=[]
# yoq_maxsulot=[]

# for zakaz in range(5):
#         savat.append(input(f"saavatga {zakaz+1}-maxsulotni qo'shing: "))
# for zakaz in savat:
#         if zakaz in menu:
#             bor_maxsulot.append(zakaz)
#         else:
#             yoq_maxsulot.append(zakaz)
# if yoq_maxsulot:
#       print(f"do'konimizda quyidagi maxsulotlar yoq: ")
#       for maxsulot in yoq_maxsulot:
#             print(maxsulot)
# else:
#       print("siz so'ragan barcha maxsulotlar do'konimizda bor")
# ____________________________________________________________________________


# foydalanuvchilar=['umar','miron','abdullo','ibosh','abush']
# login=input('yangi login kiriting: ')

# if login in foydalanuvchilar:
#         print('xush kelibsiiz!')
# else:
#         print('bu login ishlatilgan')
# ____________________________________________________________________________
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz','kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in mavjud_emas:
#   print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# ____________________________________________________________________________
# son = float(input("Juft son kiriting: "))
# if son%2==0:
#     print("Bu son juft emas.")
# else:
#     print("Rahmat!")
# ____________________________________________________________________________
# yosh = int(input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
#     print(f"Chipta {narh} so'm")
# ____________________________________________________________________________
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")
# ____________________________________________________________________________
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz','kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat=[]

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")
# ____________________________________________________________________________
# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
# ____________________________________________________________________________
# users = ['alisher1983','aziza','yasina' 'umar']

# login = input("Yangi login tanlang: ")

# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")

# ____________________________________________________________________________
# son=int(input("xoxlagan sonni kiriting: "))


# for i in range(son):
#     print(f"{son}ning kvadrati {son**2}")
# ____________________________________________________________________________
# son=int(input("xoxlagan sonni kiriting: "))


# if son==2:
#         print(f"shu sonlar ichida 2  soni {son} ta bor")
# else:
#         print(f"bu yerda 2 soni yoq") 
# ____________________________________________________________________________
# a=int(input('lubboy son kirit: '))
# b=int(input('lubboy son kirit: '))

# if a<b:
#     for c in range(a,b+1):
#         print(c)
# elif a>b:
#     for c in range(b,a-1):
#         print(c)
# ____________________________________________________________________________
