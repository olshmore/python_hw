def my_func(arg_1, arg_2, arg_3):
    return arg_1 + arg_2 + arg_3 - min(arg_1, arg_2, arg_3)


a = int(input('First argument: '))
b = int(input('Second argument: '))
c = int(input('Third argument: '))

print(my_func(a, b, c))
