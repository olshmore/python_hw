# list
month = int(input("Enter a month number of a year "))

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

if month in winter:
    print('winter')
if month in spring:
    print('spring')
if month in summer:
    print('summer')
if month in autumn:
    print('autumn')

# dict
month = (input("ВEnter a month number of a year "))

my_dict = {'12': 'winter', '1': 'winter', '2': 'winter', '3': 'spring', '4': 'spring', '5': 'spring', '6': 'summer', '7': 'summer', '8': 'summer', '9': 'autumn', '10': 'autumn', '11': 'autumn'}
print(my_dict[month])