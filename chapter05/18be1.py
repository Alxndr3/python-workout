"""Iterate over the lines of a text file. Find all of the words (i.e.,
non-whitespace surrounded by whitespace) that contain only integers, and sum
them."""

def iterate_sum(filename):
    for line in open(filename):
        sum_int = 0
        for i in line.strip().split(":"):
            try:
                sum_int += int(i)
            except:
                pass
        print(sum_int)


"""Solution to chapter 5, exercise 18, beyond 1: sum_ints"""

def sum_ints(filename):
    total = 0

    for one_line in open(filename):
        for one_word in one_line.split():
            if one_word.isdigit():
                total += int(one_word)

    return total

iterate_sum("/etc/passwd")

