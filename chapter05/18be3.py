"""Read through a text file, line by line. Use a dict to keep track of how many
times each vowel (a, e, i, o, and u) appears in the file. Print the resulting
tabulation. """

def track_vowels(filename):
    vowels_dict = {}

    for line in open(filename):
        for v in line:
            if v in 'aeiou':
                if v not in vowels_dict:
                    vowels_dict[v] = 1
                else:
                    vowels_dict[v] += 1

    for k, v in vowels_dict.items():
        print(k, v)


"""Solution to chapter 5, exercise 18, beyond 3: count_vowels"""

def count_vowels(filename):
    output = dict.fromkeys('aeiou', 0)

    for one_line in open(filename):
        for one_character in one_line.lower():
            if one_character in output:
                output[one_character] += 1

    return output


track_vowels('/etc/passwd')

