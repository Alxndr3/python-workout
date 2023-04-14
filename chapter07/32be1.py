"""Given a string containing several (space-separated) words, create a dict in
which the keys are the words, and the values are the number of vowels in each
word. If the string is “this is an easy test,” then the resulting dict would
be {'this':1, 'is':1, 'an':1, 'easy':2, 'test':1}."""


from collections import Counter


def string_vowel(string):
    return Counter(
            word for word in string.split()
            for letter in word
            if letter in 'aeiou')


"""Solution to chapter 7, exercise 32, beyond 1: word_vowels"""


def vowel_count(word):
    total = 0
    for one_letter in word.lower():
        if one_letter in 'aeiou':
            total += 1
    return total


def word_vowels(s):
    return {one_word: vowel_count(one_word)
            for one_word in s.split()}


string = "hello there beautifull world"
print(string_vowel(string))
