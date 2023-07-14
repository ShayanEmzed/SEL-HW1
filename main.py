import string
import random


letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation[:len(string.punctuation) // 3]

pwd_len = 6
alphabet = letters + digits + special_chars

pwd = ''
for _ in range(pwd_len):
    pwd += random.choice(alphabet)

print(pwd)
