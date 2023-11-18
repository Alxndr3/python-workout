import os
import subprocess


def all_lines(mydir, pattern="root"):
    try:
        yield subprocess.run(['grep', '-R', pattern, mydir],
                capture_output=True, text=True).stdout
    except OSError:
        pass


def all_lines_bs(path, s):
    for filename in os.listdir(path):
        full_filename = os.path.join(path, filename)
        try:
            for line in open(full_filename):
                if s in line:
                    yield line
        except OSError:
            pass


mydir = '/home/alexandre/PythonWorkout/chapter10/test/'

for file in all_lines(mydir):
    print(file)
