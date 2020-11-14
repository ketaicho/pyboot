def remove_negatives(aList):
    return list(filter(lambda a: a >= 0 , aList))

#print(remove_negatives([-1,3,4,-99]))
#print(remove_negatives([-7,0,1,2,3,4,5]))
print(remove_negatives([50,60,70]))