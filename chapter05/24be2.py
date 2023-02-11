"""Given an existing text file, create two new text files. The new files will
each contain the same number of lines as the input file. In one output file,
you’ll write all of the vowels (a, e, i, o, and u) from the input file. In the
other, you’ll write all of the consonants. (You can ignore punctuation and
whitespace.)"""


def write_vowel_consonants(filename, v_filename, c_filename):
    """Hello """
    with open(filename, 'r') as f, open(v_filename, 'a') as v, open(c_filename, 'a') as c:
        for x in f.readlines():
            for y in x.strip():
                if y.lower() in 'aeioy':
                    v.write(y)
                else:
                    c.write(y)
            v.write('\n')
            c.write('\n')


write_vowel_consonants("./files/passwd", "./files/vowels",
        "./files/consonants")


"""Solution to chapter 5, exercise 24, beyond 2: vowels_and_consonants"""

import string


def vowels_and_consonants(infilename, vowel_filename, consonant_filename):
    with open(infilename) as infile, open(vowel_filename, 'w') as vowel_out, open(consonant_filename, 'w') as consonant_out:
        for one_line in infile:
            for one_character in one_line:
                if one_character.lower() in 'aeiou':
                    vowel_out.write(one_character)
                elif one_character.lower() in string.ascii_lowercase:
                    consonant_out.write(one_character)

