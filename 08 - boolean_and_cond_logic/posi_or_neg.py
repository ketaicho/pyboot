# given two vars, if both positive, print "both positive"
# if both are negative, print "both negative"
# otherwise, state which is positive and which is negative

from random import randint
x = randint(-100, 100)
while x == 0:
    x = randint(-100, 100)
y = randint(-100, 100)
while y == 0:
    y = randint(-100, 100)

print(f"X Value: {x}, Y Value: {y}")

if (x >= 0) and (y >= 0):
    print("both positive")
elif (x < 0) and (y < 0):
    print("both negative")
elif (x >= 0) and (y < 0): 
    print("x is positive and y is negative")
elif (y >= 0) and (x < 0): 
    print("y is positive and x is negative")