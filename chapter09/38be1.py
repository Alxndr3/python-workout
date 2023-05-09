"""Write a Beverage class whose instances will represent beverages. Each
beverage should have two attributes: a name (describing the beverage) and a
temperature. Create several beverages and check that their names and
temperatures are all handled correctly."""


class Beverage:

    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature


coffee = Beverage('coffee', 75)
print(coffee.name, coffee.temperature)

coffee.temperature = 80
print(coffee.name, coffee.temperature)

beer = Beverage('beer', 0)
print(beer.name, beer.temperature)
