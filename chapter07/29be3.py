"""Define a list of five dicts. Each dict will have two key-value pairs, name
and age, containing a person’s name and age (in years). Use a list
comprehension to produce a list of dicts in which each dict contains three
key-value pairs: the original name, the original age, and a third age_in_months
key, containing the person’s age in months. However, the output should exclude
any of the input dicts representing people over 20 years of age."""


def person_age_month(people):
    # new_person = []
    # for person in people:
    #     person['age_in_months'] = person['age'] * 12
    #     if person['age'] < 20:
    #         new_person.append(person)
    #
    # return new_person

    return [dict(person, age_in_months=person['age'] * 12)
            for person in people if person['age'] < 20]


"""Solution to chapter 7, exercise 29, beyond 3: age_in_months"""


def age_in_months(list_of_people):
    return [dict(**one_person, age_in_months=one_person['age'] * 12)
            for one_person in list_of_people
            if one_person['age'] <= 20]


people = [{'name': 'bob', 'age': 10},
    {'name': 'debora', 'age': 39},
    {'name': 'rafael', 'age': 41},
    {'name': 'suzane', 'age': 25},
    {'name': 'michel', 'age': 44}]

print(person_age_month(people))

print(age_in_months(people))
