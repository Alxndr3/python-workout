def circle(data, max_times):

    for index in range(max_times):
        yield data[index % len(data)]


print(list(circle("hello", 2)))
