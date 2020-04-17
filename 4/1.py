from sys import argv

script_name, production, rate, bonus = argv

print("Salary: ", float(production)*float(rate)+float(bonus))
