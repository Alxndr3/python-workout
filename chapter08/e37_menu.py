def menu(**kwargs):
    choice = input("Choose as function: ")
    while choice not in kwargs.keys():
        print("try again")
        choice = input("Choose as function: ")

    return kwargs[choice]()


def func1():
    return 'A'


def func2():
    return 'B'


"""Solution to chapter 8, exercise 37: menu"""


def menu_bs(**options):
    """Function that takes keyword arguments. The value
associated with each key is a function taking zero arguments.
The user is asked to enter input.
If the input matches a keyword, then the associated function
is invoked, and its return value is returned to the user.
If the input doesn't match a keywork, the user is asked to
try again.
"""
    while True:
        option_string = '/'.join(sorted(options))
        choice = input(f'Enter an option ({option_string}): ')
        if choice in options:
            return options[choice]()

        print('Not a valid option')


print(menu(a=func1, b=func2))
