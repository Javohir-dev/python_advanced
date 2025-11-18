import random as r

a = r.random()  # Generates a random float between 0.0 and 1.0
print(a)

b = r.uniform(1, 10)  # Generates a random float between 1 and 10
print(b)

c = r.randint(1, 10)  # Generates a random integer between 1 and 10
print(c)

d = r.randrange(1, 10)  # Generates a random odd integer between 1 and 10
print(d)

e = r.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # Randomly selects an element from the list
print(e)

f = r.choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k=3)  # Elementlari takrorlanishi mumkin bo'lgan 3 ta elementni tanlaydi
print(f)

f2 = r.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3)  # Elementlari takrorlanmaydigan 3 ta elementni tanlaydi
print(f2)

g = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
r.shuffle(g)  # Listni tasodifiy tartibda aralashtiradi
print(g)

r.seed(1)
print(r.random())  # Har doim bir xil natijani beradi, chunki urug' o'rnatilgan
print(r.randint(1, 10))

r.seed(2)
print(r.random())  # Har doim bir xil natijani beradi, chunki urug
print(r.randint(1, 10))

import secrets

# Generate a 32-byte (256-bit) secret key
secret_key = secrets.token_hex(32)
print(f"SECRET_KEY = '{secret_key}'")

# Alternative: URL-safe base64 encoded key
secret_key_urlsafe = secrets.token_urlsafe(32)
print(f"SECRET_KEY = '{secret_key_urlsafe}'")

# import secrets as s

# h = s.randbelow(10)  # 0 dan 9 gacha bo'lgan tasodifiy butun sonni generatsiya qiladi
# print(h)

# import numpy as np

# i = np.random.rand(3)  # 3 ta tasodifiy float sonlardan iborat massiv yaratadi
# print(i)

# num = np.random.randint(0, 10, (3, 4))  # 3x4 o'lchamdagi tasodifiy butun sonlardan iborat massiv yaratadi
# print(num)

