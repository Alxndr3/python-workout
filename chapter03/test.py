from operator import itemgetter
from collections import namedtuple
from pprint import pprint


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

def tuple_to_named_tuple(list_tuple):
    nominated_movies = namedtuple('nominated_movies', ['title', 'time', 'director'])
    return [nominated_movies(*x) for x in list_tuple]

def last_year_oscar_multiple_sort(movies):

    for movie in movies:
        print(sorted(movie, key=itemgetter(movie.title)))






movies = tuple_to_named_tuple(MOVIES)

print(last_year_oscar_multiple_sort(movies))

