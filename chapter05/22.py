"""For this exercise, create a function, passwd_to_csv, that takes two
filenames as arguments: the first is a passwd-style file to read from, and the
second is the name of a file in which to write the output.
The new file’s contents are the username (index 0) and the user ID (index 2).
Note that a record may contain a comment, in which case it will not have
anything at index 2; you should take that into consideration when writing the
file. The output file should use TAB characters to separate the elements."""


import csv


def passwd_to_csv(filename1, filename2):
    with open(filename1, 'r') as f:
        pwd = f.readlines()

    with open(filename2, 'w') as f2:
        o = csv.writer(f2, delimiter='\t')
        o.writerow((list(map(lambda x: f"{x.split(':')[0]} {x.split(':')[2]}", pwd))))



"""Solution to chapter 5, exercise 22: passwd_to_csv"""

def passwd_to_csv_bs(passwd_filename, csv_filename):
    with open(passwd_filename) as passwd, open(csv_filename, 'w') as output:
        infile = csv.reader(passwd, delimiter=':')
        outfile = csv.writer(output, delimiter='\t')
        for record in infile:
            print(record)
            if len(record) > 1:
                outfile.writerow((record[0], record[2]))


#passwd_to_csv("./files/passwd", "./files/new_file.csv")
passwd_to_csv_bs("./files/passwd", "./files/new_file.csv")

