"""Write a function, transform_lines, that takes three arguments: a function
that takes a single argument, the name of an input file, and the name of an
output file. Calling the function will run the function on each line of the
input file, with the results written to the output file. (Hint: the previous
exercise and this one are closely related.)"""


def transform_lines(func, infile, outfile):
    with func(infile, 'r') as inf, func(outfile, 'w') as outf:
        for x in inf.readlines():
            outf.write(x.upper())


transform_lines(open, "input.txt", "output.txt")


"""Solution to chapter 6, exercise 26, beyond 3: transform_lines"""


def transform_lines(f, infilename, outfilename):
    with open(infilename) as infile, open(outfilename, 'w') as outfile:
        for one_line in infile:
            outfile.write(f(one_line))

