"""If you’re going to be programming with objects, then you’ll be creating
classes--lots of classes. Each class should represent one type of object and
its behavior. You can think of a class as a factory for creating objects of
that type--so a Car class would create cars, also known as “car objects” or
“instances of Car.” Your beat-up sedan would be a car object, as would a
fancy new luxury SUV.

In this exercise, you’ll define a class, Scoop, that represents a single scoop
of ice cream. Each scoop should have a single attribute, flavor, a string that
you can initialize when you create the instance of Scoop.

Once your class is created, write a function (create_scoops) that creates three
instances of the Scoop class, each of which has a different flavor (figure
9.1). Put these three instances into a list called scoops (figure 9.2).
Finally, iterate over your scoops list, printing the flavor of each scoop of
ice cream you’ve created."""


class Scoop():

    def __init__(self, flavor):
        self.flavor = flavor


def create_scoops(flavors):
    scoops = [Scoop(flavor) for flavor in flavors]

    for scoop in scoops:
        print(scoop.flavor)


flavors = ['banana', 'orange', 'vanilla']

create_scoops(flavors)


"""Solution to chapter 9, exercise 38: scoop"""


class Scoop_bs():
    """Class representing a single scoop of ice cream.
The sole attribute is "flavor", a string.
"""

    def __init__(self, flavor):
        self.flavor = flavor


def create_scoops_bs():
    """Function that creates three scoops, puts them
in a list, and iterates over that list, printing the
flavors.
"""
    scoops = [Scoop('chocolate'),
              Scoop('vanilla'),
              Scoop('persimmon')]
    for scoop in scoops:
        print(scoop.flavor)
