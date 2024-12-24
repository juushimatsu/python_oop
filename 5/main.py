class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32

    @classmethod
    def from_kelvin(cls, kelvin):
        celsius = kelvin - 273.15
        return cls(celsius)

    def __init__(self, celsius):
        self.celsius = celsius

    def __repr__(self):
        return f"{self.celsius:.2f}°C"

class Employee:
    @staticmethod
    def is_valid_age(age):
        return 18 <= age <= 65

    @classmethod
    def from_string(cls, data):
        name, age, position = map(str.strip, data.split(","))
        age = int(age)
        if not cls.is_valid_age(age):
            raise ValueError("Возраст сотрудника вне допустимого диапазона")
        return cls(name, age, position)

    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def get_details(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Должность: {self.position}"

kelvin_temperature = 300
converter = TemperatureConverter.from_kelvin(kelvin_temperature)
fahrenheit_temperature = TemperatureConverter.celsius_to_fahrenheit(converter.celsius)
print(f"Из {kelvin_temperature} К в Цельсиях: {converter}")
print(f"Из {converter.celsius:.2f}°C в Фаренгейты: {fahrenheit_temperature:.2f}°F")

employee_data = "Иван, 30, Менеджер"
employee = Employee.from_string(employee_data)
print(employee.get_details())

invalid_employee_data = "Анна, 70, Директор"
try:
    invalid_employee = Employee.from_string(invalid_employee_data)
except ValueError as e:
    print(e)
