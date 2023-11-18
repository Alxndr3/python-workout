import time


def elapsed_since(iterable):
    last_time = None
    for item in iterable:
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)
        last_time = time.perf_counter()
        yield (delta, item)


i = elapsed_since('Hello, World!')

print(next(i))
time.sleep(3)
print(next(i))
time.sleep(1)
print(next(i))
