"""
Write a copyfile function that takes one mandatory argument--the name of an
input file--and any number of additional arguments: the names of files to which
the input should be copied. Calling copyfile('myfile.txt', 'copy1 .txt',
'copy2.txt', 'copy3.txt') will create three copies of myfile.txt: one each in
copy1.txt, copy2.txt, and copy3.txt.
"""


from shutil import copyfile


def copyfile_(filename, *xargs):
    for x in xargs:
        copyfile(filename, x)


copyfile_('f1')


"""Solution to chapter 6, exercise 25, beyond 1: copyfile"""

def copyfile(infilename, *args):
    for outfilename in args:
        with open(outfilename, 'w') as outfile:
            for one_line in open(infilename):
                outfile.write(one_line)

