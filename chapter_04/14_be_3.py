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
