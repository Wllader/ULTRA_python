

# for i in range(6):
#     for j in range(i+1):
#         print("*", end="")
#     print()

# for i in range(1, 7):
#     print(i*"*")

def triangle_ra(h):
    for i in range(1, h+1):
        print(i*"*")


def triangle_el_w(w):
    for i in range(1, w+1, 2):
        pocet_mezer = (w-i)//2

        print(
            pocet_mezer*" " + i*"*" + pocet_mezer*" "
        )

def triangle_el(h):
    w = 1 + 2*(h-1)
    triangle_el_w(w)


class Triangle:
    def __init__():
        pass


if __name__ == "__main__":
    triangle_el(6)

