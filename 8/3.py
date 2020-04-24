class IsList:
    def __init__(self):
        self.my_list = []

    def run(self):
        while True:
            try:
                val = int(input('Введите значение: '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Введено не число - оно не войдет в список")


test = IsList()
print(test.run())