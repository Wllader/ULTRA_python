from time import perf_counter as pc
from contextlib import contextmanager

@contextmanager
def timer(name:str = ""):
    start_time = pc()
    try:
        yield
    finally:
        print(f"{name}\t{pc() - start_time:1.4f}s")