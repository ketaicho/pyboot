# function that takes any number of args and returns sum of args, that are floats

def sum_floats(*args):
    return sum([f for f in args if type(f)==float])

#print(sum_floats(1.5, 2.4, 'awesome', [], 1))
print(sum_floats(1,2,3,4,5))