




class Triangle:
    #Konstruktor:
    def __init__(self, vyska:int):
        self.vyska = vyska

    @staticmethod
    def fromSirka(sirka:int) -> "Triangle":
        vyska = (sirka + 1)//2
        return Triangle(vyska)

    #Privátní API
    def _triangle_ra(self, vyska:int) -> str:
        l = []

        for i in range(1, vyska+1):
            l.append(i*"*")

        return "\n".join(l)


    def _triangle_el_w(self, sirka:int) -> str:
        l = []
        for i in range(1, sirka+1, 2):
            pocet_mezer = (sirka-i) // 2
            l.append(
                pocet_mezer*" "+i*"*"+pocet_mezer*" "
            )

        return "\n".join(l)

    def _triangle_el(self, vyska:int):
        sirka = 1 + 2*(vyska - 1)
        return self._triangle_el_w(sirka)


    #Veřejné API
    def pravouhly(self) -> str:
        return self._triangle_ra(self.vyska)
    
    def rovnoramenny(self) -> str:
        return self._triangle_el(self.vyska)
    
#Todo Turn raw functions into Class "Triangle"
#Todo Triangle.pravouhly/rovnoramenny returns str


if __name__ == "__main__":
    t = Triangle(6)

    # print(t.pravouhly())
    # print(t.rovnoramenny())

    # t2 = Triangle.fromSirka(15)
    # print(t2.pravouhly())
    # print(t2.rovnoramenny())

    # f = open("trojuhelnik.txt", "w")
    # try:
    #     f.write(f"{1+1=}")
    #     f.write("\n")
    #     f.write(f"{5//1=}")
    # finally:
    #     print("Fin")
    #     f.close()


    with open("trojuhelnik.txt", "w") as f:
        f.write(f"{1+1=}")
        f.write("\n")
        f.write(f"{5//0=}")


