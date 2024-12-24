
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, year={self.year})"

class Library:
    def __init__(self):
        self.data = {} 

    def __add__(self, other):
        if not self.data.get(other.author):
            self.data[other.author] = [other] 
        else:
            self.data[other.author].append(other) 
        return self 

    def __sub__(self, other):
        if other.author not in self.data:
            return self 

        if other in self.data[other.author]:
            self.data[other.author].remove(other)  

        if not self.data[other.author]:
            del self.data[other.author]
        
        return self 

book1 = Book("thjs", "A45tyh", 1999)
book2 = Book("3e5thy", "jsthj", 2005)
book3 = Book("uksrt", "4rt6yj", 2010)

lib = Library()

lib + book1
lib + book2
lib + book3

print("Library after adding books:")
print(lib.data)

lib - book1
print("\nLibrary after removing 'Book One':")
print(lib.data)

lib - book2
print("\nLibrary after removing 'Book Two':")
print(lib.data)

lib - book3
print("\nLibrary after removing all books by 'Author A':")
print(lib.data)
