# Tuples
mytuple = ("John", 25, "Engineer")
print(mytuple)


mytuple = "John", 25, "Engineer"
print(mytuple)

mytuple = ("John",)  # Correct option
print(type(mytuple))  # Output: <class 'tuple'>

mytuple = ("John")  # This is a string, not a tuple
print(type(mytuple))  # Output: <class 'str'>

mylist = ["John", 25, "Engineer"]
mytuple = tuple(mylist)
print(mytuple) # Output: ('John', 25, 'Engineer')

# Getting item in a tuple is the same as in a list
print(mytuple[0])  # Output: John
print(mytuple[1])  # Output: 25
print(mytuple[2])  # Output: Engineer
print(mytuple[-1])  # Output: Engineer
# print(mytuple[3])  # Out of range ERROR 


# mytuple[0] = "Doe"  # ERROR: 'tuple' object does not support item assignment
# Tuples are immutable, so we cannot change their content

#  Methods
mytuple = ("John", 25, "Engineer", "John", 30)
print(len(mytuple))  # Output: 5
print(mytuple.count("John"))  # Output: 2
print(mytuple.index(25))  # Output: 1
# print(mytuple.index(32))  # ERROR: 32 is not in tuple
# Be careful guys
if 32 in mytuple:
    print(mytuple.index(32))
else:
    print("32 is not in tuple")

# If you want to add something to a tuple do this:
mytuple = mytuple + ("New Element",)
print(mytuple)

# If you want to change something to a tuple do this:
mylist = list(mytuple)
mylist[0] = "Doe"
mytuple = tuple(mylist)
print(mytuple)

numtuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numtuple[2:5])  # Output: (3, 4, 5)
print(numtuple[:4])   # Output: (1, 2, 3,
print(numtuple[6:])   # Output: (7, 8, 9, 10)
print(numtuple[::2])  # Output: (1, 3, 5, 7, 9)
print(numtuple[::-1]) # Output: (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

# Unpacking
person = ("Alice", 30, "Doctor")
name, age, profession = person
print(f"Name: {name}, Age: {age}, Profession: {profession}")

a, *b, c = numtuple  # You can use another variable name, if you want
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4, 5, 6, 7, 8, 9]
print(c)  # Output: 10


# For big data
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print("List size: ", sys.getsizeof(my_list), "bytes")
print("Tuple size:", sys.getsizeof(my_tuple), "bytes")

import timeit

tuple(my_list)

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))