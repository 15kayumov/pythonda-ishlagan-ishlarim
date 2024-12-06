# def salom_ber(ism):
#     """salom beruvchi funcsiya"""
#     print(f"assalom aleykum xurmatli {ism.title()}")

# salom_ber('hasan')
# salom_ber('ali')
# _____________________________________________
# def yosh_chiqaruvchi(yosk,joriy_yil=2024):
#     print(f"sizning yoshiz {joriy_yil-yosk} da tug'lgan siz")
# daaf=int(input("yoshizni kiriting: "))
# yosh_chiqaruvchi(daaf)
# _____________________________________________
# def yosh_hisoblash(ism,yosh):
#     print(f"sizning ismiz: {ism},\n"
#           f"sizning yoshiz {2024-yosh}")
# yosh_hisoblash(ism="vali",yosh=1991)
# _____________________________________________

# def nimadir(ism,yosh):
#     print(f"sizning ismiz {ism},\n"
#           f"sizning yoshiz {2024-yosh}")
# yoshi=int(input("tug'ulgan yiliz nechchida: "))
# ismi=input("ismiz nima: ")
# nimadir(ismi,yoshi)
# _____________________________________________

# def son(son):
#     print(f"{son} shuning kvadrati:{son**2} \n shuning kubi:{son**3}")
# soni=int(input('son kirit: '))
# son(soni)

# _____________________________________________
# def son(son_bir,son_ikkki):
#     if son_bir>son_ikkki:
#         print(f"{son_bir}>{son_ikkki}dan katta")
#     elif  son_ikkki>son_bir:
#         print(f"{son_bir}<{son_ikkki}dan kichik")
#     elif son_bir==son_ikkki:
#         print(f"{son_bir}={son_ikkki} bula ikkalasi teng")
#     elif son_ikkki==son_bir:
#         print(f"{son_bir}={son_ikkki} bula ikkalasi teng")
# sonbiri=int(input('son kirit: '))
# sonikkisi=int(input('son kirit: '))
# son(sonbiri,sonikkisi)
# _____________________________________________
# def son(son_bir,son_ikkki):
#     if son_bir>son_ikkki:
#         print(f"{son_bir}")
#     elif  son_ikkki>son_bir:
#         print(f"{son_ikkki}")
#     elif son_bir==son_ikkki:
#         print(f"sonlar teng")
#     elif son_ikkki==son_bir:
#         print(f"sonlar teng")
# sonbiri=int(input('son kirit: '))
# sonikkisi=int(input('son kirit: '))
# son(sonbiri,sonikkisi)
# _____________________________________________
# def son(x,y):
#     print(f"{x**y}")

# sonbiri=int(input('son kirit: '))
# sonikkisi=int(input('son kirit: '))
# son(sonbiri,sonikkisi)
# _____________________________________________
# def son(x,y=2):
#     print(f"{x**y}")

# sonbiri=int(input('son kirit: '))
# sonikkisi=int(input('son kirit: '))
# son(sonbiri,sonikkisi)
# _____________________________________________
def son(x):
    print({x//range(2,11)})
soni=int(input('son kirit: '))
son(soni)