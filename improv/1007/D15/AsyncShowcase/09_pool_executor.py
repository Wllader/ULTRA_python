from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
from time import sleep
from random import random

def task(n:int, greet:str):
    print(greet)
    name = current_thread().name
    print(f"+ {name} started.")
    sleep(random() * 5 + 1)
    print(f"- {name} ended.")

    return 5*n + n*n

def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(
            task,
            range(1, 7),
            [f"Greetings-{i}" for i in range(1, 7)],
        )

    print("Results:", list(results))
    print("Main thread finished")

if __name__ == "__main__":
    main()