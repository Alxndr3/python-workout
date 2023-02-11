"""For a slightly different challenge, turn each line in the file into a Python
dict. This will require identifying each field with a unique column or key
name. If you’re not sure what each field in /etc/passwd does, you can give it
an arbitrary name."""

import json


def passwd_json(filename):
    passwd_fields = ('username', 'password', 'uid', 'gid', 'home dir', 'shell')
    with open(filename, 'r') as pwd:
        fields_zip = [ dict(zip(passwd_fields, x.strip().split(':'))) for x in
                pwd.readlines() ]

    return json.dumps(fields_zip)


"""Solution to chapter 5, exercise 23, beyond 2: json_passwd_dict"""

def json_passwd_dict(filename):
    fields = ['username', 'password', 'uid', 'gid', 'name', 'homedir', 'shell']

    output = []
    for one_line in open(filename):
        if one_line.startswith('#'):
            continue
        if one_line.strip().startswith('\n'):
            continue

        output.append(dict(zip(fields, one_line.split(':'))))

    return json.dumps(output)

print(json_passwd_dict('files/passwd'))

