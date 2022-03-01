# My solution
def mysum(*args):
    total = 0
    for arg in range(len(args)):
        total += args[arg]
    return total


# Book solution
def mysum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output


# Beyonde the exercice
def mysum(nums, start=0):
    for num in nums:
        start += num
    return start


def my_average(arg):
    average = (sum(arg)) / (len(arg))
    return average


def word_average(words):
    short_word = long_word = words[0]
    avarage_lenght = 0
    for word in words:
        avarage_lenght += len(word)
        if len(short_word) > len(word):
            len_short_word = len(word)

        if len(long_word) < len(word):
            len_long_word = len(word)

    avarage_lenght = avarage_lenght / len(words)

    return f"""
    The shortest word in this list contains {len_short_word} characters')
    The longest word in this list contains {len_long_word} characters')
    The average word lenght is {avarage_lenght} characters.
    """


def sum_objects(objects):
    summed_objects = [obj for obj in objects if str(type(obj)) == "<class 'int'>"]
    return sum(summed_objects)



objects = [1, 2, 3, 4, '5']

print(sum_objects(objects))
