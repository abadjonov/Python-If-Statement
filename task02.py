son = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))

if son == son2:
    print(son, "va", son2, "teng")
else:
    if son > son2:
        print(son)
    else:
        print(son2)