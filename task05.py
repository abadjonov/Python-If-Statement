bank = float(input("Bank omonatini kriting: "))

if bank <= 100_000:
    print("5%")
else:
    if bank <= 500_000 :
        print("7%")
    else:
        print("10%") 