def my_enumerate(data, start=0):
    index = start

    for one_item in data:
        yield (index, one_item)
        index += 1


e = my_enumerate('abcde', 1)
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
