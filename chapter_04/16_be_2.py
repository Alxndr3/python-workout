"""Write a function that takes any even number of arguments and returns a dict
based on them. The even-indexed arguments become the dict keys, while the
odd-numbered arguments become the dict values. Thus, calling the function with
the arguments ('a', 1, 'b', 2) will result in the dict {'a':1, 'b':2} being
returned."""

def even_dicts(*args):
    newdict = {}

    if len(args) % 2 != 0:
        print('Needed even number of arguments.')
    else:
        for x in range(len(args)):
            if x % 2 == 0:
                newdict[args[x]] = args[x + 1]

    print(newdict)


"""Solution to chapter 4, exercise 16, beyond 2: dict_from_list"""

def dict_from_list(*args):
    if len(args) % 2:
        raise ValueError('Need an even number of args')

    output = {}

    while args:
        output[args[0]] = args[1]
        args = args[2:]

    return output


dict_from_list('a', 1, 'b', 2, 'c', 3, 'd')

