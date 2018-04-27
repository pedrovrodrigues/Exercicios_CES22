import abc
from math import pi
class Circle():
    __metaclass__ = abc.ABCMeta

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def isRound(cls):
        return True

    @staticmethod
    def perimeter_over_diameter:
        return pi

    @abc.abstractmethod
    def price(self):
        return self.perimeter_over_diameter*self.radius**2

class Coin(Circle):
    def __init__(self, radius, value):
        self.radius = radius
        self.value = value

    def price(self):
        return self.value + super(Coin,self).price()