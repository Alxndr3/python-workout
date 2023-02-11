"""
The final field in /etc/passwd is the shell, the Unix command interpreter
that’s invoked when a user logs in. Create a file, containing one line per
shell, in which the shell’s name is written, followed by all of the usernames
that use the shell; for example
"""

def shell_users(filename, shell_users):
    shell = {}
    with open(filename, 'r') as f, open(shell_users, 'w') as s:
        for x in f:
            shell.setdefault(x.strip().split(':')[-1], []).append(x.strip().split(':')[0])

        for k, v in shell.items():
            s.write(f'{k}: {", ".join(v)}\n')


shell_users("./files/passwd", "./files/shell_users")


"""Solution to chapter 5, exercise 24, beyond 3: shell_users"""

from collections import defaultdict


def shell_users(filename, outfilename):
    shells = defaultdict(list)

    with open(filename) as passwd, open(outfilename, 'w') as outfile:
        for one_line in passwd:
            if one_line.startswith(('#', '\n')):
                continue

            username, *fields, shell = one_line.strip().split(':')
            shells[shell].append(username)

        for shell, all_users in shells.items():
            outfile.write(f'{shell}\t{",".join(all_users)}\n')
