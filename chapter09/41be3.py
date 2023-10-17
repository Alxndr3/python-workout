"""Define a Bread class representing a loaf of bread. We should be able to
invoke a get_nutrition method on the object, passing an integer
representing the number of slices we want to eat. In return, we’ll
receive a dict whose key-value pairs will represent calories,
carbohydrates, sodium, sugar, and fat, indicating the nutritional
statistics for that number of slices. Now implement two new classes that
inherit from Bread, namely WholeWheatBread and RyeBread. Each class
should implement the same get_nutrition method, but with different
nutritional information where appropriate."""


class Bread:

    nutrition = {'calories': 67, 'carbohydrates': 13, 'sodium': 370, 'sugar': 2,
            'fat': 13}

    def __init__(self):
        pass

    def get_nutrition(self, slices=0):

        return {k: slices * v for k, v in self.nutrition.items()}


class WholeWheatBread(Bread):

    nutrition = {'calories': 24, 'carbohydrates': 41, 'sodium': 400, 'sugar': 6,
            'fat': 3.4}


class RyeBread(Bread):

    nutrition = {'calories': 25, 'carbohydrates': 48, 'sodium': 603, 'sugar': 2,
            'fat': 3.3}


white_bread = Bread()
whole_bread = WholeWheatBread()
rye_bread = RyeBread()

print(white_bread.get_nutrition(3))
print(whole_bread.get_nutrition(3))
print(rye_bread.get_nutrition(3))


"""Solution to chapter 9, exercise 41, beyond 3: bread"""


class Bread:
    def __init__(self):
        # nutrition per slice
        self.calories = 66
        self.carbs = 12
        self.sodium = 170
        self.sugar = 1
        self.fat = 0.8

    def get_nutrition(self, number_of_slices):
        return {key: value*number_of_slices
                for key, value in vars(self).items()}


class WholeWheatBread(Bread):
    def __init__(self):
        self.calories = 67
        self.carbs = 12
        self.sodium = 138
        self.sugar = 1.4
        self.fat = 1


class RyeBread(Bread):
    def __init__(self):
        self.calories = 67
        self.carbs = 12
        self.sodium = 172
        self.sugar = 1
        self.fat = 0.8

