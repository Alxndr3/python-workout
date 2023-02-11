"""From /etc/passwd, create a dict in which the keys are the usernames (as in
the main exercise) and the values are themselves dicts with keys (and
appropriate values) for user ID, home directory, and shell."""


from collections import defaultdict


def passwd_dict(filename):
    keys = ('ID', 'Home', 'Shell')
    d = defaultdict(dict)
    for l in open(filename, 'r'):
        l = l.split(':')
        for k in keys:
            if k[0]:
                d[l[0]].update({k: l[2]})
            elif k[1]:
                d[l[0]].update({k: l[-2]})
            elif k[2]:
                d[l[0]].update({k: l[-1]})

    return d


passwd_dict("/etc/passwd")


"""Solution to chapter 5, exercise 19, beyond 2: user_info"""

def user_info(filename):
    output = {}

    for one_line in open(filename):
        if one_line.startswith(('#', '\n')):
            continue
        username, passwd, uid, *ignore, homedir, shell = one_line.strip().split(':')

        output[username] = {'uid': uid,
                            'homedir': homedir,
                            'shell': shell}

    return output


print(user_info("/etc/passwd"))

