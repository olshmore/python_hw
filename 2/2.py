my_list = list((input('Введите элементы списка через пробел ').split()))

i = 0
length = len(my_list)

if length % 2 == 1:
    length = length - 2

while i < length:
    k = (my_list[i])
    (my_list[i]) = (my_list[i+1])
    (my_list[i+1]) = k
    i += 2

print(my_list)