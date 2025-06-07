from contextlib import contextmanager
from time import perf_counter as pc


@contextmanager
def timer(name=None):
    start_time = pc()
    try:
        yield
    finally:
        print(f"{name}\t{pc() - start_time:.4f}s")


if __name__ == "__main__":
    with timer():
        l = list(range(25, 10_000_000))
        l = [ i**2 for i in l ]