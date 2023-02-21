"""
Write a function, apply_to_each, that takes two arguments: a function that
takes a single argument, and an iterable. Return a list whose values are the
result of applying the function to each element in the iterable. (If this
sounds familiar, it might be--this is an implementation of the classic map
function, still available in Python. You can find a description of map in
chapter 7.)
"""


def apply_to_each(func, ite):
    for x in ite:
        print(func(x, x))


apply_to_each(pow, (1, 2, 3, 4))



"""Solution to chapter 6, exercise 26, beyond 2: apply_to_each"""


def apply_to_each(f, seq):

    return [f(one_item)
            for one_item in seq]

