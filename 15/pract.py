class List:
    def __init__(self, *data):
        self._data = list(data)

    def __getitem__(self, index):
        if index >= len(self._data):
            return self._data[-1]
        return self._data[index]

    def __setitem__(self, index, value):
        if index >= len(self._data):
            self._data[-1] = value
        else:
            self._data[index] = value

    def __delitem__(self, index):
        if index >= len(self._data):
            del self._data[-1]
        else:
            del self._data[index]

    def __repr__(self):
        return f"List({', '.join(map(str, self._data))})"

custom_list = List(1, 2, 3, 4, 5)

print(custom_list[2])
print(custom_list[10])

custom_list[2] = 10
print(custom_list)

custom_list[10] = 99
print(custom_list)

del custom_list[1]
print(custom_list)

del custom_list[10]
print(custom_list)
