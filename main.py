import string
import random


letters = string.ascii_letters
pwd_len = 6

alphabet = letters
pwd = ''

for _ in range(pwd_len):
    pwd += random.choice(alphabet)

print(pwd)
