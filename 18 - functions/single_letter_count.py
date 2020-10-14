# function with inputs of a word and a char
# counts how many times the char appears in the word

word = input("Enter word: ")
letter = input("Enter letter: ")


def single_letter_count(word, letter):
    if (len(word) > 0) & (word.isalpha()):
        if (len(letter) == 1) & (letter.isalpha()):
            return((word.lower()).count(letter.lower()))
        else:
            return ("Error: Letter must be char of length 1!")
    else:
        return("Error: Enter a valid word!")


print(single_letter_count(word,letter))