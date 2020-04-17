class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки. У вас в руках {self.title}'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки. У вас в руках {self.title}'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки. У вас в руках {self.title}'


pen = Pen('ручка')
print(pen.draw())
pencil = Pencil('карандаш')
print(pencil.draw())
handle = Handle('маркер')
print(handle.draw())
