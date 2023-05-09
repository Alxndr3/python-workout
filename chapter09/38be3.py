"""Create a new LogFile class that expects to be initialized with a filename.
Inside of __init__, open the file for writing and assign it to an attribute,
file, that sits on the instance. Check that it’s possible to write to the file
via the file attribute."""


class LogFile:

    def __init__(self, filename):
        self.filename = filename

        self.f = open(self.filename, 'a')


hello = LogFile('hello')
hello.f.write('world\n')


"""Solution to chapter 9, exercise 38, beyond 3: logfile"""


class Logfile:
    def __init__(self, filename):
        self.file = open(filename, 'w')
