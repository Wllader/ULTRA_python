from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
from time import sleep
from random import random


def task(name:str, n:int):
    print(f"+ {name} started @ {current_thread().name}")
    sleep(random() * 5 + 1)
    print(f"- {name} ended")

    return 5*n + n*n

def main():    
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(
            task,
            [f"Task-{i}" for i in range(1, 7)], # <-- First iterable is itrable of first arguments for all the tasks
            range(1, 7)                         # <-- Second is for second arguments for all the tasks
        )

    print("Results:", list(results))
    print("Main thread finished")

if __name__ == "__main__":
    main()
