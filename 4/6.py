from itertools import count, cycle

print('Part a')
start = int(input('Enter starting value '))
for i in count(start):
    print(i)
    if i > start + 6:
        break

print('_____________')
print('Part b')

my_list = [1, 2, 3]
for num, i in enumerate(cycle(my_list)):
    print(i)
    if num > 10:
        break

