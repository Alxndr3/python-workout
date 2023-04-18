"""Many programs’ functionality is modified via configuration files, which are
often set using name-value pairs. That is, each line of the file contains text
in the form of name=value, where the = sign separates the name from the value.
I’ve prepared one such sample config file at http://mng.bz/rryD. Download this
file, and then use a dict comprehension to read its contents from disk, turning
it into a dict describing a user’s preferences. Note that all of the values
will be strings."""


def read_conf(conf):
    return {line.split('=')[0]: line.split('=')[1].strip()
            for line in open(conf)}


"""Solution to chapter 7, exercise 35a, beyond 1: read_config"""

# Yes, this is a duplicate of e32 b3!  Sorry!


def read_config(filename):
    return {one_line.split('=')[0]: one_line.split('=')[1].strip()
            for one_line in open(filename)}


print(read_conf('rryD'))
