# function that takes any number of args and returns sum of args, that are div by 2

def sum_even_values(*args):
    sumList = []
    for i in args:
        if i%2 == 0:
            sumList.append(i)

    return sum(sumList)

#print(sum_even_values(4,2,1,10))
print(sum_even_values(1))