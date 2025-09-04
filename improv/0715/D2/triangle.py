
# def triangle_ra(vyska):
#     for n in range(1, vyska+1):
#         print(n*"*")

# def triangle_el_w(sirka):
#     for i in range(1, sirka+1, 2):
#         pocet_mezer = (sirka - i) // 2

#         print(
#             f"{pocet_mezer*" "}{i*"*"}{pocet_mezer*" "}"
#         )

# def triangle_el(vyska):
#     sirka = 1 + (vyska - 1)*2
#     triangle_el_w(sirka)


class Triangle:
    def __init__(self, vyska):
        self.vyska = vyska

    #Privátni API
    def _triangle_ra(self, vyska):
        rows = []

        for n in range(1, vyska+1):
            rows.append(n*"*")

        return "\n".join(rows)
    
    def _triangle_el_w(self, sirka):
        rows = []

        for i in range(1, sirka+1, 2):
            pocet_mezer = (sirka - i) // 2

            rows.append(
                f"{pocet_mezer*" "}{i*"*"}{pocet_mezer*" "}"
            )

        return "\n".join(rows)
    
    def _triangle_el(self, vyska):
        sirka = 1 + 2*(vyska - 1)
        return self._triangle_el_w(sirka)

    #Veřejné API
    def pravouhly(self) -> str:
        return self._triangle_ra(self.vyska)

    def rovnoramenny(self) -> str:
        return self._triangle_el(self.vyska)


if __name__ == "__main__":
    t = Triangle(12)

    print(
        t.pravouhly(),
        t.rovnoramenny(),

        sep="\n\n"
    )

    Triangle.pravouhly(t)
    t.pravouhly()