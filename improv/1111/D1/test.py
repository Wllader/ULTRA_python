
# a = 5

# b = 5.8
# b2 = 5.
# b3 = .3

# c = 'I\'m gonna be home by 8:30'
# c2 = "Představujeme Honzu \"Bouráka\" Mikulku"

# d = True
# d2 = 3 > 5

height = 215
barva = "Red"

# if barva == "Red": print("Třešeň")
# elif barva == "Green": print("Jablko")
# elif height >= 165: print("!!!")
# elif barva == "Teal": pass
# else: print("???")


# match barva:
#     case "Red":
#         print("Třešeň")

#     case "Green":
#         print("Jablko")

#     case "Yellow":
#         print("Banán")

#     case "Teal":
#         pass

#     case _:
#         print("???")




# i = 0
# while i < 4:
#     print("Thinking")
#     i += 1

# for _ in range(4):
#     print("Thinking")

s = "Hmmm..."
l = [5, "Ahoj", 5.5, True, s]

# for i in range(len(l)):
#     print(l[i])

# for item in l:
#     print(item)


# for i in range(len(l)):
#     if i == 3:
#         l[i] = 999

# for item in l:
#     item = 999

# print(l)


# i = 0
# for item in l:
#     print(i, item)
#     i += 1


# for i in range(len(l)):
#     item = l[i]
#     print(i, item)


# for i, item in enumerate(l):
#     print(i, item)


players = ["Marie123", "Wllader", "xXTomasXx"]
hps     = [28, 100, 3]


# for i in range(len(players)):
#     # print(players[i], hps[i])
#     print(f"Hráč: {players[i]}\t| {hps[i]}")


# for p, hp in zip(players, hps):
#     print(f"Hráč: {p}\t| {hp}")


# print(
#     list(range(200, 250, 5))
# )

# l = ["Marie123", "Wllader", "xXTomasXx"]
# t = ("Marie123", "Wllader", "xXTomasXx")

# t = ("Marie123", "Martin88", "xXTomasXx")

# print(t[1])


# d = {
#     "Ahoj" : 3,
#     (1, 2, 3) : "k"
# }

# print(
#     d.keys(), d.values(), d.items(),
#     sep="\n"
# )


# s = set([3, 2, 1])

# if 4 in s:
#     print("!!!")


s = "Ahoj, já jsem dlouhý string!"
# l = list(s)

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
#     if ch != " ":
#         l.append(ch.upper())

# l = [ ch.upper() for ch in s if ch not in " ,!" ]
# # s = { ch.upper() for ch in s }
# d = { ch.upper() : i for i, ch in enumerate(s) if ch not in " ,!" }
# g = tuple( ch.upper() for ch in s )
# print(s)
# print(g)




