
# print(20*"#")
# print("#" + 18*" " + "#")
# print("#" + 18*" " + "#")
# print("#" + 18*" " + "#")
# print("#" + 18*" " + "#")
# print(20*"#")


def table_full_line(l, char="#"):
    print(l*char)

def table_row(l, char="#"):
    print(char + (l-2)*" " + char)

def table_rows(l, count, char="#"):
    for _ in range(count):
        table_row(l, char=char)


table_full_line(20, char="=")
table_rows(20, 5, char="|")
table_full_line(20, char="=")