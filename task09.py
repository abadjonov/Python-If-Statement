uchi1 = int(input("Birinchi tomonni kiriting: "))
uchi2 = int(input("Ikkinchi tomonni kirting: "))
uchi3 = int(input("Uchinchi tomonni kiriting: "))

if uchi1 == uchi2 and uchi2 == uchi3:
    print("Teng tomonli!")
else:
    if uchi1 == uchi2 or uchi2 == uchi3 or uchi1 == uchi3:
        print("Teng yonli!")
    else:
        print("Turli tomonli!")

5