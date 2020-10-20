from random import randint

number = randint(0,10)
i = 0

while number != 5:
    i += 1
    number = randint(0,10)
    
print(f"i: {i}")