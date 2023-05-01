"""Income tax in many countries is not a flat percentage, but rather the
combination of different “brackets.” So a country might not tax you on your
first $1,000 of income, and then 10% on the next $10,000, and then 20% on the
next $10,000, and then 50% on anything above that. Write a function that takes
someone’s income and returns the amount of tax they will have to pay, totaling
the percentages from various brackets."""


def income_tax(income=0):
    match income:
        case income if income < 1000:
            return f'Tax: {0.0:.2f}'
        case income if 1000 <= income < 10000:
            return f'Tax: {income * 0.1:.2f}'
        case income if 10000 <= income < 20000:
            return f'Tax: {income * 0.2:.2f}'
        case income if income >= 20000:
            return f'Tax: {income * 0.2:.2f}'


"""Solution to chapter 8, exercise 36, beyond 1: tax_brackets"""


brackets = [{'start': 0, 'end': 1000, 'tax': 0},
            {'start': 1000, 'end': 10000, 'tax': .1},
            {'start': 10000, 'end': 20000, 'tax': .2},
            {'start': 20000, 'end': 999999999999, 'tax': .5}]


def tax_brackets(amount, brackets):
    tax_owed = 0

    for one_bracket in brackets:
        if amount < one_bracket['start']:
            continue

        taxed_amount = min(amount, one_bracket['end'])
        taxed_amount -= one_bracket['start']

        tax_owed += taxed_amount * one_bracket['tax']

    return tax_owed


if __name__ == "__main__":
    print(income_tax())

