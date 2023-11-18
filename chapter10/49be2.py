import os


def file_usage_timing(path):
    for file in os.listdir(path):
        yield (file,
               os.stat(os.path.join(path, file)).st_mtime,
               os.stat(os.path.join(path, file)).st_ctime,
               os.stat(os.path.join(path, file)).st_atime)


statistic = file_usage_timing('./test')

for x in statistic:
    print(x)

