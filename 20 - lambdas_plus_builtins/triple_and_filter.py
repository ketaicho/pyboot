# function that accepts a list of numbers, filter numbers not divisible by 4,
# and return list where remaining numbers are tripled

def triple_and_filter(numList):
    filtList = list(filter(lambda f: f%4==0, numList))
    tripList = [i * 3 for i in filtList]
    return print(tripList)

triple_and_filter([1,2,3,4])
#triple_and_filter([6,8,10,12])
