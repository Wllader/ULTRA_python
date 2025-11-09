from threading import Thread, current_thread
from queue import Queue
from time import sleep
from random import random, randint

def producer(q:Queue, n:int=5):
    name = current_thread().name
    for i in range(n):
        item = f"{name}.{i}"
        print(f"-> Produced\t{item}")
        q.put(item)
        sleep(random() * 1.5 + 0.5)

    q.put(None)

def consumer(q:Queue):
    while True:
        item = q.get()
        if item is None: break
        print(f"<- Consuming\t{item}")
        sleep(random() * 1.5 + 2)


def main():
    q = Queue()

    threads:list[Thread] = []
    for _ in range(3):
        pt = Thread(
            target=producer,
            args=(q, randint(1, 5))
        )

        threads.append(pt)

    ct = Thread(
        target=consumer,
        args=(q,)
    )
    threads.append(ct)

    for t in threads:
        t.start()

    print("Main thread finished")

if __name__ == "__main__":
    main()
