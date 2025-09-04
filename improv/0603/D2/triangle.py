
class Triangle:
    #Konstruktor:
    def __init__(self, vyska):
        self.vyska = vyska

    @staticmethod
    def fromSirka(sirka):
        vyska = (sirka + 1)//2
        return Triangle(vyska)

    #Privátni API
    def _triangle_ra(self, vyska):
        l = []

        for i in range(1, vyska+1):
            l.append(i*"*")

        return "\n".join(l)


    def _triangle_el_w(self, sirka):
        l = []

        for i in range(1, sirka+1, 2):
            pocet_mezer = (sirka - i) // 2

            l.append(pocet_mezer*" " + i*"*" + pocet_mezer*" ")

        return "\n".join(l)


    def _triangle_el(self, vyska):
        sirka = 1 + 2*(vyska - 1)
        return self._triangle_el_w(sirka)


    #Veřejné API
    def pravouhly(self) -> str:
        return self._triangle_ra(self.vyska)

    def rovnoramenny(self) -> str:
        return self._triangle_el(self.vyska)




if __name__ == "__main__":
    t = Triangle(8)

    print(t.pravouhly())
    print()
    print(t.rovnoramenny())