from time import perf_counter as pc
from contextlib import contextmanager


@contextmanager
def timer(name:str = ""):
    start_time = pc()
    try:
        yield
    finally:
        print(f"{name} {pc() - start_time:.4f}s")


if __name__ == "__main__":
    with timer("List performance:"):
        l = list(range(25, 1000000))
        l = [ i**2 for i in l ]
