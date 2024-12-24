class Book:
    def __init__(self, title, author, publisher, year) -> None:
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

    def __hash__(self) -> int:
        return hash((self.title, self.author, self.publisher))

    def __eq__(self, other: "Book") -> bool:
        if isinstance(other, Book):
            return self.__hash__() == other.__hash__()
        return False

book1 = Book("Book Title", "Author Name", "Publisher Name", 2020)
book2 = Book("Book Title", "Author Name", "Publisher Name", 2021)
book3 = Book("Another Title", "Another Author", "Another Publisher", 2020)

book_set = {book1, book2, book3}

print(book_set)
