myset = {1, 2, 1, 4, 1}
print(myset)

myset = set([1, 2, 3, 4, 5, 5])
print(myset)

myset = set("Hello")
print(myset)

wrongset = {}
print(type(wrongset))  # <class 'dict'>

myset = set()
print(type(myset))  # <class 'set'>

myset.add(1)
myset.add(2)
myset.add(3)
print(myset)
print(len(myset))

myset.remove(2)  # Raises KeyError if 2 is not found
print(myset)

myset.discard(4)  # Does not raise an error if 4 is not found
print(myset)

print(myset.pop())  # Removes and returns an arbitrary element
print(myset)

if 3 in myset:
    print("Yes")
else:
    print("No")

adds = {1, 2, 3, 4, 5, 6}
events = {6, 7, 8, 9, 0}
union_set = adds.union(events)
print(union_set)  # {4, 5, 6, 7, 8}
print(adds.intersection(events))  # {6}

difference_set = adds.difference(events)
print(difference_set)  # {4, 5}

symmetric_difference_set = adds.symmetric_difference(events)
print(symmetric_difference_set)  # {0, 1, 2, 3, 4, 5, 7, 8, 9}

adds.update(events)
print(adds)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

adds = {1, 2, 3, 4, 5, 6}
events = {6, 7, 8, 9, 0}
adds.intersection_update(events)
print(adds)  # {6}

