class Cage:

    limit = 3

    def __init__(self, cage_id=''):
        self.cage_id = cage_id
        self.animals = []

    def add_animals(self, *animals):
        for one_animal in animals:
            if len(self.animals) < self.__class__.limit:
                self.animals.append(one_animal)

    def __repr__(self):
        output = f'Cage {self.cage_id}\n'
        output += '\n'.join('\t' + str(animal)
                            for animal in self.animals)
        return output


class BigCage(Cage):

    limit = 5


c1 = Cage(1)
c1.add_animals('wolf', 'sheep', 'elefant', 'monkey', 'tiger', 'horse')

c2 = BigCage(2)
c2.add_animals('wolf', 'sheep', 'elefant', 'monkey', 'tiger', 'horse')

print(c1)
print(c2)

