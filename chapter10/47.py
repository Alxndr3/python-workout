class CircleIterator:

    new_seq = []

    def __init__(self, seq, num):
        self.seq = seq
        self.num = num
        self.index = 0

    def __next__(self):
        if self.index >= len(self.seq):
            raise StopIteration

        while self.index <= self.num:
            for x in self.seq:
                self.index += 1
                if len(self.new_seq) < self.num:
                    self.new_seq.append(x)

        return self.new_seq


class Circle():

    def __init__(self, seq, num):
        self.seq = seq
        self.num = num

    def __iter__(self):
        return CircleIterator(self.seq, self.num)


class CircleIteratorBS():
    """Iterator for Circle."""

    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.index = 0

    def __next__(self):
        if self.index >= self.max_times:
            raise StopIteration
        print(self.index % len(self.data))
        value = self.data[self.index % len(self.data)]
        self.index += 1
        return value


class CircleBS():
    """Class that produces an iterator, which repeatedly cycles
through the elements of an iterator until returning max_times
items. """

    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times

    def __iter__(self):
        return CircleIterator(self.data, self.max_times)


o = CircleBS('hello', 8)

print(o)
print(list(o))
