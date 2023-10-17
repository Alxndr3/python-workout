"""Our zookeepers have a macabre sense of humor when it comes to placing
animals together, in that they put wolves and sheep in the first cage, and
snakes and birds in the other cage. (The good news is that with such a
configuration, the zoo will be able to save on food for half of the animals.)
Define a dict describing which animals can be with others. The keys in the dict
will be classes, and the values will be lists of classes that can compatibly be
housed with the keys. Then, when adding new animals to the current cage,
you’ll check for compatibility. Trying to add an animal to a cage that already
contains an incompatible animal will raise an exception."""


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


animal_safety = {Wolf: [Wolf, Snake, Parrot],
                 Sheep: [Sheep, Snake, Parrot],
                 Snake: [Wolf, Sheep],
                 Parrot: [Wolf, Sheep]}


class DangerousAssignmentError(Exception):
    pass


class Cage:

    limit = 6

    def __init__(self, cage_id=''):
        self.cage_id = cage_id
        self.animals = []

    def add_animals(self, *animals):
        for one_animal in animals:
            for one_current_resident in self.animals:
                if type(one_animal) not in animal_safety[type(one_current_resident)]:
                    raise DangerousAssignmentError(
                        f'You cannot put a {type(one_animal)} with a {type(one_current_resident)}!')
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
c1.add_animals(sheep, parrot)

c2 = BigCage(2)
c2.add_animals(wolf, sheep, parrot)

print(c1)
print(c2)
