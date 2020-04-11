def print_info(name, surname, birth_date, city, phone):
    print(name, surname, birth_date, city, phone)


info_list = list((input('Введите данные о пользователе через пробел ').split()))

name = info_list[0]
surname = info_list[1]
birth_date = info_list[2]
city = info_list[3]
phone = info_list[4]

print_info(name=name, surname=surname, birth_date=birth_date, city=city, phone=phone)
