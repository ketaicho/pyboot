# function to return whether an input is a palindrome
# the function should be case insensitive and it should ignore whitespace

def is_palindrome(inputStr):
    inputStr = (inputStr.lower()).replace(" ","")
    revStr = inputStr[::-1]
    if revStr == inputStr:
        return True
    return False

#print(is_palindrome('a man a plan a canal Panama'))
print(is_palindrome('tacocat'))