"""Use a dict comprehension to create a dict in which the keys are usernames
and the values are (integer) user IDs, based on a Unix-style /etc/passwd file.
Hint: in a typical /etc/passwd file, the usernames are the first field in a row
(i.e., index 0), and the user IDs are the third field in a row (i.e., index 2).
If you need to download a sample /etc/passwd file, you can get it from
http://mng.bz/ 2XXg. Note that this sample file contains comment lines, meaning
that you’ll need to remove them when creating your dict."""


import glob
import os


def user_id(filename):
    return {line.split(':')[0]: line.split(':')[2]
            for line in open(filename)
            if not line.split(':')[0].startswith('#')}


"""Solution to chapter 7, exercise 33, beyond 2: file_info"""

# Yes, this is a duplicate of exercise 33, beyond 2!  Whoops...


def file_info(dirname):
    return {one_filename: os.stat(one_filename).st_size
            for one_filename in glob.glob(f'{dirname}/*')
            if os.path.isfile(one_filename)}


print(user_id('passwd'))
