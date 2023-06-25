class Person:
    # Khoi tao thuoc tinh
    sound = "voice"

    # Phuong thuc khoi tao
    def __init__(self, name , age, phone, email):
        self.Name = name
        self.Age = age
        self._Phone = phone
        self.__Email = email
    # Khoi tao phuong thuc
    def Sleep(self):
        print(self.Name + " sleeping")
    def Confirm(self):
        print("People communicate with each other by " + self.sound)

# Khoi tao doi tuong
Student  = Person("John", 20, "123456789", "john@example.com")

# Goi phuong thuc Sleep va Confirm cua doi tuong Student
Student.Sleep()
Student.Confirm()