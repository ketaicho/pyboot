# function that takes in a list and returns a list of values that are truthy

def compact(aList):
    return [lst for lst in aList if lst]

print(list(compact([0,1,2,"",[], False, {}, None, "All done"])))