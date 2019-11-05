from random import randint

rand_num = randint(1,10)
print(f"NUMBER: {rand_num}\n")

play = 'y'
cont = 'n'

guess = input("Guess a number between 1 and 10: ")
guess = int(guess) #need some sanitizing/error-checking here 

while play == 'y':
    if (guess >= 0) and (guess <= 10):
        if guess > rand_num:
            print("Too high, try again!")
        elif guess < rand_num:
            print("Too low, try again!")
        else:
            print("You guessed it! You WON!")
        cont = input("Do you want to keep playing? ")
    else:
        print("Please enter a valid response!")
    
    if (cont != 'y') or (cont != 'n') or (cont == 'n'):
        play = 'n'
    else:
        play = 'y'

print("\n")