"""The built-in enumerate method takes a second, optional argument--an integer,
representing the first index that should be used. (This is particularly handy
when numbering things for nontechnical users, who believe that things should be
numbered starting with 1, rather than 0.)"""


class MyEnumerateIterator:
    def __init__(self, data, start):
        self.data = data
        self.index = 0
        self.start = start

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (self.index + self.start, self.data[self.index])
        self.index += 1
        return value


class MyEnumerate():
    def __init__(self, data, start=0):
        self.data = data
        self.start = start

    def __iter__(self):
        return MyEnumerateIterator(self.data, self.start)


e = MyEnumerate('abcde', 1)

print('***** A *****')
for x in e:
    print(x)

print('\n***** B *****')
for x in e:
    print(x)
