"""In this exercise, you can assume that your Python program contains a list
of integers. We want to print the number of different integers contained within
that list. Thus, consider the following:

numbers = [1, 2, 3, 1, 2, 3, 4, 1]

With the definition provided, running len(numbers) will return 7, because the
list contains seven elements. How can we get a result of 4, reflecting the fact
that the list contains four different values? Write a function, called
how_many_different_numbers, that takes a single list of integers and returns
the number of different integers it contains."""


def how_many_different_number(n):
    return set(n)


def how_many_different_numbers_bs(numbers):
    unique_numbers = set(numbers)         ❶
    return len(unique_numbers)


numbers = [1, 2, 3, 1, 2, 3, 4, 1]
print(how_many_different_number(numbers))

