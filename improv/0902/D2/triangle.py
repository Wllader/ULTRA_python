

class Triangle:
    def __init__(self, vyska):
        self.h = vyska

    # Privátní API
    def _ra(self):
        for i in range(1, self.h+1):
            print(i*"*")

    def _el_w(self, w):
        for i in range(1, w+1, 2):
            pocet_mezer = (w - i) // 2

            print(
                pocet_mezer*" " + i*"*" + pocet_mezer*" "
            )

    def _el(self):
        # a_n = a_1 + (n-1)*d
        w = 1 + 2*(self.h - 1)
        self._el_w(w)


    # Veřejné API
    def pravouhly(self):
        self._ra()

    def rovnoramenny(self):
        self._el()


t = Triangle(6)

t.pravouhly()
t.rovnoramenny()