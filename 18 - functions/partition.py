# function that takes - a list of numbers
# return two sublists in a list, with each sublist containing truthy and falsy values

def isEven(num):
    return num % 2 == 0

def partition(theList):
    tList = []
    fList = []

    for i in theList:
        if isEven(i):
            tList.append(i)
        else:
            fList.append(i)

    return [tList, fList]

print(partition([1,2,3,4]))
