

# print(' kiritilgan sonning kvadrati qaytaruvchi dasturr ')
# son = 'son kiriting kvadrati chiqaramiz '
# son +=' (agar dastur tohtatmoqchi bulsangiz (exit) dep yozing)'
# qiymat = ' '
# while qiymat != 'exit':
#     qiymat = input(son)
#     if qiymat != 'exit':
#         print(int(qiymat)**2)
# ________________________________________________________________________
# print(' kiritilgan sonning kvadrati qaytaruvchi dasturr ')
# son = 'son kiriting kvadrati chiqaramiz '
# son += ' (agar dastur tohtatmoqchi bulsangiz (exit) dep yozing): '
# ishora = True
# while ishora:
#     qiymat = input(son)
#     if qiymat == 'exit':
#         print('programma toxtadi')
#         ishora=False
#     else:
#         print(int(qiymat)**2)
# ________________________________________________________________________
# print('yanxhi koradigan kitbini kiritadigan kod: ')

# foydalanuvchi='yaxshi koradigan kitobingizni kiriting'
# foydalanuvchi+='(agar toxtatmoqchi bolsayiz stop sozini kiritinf(:))'

# toxtatuvchi=True

# while toxtatuvchi:
#     qiymat=input(foydalanuvchi)
#     if qiymat=='stop':
#          toxtatuvchi=False
    # ________________________________________________________________________
# yosh=('yoshizni kiriting: ')

# while True:
#     qiymat=input(yosh)
#     if qiymat=='stop' or qiymat=='exit':
#         break
#     yo = int(qiymat)
#     elif yo<=7:
#         print('2000 sum')
#     elif yo<=18:
#         print('3000 sum')
#     elif yo<=65:
#         print('10000 sum')
#     elif yo>65:
#         print('bepul')
# ________________________________________________________________________
# savol = "Yoshingizni kiriting: "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
    
#     if yosh<7:
#         narh = 2000
#     elif 7<=yosh<18:
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else: narh = 0
    
#     if narh==0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")
    # ________________________________________________________________________

# savol='kirilgan sonning ildizini topadigan programma: '

# while True:
#     qiymat=input(savol)
#     if qiymat=='exit':
#         break   
#     else:
#         iidiz=int(qiymat)**0,5 
# ________________________________________________________________________
# son = 1
# while son<=5:
#     print(son, end=' ')
#     son = son + 1


# print('kiritgan soni kvarati chiqaramiz')

# son = 'son kiriting: '
# son += "(toxtatish uchun 'exit bosing')"
# ishora = True
# while ishora:
#     qiymat = input(son)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(int(qiymat)  2)
 


# print('kiritgan soni kvarati chiqaramiz')

# son = 'son kiriting: '
# son += "(toxtatish uchun 'exit bosing')"

# while True:
#     qiymat = input(son)
#     if qiymat == 'exit':
#         break
#     else:
#         print(int(qiymat)  2)

# son = list(range(1,11))
# for a in son:
#     if a ==5:
#         break
#     print(f"{a} ning kvartai {a**2} ga teng")

# son = list(range(1,11))
# for a in son:
#     if a ==5:
#       continue
#     print(f"{a} ning kvartai {a**2} ga teng")


# son = 1
# while son>0:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)
# ___________________________________________________
# son=int(input('lyuboy sonni kiriting: '))
# a=son**2

# while son<=a:
#     print(a)
#     son=son+1
# ___________________________________________________
# son=int(input('lyuboy sonni kiriting: '))

# b=1

# while b<=son/2:

#     if son%b==0:
#         print(b)
#         son += 1

# n=int(input('n natural sonni kiriting: '))

# son = 1
# while son<=n/2:
   
#     if n%son==0:
#         print(son)
#     son += 1





# son = 1
# while son>0:
#     son += 1  
#     if son%2!=0:c
#         continue
#     else:
#         print(son)
# ___________________________________________________
# yigindi=0

# while True:
#     n=int(input('n natural sonni kiriting: '))
#     if n<0:
#         break
#     else:
#         print(f"{n} ning kvadrati {n**2}")
# ___________________________________________________
b='b son kirgiz: '
a='a son kirgiz: ' 

while True:
  a_son=int(input(a))
  b_son=int(input(b))
  if a_son>b_son:
    print(f"{a_son}{b_son}")
  elif b_son>a_son:
    print(f"{b_son}{a_son}")
  else:
    print(a_son,b_son)
