translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text4_1.txt', 'r') as f:
    for i in f:
        i = i.split(' ', 1)
        new_file.append(translate[i[0]] + ' ' + i[1])

with open('text4_2.txt', 'w') as f:
    f.writelines(new_file)