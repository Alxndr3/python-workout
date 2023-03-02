"""Given a list of strings containing hexadecimal numbers, sum the numbers
together."""


def sum_hex(hexadecimals):
    return hex(sum(int(x, 16) for x in hexadecimals))


print(sum_hex(['a', 'b', 'c']))


"""Solution to chapter 7, exercise 28, beyond 2: sum_hexes"""


def sum_hexes(hex_numbers):
    return sum(int(one_number, 16)
               for one_number in hex_numbers)


print(sum_hexes(['a', 'b', 'c']))

