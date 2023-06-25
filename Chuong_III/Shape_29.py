from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

Hinh = Rectangle(int(input("Nhap vao chieu rong cua hinh chu nhat : ")), 
                 int(input("Nhap vao chieu dai cua hinh chu nhat : ")))
print("Dien tich cua hinh chu nhat la ", Hinh.area())