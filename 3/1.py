def my_func(num_1, num_2):
    if num_2 != 0:
        return num_1 / num_2
    else:
        return "Division by zero"


number_1 = int(input('dividend: '))
number_2 = int(input('divider: '))
print(my_func(number_1, number_2))
