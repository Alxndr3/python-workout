"""Create a list whose elements are strings--the names of people in your
family. Now use a set comprehension (and, better yet, a nested set
comprehension) to find which letters are used in your family members’
names."""


import string


def family_name_letters(flist):
    return {letter for name in flist for letter in name}


flist = ["alexandre", "debora", "rafael"]


"""Solution to chapter 7, exercise 34, beyond 3: letters_in_names"""


def letters_in_names(list_of_names):
    return {one_letter
            for one_letter in ''.join(list_of_names)
            if one_letter in string.ascii_letters}


# print(family_name_letters(flist))
print(letters_in_names(flist))
