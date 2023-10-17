""" That is, you can add as many scoops in each call  to Bowl.add_scoops as you
want, and you can call that method as many times as you want--but only the
first three scoops will actually be added. Any additional scoops will be
ignored."""


class Scoop():

    def __init__(self, flavor):
        self.flavor = flavor


class Bowl():

    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        """Add one or more scoops to the bowl"""
        for one_scoop in new_scoops:
            if len(self.scoops) < Bowl.max_scoops:
                self.scoops.append(one_scoop)

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)


s1 = Scoop('vanilla')
s2 = Scoop('mint')
s3 = Scoop('chocolate')
s4 = Scoop('strawberry')


b1 = Bowl()
b1.add_scoops(s1)
b1.add_scoops(s2)
b1.add_scoops(s3)
b1.add_scoops(s4)

print(b1)





class Bowl:

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for scoop in new_scoops:
            self.scoops.append(scoop)

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)


