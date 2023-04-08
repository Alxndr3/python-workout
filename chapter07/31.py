"""In this exercise, I want you to write a function that takes a filename as an
argument. It returns a string with the file’s contents, but with each word
translated into Pig Latin, as per our plword function in chapter 2 on
“strings.” The returned translation can ignore newlines and isn’t required
to handle capitalization and punctuation in any specific way."""


def pig_latin(filename):
    return ' '.join(f'{oneword}way' if oneword[0] in 'aeiou'
            else f'{oneword[1:]}{oneword[0]}way'
            for oneline in open(filename)
            for oneword in oneline.split())


"""Solution to chapter 7, exercise 31: plfile"""


def plword(word):
    """Takes a string as input. It should be a single
word.  Returns a string, the input word translated into
Pig Latin.
"""
    if word[0] in 'aeiou':
        return word + 'way'

    return word[1:] + word[0] + 'ay'


def plfile(filename):
    """Takes a filename as input. Returns a string
containing the file's contents, with each word
translated into Pig Latin.
"""
    return ' '.join(plword(one_word)
                    for one_line in open(filename)
                    for one_word in one_line.split())


print(pig_latin("./piglatin.txt"))
print(plfile("./piglatin.txt"))

