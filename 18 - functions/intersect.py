# function that takes 2 lists as params and returns list of the intersection

def intersection(list1, list2):
    return [i for i in list1 for j in list2 if i==j]


print(intersection([1,2,3], [2,3,4]))
