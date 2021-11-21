def hex_output(hex_num):
    """
    hex_output() converts hexadecimal number in decimal
    """


    value = 0
    new_num = list()
#    new_num = list(x[1] if x[1] not in 'abcdef0123456789' else print(f'{x[1]} will be skipped.') for x in enumerate(hex_num))

    for x in enumerate(hex_num):
        if x[1] in 'abcdef0123456789':
            new_num.append(x[1])
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


print(hex_output('ic3g'))

