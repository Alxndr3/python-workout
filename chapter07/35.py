"""This exercise, the result of which you’ll use in the next one, asks that
you create a dict whose keys are the (lowercase) letters of the English
alphabet, and whose values are the numbers ranging from 1 to 26. And yes, you
could simply type {'a':1, 'b':2, 'c':3} and so forth, but I’d like you to do
this with a dict comprehension."""


import string
from string import ascii_lowercase


def create_dict():
    return {item[1]: item[0]
            for item in enumerate(ascii_lowercase, 1)}


"""Solution to chapter 7, exercise 35a: gematria_dict"""


def gematria_dict():
    """Function that returns a dictionary of ASCII values
for all lowercase letters. The keys are the letters, and
the values are the numbers, starting with 1 for 'a'.
"""
    return {char: index
            for index, char in enumerate(string.ascii_lowercase, 1)}


print(create_dict())
