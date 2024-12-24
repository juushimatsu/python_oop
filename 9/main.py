class Power:
    def __init__(self, n):
        self.n = n
    
    def __call__(self, x):
        return x ** self.n

power_of_2 = Power(2)  
print(power_of_2(3)) 

class Repeat:
    def __init__(self, times):
        self.times = times

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.times):
                func(*args, **kwargs)
        return wrapper

@Repeat(3) 
def greet(name):
    print(f"Привет, {name}!")

greet("Иван")  
