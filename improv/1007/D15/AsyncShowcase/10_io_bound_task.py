from threading import Thread, Event
import requests
from time import perf_counter as pc

urls:list[str] = {
    "https://www.python.org",
    "https://www.seznam.cz",
    "https://www.twitch.tv",
    "https://www.youtube.com",
    "https://www.google.com"
}


def fetch_url(url:str, event:Event=None):
    if event is not None:
        event.wait()

    response = requests.get(url)
    print(f"Fetched {url}: {len(response.content)} bytes")

def concurrent_fetching():
    global urls

    event = Event()
    threads:list[Thread] = []
    for url in urls:
        t = Thread(
            target=fetch_url,
            args=(url, event)
        )
        threads.append(t)
        t.start()

    start_time = pc()
    event.set()

    for t in threads:
        t.join()

    end_time = pc()

    return end_time - start_time

def serial_fetching():
    start_time = pc()

    for url in urls:
        fetch_url(url)

    end_time = pc()

    return end_time - start_time

if __name__ == "__main__":
    runs = 20
    serial_time, concurent_time = 0, 0
    print("\n\nStarting serial runs:")
    for _ in range(runs):
        serial_time += serial_fetching()

    print("\n\nStarting concurrent runs:")
    for _ in range(runs):
        concurent_time += concurrent_fetching()


    print("\n\nPrinting results:")
    serial_time /= runs
    concurent_time /= runs

    print(f"{serial_time=:1.4f}s")
    print(f"{concurent_time=:1.4f}s")
    print(f"Improvement: {serial_time/concurent_time:1.4f}x")
