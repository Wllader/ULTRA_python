from threading import Thread
from queue import Queue
from time import sleep
from random import random, randint

def producer(q:Queue, name:str, n:int=5):
    for i in range(n):
        item = f"{name}.{i}"
        print(f"--> {name} produced\t{item}")
        q.put(item) # <-- This actually waits when there is space in the Queue
        sleep(random() * 1.5 + 0.5)

    q.put(None)     # <-- Signaling that the production is over


def consumer(q:Queue):
    while True:
        item = q.get()  # <-- This actually waits for items to appear
        if item is None: break
        print(f"<-- Consuming\t{item}")
        sleep(random() * 1.5 + 1.5)        # <-- Simulating slower thread


def main():
    q = Queue() # <-- Can have max capacity

    threads:list[Thread] = []
    for i in range(3):
        pt = Thread(
            target=producer,
            args=(q, f"p{i}", randint(1, 5))
        )

        threads.append(pt)

    ct = Thread(
        target=consumer,
        args=(q,)
    )
    threads.append(ct)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("Main thread finished")


# This is called MPSC (Multiple Producers, Single Consumer)
if __name__ == "__main__":
    main()