from time import sleep
from itertools import cycle


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        for color in cycle(self.__color):
            if color == 'red':
                print('red')
                sleep(7)
            elif color == 'yellow':
                print('yellow')
                sleep(2)
            elif color == 'green':
                print('green')
                sleep(7)


traffic_light = TrafficLight()
traffic_light.running()
