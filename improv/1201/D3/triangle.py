
def triangle_ra(h:int):
    for i in range(1, h+1):
        print(i*"*")

def triangle_el(h:int):
    w = 1 + (h-1)*2
    triangle_el_w(w)


def triangle_el_w(w:int):
    for i in range(1, w+1, 2):
        pocet_mezer = (w-i) // 2

        print(pocet_mezer*" " + i*"*" + pocet_mezer*" ")


class Triangle: #todo implement
    def __init__(self, h:int):
        self.vyska = h

    # Funkce...
    def _triangle_el_w(self, w:int) -> str:
        l = []
        for i in range(1, w+1, 2):
            pocet_mezer = (w-i) // 2
            l.append(pocet_mezer*" " + i*"*" + pocet_mezer*" ")

        return "\n".join(l)

    def get_pravouhly(self) -> str:
        l = []
        for i in range(1, self.vyska+1):
            l.append(i*"*")

        return "\n".join(l)

    def get_rovnoramenny(self) -> str:
        w = 1 + (self.vyska-1)*2
        return self._triangle_el_w(w)

    def pravouhly(self):
        print(self.get_pravouhly())

    def rovnoramenny(self):
        print(self.get_rovnoramenny())



t = Triangle(6)
# t.pravouhly()
# t.rovnoramenny()


# try:
#     print("Otevírání souboru...")
#     f = open("trojuhelniky.txt", "w")
#     print("Soubor otevřen.")

#     print("Zápis...")
#     f.write(f"{1/2}")
#     f.write(f"{1/0}")
#     print("Konec zápisu.")
# # except:
# #     print("A jéje! Výjimka!")

# finally:
#     print("Zavírání souboru...")
#     f.close()
#     print("Soubor uzavřen.")

with open("trojuhelniky.txt", "w") as f:
    f.write(f"{1/2}\n")
    f.write(t.get_pravouhly())
    f.write(f"{1/0}")


