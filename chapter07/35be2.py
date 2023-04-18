"""Create a dict based on the config file, as in the previous exercise, but
this time, all of the values should be integers. This means that you’ll need
to filter out (and ignore) those values that can’t be turned into integers."""


def read_conf(conf):
    return {line.split('=')[0]: line.split('=')[1].strip()
            for line in open(conf)
            if line.split('=')[1].strip().isdigit()}


"""Solution to chapter 7, exercise 35a, beyond 2: read_config_int"""


def read_config(filename):
    return {one_line.split('=')[0]: int(one_line.split('=')[1].strip())
            for one_line in open(filename)
            if one_line.split('=')[1].strip().isdigit()}


print(read_conf('rryD'))
