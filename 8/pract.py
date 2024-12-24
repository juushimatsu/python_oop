class Product:
    __id = 0

    def __new__(cls, *args, **kwargs):
        cls.__id += 1
        obj = super().__new__(cls)
        obj.id = cls.__id
        return obj

    def __init__(self, name: str, weight: float, price: float):
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, name: str, value):
        type_dict = {
            "id": int,
            "name": str,
            "weight": (int, float),
            "price": (int, float),
        }
        if name in type_dict:
            if not isinstance(value, type_dict[name]):
                raise TypeError(f"Неверный тип данных для '{name}'.")
        if name == "weight" and not value > 0:
            raise ValueError("Вес должен быть положительным числом.")
        if name == "price" and not value > 0:
            raise ValueError("Цена должна быть положительным числом.")
        super().__setattr__(name, value)

    def __delattr__(self, name: str):
        if name == "id":
            raise AttributeError("Атрибут 'id' удалять запрещено.")
        super().__delattr__(name)


class Shop:
    def __init__(self):
        self.goods = []

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product.")
        self.goods.append(product)

    def remove_product(self, product: Product):
        if product in self.goods:
            self.goods.remove(product)

    def display_goods(self):
        return [f"{prod.id}: {prod.name}, Вес: {prod.weight}, Цена: {prod.price}" for prod in self.goods]


shop = Shop()

product1 = Product(name="Яблоки", weight=1.5, price=100)
product2 = Product(name="Бананы", weight=1.2, price=120)

shop.add_product(product1)
shop.add_product(product2)

print("Товары в магазине:")
print("\n".join(shop.display_goods())) 

shop.remove_product(product1)

print("\nПосле удаления:")
print("\n".join(shop.display_goods())) 