# a function that takes in one parameter and returns a dictionary
# with the keys being the letters, and the values being the count of the letter

def multiple_letter_count (inputWord=''):
    lowerInput = inputWord.lower()
    if inputWord == '':
        return "Please enter a word"
    return {i: lowerInput.count(i) for i in lowerInput}

print(multiple_letter_count("Accordiona"))