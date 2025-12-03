


# height = 5
# width = 20
# for x in range(0, width):
#     if x == width - 1:
#         print("#")
#     else:
#         print("#", end="")

# for x in range(0, height):
#     for y in range(0, width):
#         if width - y == width:
#             print("#", end="")
#         elif y == width - 1:
#             print("#")
#         else:
#             print(" ", end="")

# for x in range(0, width):
#     print("#", end="")


# def box_full_line(w, char:str="#"):
#     print(w*char)

# def box_row(w, char:str="#"):
#     print(char + (w-2)*" " + char)

# def box_rows(w, h, char:str="#"):
#     for _ in range(0, h-2):
#         box_row(w, char)


# def print_box(w, h, char_v:str="#", char_h:str="#"):
#     box_full_line(w, char_h)
#     box_rows(w, h, char_v)
#     box_full_line(w, char_h)


# print_box(5, 6)
# print_box(7, 12, char_v="|", char_h="-")
# print_box(8, 8, char_h=".")
# print_box(3, 3)



class Box:
    def __init__(self, char_h="#", char_v=None): #todo: char->char_h, add char_v
        self.char_h = char_h
        # self.char_v = char_v if char_v is not None else char_h
        self.char_v = char_v or char_h

    def _full_line(self, l:int):
        print(l*self.char_h)

    def _row(self, l:int):
        print(self.char_v + (l-2) * " " + self.char_v)

    def _rows(self, l:int, count:int):
        for _ in range(count):
            self._row(l)

    
    def draw(self, w, h=None):
        _h = h or w

        self._full_line(w)
        self._rows(w, _h-2)
        self._full_line(w)



b = Box("*")
b2 = Box("-", "|")
b.draw(5)
b2.draw(6, 8)



Box.draw(b2, 12, 6)
b2.draw(12, 6)