import os


def all_lines_mychain(*args):
    for files in args:
        try:
            for file in open(files, 'r').readlines():
                yield file.strip()
        except OSError:
            pass


"""Solution to chapter 10, exercise 50, beyond 2: all_lines_mychain"""


def mychain(*args):
    for arg in args:
        for item in arg:
            yield item


def all_lines(path):
    return mychain(*(open(os.path.join(path, filename))
                     for filename in os.listdir(path)
                     if os.path.isfile(os.path.join(path, filename))))


print(list(all_lines_mychain('./test/passwd', './test/test')))
