

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
        l:list[str] = []
        for i in range(1, self.vyska+1):
            # print(i*"*")
            # s += i*"*" + "\n"
            l.append(i*"*")

        return "\n".join(l)

    def _triangle_el_w(self, sirka:int) -> str:
        l:list[str] = []
        for i in range(1, sirka+1, 2):
            pocet_mezer = (sirka-i)//2
            # print(pocet_mezer*" " + i*"*" + pocet_mezer*" ")
            l.append(f"{pocet_mezer*" "}{i*"*"}{pocet_mezer*" "}")
        
        return "\n".join(l)

    def _triangle_el(self) -> str:
        sirka = 1 + 2*(self.vyska-1)
        return self._triangle_el_w(sirka)


    # Veřejné API
    def pravouhly(self):
        print(self._triangel_ra())
        print()

    def rovnoramenny(self):
        print(self._triangle_el())
        print()

    def get_pravouhly(self) -> str:
        return self._triangel_ra()
    
    def get_rovnoramenny(self) -> str:
        return self._triangle_el()


if __name__ == "__main__":
    t = Triangle(6)

    # t.pravouhly()
    # t.rovnoramenny()

    # print(
    #     t.get_pravouhly(),
    #     t.get_rovnoramenny(),

    #     sep="\n---\n"
    # )

    # f = open("trojuhelnik.txt", "w")
    # f.write(t.get_pravouhly())
    # f.write("\n---\n")
    # f.write(t.get_rovnoramenny())

    # f.close()

    # try:
    #     print("Try")
    #     f = open("test.txt", "w")
    #     f.write(str(5/0))

    # # except Exception as e:
    # #     print("Except")
    # #     print(e)

    # finally:
    #     print("Finally")
    #     f.close()

    # print("Past try_block")


    with open("test.txt", "w") as f:
        f.write(str(5/3))
        f.write(str(5/0))



