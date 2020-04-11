sum = 0

try:
    while True:
        for i in map(int, input('Введите числа через пробел: ').split()):
            sum += i
        print(sum)
except ValueError:
    print(sum)
