from threading import Thread, Lock, current_thread
from time import sleep

counter = 0
counter_lock = Lock()

def add(n:int):
    global counter
    with counter_lock:
        for _ in range(n):
            print(f"{current_thread().name}: +1")
            counter += 1
            sleep(.1)

        print(f"Current state of the counter: {counter}")
        sleep(1)

def main():
    global counter
    print(f"Intial counter state: {counter}")

    threads:list[Thread] = []
    for i in range(1, 5):
        t = Thread(
            target=add,
            args=(i,)
        )

        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Final counter state: {counter}")

if __name__ == "__main__":
    main()