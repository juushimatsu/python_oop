import re

class UserSchem:
    pass

class DataBase:
    def get_data(self, url):
        with open(url, 'r', encoding='UTF-8') as f:
            result = f.readlines()
        return result

    def serializers(self, data):
        content = []
        for line in data:
            schema = {}
            # Разделяем строку по пробелам и создаем словарь с атрибутами
            line = [i for i in re.split(r'\s+', line) if i != '']
            for index in range(0, len(line)-1, 2):
                schema[line[index]] = line[index + 1]
            content.append(schema)
        return content

    def create_user(self, data):
        users = []
        for i in data:
            user = UserSchem()
            for key, item in i.items():
                setattr(user, key, item)
            users.append(user)
        return users

url = 'data.txt' 

db = DataBase()

data = db.get_data(url)

serialized_data = db.serializers(data)

users = db.create_user(serialized_data)

for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")
