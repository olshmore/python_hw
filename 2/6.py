import copy
n = int(input('Введите число товаров '))
my_list = list()
my_dict = dict()
my_dict1 = dict()
i = 0
while i < n:
    i += 1
    print('Ввод данных для товара ', i)
    my_dict['name'] = input('name: ')
    my_dict['price'] = input('price: ')
    my_dict['quantity'] = input('quantity: ')
    my_dict['units'] = input('units: ')
    my_dict1 = my_dict.copy()
    my_list.append([i, my_dict1])

my_dict_n = dict()

name_list = list()
price_list = list()
quantity_list = list()
units_list = list()

for k in my_list:
    for j in k:
        if isinstance(j, dict):
            name_list.append(j['name'])
            price_list.append(j['price'])
            quantity_list.append(j['quantity'])
            units_list.append(j['units'])

my_dict_n['name'] = name_list
my_dict_n['price'] = price_list
my_dict_n['quantity'] = quantity_list
my_dict_n['units'] = units_list

print(my_dict_n)

for key in my_dict_n.keys():
    print("%s: %s" % (key, my_dict_n[key]))