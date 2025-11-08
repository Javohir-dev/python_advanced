mylist = ["Banana", "Orange", "Kiwi"]
# print(mylist)

mylist.append("Mango")
# print(mylist)

mylist.insert(1, "Apple")
# print(mylist)

# poped_item = mylist.pop()
# print(poped_item)
# print(mylist)

# mylist.remove("Orange")
# print(mylist)

# mylist.clear()
# print(mylist)

mylist.reverse()
# print(mylist)

mylist = [3, 1, 4, 2, -5, 0, 10, 7]
# print(f"{mylist=}")

# mylist.sort()
newlist = sorted(mylist)
# print(f"{mylist=}")
# print(f"{newlist=}")

verynewlist = [0] * 5
# print(f"{verynewlist=}")

first = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
second = list(range(1, 11))
third = [n for n in range(1, 11)]

# print(f"{first=}")
# print(f"{second=}")
# print(f"{third=}")

a = first[1:5]
# print(f"{a=}")

b = first[:5]
# print(f"{b=}")

c = first[5:]
# print(f"{c=}")

d = first[::2]
# print(f"{d=}")

e = first[::-1]
# print(f"{e=}")

list_org = ["banana", "apple", "orange"]

list_copy = list_org[:]
list_copy.append("kiwi")

# print(f"{list_org=}")
# print(f"{list_copy=}")

list_copy2 = list_org.copy()
list_copy2.append("mango")
# print(f"{list_org=}")
# print(f"{list_copy2=}")

wlist = list(range(20))
w = [n*n for n in wlist]

print(f"{wlist=}")
print(f"{w=}")