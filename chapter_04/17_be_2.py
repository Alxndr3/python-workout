"""Reading from that same server log, what response codes were returned to
users? The 200 code represents “OK,” but there are also 403, 404, and 500
errors. (Regular expressions aren’t required here but will probably help.)"""

def response_codes(log_file):
    d1 = {}

    for line in open(log_file, 'r'):

        if line.split()[0] not in d1:
            d1[line.split()[0]] = set(line.split()[8])
        d1[line.split()[0]].add(line.split()[8])

    return d1


"""Solution to chapter 4, exercise 17, beyond 2: different_responses"""

def different_responses(filename):
    return {one_line.split()[8]
            for one_line in open(filename)}


print(response_codes('access.log'))



