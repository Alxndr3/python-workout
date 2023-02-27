"""For this exercise, write a function (join_numbers) that takes a range of
integers. The function should return those numbers as a string, with commas
between the numbers. That is, given range(15) as input, the function should
return this string:

ex.
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14"""


def join_numbers(numbers):
    ran = [str(x) for x in numbers]

    return ','.join(ran)


print(join_numbers(range(15)))


"""Solution to chapter 7, exercise 28: join_numbers"""


def join_numbers(numbers):
    """Takes an iterable of numbers as input.
Output is a string containing the numbers in that iterable,
separated by commas.
"""
    return ','.join(str(number)
                    for number in numbers)

