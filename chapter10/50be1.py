"""Solution to chapter 10, exercise 50, beyond 1: myzip"""


def myzip(*args):
    for i in range(len(min(args, key=len))):
        yield tuple(one_arg[i]
                    for one_arg in args)


a = (1, 2, 3)
b = ('a', 'b', 'c')

result = list(myzip(a, b))

print(result)
