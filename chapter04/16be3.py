"""Write a function , dict_partition, that takes one dict (d) and a function
(f) as arguments. dict_partition will return two dicts, each containing
key-value pairs from d. The decision regarding where to put each of the
key-value pairs will be made according to the output from f, which will be run
on each key-value pair in d. If f returns True, then the key-value pair will be
put in the first output dict. If f returns False, then the key-value pair will
be put in the second output dict."""


def odd_even(v):
    if v % 2 == 0:
        return True
    else:
        return False


def dict_partition(d, f):
    d1 = {}
    d2 = {}
    for k, v in d.items():
        if f(v):
            d1[k] = v
        else:
            d2[k] = v
    return (d1, d2)


"""Solution to chapter 4, exercise 16, beyond 3: partition_dict"""


def partition_dict(d, f):
    output_true = {}
    output_false = {}

    for key, value in d.items():
        if f(key, value):
            output_true[key] = value
        else:
            output_false[key] = value

    return output_true, output_false



d = {'a': 1, 'b': 2, 'c': 3}
f = odd_even

print(dict_partition(d, f))

