from threading import Thread
import time

def infinite_task(name:str):
    i = 0
    while True:
        i += 1
        print(f"Thread {name}: {i}")
        time.sleep(.5)

def main():
    thread = Thread(
        target=infinite_task,
        args=("Hello?",),   # <- When passing an argument, it has to be an iterable
        daemon=True         # <- Marking the thread as daemon
    )                       #  making it stop when all other threads stop
    
    thread.start()
    
    time.sleep(3)
    print(f"Finishing main thread!")

if __name__ == "__main__":
    main()