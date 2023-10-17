"""While the previous exercise might have delighted parents and upset
children, our job as ice cream vendors is to excite the children, as well as
take their parents’ money. Our company has thus started to offer a BigBowl
product, which can take up to five scoops.

Implement BigBowl for this exercise, such that the only difference between it
and the Bowl class we created earlier is that it can have five scoops, rather
than three. And yes, this means that you should use inheritance to achieve
this goal.

You can modify Scoop and Bowl if you must, but such changes should be minimal
and justifiable."""


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
            #if len(self.scoops) < self.max_scoops:
            if len(self.scoops) < self.__class__.max_scoops:
                self.scoops.append(one_scoop)

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)


class BigBowl(Bowl):

    max_scoops = 5


s1 = Scoop('vanilla')
s2 = Scoop('mint')
s3 = Scoop('chocolate')
s4 = Scoop('strawberry')
s5 = Scoop('caramel')
s6 = Scoop('mango')

b1 = Bowl()
b1.add_scoops(s1)
b1.add_scoops(s2)
b1.add_scoops(s3)
b1.add_scoops(s4)

print(b1, end='\n\n')

b2 = BigBowl()
b2.add_scoops(s1)
b2.add_scoops(s2)
b2.add_scoops(s3)
b2.add_scoops(s4)
b2.add_scoops(s5)
b2.add_scoops(s6)

print(b2)
