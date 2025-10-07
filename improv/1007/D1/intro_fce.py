
# w = 63
# h = 12

# print(w*"#")
# for _ in range(h):
#     print("#" + (w-2)*" " + "#")
# print(w*"#")


# def table_full_line(l, char="#"):
#     print(l*char)

# def table_rows(l, count, char="#"):
#     for _ in range(count):
#         # print("#" + (l-2)*" " + "#")
#         print(f"{char}{(l-2)*" "}{char}")


# table_full_line(18)
# table_rows(18, 5, "|")
# table_full_line(18, ".")


class Box:
    def __init__(self, char="#"):
        self.char = char

    def _full_line(self, l):
        print(l*self.char)

    def _rows(self, l, count):
        for _ in range(count):
            print(f"{self.char}{(l-2)*" "}{self.char}")

    def draw(self, w, h):
        self._full_line(w)
        self._rows(w, h-2)
        self._full_line(w)
        

b = Box(".")
b.draw(10, 12)

