class Product:
    def __init__(self, name, price, discount=0):
        self.name = name
        self._price = price
        self._discount = discount

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self._price = value

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Скидка должна быть от 0% до 100%.")
        self._discount = value

    @property
    def price_with_discount(self):
        return self.price * (1 - self.discount / 100)


class Employee:
    def __init__(self, name, salary, age):
        self._name = name
        self._salary = salary
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Имя не может быть пустым.")
        self._name = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 30000:
            raise ValueError("Зарплата должна быть не менее 30 000.")
        self._salary = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self._age = value

    @age.deleter
    def age(self):
        self._age = None

    def apply_raise(self, raise_amount):
        if raise_amount <= 0:
            raise ValueError("Повышение должно быть положительным числом.")
        self.salary += raise_amount


product = Product("Телефон", 50000, 10)
print(f"Цена с учетом скидки: {product.price_with_discount} руб.")  # 45000.0
product.price = 55000
product.discount = 15
print(f"Обновленная цена с учетом скидки: {product.price_with_discount} руб.")  # 46750.0

# Employee
employee = Employee("Иван", 35000, 30)
print(f"Имя: {employee.name}, Зарплата: {employee.salary}, Возраст: {employee.age}")
employee.apply_raise(5000)
print(f"После повышения: Зарплата = {employee.salary}")
del employee.age
print(f"Возраст после удаления: {employee.age}")
