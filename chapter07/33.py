"""In this exercise, we’re going to create a slight variation on map, one that
applies a function to each of the values of a dict. The result of invoking this
function, transform_values, is a new dict whose keys are the same as the input
dict, but whose values have been transformed by the function. (The name of the
function comes from Ruby on Rails, which provides a function of the same name.)
The function passed to transform_values should take a single argument, the
dict’s value."""


def transform_values(func, mydict):
    return {key: func(value, 2)
            for key, value in mydict.items()}


"""Solution to chapter 7, exercise 33: transform_values"""


def transform_values(func, a_dict):
    """Takes two arguments, a function and a dict.
Returns a dict in which the keys are the original
dict's keys, but the values are the result of invoking
the function on each original value.
"""
    return {key: func(value)
            for key, value in a_dict.items()}


mydict = {'a': 1, 'b': 2, 'c': 3}
print(transform_values(pow, mydict))

