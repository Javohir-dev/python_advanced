import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}


# Dump(s) | dumps for string, dump for file
# personJSON = json.dumps(person)
# personJSON = json.dumps(person, indent=4, separators=(";", "="))
personJSON = json.dumps(person, indent=4, sort_keys=True)

print(person)
# print(personJSON)


# with open("person.json", "w") as file:
#     json.dump(person, file, indent=4, sort_keys=True)

# With load(s) | loads for string, load for file
# person = json.loads(personJSON)
# print(person)

# # with load
# with open("person.json", "r") as file:
#     person = json.load(file)
#     print(person)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)

def encode_person(obj):
    if isinstance(obj, Person):
        return {"name": obj.name, "age": obj.age, obj.__class__.__name__: True}
    else:
        raise TypeError("Object of type Person expected")

new_person = json.dumps(person, default=encode_person)
# print(new_person)

# We can also ovverride the JSONEncoder class
from json import JSONEncoder

class PersonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age, obj.__class__.__name__: True}
        return JSONEncoder.default(self, obj)
    

# Both works well
second_person = json.dumps(person, cls=PersonEncoder)
third_person = PersonEncoder().encode(person)

# print(second_person)
# print(third_person)

# Decoding

other_person = json.loads(third_person)
print(third_person)  # {"name": "John", "age": 30, "Person": true}
print(other_person)  # {'name': 'John', 'age': 30, 'Person': True}

def decode_person(dic):
    if Person.__name__ in dic:
        return Person(name=dic['name'], age=dic['age'])
    return dic

final_person = json.loads(third_person, object_hook=decode_person)
print(final_person)  # <__main__.Person object at 0x...>
print(final_person.name)  # John
print(final_person.age)   # 30
