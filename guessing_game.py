from random import randint

rand_num = randint(1,10)

play = "y"
cont = "n"
guess = 0

while play == "y":
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess) #need some sanitizing/error-checking here 
    
    if (guess >= 1) and (guess <= 10):
        if guess > rand_num:
            print("Too high, try again!")
        elif guess < rand_num:
            print("Too low, try again!")
        else:
            print("You guessed it! You WON!")

            cont = input("Do you want to keep playing? (y/n) ")
            print("\n")
            
            if cont == "y":
                play = "y"
                rand_num = randint(1,10)
            elif (cont != "y") or (cont != "n") or (cont == "n"):
                play = "n"

    else:
        print("Please enter a valid response! \n")

print("\n")