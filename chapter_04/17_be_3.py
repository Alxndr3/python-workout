"""Use os.listdir (http://mng.bz/YreB) to get the names of files in the current
directory. What file extensions (i.e., suffixes following the final .
character) appear in that directory? It’ll probably be helpful to use
os.path.splitext (http://mng.bz/GV4v)."""

import os


def list_extensions(directory):
    return {os.path.splitext(f)[-1] for f in os.listdir(directory)}


"""Solution to chapter 4, exercise 17, beyond 3: different_extensions"""

def different_extensions(dirname):
    return {os.path.splitext(one_filename)[-1]
            for one_filename in os.listdir(dirname)}


print(list_extensions('./'))
