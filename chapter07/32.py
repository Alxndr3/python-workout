"""Turn the dict inside out, such that the keys and the values are reversed."""


def turn_dict(mydict):
    return {value: key for key, value in mydict.items()}


mydict = {"a": 1, "b": 2, "c": 3}


"""Solution to chapter 7, exercise 32: flipped_dict"""


def flipped_dict(a_dict):
    """Gets a dict as an argument.
Returns a dict as output. The output dict's keys
are the input dict's values, and vice versa.
"""
    return {value: key
            for key, value in a_dict.items()}


print(turn_dict(mydict))

