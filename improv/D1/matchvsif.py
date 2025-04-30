a = 3
b = "Čtvrtek"

if a == 5:
    print(1)
elif a == 6:
    print(2)
elif a == 7:
    print(3)
elif a == 8:
    print(4)
elif a == 9:
    print("Něco jiného")

print("Konec")

match a:
    case 5:
        print(1)
    case 6:
        print(2)
    case 7:
        print(3)