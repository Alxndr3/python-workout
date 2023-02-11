"""Read through /etc/passwd, creating a dict in which user login shells (the
final field on each line) are the keys. Each value will be a list of the users
for whom that shell is defined as their login shell."""

from collections import defaultdict


def read_login_shell(filename):

    d = defaultdict(list)

    with open(filename, 'r') as passwd:
        for l in passwd:
            d[l.split(':')[-1]].append(l.split(':')[0])

    return d


print(read_login_shell("/etc/passwd"))


"""Solution to chapter 5, exercise 19, beyond 1: shells_users"""

from collections import defaultdict


def shells_users(filename):
    output = defaultdict(list)

    for one_line in open(filename):
        if one_line.startswith(('#', '\n')):
            continue
        username, *ignore, shell = one_line.strip().split(':')

        output[shell].append(username)

    return output
