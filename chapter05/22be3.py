"""Create a CSV file, in which each line contains 10 random integers between 10
and 100. Now read the file back, and print the sum and mean of the numbers on
each line."""

import csv
import random


def write_csv():
    l = []
    with open("./files/sum_mean_line.csv", "w") as f:
        wcsv = csv.writer(f)
        for _ in range(10):
            for _ in range(10):
                l.append(random.randint(1, 100))
            wcsv.writerow(l)
            l.clear()


def sum_mean():
    with open("./files/sum_mean_line.csv", 'r') as f:
        infile = csv.reader(f, delimiter=':')
        for i, x in enumerate(infile):
            l = [ int(y) for y in x[0].split(',') ]
            print("line:", i + 1,':', 'sum: ', sum(l), '-', 'min: ', min(l))


write_csv()
sum_mean()


"""Solution to chapter 5, exercise 22, beyond 3: random_csv"""

def random_csv(csv_filename):

    with open(csv_filename, 'w') as output:
        outfile = csv.writer(output)

        for i in range(10):
            output = []
            for j in range(10):
                output.append(random.randint(10, 100))

            outfile.writerow(output)

    for one_line in open(csv_filename):
        numbers = [int(one_item)
                   for one_item in one_line.split(',')]

        print(f'sum = {sum(numbers)}, mean = {sum(numbers)/len(numbers)}')
