# function which takes in a file name, a word to search for, and replacement word
# replace all instances of the word in the file with replacement word

def find_and_replace(fileName, searchWord, replaceWord):
    f = open(fileName, encoding='utf-8')
    data = f.read()
    f.close()

    newData = data.replace(searchWord, replaceWord)

    return newData

print(find_and_replace('story.txt', 'Alice', 'Teemo'))