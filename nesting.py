# car_1={
#     'model':'lacetti',
#     'narh':25000,
#     'ctage':2,
#     'tuning':'full'
# }
# car_2={
#     'model':'lacetti',
#     'narh':25000,
#     'ctage':2,
#     'tuning':'full'
# }
# car_3={
#     'model':'lacetti',
#     'narh':25000,
#     'ctage':2,
#     'tuning':'full'
# }


# cars=[car_1,car_2,car_3]

# for car in cars:
#     print(f"model={car['model'].title()}")

# malibus=[]

# for i in range(10):
#     newccar={
#              'model':'malibu',
#              'narh':None,
#              'ctage':2,
#              'tuning':'full',
#              'rang':None
#     }
#     malibus.append(newccar)


# for malibu  in malibus[0:3]:
#     malibu['rang']='qizil'


# for malibu  in malibus[0:6]:
#     malibu['rang']='qora'


# for malibu  in malibus[6:]:
#     malibu['rang']='qora'
#     malibu['narh']=50000
# for malibu  in malibus[0:6]:
#     malibu['narh']=40000

# print(malibus)

# yozuvchi=[]


# for i in range(10):
#     abdullo ={
#         'yoshi':None,
#         'kasbi':'programmer',
#         'vatani': "O'zbekiston",
#         'notbuki': None,
#         'ism': None
#     }
#     yozuvchi.append(abdullo)


# for rajabov  in yozuvchi[0:3]:
#     rajabov['yoshi']=15
#     rajabov['ism']='abdullo'
#     rajabov['notbuki']='Victus'
# for rajabov  in yozuvchi[3:6]:
#     rajabov['yoshi']=15
#     rajabov['ism']='umid'
#     rajabov['notbuki']='lenovo'
# for rajabov  in yozuvchi[6:]:
#     rajabov['yoshi']=15
#     rajabov['ism']='saddullo'
#     rajabov['notbuki']='lenovo'

# print(yozuvchi)
# __________________________________________________________
# odam={
#     'abdullo':{
#     'familiya':'qodiriy',
#     'yili':2000,
#     'ijod':'ona va bola',
#     },
#     'sadullo':{
#         'familiya':'sadullo',
#         'yili':2000,
#         'ijod': 'kopnarsala qigan'
#     }
   
# }
# for ism,info in odam.items():
#        print(f"{ism.title()} familiyasi: {info['familiya'].title()} "
#           f"{info['yili']}-yilda tugulgan, ijodi: {info['ijod']}")
# __________________________________________________________
# odam={
#     'abdullo':[
#         'terminator',
#         'Rambo',
#         'titanic'
#     ],
#     'sadullo':[
#         'tenet',
#         'inception',
#         'marvel'
# ]
# }

# for ism,info in odam.items():
#        print(f"{ism.title()}  yaxshi korgan kinosi {info}")
# __________________________________________________________


# Respublic={
#     'Ozbekiston':{
#     'hududi':'448978 kv.km',
#     'aholisi':33000000,
#     'pul birligi':'som',
#     },
#    'Rossiya':{
#     'hududi':'448978 kv.km',
#     'aholisi':33000000,
#     'pul birligi':'rubl',
#     },
#      'America':{
#     'hududi':'448978 kv.km',
#     'aholisi':33000000,
#     'pul birligi':'dollar',
#     },
#     }
    
# for ism,info in Respublic.items():
#     print(f"{ism.title()} hududi {info['hududi'] } aholisi {info['aholisi']} pul birligi {info['pul birligi']}") 
# __________________________________________________________

# Respublic={
#     'Ozbekiston':{
#     'hududi':'448978 kv.km',
#     'aholisi':33000000,
#     'pul birligi':'som',
#     },
#    'Rossiya':{
#     'hududi':'448978 kv.km',
#     'aholisi':33000000,
#     'pul birligi':'rubl',
#     },
#      'America':{
#     'hududi':'448978 kv.km',
#     'aholisi':33000000,
#     'pul birligi':'dollar',
#     },
#     }
# a=input('Davlat nomini kiriting: ')

# if a in Respublic:    
#        info=Respublic[a]
# print(f"{info['hududi']} {info['aholisi']}  {info['pul birligi']} ")
# ___________________________________________________
menyu={
   'lagman':{
          'narh':20000
   },
   'osh':{
          'narh':110000
   },
   'manti':{
          'narh':8000
   },
   'shashlik':{
          'narh':50000
   },
   'steyk':{
          'narh':38000
   },
   'kartoshka':{
          'narh':15000
   },
   'kadimanti':{
          'narh':5000
   },
   'kola':{
          'narh':15000
   },
   'fanta':{
          'narh':14000
   },
   'sprite':{
          'narh':19000
   },
    }
arr=[]

for array in range(3):
    array=input("nima zakaz qilmoqchi siz: ")
    arr.append(array)

for a in arr:
    if a in menyu:
        print(f"{a} ning narhi {menyu[a]}") 
    else:
        print(f"kechirasiz bizada {a} tugagan") 
    
