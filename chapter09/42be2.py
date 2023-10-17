"""The RecentDict class works just like a dict, except that it contains a
user-defined number of key-value pairs, which are determined when the
instance is created. In a RecentDict(5), only the five most recent
key-value pairs are kept; if there are more than five pairs, then the
oldest key is removed, along with its value. Note: your implementation
could take into account the fact that modern dicts store their key-value
pairs in chronological order."""


class RecentDict(dict):
    # c = 0

    def __init__(self, num_items):
        super().__init__()
        self.num_items = num_items

    def __setitem__(self, key, value):

        dict.__setitem__(self, key, value)

        if len(self) > self.num_items:
            self.pop(list(self.keys())[0])


"""Solution to chapter 9, exercise 42, beyond 2: recent_dict"""


class RecentDictBS(dict):
    def __init__(self, maxsize):
        super().__init__()
        self.maxsize = maxsize

    def __setitem__(self, key, value):
        dict.__setitem__(self, str(key), value)

        if len(self) > self.maxsize:
            print(self.keys())
            self.pop(list(self.keys())[0])


mydict = RecentDict(2)

mydict[1] = 1
mydict[2] = 2
mydict[3] = 3
mydict[4] = 4

print(mydict)


