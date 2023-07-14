import string
import random


letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

pwd_len = int(input('Enter passwrod lenght: '))
alphabet = letters + digits + special_chars

pwd = ''
for _ in range(pwd_len):
    pwd += random.choice(alphabet)

print(pwd)
