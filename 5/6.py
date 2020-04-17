def to_number(s):
    for i, c in enumerate(s):
        if not c.isdigit():
            return s[:i]


hours = {}
hours_sum = {}
with open('text6.txt', 'r') as f:
    for line in f:
        subject, lecture, practice, lab = line.split()
        hours[subject] = to_number(lecture) + ' ' + to_number(practice) + ' ' + to_number(lab)
        for item in hours:
            sum_hours = 0
            for i in hours[item].split():
                sum_hours = sum_hours + int(i)
            hours_sum[subject] = sum_hours
    print(hours_sum)
