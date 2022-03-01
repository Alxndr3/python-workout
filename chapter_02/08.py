def strsort(string):
    new_string = []
    for l in string:
        new_string.append(l)
    new_string.sort()
    return ''.join(new_string)


def strsort_bs(a_string):
    return ''.join(sorted(a_string))


def beyond_exercice_1(string):
    phrase = sorted(string.split())
    for word in phrase:
        if word == phrase[-1]:
            print(word)
        else:
            print(f"{word}, ", end='')


def last_word(text_file):
    with open(text_file, 'r') as string:
        return sorted(string.readline().split())[0]


def longest_word(text_file):
    with open(text_file, 'r') as string:
        new_string = string.readline().split()
    word_len = 0
    for word in new_string:
        if len(word) > word_len:
            word_len = len(word)
            return word


print(longest_word("./text_file"))
