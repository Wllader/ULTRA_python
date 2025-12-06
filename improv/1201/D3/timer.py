from time import perf_counter as pc
from contextlib import contextmanager


@contextmanager
def timer(name:str=""):
    start_time = pc()
    try:
        yield
    finally:
        print(f"{name}\t{pc() - start_time:1.4f}s")



if __name__ == "__main__":
    with timer("test"):
        l = list(range(1, 10_000_000))
        l = [ n**2 for n in l ]