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

my_string = "one, two, three, four, five"
my_list = my_string.split(", ")
print(my_list)

new_string = ", ".join(my_list)
print(new_string)

from timeit import default_timer as timer

#  Bad 
start = timer()
my_list = ["O"] * 7000
# print(my_list)
my_string = ""
for item in my_list:
    my_string += item

# print(my_string)
end = timer()
print(f"Bad way took {end - start:2f} seconds")

# Good
start = timer()
my_list = ["O" * 7]
my_string = "".join(my_list)
# print(my_string)
end = timer()
print(f"Good way took {end - start:2f} seconds")

# %, .format(), f-String
name = "Tomy"
num = 3.14159265
print("Hello %d" % num)
print("Hello %f" % num)
print("Hello %.8f" % num)
print("Hello %s" % name)

print("Hello {}, Do you know about {}?".format(name, num))
print("Hello {}, Do you know about {:.2f}?".format(name, num))
print("Hello {}, Do you know about {:.8f}? {}".format(name, num, 1648542))

print(f"What's up {name}? Do you know about PI? This is value of the PI {num:.8f}")
