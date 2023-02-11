from collections import defaultdict
import timeit


"""Read through a text file on disk. Use a dict to track how many words of each
length are in the file--that is, how many three-letter words, four-letter
words, five-letter words, and so on. Display your results."""


def word_track():
    text = "words.txt"
    word_store = defaultdict(int)

    with open(text) as tf:
        w = tf.read().split()

    for x in w:
        word_store[len(x)] += 1

    return word_store
    #for k, v in word_store.items():
    #    print(f"{k:>2} letter(s) word: {v}")


"""Solution to chapter 4, exercise 15, beyond 3: word lengths"""


def word_lengths():
    filename = "words.txt"
    output = defaultdict(int)

    for one_line in open(filename):
        for one_word in one_line.split():
            output[len(one_word)] += 1

    return output


print(timeit.timeit(word_track, number=1000))

print(timeit.timeit(word_lengths, number=1000))

