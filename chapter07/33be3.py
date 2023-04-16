"""Write a function that takes a directory name (i.e., a string) as an
argument. The function should return a dict in which the keys are the names of
files in that directory, and the values are the file sizes. You can use
os.listdir or glob .glob to get the files, but because only regular files have
sizes, you’ll want to filter the results using methods from os.path. To
determine the file size, you can use os.stat or (if you prefer) just check the
length of the string resulting from reading the file."""


import os
from pathlib import Path


def file_sizes(dirname):
    return {file: os.stat(file)[6]
            for file in os.listdir()
            if os.path.isfile(file)}


def file_sizes_pl(directory):
    return {file.name: file.stat()[6]
            for file in Path(directory).iterdir()
            if file.is_file()}


"""Solution to chapter 7, exercise 32, beyond 3: file_info"""


def vowel_count(word):
    total = 0
    for one_letter in word.lower():
        if one_letter in 'aeiou':
            total += 1
    return total


def word_vowels(s):
    return {one_word: vowel_count(one_word)
            for one_word in s.split()}


print(file_sizes('./'))
print(file_sizes_pl('./'))
