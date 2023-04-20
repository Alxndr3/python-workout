"""
·gematria_for, which takes a single word (string) as an argument and
returns the gematria score for that word
·gematria_equal_words, which takes a single word and returns a list of those
dict words whose gematria scores match the current word’s score.
"""


from string import ascii_lowercase


def gematria_for(word):
    gemat_dict = {item[1]: item[0] for item in enumerate(ascii_lowercase, 1)}

    return sum(gemat_dict[letter.lower().strip()] for letter in word)


def gematria_equal_word(word, filename):
    return {word: [line.strip()
            for line in open(filename)
            if set(line.strip()) < set(ascii_lowercase)
            if gematria_for(word) == gematria_for(line.strip())]}


"""Solution to chapter 7, exercise 35b: gematria_equal_words"""

from e35a_gematria_1 import gematria_dict

GEMATRIA = gematria_dict()


def gematria_for(word):
    """Function that calculates the gematria
for a given word, an argument passed as a string.
"""
    return sum(GEMATRIA.get(one_char, 0)
               for one_char in word)


def gematria_equal_words(input_word):
    """Function that takes a string (word) as input,
and returns a list of strings (words) whose calculated
gematria is identical.
"""
    our_score = gematria_for(input_word.lower())
    return [one_word.strip()
            for one_word in open('/usr/share/dict/words')
            if gematria_for(one_word.lower()) == our_score]


print(gematria_equal_word('hello', 'american-english'))
