"""In this exercise, write a function, passwd_to_dict, that reads from a
Unix-style “password file,” commonly stored as /etc/passwd, and returns a
dict based on it."""

def passwd_to_dict(filename):
    pwd = {l.split(':')[0]: l.split(':')[3] for l in open(filename) }
    return pwd


def passwd_to_dict1(filename):
    with open(filename ,'r') as pw:
        pwd = {l.split(':')[0]: l.split(':')[3] for l in pw }

    return(pwd)


def passwd_to_dict_bs(filename):
    users = {}
    with open(filename) as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                users[user_info[0]] = int(user_info[2])
    return users

if __name__ == '__main__':
    for k,v in passwd_to_dict1("/etc/passwd").items():
        print(f'{k:<20} {v}')

