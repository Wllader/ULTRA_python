

s:str = "Ahoj" #string
i:int = 15 #integer
# f:float = 1.5 #floating point number
b:bool = False #boolen

# print(7 + 3)
# print("Ahoj" + " jak se máš?")
# print(15 // 4)


# if s == "Ahoj":
#     print(1)
# elif s == "123":
#     print(2)
# elif s == "Pes":
#     print(3)
# else:
#     print(0)


# match s:
#     case "Ahoj":
#         print(1)
#     case "123":
#         print(2)
#     case "Pes":
#         print(3)
#     case _:
#         print(0)



# s = "Waiting"
# # i = 0
# # while i < 4:
# #     print(s)
# #     i += 1



# for _ in range(4):
#     print(s)


l:list = [5, "Ahoj", 5.5, True]

# for i in range(len(l)):
#     print(l[i])

# for item in l:
#     print(item)

# for i in range(len(l)):
#     item = l[i]
#     print(i, item)


# for i, item, in enumerate(l):
#     print(i, item)


t:tuple = (5, 3, 9, "???")
# for item in t:
#     print(item)


# l.append("Nové")
# l[0] = "Sedmička"
# for i, item, in enumerate(l):
#     print(i, item)


# t[0] = "!!!"


S = set([1, 2, 3, 4, 8, 12, 4, 5, 9, 3])
# print(S)


# d = {
#     "Rododendron" : "První",
#     2 : "Druhá",
#     3 : "!!!",
#     0 : "???"
# }

# print(d["Rododendron"])

# # for key in d:
# #     print(key)

# # for val in d.values():
# #     print(val)


# for key, val in d.items():
#     print(key, val)


# l = list(range(25, 50))
# print(l)
# print(l[12])
# print(l[12:17])
# print(l[:6])
# print(l[22:])
# print(l[-3])
# print(l[-8:-3])
# print(l[5:10:3])

# print(S)



# s = "Ahoj, já jsem string!"
# l = list(s)
# t = tuple(s)
# S = set(s)
# d = { char : i for i, char in enumerate(s) }

# print(
#     s,
#     l,
#     t,
#     S,

#     sep="\n"
# )

# l2 = []
# for char in s:
#     l2.append(char.upper())

# print(l2)


# l3 = [ char.upper() for char in s ]
# print(l3)

# print(d)


# d2 = {
#     (1, 2, 3) : "A",
#     3 : "B"
# }

# print(d2[(1, 2, 3)])



l1 = [1, 5, 25]
l2 = [-4, 6, 12]

def secti_triprvkovy_seznam(seznam:list[int]) -> int:
    return seznam[0] + seznam[1] + seznam[2]



f = open("test.txt", "w")

f.write("Ahoje\n")
f.write(str(secti_triprvkovy_seznam(l2)))

f.close()