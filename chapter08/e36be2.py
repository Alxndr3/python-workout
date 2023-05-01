"""Write a module providing a function that, given a string, returns a dict
indicating how many characters provide a True result to each of the following
functions: str.isdigit, str.isalpha, and str.isspace. The keys should be
isdigit, isalpha, and isspace."""


def character_type(string):

    char = {'isdigit': 0, 'isalpha': 0, 'isspace': 0}

    for x in string:
        if x.isdigit():
            char['isdigit'] += 1
        elif x.isalpha():
            char['isalpha'] += 1
        elif x.isspace():
            char['isspace'] += 1

    return char


"""Solution to chapter 8, exercise 36, beyond 2: analyze_string"""


def analyze_string(s):
    output = {
            'isdigit': 0,
            'isalpha': 0,
            'isspace': 0}

    for one_character in s:
        for methodname in output:
            if getattr(one_character, methodname)():  # a sneaky, cool trick!
                output[methodname] += 1

    return output


string = 'Hello, World! 2'

if __name__ == '__main__':
    print(character_type(string))
