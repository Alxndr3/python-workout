"""Let’s say that each class’s __repr__ method should print the animal’s
sound, as well as the standard string we implemented previously. In other
words, str(sheep) would be Baa--white sheep, 4 legs. How would you use
inheritance to maximize code reuse?"""


class Animal():
    """Base class for animals. Not meant to be instantiated."""

    def __init__(self, color):
        self.species = self.__class__.__name__
        self.color = color

    def __repr__(self):
        return f'{self.sound} -- {self.color} {self.species},'
    '{self.number_of_legs} legs'


class ZeroLeggedAnimal(Animal):

    number_of_legs = 4


class TwoLeggedAnimal(Animal):

    number_of_legs = 4


class FourLeggedAnimal(Animal):

    number_of_legs = 4


class Sheep(FourLeggedAnimal):
    """Class for creating 4-legged sheep of any color"""
    sound = 'Baa'


class Wolf(FourLeggedAnimal):
    """Class for creating 4-legged wolves of any color"""
    sound = 'Woooo'


class Snake(ZeroLeggedAnimal):
    """Class for creating 0-legged snakes of any color"""
    sound = 'Pssss'


class Parrot(TwoLeggedAnimal):
    """Class for creating 2-legged parrots of any color"""
    sound = 'Dá o pé loro'


"""Solution to chapter 9, exercise 43, beyond 3: animal_noises"""


class AnimalBS():
    """Base class for animals. Not meant to be instantiated."""

    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.sound}--{self.color} {self.species}, {self.number_of_legs} legs'


class WolfBS(Animal):
    """Class for creating 4-legged wolves of any color"""

    sound = 'awooo'

    def __init__(self, color):
        super().__init__(color, 4)


class SheepBS(Animal):
    """Class for creating 4-legged sheep of any color"""

    sound = 'baa'

    def __init__(self, color):
        super().__init__(color, 4)


class SnakeBS(Animal):
    """Class for creating 0-legged snakes of any color"""

    sound = 'hiss'

    def __init__(self, color):
        super().__init__(color, 0)


class ParrotBS(Animal):
    """Class for creating 2-legged parrots of any color"""

    sound = 'Polly wants a cracker!'

    def __init__(self, color):
        super().__init__(color, 2)


blue_sheep = Sheep('blue')
print(blue_sheep)
