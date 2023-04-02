"""Redo this exercise, but replace each grandchild’s name (currently a string)
with a dict. Each dict will contain two name-value pairs, name and age. Produce
a list of the grandchildren’s names, sorted by age, from eldest to
youngest."""


def granchildrens_age(granchildren):
    return sorted([child for child in granchildren.values()], key=lambda x:
            x['age'], reverse=True)



"""Solution to chapter 7, exercise 29, beyond 3: sorted_grandchildren"""


import operator


def sorted_grandchildren(d):
    grandchildren = [one_grandchild
                     for one_grandchild_list in d.values()
                     for one_grandchild in one_grandchild_list]

    return [one_grandchild['name']
            for one_grandchild in sorted(grandchildren,
                                         key=operator.itemgetter('age'))]


children_gchildren = {
        'alex': {'name': 'rafael', 'age': 10},
        'eli': {'name': 'felipe', 'age': 13},
        'rick': {'name': 'lucas', 'age': 12}}

print(granchildrens_age(children_gchildren))

# print(sorted_grandchildren(children_gchildren))
