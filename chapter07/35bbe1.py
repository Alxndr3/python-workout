"""Create a dict whose keys are city names, and whose values are temperatures
in Fahrenheit. Now use a dict comprehension to transform this dict into a new
one, keeping the old keys but turning the values into the temperature in
degrees Celsius."""


def fahrenheit_celcius(cities):
    return {key: round((value-32) * 5/9, 1)
            for key, value in cities.items()}


"""Solution to chapter 7, exercise 35b, beyond 1: temperature"""


def dict_f_to_c(dict_of_temps):
    return {key: (value-32)/1.8
            for key, value in dict_of_temps.items()}


print(fahrenheit_celcius({'curitiba': 75, 'sao paulo': 89}))
