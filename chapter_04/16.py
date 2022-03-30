from collections import defaultdict
"""Write a function, dictdiff, that takes two dicts as arguments. The function
returns a new dict that expresses the difference between the two dicts.
If there are no differences between the dicts, dictdiff returns an empty dict.
For each key-value pair that differs, the return value of dictdiff will have a
key-value pair in which the value is a list containing the values from the two
different dicts. If one of the dicts doesn’t contain that key, it should
contain None."""


def dictdiff1(d1, d2):
    if d1 == d2:
        return {}

    for x in d1:
        nd[x] = [d1.get(x)]

    for x in d1:
        if x in d2 and d1[x] != d2[x]:
            nd[x] = [d1[x], d2[x]]

    for x in d1:
        if x not in d2:
            nd[x] = [d1[x], None]

    for x in d2:
        if x not in d1:
            nd[x] = [None, d2[x]]
    return nd


def dictdiff2(d1, d2):
    nd = {}

    for k, v in d1.items():
        if v not in d2.values():
            nd[k] = [d1.get(k), d2.get(k)]

    for k, v in d2.items():
        if v not in d1.values():
            nd[k] = [d1.get(k), d2.get(k)]

    return nd

def dictdiff_bs(first, second):
    output = {}
    all_keys = first.keys() | second.keys()

    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key),
                           second.get(key)]
    return output


d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}
d3 = {'a': 0, 'b': 2, 'd': 5}


print(dictdiff_bs(d1, d2))



