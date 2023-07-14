import string
import random


letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation[:random.randint(len(string.punctuation) // 3, 50)]

pwd_len = 16
alphabet = letters + digits + special_chars

pwd = ''
for _ in range(pwd_len):
    pwd += random.choice(alphabet)

print(pwd)
