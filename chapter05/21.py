"""In this exercise, write two functions. find_longest_word takes a filename as
an argument and returns the longest word found in the file. The second
function, find_all_longest_words, takes a directory name and returns a dict in
which the keys are filenames and the values are the longest words from each
file."""


from glob import glob
import os


def find_longest_word(filename):
    w = []
    for wlist in open(filename):
        for lword in wlist.split():
            if len(w) == 0 or len(lword) == len(w[-1]):
                w.append(lword)
            elif len(lword) > len(w[-1]):
                w.clear()
                w.append(lword)

    return(set(w))


def find_all_longest_words(dirname):
    return {os.path.relpath(x, dirname): find_longest_word(x) for x in
        glob(f"{dirname}/*")}

print(find_all_longest_words("/home/alexandre/PythonWorkout/chapter_05/files"))


def find_longest_word_bs(filename):
    longest_word = ''
    for one_line in open(filename):
        for one_word in one_line.split():
            if len(one_word) > len(longest_word):
                longest_word = one_word
    return longest_word


def find_all_longest_words_bs(dirname):
    return {filename: find_longest_word_bs(os.path.join(dirname, filename))
            for filename in os.listdir(dirname)
            if os.path.isfile(os.path.join(dirname, filename))}


print(find_all_longest_words_bs("/home/alexandre/PythonWorkout/chapter_05/files"))

