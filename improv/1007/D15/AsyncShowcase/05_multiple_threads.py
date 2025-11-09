from threading import Thread, current_thread
import time
from random import randint

def call_from_thread(message:str, count:int=5):
    for _ in range(count):
        print(f"From thread {current_thread().name}: {message}")
        time.sleep(1)

def main():
    threads:list[Thread] = []
    for i in range(3):
        thread = Thread(
            target=call_from_thread,
            args=("Hello!", randint(2, 4))
        )
        threads.append(thread)
        thread.start()

    # for t in threads:
    #     t.join()

    print(f"Finishing main thread!")

if __name__ == "__main__":
    main()