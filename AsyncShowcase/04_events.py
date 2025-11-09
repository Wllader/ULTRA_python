from threading import Event, Thread
from time import sleep

def worker(name:str, event:Event):
    print(f"Worker {name} is waiting for start")
    event.wait() # <-- Waiting for the event

    print(f"Worker {name} started.")
    for _ in range(5):
        print(f"{name} is working...")
        sleep(1)

    print(f"Worker {name} finished.")


def main():
    event = Event()
    Thread(
        target=worker,
        args=("Bob", event,)
    ).start()

    sleep(3)
    print("Main thread sets event")
    event.set()

    print("Main thread finished")

if __name__ == "__main__":
    main()
