# function that takes in a file name, and a new file name
# copies the contents of the first file to the new one

def copy(fileName, newFileName):
    f = open(fileName, encoding="utf8")
    text = f.read()
    f.close()

    n = open(newFileName, "w")
    n.write(text)
    n.close()

copy('story.txt', 'story_copy.txt')