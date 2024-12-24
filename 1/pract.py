class Human:
    height = None
    age = None
    name = None
    
human_one = Human()
human_two = Human()

print(human_one.age)
print(human_two.age)

human_one.age = 22
human_two.age = 27

human_one.height = 11
human_two.height = 11

print(human_one.age)
print(human_two.age)

delattr(human_one, 'height')
delattr(human_two, 'height')

print(hasattr(human_one, 'height'))
print(hasattr(human_two, 'height'))

human_two.name = "bebe"

print(human_one.name)