"""In this exercise, plfile applied the plword function to every word in a
file. Write a new function, funcfile, that will take two arguments--a filename
and a function. The output from the function should be a string, the result of
invoking the function on each word in the text file. You can think of this as a
generic version of plfile, one that can return any string value."""


def funcfile(filename, function):
    return ' '.join(function(word)
            for oneline in open(filename)
            for word in oneline.split())


def make_upper(word):
    return word.upper()


"""Solution to chapter 7, exercise 31, beyond 1: funcfile"""


def funcfile(filename, func):
    return ' '.join(func(one_word)
                    for one_line in open(filename)
                    for one_word in one_line.split())


print(funcfile('piglatin.txt', make_upper))
