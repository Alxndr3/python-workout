"""Convert /etc/passwd from a CSV-style file into a JSON-formatted file. The
JSON file will contain the equivalent of a list of Python tuples, with each
tuple representing one line from the file."""

import json


def convert_csv(filename):
    with open(filename, 'r') as pwd:
        json_load = { str(x.strip().split(':')[0]): tuple(x.split(':')) for x
                in pwd.readlines() }

    with open('files/passwd.json', 'w') as outfile:
        json.dump(json_load, outfile)

# convert_csv('files/passwd')


"""Solution to chapter 5, exercise 23, beyond 1: json_passwd"""

def json_passwd(filename):
    output = []
    for one_line in open(filename):
        if one_line.startswith('#'):
            continue
        if one_line.strip().startswith('\n'):
            continue

        output.append(tuple(one_line.split(':')))

    return json.dumps(output)

print(json_passwd('files/passwd'))

