"""Modify all_lines such that it doesn’t return a string with each iteration,
but rather a tuple. The tuple should contain four elements: the name of the
file, the current number of the file (from all those returned by os.listdir),
the line number within the current file, and the current line."""

import os


def all_lines(mydir):
    for count_file, file in enumerate(os.listdir(mydir)):
        try:
            for count_line, line in \
                    enumerate(open(os.path.join(mydir, file), 'r')):
                yield (count_file, count_line, line.strip())
        except OSError:
            pass


for file in all_lines('/home/alexandre/PythonWorkout/chapter08'):
    print(file)
