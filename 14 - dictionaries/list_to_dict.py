# convert a list to a dictionary
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# option 1
answer = {thing[0]: thing[1] for thing in person}

# option 2
answer = {k: v for k,v in person}

# option 3
answer = dict(person)