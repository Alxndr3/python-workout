"""The current version of all_lines returns all of the lines from the first
file, then all of the lines from the second file, and so forth. Modify the
function such that it returns the first line from each file, and then the
second line from each file, until all lines from all files are returned. When
you finish printing lines from shorter files, ignore those files while
continuing to display lines from the longer files."""

import os


def all_lines(mydir):
    ml = []
    for count_file, file in enumerate(os.listdir(mydir)):
        try:
            for count_line, line in \
                    enumerate(open(os.path.join(mydir, file), 'r')):

                ml.append([])
                ml[count_line].append(line)

        except OSError:
            pass

        yield ml


for line in all_lines('/home/alexandre/PythonWorkout/chapter10/test'):
    for l in line:
        if l != []:
            print(''.join(l).split())


def open_file_safely(filename):
    try:
        return open(filename)
    except OSError:
        return None


def all_lines_alt(path):
    all_files = [open_file_safely(os.path.join(path, filename))
                 for filename in os.listdir(path)]

    while all_files:
        for one_file in all_files:
            if one_file is None:
                all_files.remove(one_file)
                continue

            one_line = one_file.readline()

            if one_line:
                yield one_line
            else:
                all_files.remove(one_file)


