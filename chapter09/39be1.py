"""Create a Book class that lets you create books with a title, author, and
price. Then create a Shelf class, onto which you can place one or more books
with an add_book method. Finally, add a total_price method to the Shelf class,
which will total the prices of the books on the shelf."""


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


"""Solution to chapter 9, exercise 39, beyond 1: book_and_shelf"""


class Book_bs:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


class Shelf_bs:
    def __init__(self):
        self.books = []

    def add_books(self, *args):
        self.books += args

    def total_price(self):
        return sum(one_book.price
                   for one_book in self.books)


b1 = Book('hello', 'world', 34)
b2 = Book('hi', 'there', 33)
b3 = Book('Python', 'Lerner', 35)

s1 = Shelf()
s1.add_book(b1, b2)
s1.add_book(b3)
print(s1.total_price())

print(s1)
