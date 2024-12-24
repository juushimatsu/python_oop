class Model:
    def __init__(self):
        self._dict_ = {}
    
    def query(self, *args, **kwargs):
        for key, item in kwargs.items():
            self._dict_[key] = item
    
    def __str__(self):
        result = [f"{key} = {item}" for key, item in self._dict_.items()]
        return "Model: " + ", ".join(result)
    
    def __len__(self):
        return len(self._dict_)

model = Model()

model.query(name="John", age=30, occupation="Engineer")

print(model) 

print(len(model))
