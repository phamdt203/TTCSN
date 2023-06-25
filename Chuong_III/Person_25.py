class Person:
    def __init__(self):
        self.__age = 20

    def showAge(self):
        print(self.__age)
    
    def setAge(self, age):
        self.__age = age
    
Thi = Person()
print("Age of Thi :", end = '')
Thi.showAge()
Thi.__age = 99
print("Age of Thi after Thi.__age = 99 : ", end = '')
Thi.showAge()
Thi.setAge(99)
print("Age of Thi after Thi.setAge(99) : ", end = '')
Thi.showAge()