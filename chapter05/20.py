"""The challenge for this exercise is to write a wordcount function that mimics
the wc Unix command. The function will take a filename as input and will print
four lines of output:"""

def wordcount(filename):
    cchars = 0
    cwords = 0
    clines = 0
    uwords = set()

    with open(filename, 'r') as f:
        for x in f:
            clines += 1
            for y in x:
                cchars += 1

            for word in x.split():
                uwords.add(word)
                cwords += 1

        return cchars, cwords, clines, len(uwords)


print(wordcount("/etc/resolv.conf"))



"""Solution to chapter 5, exercise 20: wc"""


def wordcount_bs(filename):
    """Accepts a filename as an argument. Prints the number of lines,
characters, words (separated by whitespace) and different words
(case sensitive) in the file."""

    counts = {'characters': 0,
              'words': 0,
              'lines': 0}
    unique_words = set()

    for one_line in open(filename):
        counts['lines'] += 1
        counts['characters'] += len(one_line)
        counts['words'] += len(one_line.split())

        unique_words.update(one_line.split())

    counts['unique words'] = len(unique_words)
    for key, value in counts.items():
        print(f'{key}: {value}')


wordcount_bs("/etc/resolv.conf")
