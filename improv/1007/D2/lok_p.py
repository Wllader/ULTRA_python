

# def foo(x):
#     x.append(999)

# p = [1, 2, 3]
# print(f"{p=}")
# foo(p)
# print(f"{p=}")



def goo(diacriticable=20):
    print(diacriticable)


def main():
    dz = 5
    print(__name__)
    goo(dz)

    for i in range(10):
        print(i)

    print(i)

    def a():
        print(i)


    a()


if __name__ == "__main__":
    main()

