from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def circumference(self):
        return 2 * (self.width + self.height)

shape1 = Rectangle(float(input("Chieu dai : ")), float(input("Chieu rong : ")))
shape1.circumference()