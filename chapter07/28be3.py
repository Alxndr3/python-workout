"""Use a list comprehension to reverse the word order of lines in a text file.
That is, if the first line is abc def and the second line is ghi jkl, then you
should return the list ['def abc', 'jkl ghi']."""


def reverse_word(words):
    return [' '.join(reversed(x.split())) for x in open(words)]


words = 'words.txt'
print(reverse_word(words))


"""Solution to chapter 7, exercise 28, beyond 3: reverse_words"""


def reverse_words(filename):
    return [' '.join(reversed(one_line.split()))
            for one_line in open(filename)]


print(reverse_words(words))
