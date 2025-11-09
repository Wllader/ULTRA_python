from threading import Thread
import time

def call_from_thread(message:str, count:int=5):
    for _ in range(count):
        print(f"From thread: {message}")
        time.sleep(.5)

def main():
    thread = Thread(
        target=call_from_thread,
        args=("Hello?", 3) # <- Passing arguments to the target function
    )
    
    thread.start()
    thread.join() # <- Waiting for the thread to finish

    print(f"Finishing main thread!")

if __name__ == "__main__":
    main()