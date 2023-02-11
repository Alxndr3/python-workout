"""Extend this exercise (22) by asking the user to enter a space-separated list of
integers, indicating which fields should be written to the output CSV file.
Also ask the user which character should be used as a delimiter in the output
file. Then read from /etc/passwd, writing the user’s chosen fields, separated
by the user’s chosen delimiter."""

import csv


def passwd_to_csv(passwd_filename, csv_filename, print_fields='1 3', delim=','):
    with open(passwd_filename) as passwd, open(csv_filename, 'w') as output:
        infile = csv.reader(passwd, delimiter=':')
        outfile = csv.writer(output, delimiter=delim)
        for record in infile:
            if len(record) > 1:
                fields = [ record[int(x) - 1] for x in print_fields.split() ]
                outfile.writerow(fields)
                print(fields)

delimeter = input("Delimeter = ")
print_fields = str(input("Fields to print: "))
passwd_to_csv("./files/passwd", "./files/new_file.csv", print_fields, delimeter)


"""Solution to chapter 5, exercise 22, beyond 1: passwd_to_csv_selected"""

def passwd_to_csv_bs(passwd_filename, csv_filename, fields_to_pass='1 2', delimiter='\t'):
    fields_to_pass = [int(one_item)
                      for one_item in fields_to_pass]

    with open(passwd_filename) as passwd, open(csv_filename, 'w') as output:
        infile = csv.reader(passwd, delimiter=':')
        outfile = csv.writer(output, delimiter=delimiter)
        for record in infile:

            if len(record) > 1:
                fields = [one_field
                          for index, one_field in enumerate(record)
                          if index in fields_to_pass]

                outfile.writerow(*fields)


#passwd_to_csv_bs("./files/passwd", "./files/new_file.csv")

