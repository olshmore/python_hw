sum_salary = 0
less_twenty = []
with open('text3.txt', 'r') as f:
    content = f.readlines()
    employees = len(content)
    for i in range(len(content)):
        for item in content[i].split():
            try:
                sum_salary += float(item)
                if float(item) <= 20000:
                    less_twenty.append(i)
            except ValueError:
                continue
    print('Employees whose salary is less then 20k:')
    for i in range(len(content)):
        if i in less_twenty:
            print(content[i].strip())
    print('Average salary: ', sum_salary/employees)










