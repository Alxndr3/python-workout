"""Write a method, Shelf.has_book, that takes a single string argument and
returns True or False, depending on whether a book with the named title exists
on the shelf."""


class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self. price = price


class Shelf:

    def __init__(self):
        self.shelf = []

    def add_book(self, *args):
        for arg in args:
            self.shelf.append([arg.title, arg.author, str(arg.price)])

    def __repr__(self):
        return '\n'.join(' '.join(book) for book in self.shelf)

    def total_price(self):
        return sum(int(book[-1]) for book in self.shelf)

    def has_book(self, title_search):
        # for title in self.shelf:
        #     if title_search == title[0]:
        #         return True
        #     return False

        return [True for title in self.shelf
                if title_search == title[0]][0]


"""Solution to chapter 9, exercise 39, beyond 2: has_book"""


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


class Shelf:
    def __init__(self):
        self.books = []

    def add_books(self, *args):
        self.books += args

    def total_price(self):
        return sum(one_book.price
                   for one_book in self.books)

    def has_book(self, title):
        return title in (one_book.title
                         for one_book in self.books)

b1 = Book('hello', 'world', 34)
b2 = Book('hi', 'there', 33)
b3 = Book('Python', 'Lerner', 35)

s1 = Shelf()
s1.add_book(b1, b2, b3)

print(s1.has_book('hello'))

