from threading import Thread, current_thread
from time import sleep

def infinite_task():
    i = 0
    while True:
        i += 1
        print(f"{current_thread().name}: {i}")
        sleep(.5)

def main():
    t = Thread(
        target=infinite_task,
        daemon=True
    )

    t2 = Thread(
        target=infinite_task
    )

    t.start()
    t2.start()

    sleep(3)
    print("Finishing main thread!")

if __name__ == "__main__":
    main()