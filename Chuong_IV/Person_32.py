class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def say_hello(self):
        super().say_hello()
        print(f"I'm a student with ID {self.student_id}.")
    
person = Person("John", 30)
person.say_hello()

student = Student("Alice", 20, "12345")
student.say_hello()