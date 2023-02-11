"""Create a dict in which the keys are the names of files on your system and
the values are the sizes of those files. To calculate the size, you can use
os.stat (http://mng.bz/dyyo)."""

import os


def file_sizes1(dirname):
    file_sizes_dict = {}

    for file in os.listdir(dirname):
        file_sizes_dict[file] = os.stat(file)[6]

    return file_sizes_dict


def file_sizes2(files):
    file_sizes_dict = {}

    for file in files:
        file_sizes_dict[file] = os.stat(file)[6]

    return file_sizes_dict


"""Solution to chapter 5, exercise 20, beyond 2: file_sizes"""

import glob
import os


def file_sizes(dirname):
    counts = {one_filename: os.stat(one_filename).st_size
              for one_filename in glob.glob(f'{dirname}/*')
              if os.path.isfile(one_filename)}

    return counts


files = ["18.py", "20.py"]

