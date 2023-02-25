""" Now that you’ve written a function to create passwords, write
create_password_checker, which checks that a given password meets the IT
staff’s acceptability criteria. In other words, create a function with
four parameters: min_uppercase, min_lowercase, min_punctuation, and
min_digits. These represent the minimum number of uppercase letters,
lowercase letters, punctuations, and digits for an acceptable password.
The output from create_password_checker is a function that takes a
potential password (string) as its input and returns a Boolean value
indicating whether the string is an acceptable password."""


import string


def create_passwork_checker(min_uppercase, min_lowercase, min_puctuation,
        min_digits, min_lenght):

    def passwork_checker(password):
        uppercase = 0
        lowercase = 0
        punctuation = 0
        digits = 0

        for x in password:
            if x.isalpha() and x.upper():
                uppercase += 1
            if x.isalpha() and x.lower():
                lowercase += 1
            if x in string.punctuation:
                punctuation += 1
            if x.isdigit():
                digits += 1

        if uppercase < min_uppercase or lowercase < min_lowercase or punctuation < min_puctuation or digits < min_digits or len(password) < min_lenght:
            return False
        else:
            return True

    return passwork_checker

password = 'Hello,World1'
min_uppercase = 1
min_lowercase = 1
min_puctuation = 1
min_digits = 1
min_lenght = 8


p = create_passwork_checker(min_uppercase, min_lowercase, min_puctuation, min_digits, min_lenght)

p(password)


"""Solution to chapter 6, exercise 27, beyond 1: password_checker"""

import string


def create_password_checker(min_uppercase, min_lowercase, min_punctuation, min_digits):
    uppercase_set = set(string.ascii_uppercase)
    lowercase_set = set(string.ascii_lowercase)
    punctuation_set = set(string.punctuation)
    digits_set = set(string.digits)

    def check_password(password):

        if len([one_character
                for one_character in password
                if one_character in uppercase_set]) < min_uppercase:
            print(f'Not enough uppercase letters; min is {min_uppercase}')
            return False
        elif len([one_character
                  for one_character in password
                  if one_character in lowercase_set]) < min_lowercase:
            print(f'Not enough lowercase letters; min is {min_lowercase}')
            return False
        elif len([one_character
                  for one_character in password
                  if one_character in punctuation_set]) < min_punctuation:
            print(f'Not enough punctuation; min is {min_punctuation}')
            return False
        elif len([one_character
                  for one_character in password
                  if one_character in digits_set]) < min_digits:
            print(f'Not enough digits; min is {min_digits}')
            return False
        else:
            return True
    return check_password
