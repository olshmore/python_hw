class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}i + {self.b}'

    def __add__(self, other):
        return f'{self.a + other.a}i + {self.b + other.b}'

    def __mul__(self, other):
        return f'{self.a * other.a - self.b * other.b}i + {self.b * other.a + self.a * other.b}'


z1 = Complex(2, 2)
z2 = Complex(5, 7)

print(f'({z1}) + ({z2}) = ({z1 + z2})')
print(f'({z1}) * ({z2}) = ({z1 * z2})')
