for i in range(1,21):
    if (i == 4) or (i == 13):
        state = "unlucky"
    elif i % 2 == 0:
        state = "even"
    elif i % 2 == 1:
        state = "odd"
    print(f"{i} is {state}")