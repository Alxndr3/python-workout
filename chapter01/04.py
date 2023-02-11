def hex_output(hex_num):
    """
    hex_output() converts hexadecimal number in decimal
    """


    value = 0
    new_num = list()

    for x in str(hex_num):
        if x in 'abcdef0123456789':
            new_num.append(x)
        else:
            print(f'{x[1]} will be skipped.')

    for x in enumerate(reversed(new_num)):
        x = list(x)
        if x[1].lower() == 'a':
            x[1] = 10
        elif x[1].lower() == 'b':
            x[1] = 11
        elif x[1].lower() == 'c':
            x[1] = 12
        elif x[1].lower() == 'd':
            x[1] = 13
        elif x[1].lower() == 'e':
            x[1] = 14
        elif x[1].lower() == 'f':
            x[1] = 15

        value += int(x[1]) * (16 ** int(x[0]))
    return value

# Book solution using int() function.
def hex_output_bs():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)


# Beyonde the exercise
def triangle_name():
    name = input("What's your name? ")
    name_list = list()
    for x in name:
        name_list.append(x)
        print()
        for x in name_list:
            print(x, end='')


triangle_name()
