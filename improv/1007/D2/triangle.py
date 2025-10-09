

def triangle_ra(vyska:int):
    for i in range(1, vyska+1):
        print(i*"*")


def triangle_el_w(sirka:int):
    for i in range(1, sirka+1, 2):
        pocet_mezer = (sirka-i) // 2
        print(
            pocet_mezer*" "+i*"*"+pocet_mezer*" "
        )

def triangle_el(vyska:int):
    sirka = 1 + 2*(vyska - 1)
    triangle_el_w(sirka)


#Todo Turn raw functions into Class "Triangle"
#Todo Triangle.pravouhly/rovnoramenny returns str


if __name__ == "__main__":
    VYSKA = 6
    # triangle_ra(VYSKA)

    triangle_el(VYSKA)