class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return self.quantity - other.quantity
        else:
            return 'Other cell is bigger then initial cell'

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def make_order(self, row):
        sell_string = ''
        for k in range(round(self.quantity / row)):
            for i in range(row):
                sell_string += '*'
            sell_string += '\n'
            x = k + 1
        for i in range(self.quantity - row * x):
            sell_string += '*'
        return sell_string


cell_7 = Cell(7)
cell_9 = Cell(9)
print(cell_7 + cell_9)
print(cell_7 - cell_9)
print(cell_7 * cell_9)
print(cell_7 / cell_9)

cell_12 = Cell(12)
print(cell_12.make_order(5))