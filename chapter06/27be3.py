"""Write a function, doboth, that takes two functions as arguments (f1 and f2)
and returns a single function, g. Invoking g(x) should return the same result
as invoking f2(f1(x))."""


def doboth(f1, f2):

    def ret(g):
        return f2(f1(g))

    return ret


def f1(x):
    pass


def f2(x):
    pass


x = 1
g = doboth(f1, f2)

print(g(f1(x)))


"""Solution to chapter 6, exercise 27, beyond 3: doboth"""


def doboth(f1, f2):
    def inner(data):
        return f2(f1(data))
    return inner
