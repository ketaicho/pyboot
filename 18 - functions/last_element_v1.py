# Take a list and pop last item in loop, return 'None' when list is empty

numList = [12,23,34,45]

def last_element(numList):
    if len(numList) > 0:
        return(numList.pop(-1))
    else:
        return("None")

print(last_element(numList))