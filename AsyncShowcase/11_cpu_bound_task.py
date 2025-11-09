from threading import Thread, Event
from multiprocessing import Process
from time import perf_counter as pc


def compute(event:Event=None):
    if event is not None:
        event.wait()

    s = 0
    for i in range(10**7):
        s += i

def concurrent_computation():
    event = Event()
    threads:list[Thread] = []
    for _ in range(6):
        t = Thread(
            target=compute,
            args=(event,)
        )
        threads.append(t)
        t.start()

    start_time = pc()
    event.set()

    for t in threads:
        t.join()

    end_time = pc()

    return end_time - start_time

def parallel_computation():
    processes:list[Process] = []

    start_time = pc()
    for _ in range(6):
        p = Process(
            target=compute
        )
        processes.append(p)
        p.start()


    for p in processes:
        p.join()

    end_time = pc()

    return end_time - start_time

def serial_computation():
    start_time = pc()

    for _ in range(6):
        compute()

    end_time = pc()

    return end_time - start_time



if __name__ == "__main__":
    runs = 5
    serial_time, concurrent_time, parallel_time = 0, 0, 0
    print("Starting serial runs")
    for _ in range(runs):
        serial_time += serial_computation()

    print("Starting concurrent runs")
    for _ in range(runs):
        concurrent_time += concurrent_computation()

    print("Starting parallel runs")
    for _ in range(runs):
        parallel_time += parallel_computation()


    print("\n\nPrinting results:")
    serial_time /= runs
    concurrent_time /= runs
    parallel_time /= runs

    print(f"{serial_time=:1.4f}s")
    print(f"{concurrent_time=:1.4f}s")
    print(f"{parallel_time=:1.4f}s")
    print(f"Improvement: {serial_time/concurrent_time:1.4f}x for concurrent")
    print(f"Improvement: {serial_time/parallel_time:1.4f}x for parallel")
