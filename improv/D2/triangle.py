class Triangle:
    # Konstruktor:
    def __init__(self, vyska):
        self.vyska = vyska

    @staticmethod
    def fromSirka(sirka):
        vyska = (sirka + 1)//2
        return Triangle(vyska)

    # Privátní API
    def _triangle_ra(self, vyska):
        l = []
        for i in range(1, vyska+1):
            l.append(i*"*")
            #~ s += i*"*" + "\n"
            #~ print(i*"*")
        
        return "\n".join(l)

    def _triangle_el_w(self, sirka):
        l = []
        for i in range(1, sirka+1, 2):
            pocet_mezer = (sirka - i) // 2

            l.append(
                pocet_mezer*" " + i*"*" + pocet_mezer*" "
            )

        return "\n".join(l)

    def _triangle_el_h(self, vyska):
        sirka = 1 + (vyska - 1)*2
        return self._triangle_el_w(sirka)

    # Veřejné API:
    def pravouhly(self):
        return self._triangle_ra(self.vyska)

    def rovnoramenny(self):
        return self._triangle_el_h(self.vyska)


def main():
    t = Triangle(50)

    # t.rovnoramenny()
    # print()
    print(t.pravouhly())

    # t2 = Triangle.fromSirka(12)
    # t2.rovnoramenny()


if __name__ == "__main__": main()
