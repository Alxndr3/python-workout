import io


def first_last(sequence):
    if type(sequence) is tuple:
        return sequence[0], sequence[-1]
    if type(sequence) is list:
        return [sequence[0], sequence[-1]]
    if type(sequence) is str:
        return f"{sequence[0]} {sequence[-1]}"


def first_last_bs(sequence):
    return sequence[:1] + sequence[-1:]


def square_num(number):
    return (number * number)


def longest_element(elements):
    element_len = 0
    if type(elements) is str:
        elements = elements.split()
    for element in elements:
        if len(element) > element_len:
            element_len = len(element)
            long_element = element
    print(long_element)


def find_largest_word(source):
        iostr = io.StringIO(source)
        return filestr.read()


def even_odd_sum(elements):
    l = [0, 0]
    for e in elements:
        if e % 2 == 0:
            nl[0] += e
        else:
            nl[1] += e
    print(nl)


def plus_minus(elements):
    result = elements[0]
    for k in range(len(elements)):
        if k + 1 == len(elements):
            break
        if k % 2 == 0:
            result += elements[k + 1]
        else:
            result -= elements[k + 1]
    print(result)


def myzip(*iterables):
    list1 = []
    list2 = []
    for x in range(len(iterables[0])):
        for i in iterables:
            list1.append(i[x])
        list2.append(tuple(list1))
        list1.clear()
    return (list2)


print(myzip([10, 20, 30, 40, 50, 60], 'abcdef'))

