from collections import defaultdict
from timeit import timeit


"""Ask the user to enter the name of a text file and then (on one line,
separated by spaces) words whose frequencies should be counted in that file.
Count how many times those words appear in a dict, using the user-entered words
as the keys and the counts as the values."""

def word_count_1():
    # filename = str(input("Filename_> "))
    # word_list = str(input("Words: "))
    # dcount = {}

    filename = "./new_file"
    word_list = "alexandre root"
    dcount = defaultdict(int)

    for word in word_list.split():
        dcount[word] = 0
        for line in open(filename):
            for x in line.strip().split(":"):
                if word == x:
                    dcount[word] += 1

    return dcount

def word_count_2():
    # filename = str(input("Filename_> "))
    # word_list = str(input("Words: "))
    # dcount = {}

    filename = "./new_file"
    word_list = "alexandre root"
    dcount = defaultdict(int)

    with open(filename, 'r') as f:
        ff = f.read().split()

        for x in ff:
            if x in word_list.split():
                dcount[x] += 1

    return dcount


"""Solution to chapter 5, exercise 20, beyond 1: count_certain_words"""

def count_certain_words():
    #s = input("Enter a filename, and then words you want to track: ").strip()
    s = "new_file alexandre root"

    if not s:
        return None

    filename, *words = s.split()

    counts = dict.fromkeys(words, 0)

    for one_line in open(filename):
        for one_word in one_line.split():

            if one_word in counts:
                counts[one_word] += 1

    return counts

print(timeit(word_count_1, number=100000))
print(timeit(word_count_2, number=10000))
print(timeit(count_certain_words, number=10000))

