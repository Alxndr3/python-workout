"""Expand the transform_values exercise, taking two function arguments, rather
than just one. The first function argument will work as before, being applied
to the value and producing output. The second function argument takes two
arguments, a key and a value, and determines whether there will be any output
at all. That is, the second function will return True or False and will allow
us to selectively create a key-value pair in the output dict."""


def transform_values(func1, func2, mydict):
    return {key: func1(value)
            for key, value in mydict.items()
            if func2(key, func1(value))}


def func2(key, value):
    if key in 'aeiou' and value % 2 == 0:
        return True
    else:
        return False


"""Solution to chapter 7, exercise 33, beyond 1: transform_values2"""


def transform_values2(func1, func2, a_dict):
    return {key: func1(value)
            for key, value in a_dict.items()
            if func2(key, value)}


mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 4}

print(transform_values(lambda x: x*x, func2, mydict))

