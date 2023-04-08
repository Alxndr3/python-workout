from string import punctuation


def pig_latin():
    word = input("Type a word to be translated to latin pig: ")

    if word[0] in 'aeiou':
        if word[-1] in punctuation:
            return f"{word[:-1]}way{word[-1]}".capitalize()
        return f"{word}way".capitalize()

    else:
        if word[-1] in punctuation:
            return f"{word[:-1]}way{word[-1]}".capitalize()
        return  f"{word[1:]}{word[0]}ay".capitalize


def pig_latin_different_vowels():
    word_set = set()
    word = input("Type a word to be translated to latin pig: ")

    for l in word:
        if l in 'aeiou':
            word_set.add(l)
    if len(word_set) > 1:
        return f"{word}way"
    return f"{word[1:]}{word[0]}ay"


def pig_latin_bs(word):
    if word[0] in 'aeiou':
        return f'{word}way'

    return f'{word[1:]}{word[0]}ay'


#print(pig_latin_different_vowels())
print(pig_latin_bs(input('word: ')))
