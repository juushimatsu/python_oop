class ShoppingCart:
    def __init__(self):
        self.items = [] 
    
    def __len__(self):
        return len(self.items)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"Book(title={self.title}, author={self.author}, pages={self.pages})"
    
    def __repr__(self):
        return f"Book(title: str, author: str, pages: int)"
    
    def __len__(self):
        return self.pages

cart = ShoppingCart()
cart.items.append(Book("1991", "qefqefg", 36781))
cart.items.append(Book("1234", "egeqqw", 123))

print(f"Количество товаров в корзине: {len(cart)}")  

book = cart.items[0]
print(book) 

print(repr(book))

print(f"Количество страниц в книге: {len(book)}")
