def mychaing(*args):
    for iterable in args:
        for item in iterable:
            yield item


obj = mychaing((1, 2, 3), (4, 5, 6), {'a': 1, 'b': 2})

print(next(obj))
print(next(obj))
