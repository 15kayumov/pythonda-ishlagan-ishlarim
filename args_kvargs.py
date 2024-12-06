# def summa(*sonlar):
#     return  sum(sonlar)

# print(summa(1,2,3,4,4))

# def summa(x,y,*sonlar):
#     return x+y+sum(sonlar)

# print(summa(1,2,3))
    

# def avto_info(kompaniya,model,**modellar):
#     modellar['kompaniya']=kompaniya
#     modellar['model']=model
#     return modellar

# avto1=avto_info('gm','onix_turbo', rangi='qizil',yili=2023)
# print(avto1)  
# _______________________________________________________________-

# def summa(*sonlar):
#     yigindi = 1
#     for son in sonlar :
#         yigindi += son
#     return yigindi
    
# print(summa(1,2,3))
# _______________________________________________________________-

# def summa(x,y,*sonlar):
#     return x*y*sum(sonlar)

# print(summa(1,2,3))
# _______________________________________________________________-
# def avto_info(ism,familya,**info):
#     info['ism']=ism
#     info['familya']=familya
#     return info

# avto1=avto_info('abdullo','rajabov',yasash_joyi='OZBEKISTON',yili=2009)
# print(avto1)  
# _________________________________________________-
# def son(n):
#     for i in range(n):
#          print('-' * n)

# n = int(input("Kvadrat tomoni uzunligini kiriting: "))
# son(n)
# a=int(input())
# print(a//2)
# s = "mening_epochta@mail.com"
# print(s[:s.index('_')])
def f(x):
 if x <= 3: return x
 return f(x - 1) + 3 * f(x - 2)
print(f(7))