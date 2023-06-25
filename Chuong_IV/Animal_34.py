class Animal:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name

class CanSwim:
    def swim(self):
        print("The animal can swim.")

class CanFly:
    def fly(self):
        print("The animal can fly.")

class Duck(Animal, CanSwim, CanFly):
    def quack(self):
        print("Quack!")

duck = Duck("Donald")
duck.swim()
duck.fly()
print(duck.getName() + " is an animal.")