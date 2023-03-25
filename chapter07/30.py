"""In this exercise, we’ll practice doing such unraveling. Write a function
that takes a list of lists (just one element deep) and returns a flat,
one-dimensional version of the list. Thus, invoking

flatten([[1,2], [3,4]])

will return

[1,2,3,4]"""


def flatten_list(my_list):
    return [inner_list[x] for inner_list in my_list for x in
            range(len(inner_list))]


"""Solution to chapter 7, exercise 29: flatten"""


def flatten(mylist):
    """Expects to get a nested list (a list of lists)
as input. Returns a flattened list, containing the
elements of mylist in order, as output.
"""
    return [one_element
            for one_sublist in mylist
            for one_element in one_sublist]


print(flatten_list([[1, 2], [3, 4]]))
print(flatten([[1, 2], [3, 4]]))
