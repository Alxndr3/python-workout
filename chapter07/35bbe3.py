"""Create a dict whose keys are currency names and whose values are the price
of that currency in U.S. dollars. Write a function that asks the user what
currency they use, then returns the dict from the previous exercise as before,
but with its prices converted into the requested currency."""


def u_currency(currency):
    user_currency = input('what\'s your currency? ')
    return {key: currency[user_currency] * value
            for key, value in currency.items()
            if user_currency != key}


currency = {
        'dollar': 1.0,
        'euro': 0.8,
        'real': 5.3,
        'yen': 134.81,
        'pound': 0.8}


"""Solution to chapter 7, exercise 35b, beyond 3: currency_conversion"""


def currency_conversion(books, new_currency):
    return {title: {'first': name.split()[0],
                    'last': name.split()[1],
                    'price': price * conversions[new_currency]}
            for name, title, price in books}

print(u_currency(currency))
