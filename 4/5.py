from functools import reduce


def my_func(el_1, el_2):
    return el_1 * el_2


print({reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])})