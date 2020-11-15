#function that accepts iterable and returns true if it ONLY contains strings

def is_all_strings(iterable):
    return all([type(onlyStr) == str for onlyStr in iterable])