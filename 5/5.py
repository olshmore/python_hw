try:
    with open('text5.txt', 'w') as f:
        line = input('Введите набор чисел, разделенных пробелами \n')
        f.writelines(line)
        num = line.split()
        print(sum(map(int, num)))
except ValueError:
    print('Введены не числа')
except IOError:
    print("Произошла ошибка ввода-вывода")
