# Assert - shartni tekshirish uchun
x = 5
assert x >= 0, "x must be non-negative"


# ==================== TRY-EXCEPT ASOSLARI ====================

# 1. Bare except - hammasi exception ni ushlash (PEP 8 da tavsiya etilmaydi)
try:
    a = 5 / 0
except ZeroDivisionError:
    print("Error: ZeroDivisionError occurred. Division by zero is not allowed.")

# 2. Exception as e - xato haqida ma'lumot olish
try:
    a = 5 / 0
except Exception as e:
    print(f"Error: {e}")

# 3. Spesifik exception - faqat muayyan xatoni tutish
try:
    a = 5 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# 4. Bir nechta exceptions ni tutish
try:
    a = 5 / 1
    b = "string" + 5
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
except TypeError as e:
    print(f"TypeError: {e}")

# ==================== TRY-EXCEPT-ELSE-FINALLY ====================

# 5. Else va finally bilan
try:
    a = 5 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:  # Agar hech qanday xato bo'lmasa bajariladi
    print("Everything is fine, no exceptions occurred.")
finally:  # Doimo bajariladi (faylni yopish, resurs tozalash uchun)
    print("Execution of the try-except block is complete.")

# ==================== CUSTOM EXCEPTIONS ====================

# 6. Exception klassidan irsiy olish (oddiy)
class ValueTooHighError(Exception):
    pass

# 7. Custom exception bilan __init__ va __str__ metodlari
class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
        super().__init__(message)

    def __str__(self):
        return f"{self.message}: {self.value}"

def check_value(x):
    """Qiymatni tekshiradi va muvofiqligi bo'yicha exception ko'tarad."""
    if x > 100:
        raise ValueTooHighError("Value is too high!")
    elif x < 0:
        raise ValueTooLowError("Value is too low!", x)
    else:
        print("Value is within the acceptable range.")

# Custom exceptions ni tutish
try:
    check_value(-90)
except (ValueTooHighError, ValueTooLowError) as e:
    print(f"Custom exception caught: {e}")