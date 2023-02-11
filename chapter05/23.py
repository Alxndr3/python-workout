"""In this exercise, you’re analyzing test data in a high school. There’s a
scores directory on the filesystem containing a number of files in JSON format.
Each file represents the scores for one class. Write a function, print_scores,
that takes a directory name as an argument and prints a summary of the student
scores it finds. Your function should print the highest, lowest, and average
test scores for each subject in each class."""

import glob
import json


def print_scores(dir_name):
    scores = {}

    for x in glob.glob(dir_name):
        filename = x.split('/')[-1]

        with open(x, 'r') as jf:
            csvload = json.load(jf)
        newdict = {}
        for x in csvload:
            for k, v in x.items():
                newdict.setdefault(k, [])
                newdict[k].append(v)
            scores[filename] = newdict

    for k, v in scores.items():
        print(k)
        for v, x in v.items():
            print(f'{v} min: {min(x)}, max: {max(x)}, average: {sum(x) / len(x)}')
        print()


"""Solution to chapter 5, exercise 23: test_scores"""

def print_scores_bs(dirname):
    """Takes the name of a directory containing one or more JSON files with a
    ".json" suffix. The files contain test scores in a variety of  subjects.
    For each class, the function prints the min, max, and average score for
    each subject.
    """
    scores = {}

    for filename in glob.glob(f'{dirname}/*.json'):
        scores[filename] = {}

        with open(filename) as infile:
            for result in json.load(infile):
                for subject, score in result.items():
                    scores[filename].setdefault(subject, [])
                    scores[filename][subject].append(score)

    for one_class in scores:
        print(one_class)
        for subject, subject_scores in scores[one_class].items():
            min_score = min(subject_scores)
            max_score = max(subject_scores)
            average_score = (sum(subject_scores) /
                             len(subject_scores))

            print(subject)
            print(f'\tmin {min_score}')
            print(f'\tmax {max_score}')
            print(f'\taverage {average_score}')

print_scores_bs("scores")

