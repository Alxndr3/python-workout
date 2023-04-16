"""In this exercise, I want you to write a get_sv function that returns a set
of all “supervocalic” words in the dict. If you’ve never heard the term
supervocalic before, you’re not alone: I only learned about such words several
years ago. Simply put, such words contain all five vowels in English (a, e, i,
o, and u), each of them appearing once and in alphabetical order.

For the purposes of this exercise, I’ll loosen the definition, accepting any
word that has all five vowels, in any order and any number of times. Your
function should find all of the words that match this definition (i.e., contain
a, e, i, o, and u) and return a set containing them."""


def get_sv(ldict):
    return {word for word in open(ldict)
            if len(word) >= 5 and
            'a' in word and
            'e' in word and
            'i' in word and
            'o' in word and
            'u' in word}


def get_sv_set(ldict):
    return {word for word in open(ldict)
            if set('aeiou') < set(word)}


"""Solution to chapter 7, exercise 34: get_sv"""


def get_sv_bs(filename):
    """Given a filename (string) as input,
this function returns a set of all words
in which all five vowels can be found.
"""
    vowels = {'a', 'e', 'i', 'o', 'u'}

    return {word.strip()
            for word in open(filename)
            if vowels < set(word.lower())}


print(get_sv_set("./american-english"))


