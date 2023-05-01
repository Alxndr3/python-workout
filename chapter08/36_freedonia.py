RATES = {
        "Chico": 0.5,
        "Groucho": 0.7,
        "Harpo": 0.5,
        "Zeppo": 0.4}


def time_percentage(hour):
    """This function takes an integer from 0-24 and returns
the percentage of the day, as a float, that has passed at that hour.
"""
    return hour / 24


def calculate_tax(amount, state, hour):
    """This function returns the tax due in Freedonia based on the
original amount, the state, and the hour at which the purchase was
made. It returns the total amount, including the tax, that is due,
as a float.
"""
    return amount + (amount * RATES[state] * time_percentage(hour))


if __name__ == "__main__":
    calculate_tax(0, 'chico', 2)
