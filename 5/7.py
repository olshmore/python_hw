import json
profit = {}
sum_profit = 0
nonprofit = {}
av_profit = {}
with open('text7.txt', 'r') as f:
    content = f.readlines()
    num_firms = len(content)
with open('text7.txt', 'r') as f:
    for line in f:
        name, ownership, revenue, costs = line.split()
        profit[name] = int(revenue) - int(costs)
        if profit[name] > 0:
            sum_profit = sum_profit + int(profit[name])
        else:
            nonprofit[name] = int(profit[name])
        av_profit['average_profit'] = int(sum_profit/num_firms)
with open('json7.json', 'w') as js:
    json.dump(profit, js)
    json.dump(av_profit, js)
    json.dump(nonprofit, js)
