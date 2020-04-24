class DivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend = int(input("Enter dividend: "))
divider = int(input("Enter divider: "))

try:
    if divider == 0:
        raise DivisionByZero("Division by zero")
except ValueError:
    print("Вы ввели не число")
except DivisionByZero as err:
    print(err)
else:
    print(f"Quotient: {dividend/divider}")