
a:int = 5 #integer
barva:str = "Ahoj" #string
c:float = 3.14 #floating point
d:float = .4
e:bool = False
f = 3 > 5


barva = "Purple"
# if barva == "Red":
#     print("Třešeň")
# elif barva == "Green":
#     print("Jablko")
# elif barva == "Yellow":
#     print("Banán")
# else:
#     print("???")

# match barva:
#     case "Red":
#         print("Třešeň")

#     case "Green":
#         print("Jablko")

#     case "Yellow":
#         print("Banán")

#     case _:
#         print("???")

s = "Thinking"
# i = 0
# while i < 4:
#     print(s)
#     # i = i + 1
#     i += 1

# for _ in range(4):
#     print(s)


l:list = [5, "Ahoj", 5.5, True, s]
# for i in range(len(l)):
#     print(l[i])


# for item in l:
#     print(item)

# for i in range(len(l)):
#     item = l[i]

#     print(i, item)

# for i, item in enumerate(l):
#     print(i, item)


# range(start, stop, step) -> [0, 1, 2, 3, 4, ..., n-1]

# print(list(range(5, 20, 3)))

# t:tuple = (5, 3, 9, "???")
# print(t)
# t = (5, 3, 0, "???")
# print(t)


# d:dict = {
#     "Stačilo" : .0461,
#     "AUTO" : .0671
# }


# s:set = set([1, 2, 2, 5, 8, 3, 6, 8, 12, 21, 5, 6])
# print(s)

s = "Ahoj, já jsem dlouhý string!"
# l:list = list(s)
# print(l)
# print(l[12])
# print(l[12:17])
# print(l[:6])
# print(l[22:])
# print(l[-3])
# print(l[-8:-3])
# print(l[15:5:-1])
# print(l[::-1])


# l = []
# for ch in s:
#     l.append(ch.upper())

l = [ ch.upper() for ch in s if ch != " " ]
d = { ch : i for i, ch in enumerate(s) if ch not in (" ", ",") }

print(d)