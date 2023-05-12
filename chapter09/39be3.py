"""Modify your Book class such that it adds another attribute, width. Then add
a width attribute to each instance of Shelf. When add_book tries to add books
whose combined widths will be too much for the shelf, raise an exception."""


class Book:

    def __init__(self, title, author, price, width):
        self.title = title
        self.author = author
        self. price = price
        self.width = width


class Shelf:

    def __init__(self):
        self.shelf = []
        self.width = 500

    def __repr__(self):
        return '\n'.join(' '.join(book) for book in self.shelf)

    def add_book(self, *args):
        for arg in args:
            if arg.width > self.width:
                print('Maximum number o book achieved')
            else:
                self.shelf.append([arg.title, arg.author, str(arg.price)])

    def total_price(self):
        return sum(int(book[-1]) for book in self.shelf)


b1 = Book('jardim', 'carvalho', 30, 500)
s1 = Shelf()
s1.add_book(b1)
b2 = Book('python', 'lerner', 30, 501)
s1.add_book(b2)
print(s1)


"""Solution to chapter 9, exercise 39, beyond 2: has_book"""


class TooManyBookOnShelfError(Exception):
    pass


class Book:
    def __init__(self, title, author, price, width):
        self.title = title
        self.author = author
        self.price = price
        self.width = width


class Shelf:
    def __init__(self, width):
        self.books = []
        self.width = width

    def add_books(self, *args):
        for new_book in args:
            if self.total_width() + new_book.width > self.width:
                raise TooManyBookOnShelfError('Too many books!')
            self.books.append(new_book)

    def total_price(self):
        return sum(one_book.price
                   for one_book in self.books)

    def has_book(self, title):
        return title in (one_book.title
                         for one_book in self.books)

    def total_width(self):
        return sum(one_book.width
                   for one_book in self.books)
