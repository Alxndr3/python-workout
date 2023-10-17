"""In this exercise, we’ll also implement a subclass of dict, which I call
FlexibleDict. Dict keys are Python objects, and as such are identified with a
type. So if you use key 1 (an integer) to store a value, then you can’t use
key '1' (a string) to retrieve that value. But FlexibleDict will allow for
this. If it doesn’t find the user’s key, it will try to convert the key to
both str and int before giving up."""


"""Solution to chapter 9, exercise 42: flexible dict"""


class FlexibleDict(dict):
    """Dict that lets you use a string or int somewhat interchangeably."""

    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass

        return dict.__getitem__(self, key)


dictionary = FlexibleDict()

dictionary['1'] = 2
print(dictionary[1])
print(dictionary['1'])

d = {'hello': 'world'}
print(d)
