from threading import Thread, Lock
import time

counter = 0
counter_lock = Lock()

def add(name:str, n:int):
    global counter
    with counter_lock:  # <- Other threads will wait here while the lock is in use
        for _ in range(n):
            print(f"{name}: +1")
            counter += 1
            time.sleep(.1)

        print(f"Current counter state: {counter}")
        time.sleep(1)

def main():
    global counter
    print(f"Initial counter state: {counter}")

    threads:list[Thread] = []
    for i in range(1, 4):
        t = Thread(
            target=add,
            args=(f"Thread {i}", i)
        )

        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Final counter state: {counter}")


if __name__ == "__main__":
    main()