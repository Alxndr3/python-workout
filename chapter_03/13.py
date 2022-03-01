from collections import Counter, defaultdict
from collections import namedtuple
import operator


WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']

FILENAME = "../stuff/passwd"

PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)
          ]

MOVIES = [('Parasite', 132, 'Bong Joon-ho'),
          ('Ford v Ferrari', 152, 'James Mangold'),
          ('The Irishman', 209, 'Martin Scorsese'),
          ('Jojo Rabbit', 108, 'Taika Waititi'),
          ('Joker', 122, 'Todd Phillips'),
          ('Little Women', 135, 'Greta Gerwig'),
          ('Marriage Story', 137, 'Noah Baumbach'),
          ('1917', 119, 'Sam Mendes'),
          ('Once Upon a Time in Hollywood', 161, 'Quentin Tarantino')
          ]


"""Write a function, most_repeating_word, that takes a sequence of strings
as input. The function should return the string that contains the greatest
number of repeated letters."""

def most_repeating_word(words):
    count = 0
    new_words = [('', 0)]
    for word in words:
        for l in word:
            for x in word:
                if l == x:
                    count += 1
            if count == new_words[0][1]:
                if (word, count) not in new_words:
                    new_words.append((word, count))
            if count > new_words[0][1]:
                new_words.clear()
                new_words.append((word, count))
            count = 0
    return [x[0] for x in new_words]


"""Write a function, most_repeating_word, that takes a sequence of strings
as input. The function should return the string that contains the greatest
number of repeated letters."""

def most_repeating_word_counter(words):
    l = sorted(list(map(lambda x: Counter(x).most_common(1)[0][1], words)),
        reverse=True)[0]
    return [word for word in words if Counter(word).most_common(1)[0][1] == l]


def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]


"""Write a function, most_repeating_word, that takes a sequence of strings
as input. The function should return the string that contains the greatest
number of repeated letters."""

def most_repeating_word_bs(words):
    return max(words, key=most_repeating_letter_count)


def most_repeating_vowels(words):
    """find the word with the greatest number of repeated vowels."""
    nl = []
    for word in words:
        l = Counter(word).most_common(1)
        if l[0][0] in 'aeiou':
            nl.append((word, l[0][1]))

    return sorted(nl, key=lambda x: x[1])[-1][0]


"""Solution to chapter 3, exercise 12, beyond 1: most_repeating_vowels"""

def most_repeating_vowel_count(word):
    vowels_in_word = ''
    for one_character in word.lower():
        if one_character in 'aeiou':
            vowels_in_word += one_character

    return Counter(vowels_in_word).most_common(1)[0][1]


def most_repeating_word(words):
    return max(words, key=most_repeating_vowel_count)


def popular_shels(filename):
    with open(filename, 'r') as pw:
            shells = [line.strip().split(':')[-1] for line in pw.readlines()]
    for shell in Counter(shells).most_common():
        print(shell[0])


"""Solution to chapter 3, exercise 12, beyond 2: shells_by_popularity"""

def shells_by_popularity(filename):
    shells = Counter(one_line.split(':')[-1].strip()
                     for one_line in open(filename)
                     if not one_line.startswith(('#', '\n')))

    return sorted(shells.items(),
                  key=operator.itemgetter(1), reverse=True)


def shells_x_users(filename):
    with open(filename, 'r') as pw:
        lines = pw.readlines()
    su = [(line.strip().split(':')[0], line.strip().split(':')[-1]) for line in lines] 
    return sorted(su, key=lambda x: x[0])


"""Solution to chapter 3, exercise 12, beyond 3: shells_and_users"""

def shells_and_users_by_popularity(filename):
    shells = defaultdict(list)
    for one_line in open(filename):
        if one_line.startswith(('#', '\n')):
            continue

        username, *rest, shell = one_line.strip().split(':')

        shells[shell].append(username)

    return sorted(shells.items(), key=len)


"""Solution to chapter 3, exercise 12, beyond 3: shells_and_users"""

from collections import defaultdict


def shells_and_users_by_popularity(filename):
    shells = defaultdict(list)
    for one_line in open(filename):
        if one_line.startswith(('#', '\n')):
            continue

        username, *rest, shell = one_line.strip().split(':')

        shells[shell].append(username)

    return sorted(shells.items(), key=len)


