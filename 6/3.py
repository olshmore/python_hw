class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


new_worker = Position('Ivan', 'Ivanov', 'Developer', 100000, 50000)

print(new_worker.name)
print(new_worker.surname)
print(new_worker.position)

print(new_worker.get_full_name())
print(new_worker.get_total_income())