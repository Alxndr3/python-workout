"""Find a configuration file in which the lines look like “name=value.” Use a
dict comprehension to read from the file, turning each line into a key-value
pair."""


def file_to_dict(filename):
    return {line.split(':')[0]: line.split(':')[-1]
            for line in open(filename)}


"""Solution to chapter 7, exercise 32, beyond 3: read_config"""


def read_config(filename):
    return {one_line.split('=')[0]: one_line.split('=')[1].strip()
            for one_line in open(filename)}


filename = 'passwd'
print(file_to_dict(filename))
