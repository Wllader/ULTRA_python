# print("Ahoj světe!")

# a = 5

# b = 5.5
# b = .3
# b = 5.

# c = "I'm gonna be home by 8:30"
# c = 'Představujeme Honzu "Bouráka" Mikulku!'

# c = 'I\'m gonnabe home by 8:30'
# c = "Představujeme Honzu \"Bouráka\" Mikulku!"

# d = True
# d = False
# d = 5 < 3

# e = None


height = 215
barva = "Magenta"

# if barva == "Red":
#     print("Třešeň")
# elif barva == "Green":
#     print("Jablko")
# elif height > 200:
#     print("Páni!")
# elif barva == "Yellow":
#     print("Banán")
# else:
#     print("???")


# match (barva, height):
#     case "Red", _:
#         print("Třešeň")

#     case "Green", _:
#         print("Jablko")

#     case _, x if x > 200: # Match-guard
#         print("Páni!")

#     case "Yellow":
#         print("Banán")

#     case _:
#         print("???")



# i = 0
# while i < 5:
#     print("Načítaní...")
#     # i = i + 1
#     i += 1

# print("Konec")


# for i in range(5, 12):
#     print(i)
# print("Konec")


s = "Hmmm..."
l = [5, "Ahoj", 5.3, True, s]

# print(l[2])
# for i in range(len(l)):
#     print(l[i])

# for item in l:
#     print(item)

# for i in range(len(l)):
#     item = l[i]
#     print(i, item)


# for i, item in enumerate(l):
#     print(i, item)


players = ["Marie123", "Wllader", "xXTomasXx"]
hps     = [28, 100, 3]

# for i in range(len(players)):
#     # print(players[i], hps[i])
#     print(f"Hráč: {players[i]}\t | {hps[i]}")

# for player, hp in zip(players, hps):
#     print(f"Hráč: {player}\t | {hp}")


# l = list(zip(players, hps))
# print(l)

# l2 = list(zip(l[0], l[1], l[2]))
# l2 = list(zip(*l))
# print(l2)

# r = range(10, 500)
# l = list(r)
# print(l)

# l = [1, 2, 3]
# t = (10, 20, 30)


# l[1] = 9
# for item in l:
#     print(item)

# t[1] = 99
# for item in t:
#     print(item)

# l = [1, 2, 3]
# t = (1, 2, 3)
# d = {
#     "Ahoj" : 3,
#     t : "k"
# }

# print(
#     d[(1, 2, 3)]
# )

# print(
#     d.keys(), d.values(), d.items(),
#     sep="\n"
# )


# s = set([3, 2, 1])
# print(
#     3 in s,
#     4 in s,
#     16 in range(10, 20, 2),
#     sep="\n"
# )



s = "Ahoj, já jsem dlouhý string!"
# l = list(s)

# print(l)
# print(l[12])
# print(l[12:17])
# print(l[:6])
# print(l[22:])

# print(l[-3])
# print(l[-8:-3])
# print(l[-3:-8])
# print(l[15:5:-1])
# print(l[::-1])

l = ( "_" + ch + "_" for ch in s if ch not in " ,!" )
# for ch in s:
#     if ch not in " ,!":
#         l.append("_" + ch + "_")

d = { ch : i for i, ch in enumerate(s) if ch not in ", !" }
s = { ch for ch in s if ch not in ", !" }

print(list(set(s)))


