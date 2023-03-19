"""In the previous exercise, we took a sequence of numbers and turned it into a
sequence of strings. This time, we’ll do the opposite--take a sequence of
strings, turn them into numbers, and then sum them. But we’re going to make it
a bit more complicated, because we’re going to filter out those strings that
can’t be turned into integers.

Our function (sum_numbers) will take a string as an argument; for example

10 abc 20 de44 30 55fg 40

Given that input, our function should return 100. That’s because the function
will ignore any word that contains nondigits."""


def sum_numbers(s):
    return sum([int(x) for x in s.split() if x.isdigit()])


def sum_numbers_bs(numbers):
    return sum(int(number)
            for number in numbers.split()
            if number.isdigit())


s = "10 abc 20 de44 30 55fg 40"

