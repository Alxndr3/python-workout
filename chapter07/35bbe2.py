"""Create a list of tuples in which each tuple contains three elements: (1) the
author’s first and last names, (2) the book’s title, and (3) the book’s
price in U.S. dollars. Use a dict comprehension to turn this into a dict whose
keys are the book’s titles, with the values being another (sub -) dict, with
keys for (a) the author’s first name, (b) the author’s last name, and (c) the
book’s price in U.S. dollars."""


def ord_book(book):
    return {
            book[1]: {
                'fname': book[0].split()[0],
                'lname': book[0].split()[1],
                'price': book[-1]}
            for indice in range(len(book))}


"""Solution to chapter 7, exercise 35b, beyond 2: books"""


def make_book_dict(books):

    return {title: {'first': name.split()[0],
                    'last': name.split()[1],
                    'price': price}
            for name, title, price in books}


book = [('olavo carvalho'), ('o jardim das aflições'), ('$50')]


print(ord_book(book))
