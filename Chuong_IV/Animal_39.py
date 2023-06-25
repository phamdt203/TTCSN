class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal speaks.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("The dog barks")

dog = Dog("Fido")
dog.speak()
animal = Animal("Generic animal")
animal.speak()