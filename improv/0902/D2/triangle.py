

class Triangle:
    def __init__(self, vyska):
        self.h = vyska

    # Privátní API
    def _ra(self):
        l_rows = []

        for i in range(1, self.h+1):
            # print(i*"*")
            l_rows.append( i*"*" )

        return "\n".join(l_rows)

    def _el_w(self, w):
        l_rows = []

        for i in range(1, w+1, 2):
            pocet_mezer = (w - i) // 2

            # print(
            #     pocet_mezer*" " + i*"*" + pocet_mezer*" "
            # )
            l_rows.append( pocet_mezer*" " + i*"*" + pocet_mezer*" " )

        return "\n".join(l_rows)

    def _el(self):
        # a_n = a_1 + (n-1)*d
        w = 1 + 2*(self.h - 1)
        return self._el_w(w)


    # Veřejné API
    def pravouhly(self):
        return self._ra()

    def rovnoramenny(self):
        return self._el()


t = Triangle(6)

print(
    t.pravouhly(),
    t.rovnoramenny(),

    sep="\n\n"
)