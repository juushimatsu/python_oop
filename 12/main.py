class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages == other.pages

    def __ne__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages != other.pages

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages

    def __gt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages > other.pages

    def __le__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages <= other.pages

    def __ge__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages >= other.pages

    def __str__(self):
        return f"Book title: {self.title}, Pages: {self.pages}"


book1 = Book("egfwg", 111)
book2 = Book("weqeqw3", 111)

print(book1 == book2)
print(book1 != book2)
print(book1 < book2)
print(book1 > book2)
print(book1 <= book2)
print(book1 >= book2)

print(book1)
