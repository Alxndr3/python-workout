"""Ask the user to enter integers, separated by spaces. From this input, create
a dict whose keys are the factors for each number, and the values are lists
containing those of the users’ integers that are multiples of those
factors."""

from collections import defaultdict


def key_factors():
    d = defaultdict(list)
    nums = input("Enter numbers: ")

    for n in nums.split():
        n = int(n)
        for x in range(1, n + 1):
            if n % x == 0:
                d[n].append(x)

    return d


print(key_factors())


"""Solution to chapter 5, exercise 19, beyond 2: factors"""

from collections import defaultdict


def factors():
    output = defaultdict(list)

    numbers = input("Enter numbers, separated by spaces: ").split()

    for one_number in numbers:
        if not one_number.isdigit():
            print(f'Ignoring {one_number}')
            continue

        one_number = int(one_number)
        for i in range(1, one_number):
            if not one_number % i:
                output[one_number].append(i)

        output[one_number].append(one_number)

    return output
