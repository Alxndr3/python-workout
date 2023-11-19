def my_range(ran, step=2):
    count = 1
    while count <= ran:
        yield count
        count += step


for x in my_range(5):
    print(x)


"""Solution to chapter 10, exercise 50, beyond 3: myrange_generator"""


def myrange(first, second=None, step=1):
    if second is None:
        current = 0
        stop = first

    else:
        current = first
        stop = second

    while current < stop:
        yield current
        current += step
