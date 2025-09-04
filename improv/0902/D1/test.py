

# a:str = "Ahoj!"
# b:int = 3
# c:float = 3.14
# d:float = 3.
# e:bool = False
# f:bool = 3 == 5


# print(f"{type(a)=}")
# print(f"{type(b)=}")
# print(f"{type(c)=}")
# print(f"{type(d)=}")
# print(f"{type(e)=}")
# print(f"{type(f)=}")

# PI = 3.141592654
# pi = 3.141592654


s = "Pes"
i = 12

# if s == "Ahoj":
#     print(1)
# elif s == "123":
#     print(2)
# elif i > 5:
#     print("Aha?!")
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
# #     # i = i + 1
# #     i += 1



# # for _ in range(4):
# #     # for loop scope
# #     print(s)

# # out of for loop scope


# l:list = [5, "Ahoj", 5, 5.5, True]
# # l.append("Další")
# # l.remove(5)
# # l.pop()

# # for i in range(len(l)):
# #     print(l[i])

# l[0] = "První"
# # print(l)


# t:tuple = (1, 2, "Ahoj", 4)
# # t[0] = "První"


# s:set = set([1, 2, 1, 3, 2, 8, 9, 9, 10, 8])
# print(s)


# d:dict = {
#     "Rododendron" : "První",
#     2 : "Druhá",
#     3 : "!!!",
#     0 : "???"
# }

# print(d[3])




# l = list(range(25, 51, 5))

# print(l)
# print(l[3])
# print(l[2:5:2])
# print(l[:3])
# print(l[3:])
# print(l[:])


s = "Ahoj, já jsem string!"
# l = list(s)
# t = tuple(s)
# S = set(s)
# d = { ch : i for i, ch in enumerate(s) }

# print(
#     s,
#     l,
#     t,
#     S,

#     sep="\n"
# )

# print(d)

# l = [ char.upper() for char in s]
# print(l)

# l = []
# for i in range(0 ,len(s), 2):
#     l.append(s[i])

# print(l)


# l = [ ch for i, ch in enumerate(s) if i % 2 == 0 ]
# print(l)


l1 = [1, 5, 25]
l2 = [-4, 6, 12]

def secti_triprvkovy_seznam(seznam:list[int]) -> int:
    return seznam[0] + seznam[1] + seznam[2]

f = open("test.txt", "w")

f.write("Ahoj!\n")
f.write(str(secti_triprvkovy_seznam(l2)))

f.close()