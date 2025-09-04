

# l = list("Ahoj!")

# for i in range(0, len(l)):
#     char = l[i]
#     print(char)

# for char in l:
#     print(char)

# for i, char in enumerate(l):
#     print(f"{i}: {char}")


# players = ["Wllader", "Boris", "Honza21"]
# hps = [100, 56, 11]


# for p, hp in zip(players, hps):
#     print(f"{p} : {hp}")


from sys import getsizeof


r = range(1, 1_000_000)
l = list(r)

print(f"Range: {getsizeof(r)}\nList: {getsizeof(l)}")
