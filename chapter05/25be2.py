"""
Write a “factorial” function that takes any number of numeric arguments and
returns the result of multiplying them all by one another.
"""


def factorial(*xargs):
    fact = xargs[0]
    for x in range(len(xargs)):
        if x:
            fact *= xargs[x]

    print(fact)


factorial(1, 2, 3, 4)


"""Solution to chapter 6, exercise 25, beyond 2: factorialish"""

def factorialish(*args):
    if not args:
        return 0

    total = args[0]
    for one_number in args[1:]:
        total *= one_number

    return total

