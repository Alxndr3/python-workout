import os


def all_lines(mydir):
    for file in os.listdir(mydir):
        try:
            for line in open(os.path.join(mydir, file), 'r').readlines():
                yield line.strip()
        except OSError:
            pass


print(list(all_lines('/home/alexandre/PythonWorkout/chapter08')))
