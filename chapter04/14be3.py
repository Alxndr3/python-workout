from datetime import date


"""Define a dict whose keys are names of people in your family, and whose
values are their birth dates, as represented by Python date objects
(http://mng.bz/ jggr). Ask the user to enter the name of someone in your
family, and have the program calculate how many days old that person is."""

birthday = {
        'alexandre': date(1982, 8, 6),
        'debora': date(1983, 9, 11),
        'rafa': date(2012, 4, 16)
        }

def days_old():
    name = input("Name: ")
    if name not in birthday:
        print("I don't know.")
    else:
        days = date.today() - birthday[name]
        print(f"{name.title()} is {days.days} days old.")


days_old()


"""Solution to chapter 4, exercise 14: beyond 3: days_old"""


from datetime import date


PEOPLE = {'Reuven': date.fromisoformat('1970-07-14'),
          'Atara': date.fromisoformat('2000-12-16'),
          'Shikma': date.fromisoformat('2002-12-17'),
          'Amotz': date.fromisoformat('2005-10-31')
          }


def calculate_days():
    while True:
        name = input("Enter a person's name: ").strip()

        if not name:
            break

        today = date.today()

        if name in PEOPLE:
            print(f'{name} is {(today - PEOPLE[name]).days}')
        else:
            print(f'{name} is not in the system.')

# calculate_days()
