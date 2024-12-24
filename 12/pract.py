class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade  

    def __eq__(self, other):
        return self.grade == other.grade

    def __ne__(self, other):
        return self.grade != other.grade

    def __lt__(self, other):
        return self.grade < other.grade

    def __gt__(self, other):
        return self.grade > other.grade

    def __le__(self, other):
        return self.grade <= other.grade

    def __ge__(self, other):
        return self.grade >= other.grade

student1 = Student("Дима", 85)
student2 = Student("Илья", 90)

print(student1 == student2)  
print(student1 != student2)  
print(student1 < student2)  
print(student1 > student2)  
print(student1 <= student2) 
print(student1 >= student2) 
