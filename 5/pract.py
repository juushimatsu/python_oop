import re
from string import ascii_uppercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_uppercase + digits

    @staticmethod
    def check_card_number(number):
        pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
        return bool(re.match(pattern, number))

    @classmethod
    def check_name(cls, name):
        words = name.split()
        if len(words) != 2:
            return False
        first_name, last_name = words
        return all(char in cls.CHARS_FOR_NAME for char in first_name) and \
               all(char in cls.CHARS_FOR_NAME for char in last_name)

card_number = "1234-5678-9101-1121"
name = "BEBE"

print(CardCheck.check_card_number(card_number))
print(CardCheck.check_name(name)) 

invalid_card_number = "12345-6789-1011-121"
invalid_name = "BEBE"

print(CardCheck.check_card_number(invalid_card_number)) 
print(CardCheck.check_name(invalid_name)) 
