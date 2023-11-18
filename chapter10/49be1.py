import time


def elapsed_since(iterable, wait):
    last_time = None
    for item in iterable:
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)

        if delta < wait:
            last_time = time.perf_counter()
        time.sleep(wait)
        yield (delta, item)


def elapsed_since_bs(data, min_wait):
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)

        if delta < min_wait:
            time.sleep(min_wait - delta)

        last_time = time.perf_counter()
        yield (delta, item)


i = elapsed_since('Hello, World!', 2)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
