"""Create a dict whose keys are filenames and whose values are the lengths of
the files. The input can be a list of files from os.listdir
(http://mng.bz/YreB) or glob.glob (http://mng.bz/044N)."""


from pathlib import Path
import glob
import os


def files_length(directory):
    return {file.name: f'{file.stat()[6]}k'
            for file in directory.iterdir()}


def files_length_os(directory):
    return {file: f'{os.stat(file)[6]}k'
            for file in os.listdir(directory)}


"""Solution to chapter 7, exercise 32, beyond 2: file_info"""


def file_info(dirname):
    return {one_filename: os.stat(one_filename).st_size
            for one_filename in glob.glob(f'{dirname}/*')
            if os.path.isfile(one_filename)}


directory = Path.cwd()
print(files_length(directory))
print(files_length_os('./'))
