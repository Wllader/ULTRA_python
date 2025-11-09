from threading import Thread, current_thread
import time

def call_from_thread():
    for _ in range(5):
        print(f"Hello from {current_thread().name} thread!")
        time.sleep(1)

def main():
    thread = Thread(target=call_from_thread)
    thread.start()
    thread.join()

    print(f"Finishing main thread!")

if __name__ == "__main__":
    main()