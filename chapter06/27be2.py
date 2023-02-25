"""Write a function, getitem, that takes a single argument and returns a
function f. The returned f can then be invoked on any data structure whose
elements can be selected via square brackets, and then returns that item. So if
I invoke f = getitem('a'), and if I have a dict d = {'a':1, 'b':2}, then f(d)
will return 1. (This is very similar to operator.itemgetter, a very useful
function in many circumstances.)"""


def getitem(arg):

    def f(data):
        try:
            for x in data:
                if x == arg:
                    return data[arg]
        except TypeError:
            for x in data:
                if x == arg:
                    return x

    return f


d = {'a': 1, 'b': 2}

f = getitem('a')

print(f(d))


"""Solution to chapter 6, exercise 27, beyond 2: getitem"""


def getitem(index):
    def inner(data):
        return data[index]
    return inner
