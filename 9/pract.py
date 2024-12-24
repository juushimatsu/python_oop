class Handler:
    def __init__(self, methods=("GET",)):
        self.methods = set(methods)

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            if request["method"] not in self.methods:
                raise ValueError(f"Данная страница не принимает тип запроса '{request['method']}'")

            type_methods = {
                "GET": self.get,
                "POST": self.post,
            }

            return type_methods[request["method"]](func, request, *args, **kwargs)

        return wrapper

    def get(self, func, request, *args, **kwargs):
        return func(request, *args, **kwargs)

    def post(self, func, request, *args, **kwargs):
        return func(request, *args, **kwargs)

@Handler(methods=("POST",))
def get_page(request):
    return "Привет мир"


request = {
    "method": "POST",  
}

try:
    print(get_page(request))  
except ValueError as e:
    print(e)


request_invalid = {
    "method": "GET",  
}

try:
    print(get_page(request_invalid)) 
except ValueError as e:
    print(e)  
