# create a variable, which is a list containing the first letter of each name in the list
names = ["Elie","Tim","Matt"]
answer = [name[0] for name in names]

# create a variable which is a list of all even values
numbers = [1,2,3,4,5,6]
answer2 = [even for even in numbers if even%2 == 0]

# given two lists, create a new list that is the intersection of the two
list1 = [1,2,3,4]
list2 = [3,4,5,6]
answer = [i for i in list1 if i in list2]

# create a list of the words in the original list reversed and in lower case
names = ['Elie','Tim','Matt']
answer2 = [n.lower()[::-1] for n in names]

# for numbers 1-100, create a list with all the numbers divisible by 12
answer = [i for i in range(1,101) if i % 12 == 0]

# create a list of the string "amazing", minues the vowels
answer = [i for i in "amazing" if 'a'!=i and 'e'!=i and 'i'!=i and 'o'!=i]

# create a nested list of [0,1,2] - [[0,1,2],[0,1,2],[0,1,2]]
answer = [[i for i in range(0,3)] for j in range(0,3)]

# create a 10x10 array
answer = [[i for i in range(0,10)] for j in range(0,10)]