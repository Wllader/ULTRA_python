from threading import Thread, Event
from time import sleep
from random import random

def worker(name:str, event:Event):
    print(f"Worker {name} is waiting for start")
    event.wait() # <-- Waiting for event

    print(f"Worker {name} started.")
    for _ in range(5):
        print(f"{name} is working")
        sleep(random() * 3 + 2)

    print(f"Worker {name} finished")

def main():
    event = Event()
    names = ["Bob", "Charlie", "Diana", "Elmo"]

    for name in names:
        Thread(
            target=worker,
            args=(name, event)
        ).start()

    sleep(3)
    print("Main thread sets event")
    event.set()

    print("Main thread is finished")

if __name__ == "__main__":
    main()