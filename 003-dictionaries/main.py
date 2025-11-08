mydict = {"name": "Alice", "age": 30, "city": "New York"}
print(mydict)

mytuple = (0, 1, 2, 3)
mydict = {mytuple: "tuple value"}
print(mydict)

# mylist = [0, 1, 2, 3]
# mydict = {mylist: "tuple value"}
# print(mydict)

mydict2 = {3: 6, 36: 9, 12: 15}
print(mydict2)

volue = mydict2[3]
print(volue)

mydict = dict(name="Alice", age=30, city="New York")
print(mydict)

value = mydict["name"]
print(value)

# Adding a new key-value pair
mydict["email"] = "Javohir.py@gmail.com"
print(mydict)

# Updating an existing key-value pair
mydict["email"] = "Javohir@gmail.com"
print(mydict)

# Deleting a key-value pair
del mydict["age"]
print(mydict)

mydict.pop("city")
print(mydict)

mydict.popitem()
print(mydict)

for key in mydict:
    print(key, mydict[key])

for key, value in mydict.items():
    print(key, value)

for key in mydict.keys():
    print(key, mydict[key])

for value in mydict.values():
    print(value)

# Copying a dictionary
newdict = mydict.copy()
print(newdict)

# Merging two dictionaries
anotherdict = {"name": "John", "country": "USA", "profession": "Engineer"}
mydict.update(anotherdict)
print(mydict)

