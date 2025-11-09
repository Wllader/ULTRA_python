from threading import Thread
import time

def call_from_thread(name:str, count:int=5):
    for i in range(count):
        print(f"Thread {name}: {i+1}/{count}")
        time.sleep(.5)

def main():
    threads:list[Thread] = []
    for i in range(3):
        thread = Thread(
            target=call_from_thread,
            args=(f"{i+1}", 3) # <- Passing arguments to the target function
        )

        threads.append(thread)
        thread.start()

    for t in threads:
        t.join() # <- Waiting for all the threads to finish

    print(f"Finishing main thread!")

if __name__ == "__main__":
    main()