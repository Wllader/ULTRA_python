
# w = 9
# h = 12

# print(w*"#")
# for _ in range(h-2):
#     print("#" + (w-2)*" " + "#")
# print(w*"#")


# def table_full_line(l, char="#"):
#     print(l*char)


# def table_rows(l, count, char="#"):
#     for _ in range(count):
#         print(f"{char}{(l-2)*" "}{char}")


# table_full_line(18, "x")
# table_rows(18, 5, "|")
# table_full_line(18, "^")


class Box:
    def __init__(self, char_h="#", char_v=None):
        self.char_h = char_h
        self.char_v = char_v or char_h


    def _full_line(self, l):
        print(l*self.char_h)


    def _rows(self, l, count):
        for _ in range(count):
            print(f"{self.char_v}{(l-2)*" "}{self.char_v}")


    def draw(self, w, h=None):
        h_ = h or w

        self._full_line(w)
        self._rows(w, h_-2)
        self._full_line(w)


b = Box("-", "|")
b2 = Box("*")
b.draw(12, 6)
b2.draw(10)