"""The dict.update method merges two dicts. Write a function that takes any
number of dicts and returns a dict that reflects the combination of all of
them. If the same key appears in more than one dict, then the most recently
merged dict’s value should appear in the output."""

def merge_dict(*dicts):
    newdict = {}

    for x in dicts:
        newdict.update(x)

    return newdict


d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 2, 'd': 2, 'e': 3}
d3 = {'f': 1, 'g': 2, 'h': 3}

print(merge_dict(d1, d2, d3))

