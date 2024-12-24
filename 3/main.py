class Node:
    def __init__(self, data=None):
        """Конструктор узла, который хранит данные и ссылку на следующий узел."""
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        """Инициализация пустого связанного списка."""
        self.start = None
        self.end = None

    def len(self):
        """Возвращает количество элементов в списке."""
        count = 0
        current = self.start
        while current:
            count += 1
            current = current.next
        return count

    def search(self, data):
        """Ищет узел с заданными данными и возвращает его."""
        current = self.start
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def append(self, obj):
        """Добавляет новый узел в конец списка."""
        new_node = Node(obj)
        if not self.start:
            self.start = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node

    def remove(self, index):
        """Удаляет узел по индексу."""
        if index < 0 or index >= self.len():
            print("Index out of range")
            return
        
        current = self.start
        if index == 0:
            self.start = current.next
            if not self.start:
                self.end = None
            return

        prev = None
        for i in range(index):
            prev = current
            current = current.next
        
        prev.next = current.next
        if current.next is None:
            self.end = prev

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print(f"Length: {ll.len()}")
node = ll.search(20)
if node:
    print(f"Found: {node.data}") 

ll.remove(1) 
print(f"Length after removal: {ll.len()}") 

node = ll.search(20)
if node:
    print(f"Found: {node.data}")
else:
    print("20 not found")
