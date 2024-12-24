from datetime import datetime

class Car:
    def __init__(self, model, year, mileage):
        self.model = model 
        self._year = year
        self.__mileage = mileage  

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self._year

    def set_year(self, year):
        current_year = datetime.now().year
        if 1886 <= year <= current_year:
            self._year = year
        else:
            raise ValueError(f"Год выпуска должен быть между 1886 и {current_year}")

    def get_mileage(self):
        return self.__mileage

    def set_mileage(self, mileage):
        if mileage >= 0:
            self.__mileage = mileage
        else:
            raise ValueError("Пробег не может быть отрицательным")

    def display_info(self):
        return f"Модель: {self.model}, Год выпуска: {self._year}, Пробег: {self.__mileage} км"

try:
    car1 = Car("Toyota Camry", 2020, 15000)

    print(car1.get_model()) 
    car1.set_model("Toyota Corolla")
    print(car1.get_model()) 

    print(car1.get_year()) 
    car1.set_year(2018)
    print(car1.get_year())

    print(car1.get_mileage())
    car1.set_mileage(20000)
    print(car1.get_mileage()) 
    
    print(car1.display_info()) 

    car1.set_year(1800) 
except ValueError as e:
    print(e)

try:
    car1.set_mileage(-500) 
except ValueError as e:
    print(e)
