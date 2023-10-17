"""Instead of each animal class inheriting directly, from Animal, define
several new classes, ZeroLeggedAnimal, TwoLeggedAnimal, and FourLeggedAnimal,
all of which inherit from Animal, and dictate the number of legs on each
instance. Now modify Wolf, Sheep, Snake, and Parrot such that each class
inherits from one of these new classes, rather than directly from Animal. How
does this affect your method definitions?"""


class Animal():
    """Base class for animals. Not meant to be instantiated."""

    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


class ZeroLeggedAnimal(Animal):

    def __init__(self, color):
        super().__init__(color, 0)


class TwoLeggedAnimal(Animal):

    def __init__(self, color):
        super().__init__(color, 2)


class FourLeggedAnimal(Animal):

    def __init__(self, color):
        super().__init__(color, 4)


class Sheep(FourLeggedAnimal):
    """Class for creating 4-legged sheep of any color"""

    def __init__(self, color):
        super().__init__(color)


class Wolf(FourLeggedAnimal):
    """Class for creating 4-legged wolves of any color"""

    def __init__(self, color):
        super().__init__(color, 4)


class Snake(ZeroLeggedAnimal):
    """Class for creating 0-legged snakes of any color"""

    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(TwoLeggedAnimal):
    """Class for creating 2-legged parrots of any color"""

    def __init__(self, color):
        super().__init__(color, 2)


"""Solution to chapter 9, exercise 43, beyond 1: legged_animals"""


class AnimalBS():
    """Base class for animals. Not meant to be instantiated."""

    def __init__(self, color):
        self.species = self.__class__.__name__
        self.color = color

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


class TwoLeggedAnimalBS(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.number_of_legs = 2


class FourLeggedAnimalBS(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.number_of_legs = 4


class ZeroLeggedAnimalBS(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.number_of_legs = 0


class WolfBS(FourLeggedAnimal):
    """Class for creating 4-legged wolves of any color"""

    def __init__(self, color):
        super().__init__(color)


class SheepBS(FourLeggedAnimal):
    """Class for creating 4-legged sheep of any color"""

    def __init__(self, color):
        super().__init__(color)


class SnakeBS(ZeroLeggedAnimal):
    """Class for creating 0-legged snakes of any color"""

    def __init__(self, color):
        super().__init__(color)


class ParrotBS(TwoLeggedAnimal):
    """Class for creating 2-legged parrots of any color"""

    def __init__(self, color):
        super().__init__(color)


s = Sheep('Yellow')
print(s)