def format_sort_records(people):
    for person in sorted(people, key=lambda x: x[1]):
        print(f"{person[1]:<10}{person[0]:<10}{person[2]:>5.2f}")


def format_sort_records_bs(list_of_tuples):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    for person in sorted(list_of_tuples,
            key=operator.itemgetter(1, 0)):

        output.append(template.format(*person))
    return output

# print('\n'.join(format_sort_records_bs(PEOPLE)))


def format_sort_records_be(list_of_tuples):
    Schedule = namedtuple('Schedule', ['first_name', 'last_name', 'arriving_time'])
    nt = [Schedule(*x) for x in list_of_tuples]
    return [president for president in sorted(nt, key=lambda x: x.last_name)]


#sch = format_sort_records_be(PEOPLE)
#
#for s in sch:
#    print(f"{s.first_name:<10}{s.last_name:<10}{s.arriving_time:>5.2f}")


"""Solution to chapter 3, exercise 13, beyond 1: namedtuple_records"""

import operator
from collections import namedtuple

Person = namedtuple('Person', ['first', 'last', 'distance'])


def format_sort_records(list_of_tuples):
    output = []
    template = '{last:10} {first:10} {distance:5.2f}'
    for person in sorted(list_of_tuples, key=operator.attrgetter('last', 'first')):
        output.append(template.format(*(person._asdict())))
    return output


def tuple_to_named_tuple(list_tuple):
    nominated_movies = namedtuple('nominated_movies', ['title', 'len_time', 'director'])
    return [nominated_movies(*x) for x in list_tuple]


"""Define a list of tuples, in which each tuple contains the name, length (in
minutes), and director of the movies nominated for best picture Oscar awards
last year. Ask the cuserwhether they want to sort the list by title, length, or
director's name, and then present the list sorted by the user’s choice of
axis."""

def last_year_oscar(movies):
    print('Order by', end='\n\n')
    choice = int(input("1 - Title, 2 - Time length, 3 - Director "))
    match choice:
        case (1):
            return [x for x in sorted(movies, key=lambda x: x.title)]
        case (2):
            return [x for x in sorted(movies, key=lambda x: x.len_time)]
        case (3):
            return [x for x in sorted(movies, key=lambda x: x.director)]


"""Solution to chapter 3, exercise 13, beyond 2: sorted_movies"""

FIELDS = {'name': 0,
          'length': 1,
          'director': 2}


def sort_movies():
    sort_by = input("Enter sort field (name/length/director): ").strip()

    if sort_by in FIELDS:

        output = []
        template = '{0:30} {1:3} {2:20}'
        for one_movie in sorted(MOVIES, key=operator.itemgetter(FIELDS[sort_by])):
            output.append(template.format(*one_movie))
        return output

    print(f'No such field {sort_by}')


"""Extend this exercise by allowing the user to sort by two or three of these
fields, not just one of them. The user can specify the fields by entering them
separated by commas; you can use str.split to turn them into a list."""

def last_year_oscar_multiple_sort(movies):
    choice = ''
    ord_movies = []

    print("Choose the order to display the movies.")

    for x in range(1, 4):
        print(f"choice {x}")
        choice += (input("1 - Title, 2 - Time length, 3 - Director "))

    ch1 = int(choice[0]) - 1
    ch2 = int(choice[1]) - 1
    ch3 = int(choice[2]) - 1

    for movie in sorted(movies, key=operator.itemgetter(ch1, ch2, ch3)):
        ord_movies.append(movie)

    return(ord_movies)


"""Solution to chapter 3, exercise 13, beyond 3: sorted_movies_multifield"""

FIELDS = {'name': 0,
          'length': 1,
          'director': 2}


def sort_movies_multifield():
    """The user can enter more than one sort field, separated by whitespace"""

    sort_by = input("Enter sort fields (name/length/director): ").split()

    if all(field_name in FIELDS
           for field_name in sort_by):

        output = []
        template = '{0:30} {1:3} {2:20}'
        for one_movie in sorted(MOVIES, key=operator.itemgetter(*[FIELDS[field_name]
                                                                  for field_name in sort_by])):
            output.append(template.format(*one_movie))
        return output

    print(f'No such field {sort_by}')


movies = (tuple_to_named_tuple(MOVIES))
# print(last_year_oscar_multiple_sort(movies))
sort_movies_multifield()
