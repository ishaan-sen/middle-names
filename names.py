import random
from math import floor
from sys import argv
from hashlib import sha256

first_name = argv[1]
last_name = argv[2]

hash = sha256(bytes(first_name + last_name, 'utf-8')).hexdigest()
random.seed(int(hash[:16], 16))

f = open("names.list")

lines = f.readlines()
lines = [line.strip() for line in lines]

def middle_name():
    first = random.choice(lines)
    last = random.choice(lines)

    print(first, last)

    middle = last[:floor(len(last) / 2)] + first[floor(len(first) / 2):]
    return middle

full_name = first_name + ' '

for i in range(random.randint(1, 3)):
    full_name = full_name + middle_name() + ' '

full_name = full_name + last_name

print(full_name)
