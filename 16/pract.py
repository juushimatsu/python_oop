class InfiniteRange:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        return self.start

infinite_range = InfiniteRange(0)

for i in infinite_range:
    print(i)
    if i >= 10: 
        break
