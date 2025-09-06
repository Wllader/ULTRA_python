from time import perf_counter as pc
from contextlib import contextmanager


# f = open("test.txt", "w")
# try:
#     f.write(str(1 / 0))
# finally:
#     print("Zavřít!")
#     f.close()


# with open("text.txt", "w") as f:
#     f.write(str(5/0))


@contextmanager
def timer(name:str = ""):
    start_time = pc()
    try:
        yield
    finally:
        print(f"{name}\t{pc() - start_time:.4f}s")



if __name__ == "__main__":
    with timer("List performance"):
        l = list(range(25, 10000000))
        l = [ i**2 for i in l ]


