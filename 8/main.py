class Product:
    _id = 0  

    def __new__(cls, *args, **kwargs):
        cls._id += 1  
        obj = super().__new__(cls)
        obj.id = cls._id 
        return obj

    def __init__(self, name: str, weight: float, price: float):
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, name: str, value) -> None:
        type_dict = {
            "id": int,
            "name": str,
            "weight": (int, float),
            "price": (int, float),
        }
        if name in type_dict and not isinstance(value, type_dict[name]):
            raise TypeError(f"Неверный тип присваиваемых данных для {name}")
        if name == "weight" and not value > 0:
            raise TypeError("Вес товара должен быть положительным числом.")
        if name == "price" and not value > 0:
            raise TypeError("Цена товара должна быть положительным числом.")
        super().__setattr__(name, value)

    def __delattr__(self, name: str) -> None:
        if name == "id":
            raise AttributeError("Атрибут 'id' нельзя удалить.")
        super().__delattr__(name)


class Shop:
    def __init__(self):
        self.goods = {}

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product.")
        self.goods[product.id] = product

    def remove_product(self, product_id):
        if product_id in self.goods:
            del self.goods[product_id]

    def display_goods(self):
        return [f"ID: {prod.id}, Название: {prod.name}, Вес: {prod.weight}, Цена: {prod.price}"
                for prod in self.goods.values()]

class Library:
    def __init__(self, name, max_books):
        self._name = name 
        self._max_books = max_books 
        self.books = []

    def __setattr__(self, name, value):
        if name == "_max_books" and hasattr(self, "_max_books"):
            raise AttributeError("Атрибут 'max_books' нельзя изменить после инициализации.")

        if name == "books" and len(value) > self._max_books:
            raise ValueError("Количество книг превышает допустимый максимум.")

        super().__setattr__(name, value)

    def __getattribute__(self, name):
        print(f"Доступ к атрибуту '{name}'")
        return super().__getattribute__(name)

    def __getattr__(self, name):
        return f"Атрибут '{name}' не найден."

    def __delattr__(self, name):
        if name == "name":
            raise AttributeError("Атрибут 'name' удалять запрещено.")
        print(f"Атрибут '{name}' удалён.")
        super().__delattr__(name)

    def add_book(self, book):
        if len(self.books) < self._max_books:
            self.books.append(book)
        else:
            raise ValueError("Невозможно добавить книгу: превышен лимит.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def list_books(self):
        return self.books


shop = Shop()
product1 = Product(name="Яблоки", weight=1.5, price=100)
product2 = Product(name="Бананы", weight=1.2, price=120)

shop.add_product(product1)
shop.add_product(product2)

print("Товары в магазине:")
print("\n".join(shop.display_goods()))

shop.remove_product(product1.id)
print("\nПосле удаления:")
print("\n".join(shop.display_goods()))

library = Library(name="Городская библиотека", max_books=3)
library.add_book("Мастер и Маргарита")
library.add_book("Война и мир")
print("\nКниги в библиотеке:")
print(library.list_books())

try:
    library.add_book("Преступление и наказание")
    library.add_book("Три товарища")  
except ValueError as e:
    print(f"Ошибка: {e}")

library.remove_book("Война и мир")
print("\nПосле удаления книги:")
print(library.list_books())
