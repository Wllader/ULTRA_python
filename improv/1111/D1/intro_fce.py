
# w = 9
# h = 12

# print(w*"#")
# for _ in range(h-2):
#     print("#" + (w-2)*" " + "#")
# print(w*"#")


def table_full_line(l, char="#"):
    print(l*char)


def table_rows(l, count, char="#"):
    for _ in range(count):
        print(f"{char}{(l-2)*" "}{char}")


table_full_line(18, "x")
table_rows(18, 5, "|")
table_full_line(18, "^")
