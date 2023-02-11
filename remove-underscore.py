import glob
import os


def remove_underscore(dirname):
    new_name = ''
    for filename in glob.glob(f'{dirname}/*.py'):
        print(filename)
        for x in filename.split('/')[-1]:
            if x not in  '_':
                new_name += x
        os.rename(filename, new_name)
        new_name = ''



remove_underscore('.')

