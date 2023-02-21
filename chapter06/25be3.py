"""
Write an anyjoin function that works similarly to str.join, except that the
first argument is a sequence of any types (not just of strings), and the second
argument is the “glue” that we put between elements, defaulting to " " (a
space). So anyjoin([1,2,3]) will return 1 2 3, and anyjoin('abc', pass:'**')
will return pass:a**b**c.
"""


def anyjoin(*xargs, glue=" "):
    joint = ''
    for x in xargs:
        for y in x:
            joint += str(y)
            if y != x[-1]:
                joint += glue

    print(joint)


anyjoin([1, 2, 3], glue="**")


"""Solution to chapter 6, exercise 25, beyond 3: anyjoin"""

def anyjoin_bs(seq, glue=' '):
    return glue.join([str(one_item)
                      for one_item in seq])

