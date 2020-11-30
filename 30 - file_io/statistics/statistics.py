# function which takes a file name, and returns a dict with num of lines, words and chars

def statistics(fileName):
    f = open(fileName, encoding="utf-8")
    if f.mode == "r":                   #check to see if we are in read mode
        text = f.read()
        f.seek(0)
        numLines = len(f.readlines())
    f.close()

    numChars = len(text)
    numWords = len(text.split())

    stat_dict = {}
    stat_dict["lines"] = numLines
    stat_dict["words"] = numWords
    stat_dict["characters"] = numChars

    return stat_dict

print(statistics('story.txt'))