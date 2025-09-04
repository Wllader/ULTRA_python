


# def print_full_line(l:int):
#     print(l*"#")

# def print_row(l):
#     # print("#" + (l-2)*" " + "#")
#     print(f"#{(l-2)*" "}#")

# def print_rows(l, count=1):
#     for _ in range(count):
#         print_row(l)



# print_full_line(20)
# print_rows(20, 4)
# print_full_line(20)


class Table:
    def __init__(self, char_h, char_v):
        self.char_h = char_h
        self.char_v = char_v

    #Privátní API
    def _table_full_line(self, l, char):
        print(l*char)

    def _table_rows(self, l, char, count=1):
        for _ in range(count):
            print(f"{char}{(l-2)*" "}{char}")

    #Veřejné API
    def draw(self, w, h):
        self._table_full_line(w, self.char_h)
        self._table_rows(w, self.char_v, h-2)
        self._table_full_line(w, self.char_h)



# s = "Ahoj"
# f = 3.14
# i = 8
# b = True

# k = f * i
# q = 5*s + "!!"

# print(f"{f**2 + 9 // 4=}")
# print(f"{f*i=}, {5*s+"!!"=}")


def _min(l:list[float]) -> float:
    return min(l)


print(_min([1, 2, -6, 12, -12]))