"""Given a text file, what are the lengths of the different words? Return a set
of different word lengths in the file."""


def words_length(filename):
    return {len(wlen) for wlen in open(filename)}


"""Solution to chapter 7, exercise 34, beyond 2: word_lengths"""


def word_lengths(filename):
    return {len(one_word)
            for one_line in open(filename)
            for one_word in one_line.split()}


print(words_length("american-english"))
