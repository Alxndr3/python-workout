"""Instead of writing an __init__ method in each subclass, we could also
have a class attribute, number_of_legs, in each subclass--similar to what
we did earlier with Bowl and BigBowl. Implement the hierarchy that way.
Do you even need an __init__ method in each subclass, or will
Animal.__init__ suffice?"""


class Animal():
    """Base class for animals. Not meant to be instantiated."""

    def __init__(self, color):
        self.species = self.__class__.__name__
        self.color = color

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


class ZeroLeggedAnimal(Animal):

    number_of_legs = 4


class TwoLeggedAnimal(Animal):

    number_of_legs = 4


class FourLeggedAnimal(Animal):

    number_of_legs = 4


class Sheep(FourLeggedAnimal):
    """Class for creating 4-legged sheep of any color"""
    pass


class Wolf(FourLeggedAnimal):
    """Class for creating 4-legged wolves of any color"""
    pass


class Snake(ZeroLeggedAnimal):
    """Class for creating 0-legged snakes of any color"""
    pass


class Parrot(TwoLeggedAnimal):
    """Class for creating 2-legged parrots of any color"""
    pass


"""Solution to chapter 9, exercise 43, beyond 2: class_legs"""


class AnimalBS():
    """Base class for animals. Not meant to be instantiated."""

    def __init__(self, color):
        self.species = self.__class__.__name__
        self.color = color

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


class WolfBS(Animal):
    """ClaBSBSBSss for creating 4-legged wolves of any color"""

    number_of_legs = 4

    def __init__(self, color):
        super().__init__(color)


class SheepBS(Animal):
    """Class for creating 4-legged sheep of any color"""

    number_of_legs = 4

    def __init__(self, color):
        super().__init__(color)


class SnakeBS(Animal):
    """Class for creating 0-legged snakes of any color"""

    number_of_legs = 0

    def __init__(self, color):
        super().__init__(color)


class ParrotBS(Animal):
    """Class for creating 2-legged parrots of any color"""

    number_of_legs = 2

    def __init__(self, color):
        super().__init__(color)


blue_sheep = Sheep('blue')
print(blue_sheep)
