class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')

person = Person("Hung", 20)
person.greet() # Hello, my name is Hung and I am 20 years old.