class Car:
    def __init__(self, make, model, year):
        self.make = make    # public attribute
        self._model = model # protected attribute
        self.__year = year  # private attribute
    def start(self):
        print("Car started.") # public method
    
    def _stop(self):
        print("Car stopped") # protected method
    
    def __drive(self):
        print("Car driving") # private method

car = Car("Toyota", "Camry", 2021)

print(car.make)   # Output : Toyota
print(car._model) # Output : Camry
# print(car.__year) # Error : 'Car' object has no attribute '__year'

car.start()    # Output : Car started.
car._stop()    # Output : Car stopped.
# car.__drive()  # Error : 'Car'object has no attribute '__drive'
