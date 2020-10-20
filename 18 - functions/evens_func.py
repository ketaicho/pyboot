#Define empty list
evens = []

#define function to return list of even numbers between 0 and 50, excluding 50
def generate_evens():
    for i in range(1, 50):
        if (i%2 == 0):
            evens.append(i)
    return(evens)