import re

class UserSchem:
    pass

class DataBase:
    users = []

    def get_data(self, url):
        with open(url, 'r', encoding='UTF-8') as f:
            result = f.readlines()
        return result

    def serializers(self, data):
        content = []
        for line in data:
            schema = {}
            line = [i for i in re.split(r'\s+', line) if i != '']
            for index in range(0, len(line)-1, 2):
                schema[line[index]] = line[index + 1]
            content.append(schema)
        return content

    def create_user(self, data):
        for i in data:
            user = UserSchem()
            for key, item in i.items():
                setattr(user, key, item)
            self.users.append(user)

    def search(self, **kwargs):
        for user in self.users:
            match = True
            for key, value in kwargs.items():
                if getattr(user, key, None) != value:
                    match = False
                    break
            if match:
                return user 
        return None 

class Translator:
    tr = {}

    def add(self, eng, rus):
        if eng not in self.tr:
            self.tr[eng] = [rus]
        else:
            if rus not in self.tr[eng]:
                self.tr[eng].append(rus)

    def remove(self, eng):
        if eng in self.tr:
            del self.tr[eng]

    def translate(self, eng):
        if eng in self.tr:
            return self.tr[eng][0] 
        return None

url = 'data.txt'

db = DataBase()

data = db.get_data(url)

serialized_data = db.serializers(data)

db.create_user(serialized_data)

user = db.search(id='1')
if user:
    print(f"Found user: ID: {user.id}, Name: {user.name}, Age: {user.age}")
else:
    print("User not found")

translator = Translator()
translator.add('hello', 'привет')
translator.add('world', 'мир')
translator.add('hello', 'здравствуй')

print(translator.translate('hello'))
translator.remove('world')
print(translator.tr)
