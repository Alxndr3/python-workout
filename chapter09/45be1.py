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


class Zoo():

    def __init__(self):
        self.cages = []

    def add_cages(self, *cages):
        for one_cage in cages:
            self.cages.append(one_cage)

    def __repr__(self):
        output = '\n'.join(str(cage) for cage in self.cages)
        return output

    def animals_by_color(self, *color):
        if not color:
            raise NoColorsPassedError

        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.color in color]

    def animals_by_legs(self, number_of_legs):
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.number_of_legs ==
                        number_of_legs]

    def number_of_legs(self):
        return sum(one_animal.number_of_legs
                   for one_cage in self.cages
                   for one_animal in one_cage.animals)


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

z = Zoo()
z.add_cages(c1, c2, c3)

# print(z)
print(z.animals_by_color())
# print(z.animals_by_legs(4))
# print(z.number_of_legs())
