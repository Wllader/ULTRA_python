

a:int = 23
c:float = .9
d:bool = False


text = "189"
cislo = bool(text)
# print([cislo, text])


# if a > 20:
#     print("A je vetsi nez 20")
# elif a > 10:
#     print("A je vetsi nez 10")
# else:
#     print("A je male")


b:str = "Red"
# if b == "Red":
#     print("Třešeň")
# elif b == "Green":
#     print("Jablko")
# elif b == "Yellow":
#     print("Banán")
# else:
#     print("???")


# match b:
#     case "Red":
#         print("Třešeň")
#     case "Green":
#         print("Jablko")
#     case "Yellow":
#         print("Banán")
#     case _:
#         print("???")


# i = 0
# while i < 10:
#     print("Loading", i)
#     i += 1


# for i in "Ahoj!":
#     print("Loading", i)


# print(list(range(5, 20, 5)))

S = "Tohle je text"
# for i, ch in enumerate(S):
#     print(f"{i}\t:\t{ch}")


hraci = ["Wllader", "Loki", "Magda"]
hps = [100, 85, 1]

# print(*hraci, sep="\n")

# for i in range(len(hraci)):
#     print(hraci[i], hps[i])

# for h, hp in zip(hraci, hps):
#     print(h, hp)

# print(list(zip(*list(zip(hraci, hps)))))




l = list(S)
# print(l)
# print(l[4:9])
# print(l[4:9:2])
# print(l[:12])
# print(l[4:])
# print(l[:])

# B = A[:]
# B[0] = 100

# print(B)
# print(A)

t = tuple(S)
# print(t)

# t[5] = 1000
# print(t)


s = set(S)
# print(
#     l,
#     t,
#     s,

#     sep="\n"
# )


d = {
    (1, 2, 3) : 5,
    "Simona" : 12,
    "Michal" : 37
}

# print(d)

# d = {
#     ch : i for i, ch in enumerate(S)
# }

# print(d)

# t = (2*i for i in range(7))
# print(t)

# def foo(n:int = 0) -> int:
#     return 6*n

# print(foo())


l1 = [1, 5, 25, 50, -28, -12, -10]
l2 = [-4, 6, 12]

def secti_seznam(seznam:list[int]) -> int:
    return sum(seznam)




# f = open("data/test.txt", "w")
# try:
#     print("Zapisovani do souboru")
#     f.write(secti_seznam(l1))
# finally:
#     print("Zaviram soubor")
#     f.close()

# print("Hotovo")


# from numpy import random
# from string import ascii_lowercase


# with open("data/test.txt", "w") as f:
#     for i in range(50):
#         f.write(f"{i}: ")
#         f.write(ascii_lowercase[:random.randint(5,26)])
#         f.write("\n")


with open("data/test.txt", "r") as f:
    print(f.read(28))




