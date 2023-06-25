class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __del__(self):
        print("Object is deleted")

person = Person("Hung", 20)
del Person