"""In the United States, phone numbers have 10 digits--a three-digit area
code, followed by a seven-digit number. Several times during my childhood,
area codes would run out of phone numbers, forcing half of the population to
get a new area code. After such a split, XXX-YYY-ZZZZ might remain
XXX-YYY-ZZZZ, or it might become NNN-YYY-ZZZZ, with NNN being the new area
code. The decision regarding which numbers remained and which changed was often
made based on the phone numbers’ final seven digits. Use a list comprehension
to return a new list of strings, in which any phone number whose YYY begins
with the digits 0-5 will have its area code changed to XXX+1. For example,
given the list of strings ['123-456-7890', '123-333-4444', '123-777-8888'], we
want to convert them to ['124-456-7890', '124-333-4444', '124-777-8888']."""


def change_area_code(phones):
    return [f"124-{x.split('-')[1]}-{x.split('-')[2]}"
            for x in phones if x.split('-')[1][0]
            in '12345']


"""Solution to chapter 7, exercise 29, beyond 2: increment_area_code"""


def increment_area_code(full_phone_number):
    area_code, phone_number = full_phone_number.split('-', 1)

    if area_code[0] in '012345':
        area_code = str(int(area_code) + 1)

    return f'{area_code}-{phone_number}'


def increment_all_area_codes(area_codes):
    return [increment_area_code(one_phone_number)
            for one_phone_number in area_codes]


phones = ['123-456-7890', '123-333-4444', '123-777-8888']

print(change_area_code(phones))
