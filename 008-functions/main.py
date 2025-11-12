from datetime import datetime

"""
https://youtu.be/mSoEjBpJUJ0?si=bEE8Yh5HfsD5bMir
1. Funksiya doim iloji boricha qisqa va aniq nomga ega bo'lishi kerak.
2. Funksiya nomi uning nima qilayotganini aniq ifoda etishi kerak.
3. Funksiya nima qaytarishini berib ketish kerak.
4. Funksiya nima ish bajarinishini tavsiflovchi docstring qo'shish kerak.
"""


#  Bad example
def get_time_in_current_users_locate():
    """
    Returns the current time in the user's local timezone formatted as 'YYYY-MM-DD HH:MM:SS'.
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# Good example
def get_time() -> str:
    """
    Returns the current local time formatted as 'YYYY-MM-DD HH:MM:SS'.

    Example:
    >>> get_time()
    '2024-06-01 12:34:56'  # Example output
    """
    now: datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return now

result = get_time()
print(type(result))
print(result)