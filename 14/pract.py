class Man:
    def __init__(self, balance: int, credit: int) -> None:
        self.balance = balance
        self.credit = credit

    def __bool__(self):
        return self.balance > 0 and self.credit > 0

man1 = Man(100, 50)
man2 = Man(-100, 50)
man3 = Man(100, -50)
man4 = Man(-100, -50)

print(bool(man1))
print(bool(man2))
print(bool(man3))
print(bool(man4))
