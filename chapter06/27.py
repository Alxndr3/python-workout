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


