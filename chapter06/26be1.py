"""
Expand the program you wrote, such that the user’s input can contain any
number of numbers, not just two. The program will thus handle + 3 5 7 or / 100
5 5, and will apply the operator from left to right--giving the answers 15 and
4, respectively.
"""


import operator


def calc(operation):

    op = operation.split()[0]
    nums = operation.split()[1:]
    count = 0
    res = 0


    match op:
        case '+':
            for x in nums:
                if count == 0:
                    res = int(nums[0])
                    count += 1
                else:
                    res += int(x)
            return res
        case '-':
            for x in nums:
                if count == 0:
                    res = int(nums[0])
                    count += 1
                else:
                    res -= int(x)
            return res
        case '*':
            for x in nums:
                if count == 0:
                    res = int(nums[0])
                    count += 1
                else:
                    res *= int(x)
            return res
        case '%':
            for x in nums:
                if count == 0:
                    res = int(nums[0])
                    count += 1
                else:
                    res %= int(x)
            return res

        case '/':
            for x in nums:
                if count == 0:
                    res = int(nums[0])
                    count += 1
                else:
                    res /= int(x)
            return res
        case '**':
            for x in nums:
                if count == 0:
                    res = int(nums[0])
                    count += 1
                else:
                    res = int(res) ** int(x)
            return res
        case _:
            return 'Please choose one mathematical operation: + - * % / **'


#print(calc('** 3 3 3'))


"""Solution to chapter 6, exercise 26, beyond 1: calc_args"""

import operator


def calc_args(to_solve):

    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}

    op, *numbers = to_solve.split()

    if not numbers:
        return 0

    output = int(numbers[0])
    for one_number in numbers[1:]:
        output = operations[op](output, int(one_number))

    return output


