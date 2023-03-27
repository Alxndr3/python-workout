"""Write a version of the flatten function mentioned earlier called flatten_odd
_ints. It’ll do the same thing as flatten, but the output will only contain
odd integers. Inputs that are neither odd nor integers should be excluded.
Inputs containing strings that could be converted to integers should be
converted; other strings should be excluded."""


def flatten_odd_ints(mylist):
    return [int(one_item) for one_sublist in mylist
            for one_item in one_sublist
            if isinstance(one_item, str)
            and int(one_item) % 2 != 0
            or isinstance(one_item, int)
            and one_item % 2 != 0]


"""Solution to chapter 7, exercise 29, beyond 1: flatten_odd_ints"""


def flatten_odd_ints_bs(mylist):
    return [int(str(one_element))
            for one_sublist in mylist
            for one_element in one_sublist
            if str(one_element).strip().isdigit() and int(one_element) % 2 == 1]


print(flatten_odd_ints([[1, 2], ['3', '4'], [5.3, 6.4]]))
print(flatten_odd_ints_bs([[1, 2], ['3', '4'], [5.3, 6.4]]))

