from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self):
        self.name = ' '

    @abstractmethod
    def cloth_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def cloth_consumption(self):
        return self.v/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def cloth_consumption(self):
        return 2*self.h + 0.3


new_coat = Coat(40)
new_suit = Suit(1.70)

print(new_coat.cloth_consumption)
print(new_suit.cloth_consumption)
