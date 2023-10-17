"""It’s not very realistic to say that we would limit the number of animals in
a cage. Rather, it makes more sense to describe how much space each animal
needs and to ensure that the total amount of space needed per animal isn’t
greater than the space in each cage. You should thus modify each of the Animal
subclasses to include a space_required attribute. Then modify the Cage and
BigCage classes to reflect how much space each one has. Adding more animals
than the cage can contain should raise an exception."""


class Animal():
    """Base class for animals. Not meant to be instantiated."""

    def __init__(self, color, cage_size):
        self.species = self.__class__.__name__
        self.color = color
        self.cage_size = cage_size

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


class Cage:

    limit = 6

    def __init__(self, cage_id=''):
        self.cage_id = cage_id
        self.animals = []

    def add_animals(self, *animals):
        cage = 0
        for one_animal in animals:
            cage += one_animal.cage_size
            if cage <= self.__class__.limit:
                self.animals.append(one_animal)

    def __repr__(self):
        output = f'Cage {self.cage_id}\n'
        output += '\n'.join('\t' + str(animal)
                            for animal in self.animals)
        return output


class BigCage(Cage):

    limit = 8


sheep = Sheep('blue', 2)
wolf = Wolf('black', 4)
parrot = Parrot('blue', 2)

c1 = Cage(1)
c1.add_animals(sheep, wolf)

c2 = BigCage(2)
c2.add_animals(wolf, sheep, parrot)

print(c1)
print(c2)

