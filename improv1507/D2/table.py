
# def print_full_line(l:int):
#     print(l*"#")

# def print_row(l:int):
#     print("#" + (l-2)*" " + "#")

# def print_rows(l:int, n:int = 5):
#     for _ in range(n):
#         print_row(l)



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
    def draw(self, w:int, h:int):
        self._table_full_line(w, self.char_h)
        self._table_rows(w, self.char_v, h-2)
        self._table_full_line(w, self.char_h)



def main():
    t = Table("-", "|")
    t.draw(15, 30)


if __name__ == "__main__":
    main()