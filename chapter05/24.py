"""In many cases, we want to take a file in one format and save it to another
format. In this function, we do a basic version of this idea. The function
takes two arguments: the names of the input file (to be read from) and the
output file (which will be created).

For example, if a file looks like

abc def
ghi jkl

then the output file will be

fed cba
lkj ihg

Notice that the newline remains at the end of the string, while the rest of the
characters are all reversed."""


def reverse_line(infile, outfile):
    with open(infile, 'r') as inf, open(outfile, 'a') as ouf:
        for x in inf.readlines():
            ouf.write(x[::-1].strip() + '\n')

reverse_line('files/infile', 'files/outfile')

"""Solution to chapter 5, exercise 24: reverse_lines"""


def reverse_lines(infilename, outfilename):
    """Takes two filenames as arguments. The
first is for reading, and the second is for writing.
The contents of the first file are written to
the second, but in reverse order.
"""
    with open(infilename) as infile, open(outfilename, 'w') as outfile:
        for one_line in infile:
            outfile.write(f'{one_line.rstrip()[::-1]}\n')


