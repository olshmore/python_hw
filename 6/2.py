class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass_count(self):
        return self._length * self._width * int(125)


new_road = Road(1000, 4)
print(new_road.mass_count())
