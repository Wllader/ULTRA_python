from threading import Thread
import time

def call_from_thread():
    for _ in range(5):
        print(f"Hello from thread!")
        time.sleep(1)

def main():
    thread = Thread(target=call_from_thread)
    thread.start()

    print(f"Finishing main thread!")

if __name__ == "__main__":
    main()