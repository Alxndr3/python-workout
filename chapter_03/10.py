def mysum(*args):
    result = args[0]

    for x in range(len(args)):
        if x == 0:
            pass
        else:
            result += args[x]
    return result


def mysum_bs(*items):
    if not items:
        return items
    output = items[0]
    for item in items[1:]:
        output += item
    return ouput


def mysum_bigger_than(threashold=None, *args):
    if not threashold:
        return None
    output = args[0]
    for arg in args[1:]:
        if arg < threashold:
            pass
        else:
            output += arg
    return output


def sum_numeric(*args):
    """Write a function, sum_numeric, that takes any number of arguments. If
    the argument is or can be turned into an integer, then it should be added
    to the total. Arguments that can’t be handled as integers should be ignored.
    The result is the sum of the numbers. Thus, sum_numeric(10, 20, 'a', '30', 'bcd')
    would return 60. Notice that even if the string 30 is an element in the list,
    it’s converted into an integer and added to the total.
    """
    soma = 0

    for arg in args:
        try:
            soma += int(arg)
        except:
            pass
    return soma


def join_dicts(dict_list):
    """Return a dict from a list of dicts combining them all. if a key occurs
    in more than one, then teh value shoud be a list containing all values from
    the argumens.
    """

    d1 = {}

    for x in dict_list:
        for k, v in x.items():
            if k in d1:
                if type(d1[k]) is list:
                    d1[k].append(v)
                else:
                    d1[k] = [d1[k]]
                    d1[k].append(v)
            else:
                d1[k] = v
    return d1


def combine_dicts(*args):
    """Return a dict, the result of combining all elements of args (which shoud
    be dicts). If a key occurs in more than one, then the value shoud be a list
    containing all values from the arguments.
    """

    output = {}

    for d in args:
        for key, value in d.items():
            if key in output:
                try:
                    output[key].append(value)
                except AttributeError:
                    output[key] = [output[key], value]
            else:
                output[key] = value

    return output


d1 = [{'a': 1, 'b': 2}, {'b': 3, 'a': 4}, {'d': 4, 'a': 5}, {'d': 4, 'a': 5}]
print(combine_dicts({'a': 1, 'b': 2}, {'b': 3, 'a': 4}, {'c': 1}))

