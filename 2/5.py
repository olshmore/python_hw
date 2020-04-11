my_list = [7, 5, 3, 3, 2]

rating = int(input("Enter rating "))
my_list.append(rating)
my_list.sort(reverse=True)

print(my_list)