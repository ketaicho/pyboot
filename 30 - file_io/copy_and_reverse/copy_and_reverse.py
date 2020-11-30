# function that takes in a file name, and a new file name
# copies the reversed contents of the first file to the new one

def copy_and_reverse(oldFile, newFile):
    with open(oldFile, encoding="utf8") as o:
        text = o.read()

    revString = text[::-1]
    with open(newFile, "w") as n:
        n.write(revString)

copy_and_reverse('story.txt','story_reversed.txt')
