
class List(list):
    def __add__(self, other):
        self.append(other)
        return self

    def __sub__(self, other):
        if other in self:
            self.remove(other)
        return self

    def __mul__(self, other):
        if isinstance(other, int) and other > 0:
            return self[:len(self) // other] 
        return self

my_list = List([1, 2, 3, 4, 5])
print("Original list:", my_list)

my_list + 6
print("After adding 6:", my_list)

my_list - 2
print("After removing 2:", my_list)

new_list = my_list * 2
print("After dividing the list in 2 parts:", new_list)
