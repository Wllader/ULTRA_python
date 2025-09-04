

class Table:
    def __init__(self, char_h="#", char_v=None):
        self.char_h = char_h
        self.char_v = char_v if char_v is not None else char_h

    def _full_line(self, l):
        print(l*self.char_h)

    def _rows(self, l, count=1):
        for _ in range(count):
            print(f"{self.char_v}{(l-2)*" "}{self.char_v}")

    def draw(self, w, h):
        self._full_line(w)
        self._rows(w, h-2)
        self._full_line(w)


t = Table()
t.draw(25, 8)

t2 = Table("=", "|")
t2.draw(5, 12)
