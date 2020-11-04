# function that takes a list as input. Returns product of even numbers

def multiply_even_numbers(aList):
    evenList = [i for i in aList if i%2==0]
    tot=1
    for k in evenList:
        tot = k * tot
    return tot

print(multiply_even_numbers([2,3,4,5,6]))