import shelve
import hashlib
from getpass import getpass


"""Create a dict in which the keys are usernames and the values are passwords,
both represented as strings. Create a tiny login system, in which the user must
enter a username and password. If there is a match, then indicate that the user
has successfully logged in. If not, then refuse them entry. (Note: This is a
nice little exercise, but please never store unencrypted passwords. It’s a
major security risk.)"""

def signup():

    while True:
        username = input('Name: ').lower().strip()
        if not username:
            break
        if username not in shelve.open('passwd', 'c'):
            print(f'Hello {username}')
            pass1 = getpass('Pass1: ')
            pass2 = getpass('Confirm your password: ')
            if pass1 == pass2:
                p1 = hashlib.sha224(str.encode(pass1)).hexdigest()
                print(p1)
                with shelve.open('passwd', 'c') as pw:
                    pw[username] = p1
            else:
                print("Passwords don't match, plese, try again.")
        else:
            print("Username already exists.")

def login():
    while True:
        username = input("Enter your username: ").strip()
        password = getpass("Enter your password: ").strip()

        p1 = hashlib.sha224(str.encode(password)).hexdigest()

        if shelve.open('passwd', 'r').get(username) == p1:
            return "Logged in."
        else:
            return "Incorrect username or password"

# signup()
print(login())



