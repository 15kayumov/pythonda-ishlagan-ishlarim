teelefonlar={
    'vali':'samsung44Ultra',
    'mahmud':'iphonex',
    'kali':'matarolla',
    'sali':'xiomi',
}

print(teelefonlar.items())

for kalit,qiymat in teelefonlar.items():
    print(f"kalit {kalit}")
    print(f"qiymat {qiymat}")

for kalit in teelefonlar.keys():
    print(f"kalit {kalit}")

for value in teelefonlar.values():
    print(f" value {value}")
for tel in set(teelefonlar.values()):
    print(f"value {tel}")
for tel in set(teelefonlar.keys()):
    print(f"keys {tel}")