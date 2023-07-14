import string
import random


letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation[:random.randint(len(string.punctuation) // 3, len(string.punctuation))]

pwd_len = input('Enter passwrod lenght: ')
pwd_len = int(pwd_len) if pwd_len != '' else 6
alphabet = letters + digits + special_chars

pwd = ''
for _ in range(pwd_len):
    pwd += random.choice(alphabet)

print(pwd)
