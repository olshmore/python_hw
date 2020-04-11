def my_func(x, y):
    return x ** y


def my_func_hard(x, y):
    i = 0
    a = 1
    while i < abs(y):
        a = a / x
        i += 1
    return a


num = float(4)
power = int(-4)

print(my_func(num, power))
print(my_func_hard(num, power))
