"""Use a nested list comprehension to transform a list of dicts into a list of
two-element (name-value) tuples, each of which represents one of the name-value
pairs in one of the dicts. If more than one dict has the same name-value pair,
then the tuple should appear twice."""


def two_elements(dictlist):
    return [(key, value)
            for one_dict in dictlist
            for key, value in one_dict.items()]


dictlist = [{'a': 1}, {'b': 2}, {'c': 3, 'd': 4, 'a': 1}]


"""Solution to chapter 7, exercise 31, beyond 2: dicts_to_tuples"""


def dicts_to_tuples(list_of_dicts):
    return [one_tuple
            for one_dict in list_of_dicts
            for one_tuple in one_dict.items()]


print(two_elements(dictlist))
