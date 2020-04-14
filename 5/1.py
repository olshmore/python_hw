line = input('Введите текст \n')

with open('text1.txt', 'w') as f:
    while line:
        f.writelines(line)
        line = input('Введите текст \n')

with open('text1.txt', 'r') as f:
    print(f.readlines())
