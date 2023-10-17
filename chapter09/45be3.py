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

    number_of_legs = 2


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


class Zoo():

    def __init__(self):
        self.cages = []

    def add_cages(self, *cages):
        for one_cage in cages:
            self.cages.append(one_cage)

    def __repr__(self):
        output = '\n'.join(str(cage) for cage in self.cages)
        return output

    def get_animals(self, **kwargs):

        if not kwargs['color'] or not kwargs['number_of_legs']:
            raise NoColorsPassedError

        animal = []

        for one_cage in self.cages:
            for one_animal in one_cage.animals:
                if one_animal.color == kwargs['color'] and \
                        one_animal.number_of_legs == kwargs['number_of_legs']:
                    animal.append(one_animal)

        return animal

    def number_of_legs(self):
        return sum(one_animal.number_of_legs
                   for one_cage in self.cages
                   for one_animal in one_cage.animals)

    def transfer_animal(self, animal, targe_zoo=None):
        for one_cage in self.cages:
            for one_animal in one_cage.animals:
                if one_animal == animal:
                    one_cage.animals.remove(animal)

        for one_cage in targe_zoo.cages:
            try:
                one_cage.add_animals(animal)
            except:
                pass

    def transfer_animal_bs(self, target_zoo, species):
        for one_cage in self.cages:
            for one_animal in one_cage.animals:
                if isinstance(one_animal, species):
                    one_cage.remove(one_animal)
                    target_zoo.cages[0].add_animals(one_animal)


parrot = Parrot('blue', 2)
sheep = Sheep('blue', 2)
snake = Snake('green', 1)
wolf = Wolf('black', 4)

c1 = Cage(1)
c1.add_animals(sheep, parrot)

c2 = BigCage(2)
c2.add_animals(wolf, parrot)

c3 = Cage(3)
c3.add_animals(snake)

z1 = Zoo()
z1.add_cages(c1, c2, c3)

print(z1.get_animals(color='blue', number_of_legs=4))


