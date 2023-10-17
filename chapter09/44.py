"""Now that we’ve created some animals, it’s time to put them into cages. For
this exercise, create a Cage class, into which you can put one or more animals,
as follows:

c1 = Cage(1)
c1.add_animals(wolf, sheep)

c2 = Cage(2)
c2.add_animals(snake, parrot)

When you create a new Cage, you’ll give it a unique ID number. (The uniqueness
doesn’t need to be enforced, but it’ll help us to distinguish among the
cages.) You’ll then be able to invoke add_animals on the new cage, passing any
number of animals that will be put in the cage. I also want you to define a
__repr__ method so that printing a cage prints not just the cage ID, but also
each of the animals it contains."""


from collections import defaultdict


class Cage:
    """Put animals into a cage"""
    cage = {}

    def __init__(self, cage_id=''):
        self.cage_id = cage_id
        self.animals = []

    def add_animals(self, *args):
        for animal in args:
            self.animals.append(animal)
        self.cage[self.cage_id] = self.animals

    def __repr__(self):
        return f'{self.cage}'


"""Solution to chapter 9, exercise 44: cages"""


class CageBS():
    """Class for creating cages in which to put cute, furry animals."""

    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []

    def add_animals(self, *animals):
        """Add one or more animals to a cage.  Returns None."""
        for one_animal in animals:
            self.animals.append(one_animal)

    def __repr__(self):
        output = f'Cage {self.id_number}\n'
        output += '\n'.join('\t' + str(animal)
                            for animal in self.animals)
        return output


c1 = CageBS(1)
c1.add_animals('wolf', 'sheep')

print(c1)

