def ubbi_dubbi(word):
    for letter in word:
        if letter in 'aeiouy':
            print(f'ub{letter}', end='')
        else:
            print(letter, end='')


def ubbi_dubbi_bs(word):
    output = []
    for letter in word:
        if letter in 'aeiou':
            output.append(f"ub{letter}")
        else:
            output.append(letter)
    return ''.join(output)


def ubbi_dubbi_cap(word):
    output = []
    if word[0] == word[0].upper():
       output.append(f"Ub{word[0].lower()}")
    else:
       output.append(f"ub{word[0]}")
    for letter in word[1:]:
       if letter in 'aeiouy':
           output.append(f"ub{letter}")
       else:
           output.append(letter)
    return ''.join(output)


def remove_author_names(authors, article):
    """
    authors receives a list() of authors.
    article receives a string
    """
    new_article = []
    for word in article.split():
        if not word[-1].isalnum():
            word = word[:-1]
        if word in authors:
            new_article.append('_')
        else:
            new_article.append(word)
    return ' '.join(new_article)


def url_encode_characters(string):
    new_string = []
    for l in string:
        if l.isalnum() or l in '/.':
            new_string.append(l)
        else:
            new_string.append(f"%{ord(l)}")
    return ''.join(new_string)

if '__main__' == __name__:
    authors = ['Alex', 'Rafael', 'Debora']
    article = 'Hello, World. This article belongs to Alex, Debora and Rafael.'
    print(remove_author_names(authors, article))

