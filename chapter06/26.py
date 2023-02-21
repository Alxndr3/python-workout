"""
For this exercise, I want you to write a function (calc) that expects a
single argument--a string containing a simple math expression in prefix
notation--with an operator and two numbers. Your program will parse the input
and produce the appropriate output. For our purposes, it’s enough to handle
the six basic arithmetic operations in Python: addition, subtraction,
multiplication, division (/), modulus (%), and exponentiation (**). The normal
Python math rules should work, such that division always results in a
floating-point number. We’ll assume, for our purposes, that the argument will
only contain one of our six operators and two valid numbers.
"""


def calc(operation):

    op, num1, num2 = operation.split()
    num1 = int(num1)
    num2 = int(num2)

    match op:
        case '+':
            return sum((num1, num2))
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '%':
            return num1 % num2
        case '/':
            return num1 / num2
        case '**':
            return pow(num1, num2)
        case _:
            return 'Please choose one mathematical operation: + - * % / **'


print(calc("** 2 3"))


"""Solution to chapter 6, exercise 26: calc"""

import operator


def calc_bs(to_solve):
    """This function expects to get a string containing a
two-argument math expression in prefix notation, and with
whitespace separating the operator and numbers.
The return value is the result from invoking this operation.
"""

    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}

    op, first_s, second_s = to_solve.split()
    first = int(first_s)
    second = int(second_s)

    return operations[op](first, second)
