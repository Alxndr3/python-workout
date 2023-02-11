"""Ask the user for the name of a directory. Iterate through each file in that
directory (ignoring subdirectories), getting (via os.stat) the size of the file
and when it was last modified. Create a JSON-formatted file on disk listing
each filename, size, and modification timestamp. Then read the file back in,
and identify which files were modified most and least recently, and which files
are largest and smallest, in that directory. """


import json
import os
import time


def dir_data():
    dirname = input("Type the path of a directory: ")

    if os.path.isdir(dirname):
        data = { x: ( os.stat(os.path.join(dirname, x))[6],
            time.strftime('%Y-%m-%d %H:%M:%S',
                time.localtime(os.stat(os.path.join(dirname, x))[-2]))) for x
            in os.listdir(dirname) }
    else:
        print("It's not a dir.")

    with open('./files/dir_data.json', 'w') as ddj:
        ddj.write(json.dumps(data))

# dir_data()

def read_dir_data(filename):
    with open(filename, 'r') as jread:
        json_dir_data = json.load(jread)
    #json_dir_data = json.load(open(filename))

    print('Most recent modified file: ', end='')
    print(sorted(json_dir_data.items(), key=lambda x: x[1][1])[-1][0])
    print('Least recent modified file: ', end='')
    print(sorted(json_dir_data.items(), key=lambda x: x[1][1])[0][0])
    print('Largest file: ', end='')
    print(sorted(json_dir_data.items(), key=lambda x: x[1][0])[-1][0])
    print('Smallest file: ', end='')
    print(sorted(json_dir_data.items(), key=lambda x: x[1][0])[0][0])

#read_dir_data('files/dir_data.json')

"""Solution to chapter 5, exercise 23, beyond 3: file_info"""


import os
import glob
import json


def write_file_info(dirname, outputfile):
    output = []
    for one_filename in glob.glob(f'{dirname}/*'):
        if not os.path.isfile(one_filename):
            continue

        try:
            output.append({'filename': one_filename,
                           'size': os.stat(one_filename).st_size,
                           'mtime': os.stat(one_filename).st_mtime})
        except:
            print(f'Error reading {filename}; skipping')

    return json.dump(output, open(outputfile, 'w'))


def read_file_info(filename):
    output = {}

    file_info = json.load(open(filename))

    return file_info

# write_file_info('/home/alexandre/.ssh', './files/file_info.json')
print(read_file_info('./files/file_info.json'))


