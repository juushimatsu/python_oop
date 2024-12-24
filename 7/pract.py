class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Баланс не может быть отрицательным.")
        self._balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма депозита должна быть положительной.")
        self.balance += amount
        
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно средств.")
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        self.balance -= amount

    def display_balance(self):
        return f"Текущий баланс: {self.balance} руб."

try:
    account = BankAccount(1000)

    print(account.display_balance())

    account.deposit(500)
    print(account.display_balance())

    account.withdraw(300)
    print(account.display_balance())

    account.withdraw(2000)
except ValueError as e:
    print(e)

try:
    account.deposit(-100) 
except ValueError as e:
    print(e)

try:
    account.balance = -500 
except ValueError as e:
    print(e)
