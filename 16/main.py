class FibonacciIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max_value:
            raise StopIteration
        fib = self.a
        self.a, self.b = self.b, self.a + self.b
        return fib

fib_iterator = FibonacciIterator(100)
for num in fib_iterator:
    print(num)

class MultipleIterator:
    def __init__(self, number):
        self.number = number
        self.current = number

    def __iter__(self):
        return self

    def __next__(self):
        multiple = self.current
        self.current += self.number
        return multiple

multiples_of_5 = MultipleIterator(5)
for i in multiples_of_5:
    print(i)
    if i > 50: 
        break
