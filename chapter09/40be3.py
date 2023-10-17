"""Define a Transaction class, in which each instance represents either a
deposit or a withdrawal from a bank account. When creating a new instance
of Transaction, you’ll need to specify an amount--positive for a deposit
and negative for a withdrawal. Use a class attribute to keep track of the
current balance, which should be equal to the sum of the amounts in all
instances created to date."""


class Transaction():

    amount = 0

    def __init__(self, operation):
        self.operation = operation

        if operation >= 0:
            Transaction.amount += self.operation


transaction = Transaction(10)
transaction = Transaction(-5)
transaction = Transaction(3)
transaction = Transaction(-1)

print(transaction.amount)






