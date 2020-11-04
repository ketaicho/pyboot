# function that takes in a list an a search-item
# returns how many times the search-item appears in the list

def frequency(aList, searchItem):
    return aList.count(searchItem)

print(frequency([True, False, True, True], False))