"""In the previous exercise, we created a Scoop class that represents one scoop
of ice cream. If we’re really going to model the real world, though, we should
have another object into which we can put the scoops. I thus want you to create
a Bowl class, representing a bowl into which we can put our ice cream"""


class Scoop():

    def __init__(self, flavor):
        self.flavor = flavor


class Bowl:

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for scoop in new_scoops:
            self.scoops.append(scoop)

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)


"""Solution to chapter 9, exercise 39: bowl"""


class Bowl_bs():
    """Class representing a bowl of ice cream.

The "scoops" attribute is a list, containing scoops.
You can add one or more scoops with the "add_scoops" method.
"""

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        """Add one or more scoops to the bowl"""
        for one_scoop in new_scoops:
            self.scoops.append(one_scoop)

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)


s1 = Scoop('vanilla')
s2 = Scoop('mint')
s3 = Scoop('chocolate')


b1 = Bowl()
b1.add_scoops(s1)
b1.add_scoops(s2)
b1.add_scoops(s3)

print(b1)

