# ------ Exercise 1
names = ["Elie","Tim","Matt"]
answer = [name[0] for name in names]

numbers = [1,2,3,4,5,6]
answer2 = [even for even in numbers if even%2 == 0]

# ------ Exercise 2
list1 = [1,2,3,4]
list2 = [3,4,5,6]
answer = [i for i in list1 if i in list2]

names = ['Elie','Tim','Matt']
answer2 = [n.lower()[::-1] for n in names]

# ------ Exercise 3
answer = [i for i in range(1,101) if i % 12 == 0]

# ------ Exercise 4
answer = [i for i in "amazing" if 'a'!=i and 'e'!=i and 'i'!=i and 'o'!=i and 'u'!=i]

# ------ Exercise 5
answer = [[i for i in range(0,3)] for j in range(0,3)]
