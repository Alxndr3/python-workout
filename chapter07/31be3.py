"""Assume that you have a list of dicts, in which each dict contains two
name-value pairs: name and hobbies, where name is the person’s name and
hobbies is a set of strings representing the person’s hobbies. What are the
three most popular hobbies among the people listed in the dicts?"""


def count_hobbies(hobbies):
    hobbies_count = {}
    for hobbie in hobbies:
        if hobbie not in hobbies_count:
            hobbies_count[hobbie] = 1
        else:
            hobbies_count[hobbie] += 1

    return sorted(hobbies_count.items(), key=lambda x: x[1], reverse=True)[:3]


def popular_hobbies(people_hobbies):
    return count_hobbies(set_hobbies
        for people in people_hobbies
        for set_hobbies in people['hobbies'])


"""Solution to chapter 7, exercise 31, beyond 3: most_popular_hobbies"""


import collections


def most_popular_hobbies(list_of_dicts):
    return collections.Counter([one_hobby
        for one_person in list_of_dicts
        for one_hobby in one_person['hobbies']]).most_common(3)


people_hobbies = [
    {"name": "Alice", "hobbies": {"reading", "hiking", "painting"}},
    {"name": "Bob", "hobbies": {"reading", "basketball", "cooking"}},
    {"name": "Charlie", "hobbies": {"photography", "traveling", "dancing"}},
    {"name": "David", "hobbies": {"playing guitar", "cooking", "yoga"}},
    {"name": "Emily", "hobbies": {"writing", "cooking", "skiing", "dancing"}}
]


print(popular_hobbies(people_hobbies))
