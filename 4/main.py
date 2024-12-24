class LimitedInstances:
    _instances = []
    max_instances = 5

    def __new__(cls, *args, **kwargs):
        """Переопределение метода __new__, чтобы контролировать количество объектов."""
        if len(cls._instances) < cls.max_instances:
            instance = super().__new__(cls)
            cls._instances.append(instance)
            return instance
        else:
            return cls._instances[-1] 

obj1 = LimitedInstances()
obj2 = LimitedInstances()
obj3 = LimitedInstances()
obj4 = LimitedInstances()
obj5 = LimitedInstances()
obj6 = LimitedInstances()

print(obj1, obj2, obj3, obj4, obj5, obj6)

class Book:
    _books = []

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

        if any(book.title == title and book.author == author for book in self._books):
            raise ValueError(f"Book with title '{title}' by author '{author}' already exists.")
        else:
            self._books.append(self)

book1 = Book("1337", "jkhgeUH", 1949)
book2 = Book("  KL;WE", "WFEFl23", 1960)

try:
    book3 = Book("1337", "wrfwer3", 1949)
except ValueError as e:
    print(e)

print([f"{book.title} by {book.author} ({book.year})" for book in Book._books])
