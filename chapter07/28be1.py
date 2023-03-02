"""As in the exercise, take a list of integers and turn them into strings.
However, you’ll only want to produce strings for integers between 0 and
10. Doing this will require understanding the if statement in list
comprehensions as well."""


def int_to_string(intlist):
    return ''.join([str(i) for i in intlist if i < 11])


integers = [1, 2, 3, 4, 5, 11]

print(int_to_string(integers))


"""Solution to chapter 7, exercise 28, beyond 1: join_under_10"""


def join_under_10(numbers):
    return ','.join(str(number)
                    for number in numbers
                    if 0 <= number <= 10)
