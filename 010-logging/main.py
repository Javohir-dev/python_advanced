import logging

"""
level=logging.DEBUG dagi DEBUG eng kam darajadagi loglarni ham yozib oladi, agar siz darajani WARNING qilsangiz, faqat WARNING, ERROR va CRITICAL darajadagi loglar yozib olinadi.
format uchun: https://docs.python.org/3/library/logging.html#logrecord-attributes
DateTime formatlari uchun (datefmt='%d-%m-%Y %H:%M:%S') ni ishlatish mumkin.
FilePath ni olish uchun %(pathname)s ni ishlatish mumkin.
Agar ustiga bosib aynan kerakli line ga bormoqchi bo'lsangiz [%(pathname)s:%(lineno)s] ko'rinishida ishlatish kerak.
Agar Am/PM ko'rinishida vaqt kerak bo'lsa, datefmt='%d-%m-%Y %H:%M:%S %p' ni ishlatish kerak.

"""
# logging.basicConfig(filename='app.log',
#                     encoding='utf-8',
#                     level=logging.INFO,
#                     datefmt='%d-%m-%Y %H:%M:%S',
#                     format='%(asctime)s: (%(filename)s - %(lineno)s): %(levelname)s ? %(message)s')
logging.basicConfig(filename='app.log',
                    encoding='utf-8',
                    level=logging.INFO,
                    datefmt='%d-%m-%Y %H:%M:%S %p',
                    format='%(asctime)s: [%(pathname)s:%(lineno)s]: %(levelname)s ? %(message)s')

# 5 levels of logging
# logging.debug("This is a debug message.")
# logging.info("This is an info message.")
# logging.warning("This is a warning message.")   
# logging.error("This is an error message.")
# logging.critical("This is a critical message.")

x: int = 10 + 5

logging.info(f"The value of x is {x}")

print("Logging complete.")


print("This is a very bad method")