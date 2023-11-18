class MyEnumerate:

    def __init__(self, iterable):
        self.index = 0
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.iterable):
            raise StopIteration

        value = (self.index, self.iterable[self.index])
        self.index += 1
        return value


e = MyEnumerate('abcde')

print('***** A *****')
for x in e:
    print(x)

print('\n***** B *****')
for x in e:
    print(x)
