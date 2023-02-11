"""Given a directory, read through each file and count the frequency of each
letter. (Force letters to be lowercase, and ignore nonletter characters.) Use a
dict to keep track of the letter frequencies. What are the five most common
letters across all of these files?"""

import os
import glob
from collections import defaultdict


def letter_frequency_1(dirname):
    dirname = "/home/alexandre/PythonWorkout"
    lcount = defaultdict(int)
    for filename in glob.glob(f"{dirname}/*"):
        if os.path.isfile(filename):
            for oneline in open(filename):
                for letter in oneline:
                    if letter.isalpha():
                        lcount[letter.lower()] += 1

    return lcount


def most_common_letters(lf):
    for x in range(5):
        print(sorted(lf.items(), key=lambda v:v[1], reverse=True)[x])



lf = letter_frequency_1("/home/alexandre/PythonWorkout")
# print(lf)
most_common_letters(lf)


"""Solution to chapter 5, exercise 20, beyond 3: most_common_letters"""

from collections import Counter
import glob


def most_common_letters_bs(dirname):
    counts = Counter()

    for one_filename in glob.glob(f'{dirname}/*'):
        try:
            for one_line in open(one_filename):
                counts.update(one_line)
        except:
            pass

    return list(dict(counts.most_common(5)).keys())

print(most_common_letters_bs("/home/alexandre/PythonWorkout/"))
