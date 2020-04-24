class Date:
    def __init__(self, dmy):
        self.dmy = dmy

    @classmethod
    def extract(cls, dmy):
        date = []
        for i in dmy.split():
            date.append(i)
        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def validate(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2021:
                    return 'Validation completed'
                else:
                    return 'Year out of range'
            else:
                return 'Month out of range'
        else:
            return 'Day out of range'


new_date = Date('24 04 2020')
print(new_date.extract('24 04 2020'))
print(new_date.validate(24, 4, 2020))
print(new_date.validate(242, 42, 2022))
