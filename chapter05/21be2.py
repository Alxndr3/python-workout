"""Ask the user for a directory name. Show all of the files in the directory,
as well as how long ago the directory was modified. You will probably want to
use a combination of os.stat and the Arrow package on PyPI (http://mng.bz/nPPK)
to do this easily."""


import arrow
import glob
import os


def files_stat(dirname):
    return { os.path.relpath(one_file, dirname): arrow.get(os.stat(one_file)[7]).format() for one_file in
            glob.glob("%s/*" % dirname) }


"""Solution to chapter 5, exercise 21, beyond 2: mod_times"""

def mod_times(dirname):
    output = {}

    for one_filename in glob.glob(f'{dirname}/*'):
        try:
            mod_time = os.stat(one_filename).st_mtime
            output[one_filename] = (arrow.now() - arrow.get(1503636889)).days

        except:
            pass

    return output

print(files_stat("/home/alexandre/PythonWorkout/chapter_02"))
print(mod_times("/home/alexandre/PythonWorkout/chapter_02"))

