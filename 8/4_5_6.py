class Warehouse:
    def __init__(self, subdivision):
        self.subdivision = subdivision


class OfficeEquipment(Warehouse):
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def to_warehouse(self):
        try:
            item_quantity = int(input(f'Введите количество добавленных товаров '))
            self.quantity += item_quantity
        except:
            return f'Ошибка ввода данных'

    def __str__(self):
        return f'На складе: {self.quantity} шт. {self.name}'

class Printer(OfficeEquipment):
    def __init__(self, name, quantity):
        super().__init__(name, quantity)
        self.colors = []

    def print(self):
        return f'{self.name}: available colors: {self.colors}'


class Scanner(OfficeEquipment):
    def __init__(self, name, quantity):
        super().__init__(name, quantity)
        self.formats = ['jpg', 'pdf', 'rtf']

    def scan(self):
        return f'{self.name}: available formats: {self.formats}'


class Xerox(OfficeEquipment):
    def __init__(self, name, quantity):
        super().__init__(name, quantity)

    def photocopy(self):
        return f'{self.name}: xerox temporarily unavailable'


new_printer = Printer('HP', 1)
new_printer.colors.append('blue')
new_printer.colors.append('black')
print(new_printer.print())
new_printer.to_warehouse()
print(new_printer)

new_scanner = Scanner('Canon', 10)
print(new_scanner.scan())
new_scanner.to_warehouse()
print(new_scanner)