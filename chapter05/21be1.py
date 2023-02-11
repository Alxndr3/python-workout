"""Use the hashlib module in the Python standard library, and the md5 function
within it, to calculate the MD5 hash for the contents of every file in a
user-specified directory. Then print all of the filenames and their MD5
hashes."""


import hashlib
import os
from glob import glob


def file_hashes(dirname):
    for k, v in { os.path.relpath(filename, dirname):
            hashlib.md5(open(filename).read().encode()).hexdigest() for
            filename in glob(f"{dirname}/*") if os.path.isfile(filename)
            }.items():
        print(f'{k:<15} {v}')


file_hashes("/home/alexandre/PythonWorkout/chapter_05/")


import glob


"""Solution to chapter 5, exercise 21, beyond 1: md5_files"""

def md5_files(dirname):
    output = {}

    for one_filename in glob.glob(f'{dirname}/*'):
        try:
            m = hashlib.md5()
            m.update(one_filename.encode())
            output[one_filename] = m.hexdigest()
        except:
            pass

    return output


print(md5_files("/home/alexandre/PythonWorkout/chapter_05"))

