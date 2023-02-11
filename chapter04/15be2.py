"""Open a log file from a Unix/Linux system--for example, one from the Apache
server. For each response code (i.e., three-digit code indicating the HTTP
request’s success or failure), store a list of IP addresses that generated
that code."""


def log_analyses(log_file):
    http_ip = {}

    with open(log_file) as lf:
        for x in lf.readlines():
            if x.strip().startswith('10.20.121.193'):
                continue

            if x.split()[8] not in http_ip:
                http_ip[x.split()[8]] = [x.split()[0]]

            else:
                http_ip[x.split()[8]].append(x.split()[0])

    for k, v in http_ip.items():
        print(k, v)
        print()


"""Solution to chapter 4, exercise 15, beyond 2: errors with IP addresses"""


from collections import defaultdict


def error_ip_addresses(filename):
    output = defaultdict(list)

    for one_line in open(filename):
        fields = one_line.split()
        ip_address = fields[0]
        response_code = fields[8]
        output[response_code].append(ip_address)

    return output



# log_analyses("access.log")
print(error_ip_addresses("access.log"))

