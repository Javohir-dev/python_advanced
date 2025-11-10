# Don't use this for tutorials, only for testing collections module
from collections import Counter, defaultdict

text = "aaabbbcc"
my_counter = Counter(text)
print(my_counter)  # Output: Counter({'a': 3, 'b': 3, 'c': 2})
print(my_counter.keys())  # Output: dict_keys(['a', 'b', 'c'])
print(my_counter.values())  # Output: dict_values([3, 3, 2])

print(my_counter.most_common(1))  # Output: [('a', 3)]
print(my_counter.most_common(1)[0])  # Output: ('a', 3)
print(my_counter.most_common(1)[0][0])  # Output: 'a'
print(my_counter.most_common(1)[0][1])  # Output: 3

print(list(my_counter.elements()))

a = {}
# print(a['c'], "aa") # KeyError

b = defaultdict(int)
print(b['c'], "bb")  # Output: 0