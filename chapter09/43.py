"""For the purposes of these exercises, you are the director of IT at a zoo.
The zoo contains several different kinds of animals, and for budget reasons,
some of those animals have to be housed alongside other animals.

We will represent the animals as Python objects, with each species defined as
a distinct class. All objects of a particular class will have the same
species and number of legs, but the color will vary from one instance to
another. We can thus create a white sheep:

s = Sheep('white')

I can similarly get information about the animal back from the object by
retrieving its attributes:

print(s.species)          ❶
print(s.color)            ❷
print(s.number_of_legs)   ❸

❶ Prints “sheep”

❷ Prints “white”

❸ Prints “4”

If I convert the animal to a string (using str or print), I’ll get back a
string combining all of these details:

print(s)    ❶

❶ Prints “White sheep, 4 legs”

We’re going to assume that our zoo contains four different types of animals:
sheep, wolves, snakes, and parrots. (The zoo is going through some budgetary
difficulties, so our animal collection is both small and unusual.) Create
classes for each of these types, such that we can print each of them and get a
report on their color, species, and number of legs."""


class Animal:

    def __init__(self, color=''):
        self.color = color

    def __repr__(self):
        return f'{self.color.title()} {self.specie}, {self.legs} leg'


class Sheep(Animal):

    def __init__(self, color=''):
        super().__init__(color)
        self.specie = "Sheep"
        self.legs = 4


class Wolves(Animal):

    def __init__(self, color):
        super().__init__(color)
        self.specie = "Wolf"
        self.legs = 4


class Snakes(Animal):

    def __init__(self, color):
        super().__init__(color)
        self.specie = "Snake"
        self.legs = 0


class Parrots(Animal):

    def __init__(self, color):
        super().__init__(color)
        self.specie = "Parrot"
        self.legs = 2


"""Solution to chapter 9, exercise 43: animals"""


class AnimalBS():
    """Base class for animals. Not meant to be instantiated."""

    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


class WolfBS(Animal):
    """Class for creating 4-legged wolves of any color"""

    def __init__(self, color):
        super().__init__(color, 4)


class SheepBS(Animal):
    """Class for creating 4-legged sheep of any color"""

    def __init__(self, color):
        super().__init__(color, 4)


class SnakeBS(Animal):
    """Class for creating 0-legged snakes of any color"""

    def __init__(self, color):
        super().__init__(color, 0)


class ParrotBS(Animal):
    """Class for creating 2-legged parrots of any color"""

    def __init__(self, color):
        super().__init__(color, 2)

s = Sheep('Yellow')
print(s)

