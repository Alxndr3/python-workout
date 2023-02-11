"""Read through a server (e.g., Apache or nginx) log file. What were the
different IP addresses that tried to access your server?"""


def different_ips(log_file):
    ips = set()
    for line in open(log_file, 'r'):
        ips.add(line.split()[0])

    return ips


"""Solution to chapter 4, exercise 17, beyond 1: different_ips"""


def different_ips(filename):
    return {one_line.split()[0]
            for one_line in open(filename)}


log_file = "access.log"
print(different_ips(log_file))
