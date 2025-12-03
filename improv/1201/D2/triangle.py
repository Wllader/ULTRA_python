
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
        pass

    # Funkce...
    def get_pravouhly(self) -> str:
        pass

    def get_rovnoramenny(self) -> str:
        pass

    def pravouhly(self):
        pass

    def rovnoramenny(self):
        pass




# Useful hints:
def foo(n:int) -> str:
    return str(n)


def goo(l:list[str]) -> str:
    return "__".join(l)