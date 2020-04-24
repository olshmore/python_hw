class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is going'

    def stop(self):
        return 'stoped'

    def turn(self, direction):
        return f'{self.name} turned ' + direction

    def show_speed(self):
        return f'Speed of {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Speed of town car {self.name} is {self.speed}')
        if self.speed > 60:
            return f'{self.name}: SPEED LIMIT EXCEEDED'


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Speed of town car {self.name} is {self.speed}')
        if self.speed > 40:
            return f'{self.name}: SPEED LIMIT EXCEEDED'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def acab(self):
        if self.is_police:
            return 'oops cops are here'


volvo = TownCar(80, 'White', 'Volvo', False)
lamborghini = SportCar(300, 'Black', 'Lamborghini', False)
ford = WorkCar(70, 'Red', 'Ford', False)
nine = PoliceCar(110, 'Blue', 'Lada', True)

print(volvo.go())
print(volvo.turn(direction='left'))
print(volvo.show_speed())
print(lamborghini.go(), lamborghini.show_speed())
print(nine.acab())
