import os


def list_recursively_dir(directory):
    for f in os.walk(directory):
        if 'env' not in f[0] or '.git' not in f[0].split('/'):
            print(f)





list_recursively_dir('./')

