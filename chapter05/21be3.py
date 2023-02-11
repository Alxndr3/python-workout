"""Open an HTTP server’s log file. (If you lack one, then you can read one
from me at http://mng.bz/vxxM.) Summarize how many requests resulted in numeric
response codes--202, 304, and so on."""


from collections import defaultdict


def response_codes(filename):
    d = defaultdict(int)
    for oneline in open(filename):
        try:
            d[(oneline.split()[8])] += 1
        except:
            pass

    return d


"""Solution to chapter 5, exercise 21, beyond 3: response_counts"""

from collections import Counter


def response_counts(filename):
    output = Counter()

    for one_line in open(filename):
        try:
            output[one_line.split()[8]] += 1
        except:
            pass

    return output


print(response_codes("/home/alexandre/PythonWorkout/chapter_05/files/access-log.txt"))
print(response_counts("/home/alexandre/PythonWorkout/chapter_05/files/access-log.txt"))

