# def avto_kompaniya(kompaniya,model,rang,yil,narh=None):
#     avto={
#         'kompaniya':kompaniya,
#         'model':model,
#         'rang':rang,
#         'yil':yil,
#         'narh':narh
#     }
#     return avto

# avto1=avto_kompaniya('gm','cobalt','qora',2022,20000)
# avto2=avto_kompaniya('gm','cobalt','qora',2020)
# avtolar=[avto1,avto2]

# for avto in avtolar :
#     if avto['narh']:
#         avto['narh']='narh'
#     else:
#         narh='nomalum'
# print(f"{avtolar}")
# _____________________________________________
# def son(n):
#         if n==1:
#           print("I")
#         if n==2:
#            print("II")
#         if n==3:
#            print("III")
#         if n==4:
#            print("IV")
#         if n==5:
#            print("V")
#         if n==6:
#            print("VI")
#         if n==7:
#            print("VII")
#         if n==8:
#            print("VIII")
#         if n==9:
#            print("IX")
#         if n==10:
#            print("x")
# raqam=int(input("buronta son chiqor"))
# son(raqam)
# _____________________________________________
def son(a,b):
    print(f"{a} ning {b} darajasi {a**b}")

sonlar1=int(input("son kitit: "))
sonlar2=int(input("son kitit: "))

son(sonlar1,sonlar2)                 