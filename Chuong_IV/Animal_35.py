class Animal:
    def make_sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def make_sound(self):
        print("The dog barks.")

animal = Animal()
animal.make_sound()

dog = Dog()
dog.make_sound()