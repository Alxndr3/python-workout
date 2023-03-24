"""Show the lines of a text file that contain at least one vowel and contain
more than 20 characters."""


def show_lines(filename):

    with open(filename, 'r') as f:
        return [line for line in f.readlines()
                if len(line) > 20 and
                [x for x in line
                    if x in ['a', 'e', 'i', 'o', 'u']]]


filename = 'words.txt'

print(show_lines(filename))


"""Solution to chapter 7, exercise 29, beyond 1: lines_with_1v20c"""


def lines_with_1v20c(filename):
    return [one_line
            for one_line in open(filename)
            if len(one_line) >= 20 and
            len(set('aeiou') & set(one_line)) >= 1]
