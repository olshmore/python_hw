revenue=int(input('Введите размер выручки'))
costs=int(input('Введите размер издержек'))
if revenue>costs:
    print('Прибыль')
    print('Рентабельность составляет', (revenue-costs)/revenue)
    employees=int(input('Введите численность сотрудников фирмы'))
    print('Прибыль фирмы в расчете на одного сотрудника составляет',
          (revenue-costs)/revenue/employees)
else:
    print('Убыток')