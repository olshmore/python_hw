my_list = list((input('Введите строку из нескольких слов, разделённых пробелами ').split()))

i = 0
while i < len(my_list):
    my_list[i] = my_list[i][:10]
    i += 1

for num, value in enumerate(my_list, start=1):
    print(num, value)