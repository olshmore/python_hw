from itertools import count
from math import factorial


def fact(m):
    for i in count(m):
        yield factorial(i)


j = int(input('Enter factorial base: '))
n = 1

for el in fact(n):
    print(el)
    n += 1
    if n == j + 1:
        break
