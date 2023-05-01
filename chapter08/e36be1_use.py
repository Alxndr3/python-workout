from e36be1 import income_tax
from e36be1 import tax_brackets


print(income_tax(999))
print(income_tax(1000))
print(income_tax(5000))
print(income_tax(12000))
print(income_tax(20000))


brackets = [{'start': 0, 'end': 1000, 'tax': 0},
          {'start': 1000, 'end': 10000, 'tax': .1},
          {'start': 10000, 'end': 20000, 'tax': .2},
          {'start': 20000, 'end': 999999999999, 'tax': .5}]

print(tax_brackets(20000, brackets))
