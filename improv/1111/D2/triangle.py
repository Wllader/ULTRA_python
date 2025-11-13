

# for i in range(6):
#     for j in range(i+1):
#         print("*", end="")
#     print()

# for i in range(1, 7):
#     print(i*"*")

# def triangle_ra(h):
#     for i in range(1, h+1):
#         print(i*"*")


# def triangle_el_w(w):
#     for i in range(1, w+1, 2):
#         pocet_mezer = (w-i)//2

#         print(
#             pocet_mezer*" " + i*"*" + pocet_mezer*" "
#         )

# def triangle_el(h):
#     w = 1 + 2*(h-1)
#     triangle_el_w(w)


class Triangle:
    def __init__(self, vyska:int):
        self.vyska = vyska

    # Privátní API
    def _triangel_ra(self) -> str:
        for i in range(1, self.vyska+1):
            print(i*"*")

    def _triangle_el_w(self, sirka:int) -> str:
        for i in range(1, sirka+1, 2):
            pocet_mezer = (sirka-i)//2

            print(
                pocet_mezer*" " + i*"*" + pocet_mezer*" "
            )

    def _triangle_el(self) -> str:
        sirka = 1 + 2*(self.vyska-1)
        self._triangle_el_w(sirka)


    # Veřejné API
    def pravouhly(self):
        self._triangel_ra()
        print()

    def rovnoramenny(self):
        self._triangle_el()
        print()


if __name__ == "__main__":
    t = Triangle(6)

    t.pravouhly()
    t.rovnoramenny()

