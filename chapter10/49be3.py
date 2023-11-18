def pow_func(element):
    return pow(2, element)


def gen_func(iterable, func):
    for element in iterable:
        yield func(element)


"""Solution to chapter 10, exercise 49, beyond 3: yield_filter"""


def yield_filter(data, func):
    for one_item in data:
        if func(one_item):
            yield one_item


y = gen_func([1, 2, 3, 4, 5], pow_func)

print(list(y))
