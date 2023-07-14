import string
import random


letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation[:random.randint(len(string.punctuation) // 3, len(string.punctuation))]

pwd_len = input('Enter passwrod length: ')
pwd_len = int(pwd_len) if pwd_len != '' else 6
alphabet = letters + digits + special_chars
pwd_strong = False

while not pwd_strong:
    pwd = ''
    for _ in range(pwd_len):
        pwd += random.choice(alphabet)
    
    if any(c in special_chars for c in pwd) and sum(c in digits for c in pwd) >= 2:
        pwd_strong = True

print(f'Number of letters: {sum(c in letters for c in pwd)}')
print(f'Number of digits: {sum(c in digits for c in pwd)}')
print(f'Number of letters: {sum(c in special_chars for c in pwd)}')
print()
print(f'Password: {pwd}')
