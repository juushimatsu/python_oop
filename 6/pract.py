class Book:
    def __init__(self, title, author, pages):
        self.title = title 
        self._author = author  
        self.__pages = pages  

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def get_pages(self):
        return self.__pages

    def set_pages(self, pages):
        if pages > 0:
            self.__pages = pages
        else:
            raise ValueError("Количество страниц должно быть положительным числом")

    def display_info(self):
        return f"Название: '{self.title}', Автор: {self._author}, Страниц: {self.__pages}"

book1 = Book("йуайцуайуа", "прцуцкй3у", 352)

print(book1.title)
book1.title = "уайацыацыуаыа"

print(book1.get_author())  
book1.set_author("апранкенн")

print(book1.get_pages())  
book1.set_pages(352)

print(book1.display_info())

try:
    book1.set_pages(-10) 
except ValueError as e:
    print(e) 
