# String: immutable, text representation in Python
my_string = "        Hello, World!           "
print(my_string.strip())
print(my_string.lstrip())
print(my_string.rstrip())

my_string = my_string.strip()
print(my_string)

my_string = "HeLlO, WorlD!"
print(my_string.lower())
print(my_string.upper())
print(my_string.title())
my_string = my_string.lower()
print(my_string)
print(my_string.startswith("hello"))
print(my_string.endswith("world!"))

print(my_string.find("p"))
print(my_string.count("l"))

other_string = my_string.replace("world", "Univers")  # Agar topolmasa xato chiqmaydi shunchaki skip qiladi.
print(other_string.title())