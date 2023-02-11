"""Write a function that writes a dict to a CSV file. Each line in the CSV file
should contain three fields: (1) the key, which we’ll assume to be a string,
(2) the value, and (3) the type of the value (e.g., str or int)."""


import csv


def write_dict(mydict):
    with open('./files/new_csv', 'w') as f:
        dict_csv = csv.writer(f)
        for k, v in mydict.items():
            dict_csv.writerow((k, v, type(v)))


mydict = {"1": "hello", "2": 3}
write_dict(mydict)


"""Solution to chapter 5, exercise 22, beyond 2: dict_to_csv"""

def dict_to_csv(d, csv_filename):

    with open(csv_filename, 'w') as output:
        outfile = csv.writer(output, delimiter=delimiter)

        for key, value in d.items():
            outfile.writerow([key, value, type(value)])

