class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal speaks")
    
    def __del__(self):
        print("Animal deleted")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("The dog barks")
    
    def __del__(self):
        super().__del__()
        print("Dog deleted")
