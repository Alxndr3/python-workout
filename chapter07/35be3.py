"""It’s sometimes useful to transform data from one format into another.
Download a JSON-formatted list of the 1,000 largest cities in the United States
from http://mng.bz/Vgd0. Using a dict comprehension, turn it into a dict in
which the keys are the city names, and the values are the populations of those
cities. Why are there only 925 key-value pairs in this dict? Now create a new
dict, but set each key to be a tuple containing the state and city. Does that
ensure there will be 1,000 key-value pairs?"""


import json


def largest_cities(filename):
    return {(city['city'], city['state']): city['population']
            for city in json.load(open(filename))}


"""Solution to chapter 7, exercise 35a, beyond 3: cities"""


def get_city_data(filename):
    return {one_city['city']: one_city['population']
            for one_city in json.load(open(filename))
            }


def get_city_data2(filename):
    return {(one_city['city'], one_city['state']): one_city['population']
            for one_city in json.load(open(filename))
            }


print(largest_cities('Vgd0'))
