from pprint import pprint
from operator import itemgetter


PEOPLE = [{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
        {'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},
        {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'},
        {'first':'Alexandre', 'last':'Cardoso', 'email':'alxndr3@gmail.com'}]

NUMBERS = [-1, -4, 4, 2, 12, -3, -5, 12, -5, -8]

WORDS_LIST = ['hello', 'world', 'universe', 'earth', 'spectacular']

LISTA = [[5, 3, 4], [1, 2, 3], [3, 4, 5], [1, 1, 1]]

def alphabetize_names(people, order_by='last'):
    return sorted(people, key=lambda x: x[order_by])


def alphabetize_name_itemgetter(people, order_by='last'):
    return sorted(people, key=itemgetter(order_by))


def alphabetize_names_bs(list_of_dicts):
    return sorted(list_of_dicts, key=itemgetter('last', 'first'))


"""Given a sequence of positive and negative numbers, sort them by absolute
value.
"""


def sort_by_absolute(sequence):
    return sorted(sequence, key=abs)


"""Given a list of strings, sort them according to how many vowels they
contain.
"""


def sort_by_vowel_nubmer(words_list):

    def count_vowel(words_list):
        nv = 0
        nd = []
        for word in words_list:
            for v in word:
                if v in 'aeiou':
                    nv += 1
            nd.append((word, nv))
            nv = 0
        return nd
    nd = count_vowel(words_list)
    print(nd)
    return [x[0] for x in sorted(nd, key=lambda x: x[1])]



def by_vowel_count(one_word):
    total = 0
    for one_character in one_word.lower():
        if one_character in 'aeiou':
            total += 1
    return total


"""Given a list of strings (words), return a list of those words sorted by
the number of vowels they contain.
"""


def sort_by_vowel_count(words):
    return sorted(words, key=by_vowel_count)


"""Given a list of lists, with each list containing zero or more numbers,
sort by the sum of each inner list’s numbers.
"""


def sort_sum_inner_list(lista):
    new_lista = [(x, sum(x)) for x in lista]
    return [x[0] for x in sorted(new_lista, key=lambda x: x[1])]


"""Given a list of lists, in which the inner lists contain
numbers, return the outer list sorted by each inner list's sum.
"""


def sort_by_sum(list_of_lists):
    return sorted(list_of_lists, key=sum)


# pprint(sort_by_sum(LISTA))
# pprint(sort_sum_inner_list(LISTA))
# pprint(sort_by_vowel_nubmer(WORDS_LIST))
# pprint(sort_by_absolute(NUMBERS))
# pprint(alphabetize_names_bs(PEOPLE))
# pprint(alphabetize_name_itemgetter(PEOPLE, 'first'))
# pprint(alphabetize_names(PEOPLE, 'last'))

