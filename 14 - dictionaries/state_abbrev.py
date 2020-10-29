# given two lists, create a dictionary

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i]: list2[i] for i in range(len(list2))}
# {k: v for (k,v) in zip(list1,list2)}