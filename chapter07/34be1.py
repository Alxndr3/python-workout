"""In the /etc/passwd file you used earlier, what different shells (i.e.,
command interpreters, named in the final field on each line) are assigned to
users? Use a set comprehension to gather them."""


def dif_shells(filename):
    return {shell.split(":")[-1] for shell in open(filename)}


"""Solution to chapter 7, exercise 34, beyond 1: different_shells"""


def different_shells(filename):
    return {one_line.split(':')[-1].strip()
            for one_line in open(filename)
            if not one_line.startswith(('\n', '#'))}


print(dif_shells("passwd"))
