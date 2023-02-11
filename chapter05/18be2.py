"""Create a text file (using an editor, not necessarily Python) containing two
tab-separated columns, with each column containing a number. Then use Python to
read through the file you’ve created. For each line, multiply each first
number by the second, and then sum the results from all the lines. Ignore any
line that doesn’t contain two numeric columns."""

from random import randint


def write_file():
    with open("new_file", "a") as f:
        for x in range(5):
            f.write(f'{randint(1, 10)}\t\t{randint(1, 10)}\n')


def multiply_sum(filename):
    total = 0
    for line in open(filename):
        total += int(line.split()[0]) * int(line.split()[0])

    return total


"""Solution to chapter 5, exercise 18, beyond 2: sum_mult_columns"""

def sum_mult_columns(filename):
    total = 0

    for one_line in open(filename):
        fields = one_line.split()

        if len(fields) != 2:
            continue

        first, second = fields

        if not first.isdigit():
            continue

        if not second.isdigit():
            continue

        total += int(first) * int(second)

    return total


print(multiply_sum("new_file"))

