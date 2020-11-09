def combine_words(word, **kwargs):
    if word:
        if "prefix" in kwargs:
            return kwargs["prefix"] + word
        elif "suffix" in kwargs:
            return word + kwargs["suffix"]
        else:
            return word

#print(combine_words("child"))
#print(combine_words("child", prefix="man"))
print(combine_words("child", suffix="ish"))