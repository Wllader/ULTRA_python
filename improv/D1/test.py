

text = "asdasd"
i = 9
f = 9.3
b = False


# if text == "Ahoj":
#     print(1)
# elif i > 5:
#     print(2)
# elif type(f) == float:
#     print(3)
# else:
#     print(10)

# match text:
#     case "Ahoj":
#         print(11)
#         print(12)
#     case "Cau":
#         print(20)
#     case _:
#         print("???")

# i = 1
# while i <= 10:
#     print(i)
#     i += 1 # i = i + 1


# for i in range(10+1):
#     print(i)

# print("Konec")

# l = [1, "a", 8.3, 6, 9]

# for i in range(len(l)):
#     l[i] = 0


# for item in l:
#     item = 0

# print(l)

# cislo = "92"
# print(int(cislo))

# hraci = ["Wllader", "Pavel", "Mikuláš"]
# hps = [100, 73, 5]

# for h in hraci:
#     for hp in hps:
#         print("Hráč " + h + " má " + str(hp) + " životů!")

# for i in range(len(hraci)):
#     print("Hráč " + hraci[i] + " má " + str(hps[i]) + " životů!")

# for i, h in enumerate(hraci):
#     print("Hráč č. " + str(i) + ": " + h + " má " + str(hps[i]) + " životů!")

# for hrac, hp in zip(hraci, hps):
#     # print("Hráč " + hrac + " má " + str(hp) + " životů!")
#     print(f"Hráč {hrac} má {hp} životů!")

from sys import getsizeof

# l = []

# for i in range(0, 25, 3):
#     print(i)
#     if i % 2:
#         l.append(1)
#         l.append(2)
#     else:
#         if len(l) > 0:
#             l.pop()

# print(l)

# print(
#     list(
#         range(1, 25, 2)
#     )
# )

# l = []
# for i in range(25):
#     if i % 2 == 1:
#         l.append(i)

#     print("?")

# print(l)



st = "Tohle je string"
# l = list(st)
# t = tuple(st)
# s = set(st)
# d = {
#     "apple" : "jablko",
#     "pear"  : "hruška",
#     1 : "2",

# }

# a současně : and
# nebo : or

abc = "abcdefghijklmnopqrstuvwxyz"
# li = []
# for letter in st.lower():
#     print(letter)
#     if letter in abc and abc.index(letter) < 12:
#         li.append(letter)


# li = [ f"Písmenko: {letter}" for letter in st.lower() if letter in abc and abc.index(letter) < 12 ]

# g = ( n*2 for n in [1, 8, 25, 1238] )
# print(g)

# s = { letter for letter in "abcefgccgga" }
# print(s)

# d = { letter : letter.capitalize() for letter in abc }
# print(d["s"])

# paskvil = {
#     i : abc[i:] for i in range(len(abc))
# }
# print(paskvil)

# print(
#     abc,
#     abc[:],
#     abc[5:],
#     abc[:16],
#     abc[5:16],

#     sep="\n"
# )


# print(20*"#")
# print(f"#{18*" "}#")
# print(f"#{18*" "}#")
# print(f"#{18*" "}#")
# print(f"#{18*" "}#")
# print(20*"#")

# def table_full_line(l, char):
#     print(l*char)

# def table_rows(l, char, count):
#     for i in range(count):
#         print(f"{char}{(l-2)*" "}{char}")


# table_full_line(20, "-")
# table_rows(20, "|", 4)
# table_full_line(20, "-")

class Table:
    def __init__(self, char_h, char_v):
        self.char_h = char_h
        self.char_v = char_v

    def _table_full_line(self, l, char):
        print(l*char)

    def _table_rows(self, l, char, count):
        for i in range(count):
            print(f"{char}{(l-2)*" "}{char}")

    def draw(self, w, h):
        self._table_full_line(w, self.char_h)
        self._table_rows(w, self.char_v, h-2)
        self._table_full_line(w, self.char_h)


t = Table("-", "|")
t.draw(25, 12)


t2 = Table("#", "#")
t2.draw(25, 12)

