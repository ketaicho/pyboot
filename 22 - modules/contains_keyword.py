# function that accepts any number of string args, and returns 'True' if any of them is a Python keyword

import keyword

def contains_keyword(*args):
    for arg in args:
        if keyword.iskeyword(arg):
            return True
    return False

print(contains_keyword('def', 'lol', 'chicken', 'alaska'))