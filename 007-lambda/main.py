# Regular Function
def add10(x):
    return x + 10

result = add10(5)
print(result)  # Output: 15

# With Lambda Functions
add10 = lambda  x: x + 10
result2 = add10(5)
print(result2)  # Output: 15

something = [(1, 2), (20, 16), (-1, 6), (15, 1)]
something_sorted = sorted(something)  # default tuple ichidagi birinchisiga qaravotti
print(something)
print(something_sorted)

something_sorted_by_second = sorted(something, key=lambda x: x[1])
print(something_sorted_by_second)  # bunda esa ikkinchisiga qaraydi

something_sorted_by_sum = sorted(something, key=lambda x: x[0] + x[1])
print(something_sorted_by_sum)  # bunda esa yig'indisiga qaraydi

# Lambda with map
numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x*2, numbers))  # map har bir elementga lambda funksiyasini qo'llaydi va natijani qaytaradi
print(squared_numbers)  # Output: [2, 4, 6, 8, 10]

# with for loop
with_for = [x*2 for x in numbers]
print(with_for)  # Output: [2, 4, 6, 8, 10]

# Lambda with filter
numbers += [6, 7]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # filter faqat lambda funksiyasi True qaytargan elementlarni oladi
print(even_numbers)  # Output: [2, 4, 6]

# with for loop
with_for_filter = [x for x in numbers if x % 2 == 0]
print(with_for_filter)  # Output: [2, 4, 6]

# Lambda with reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)  # reduce ro'yxatdagi barcha elementlarni ketma-ketlikda lambda funksiyasiga o'tkazadi va yakuniy natijani qaytaradi
print(product)  # Output: 120  ||  1×2×3×4×5=120

def times(x, y):
    return x * y