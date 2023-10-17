"""Define a Person class, and a population class attribute that increases
each time you create a new instance of Person. Double-check that after
you’ve created five instances, named p1 through p5, Person.population
and p1.population are both equal to 5."""


class Person():

    population = 0

    def __init__(self):
        Person.population += 1


p1 = Person()
p2 = Person()
p3 = Person()
p4 = Person()
p5 = Person()

print(p1.population)
print(Person.population)
print(p5.population)
print(p5.population)

