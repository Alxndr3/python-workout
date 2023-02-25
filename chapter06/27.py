"""You’ll thus call the function create_password _generator with a string.
That string will return a function, which itself takes an integer argument.
Calling this function will return a password of the specified length, using the
string from which it was created"""


from random import choice


def create_password_generator(pwd):
    def password_generator(lenght):
        a = ''
        for x in range(lenght):
            a += choice(pwd)
        return a
    return password_generator


new_pass = create_password_generator('##%%helloworld')

print(new_pass(5))


"""Solution to chapter 6, exercise 27: makepw"""

import random


def create_password_generator(characters):
    """This function takes a string as input.

It returns a function that, when invoked with an
integer argument, returns a string containing
a random selection from "characters", of length
"length".
"""
    def create_password(length):
        output = []

        for i in range(length):
            output.append(random.choice(characters))
        return ''.join(output)
    return create_password

