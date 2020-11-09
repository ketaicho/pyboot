# function that takes any number of args, and returns True if any of args is 'purple'

def contains_purple(*args):
    if 'purple' in args:
        return True
    return False

print(contains_purple(25,"purple"))