# function that accepts two strings and returns a new string, made of the two inputs combined

def interleave(s1, s2):
    zippedList = list(zip(s1, s2))
    joinedTuple = [''.join(i) for i in zippedList]
    joinedList = [''.join(joinedTuple)]
    return joinedList[0]

#str1 = 'lzr'
#str2 = 'iad'
#str1 = 'hi'
#str2 = 'ha'
str1 = 'aaa'
str2 = 'zzz'
print(interleave(str1, str2))