from threading import Thread, current_thread
import time

def call_from_thread(message:str, count:int=5):
    for _ in range(count):
        print(f"From thread: {message}")
        time.sleep(1)

def main():
    thread = Thread(
        target=call_from_thread,
        args=("Hello!",)
    )
    thread.start()
    thread.join()

    print(f"Finishing main thread!")

if __name__ == "__main__":
    main()