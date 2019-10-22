import random

rand = random.randint(0,2)

print("... rock ...")
print("... paper ...")
print("... scissors ...\n")

winner = None
pc_play = None
rock = "rock"
paper = "paper"
scissors = "scissors"

if rand == 0:
    pc_play = rock
elif rand == 1:
    pc_play = paper
elif rand == 2:
    pc_play = scissors

player1 = input("Enter Player 1's choice: ")
print(f"Computer played: {pc_play}")
    
if player1:
    if ((player1 == rock) or (player1 == paper) or (player1 == scissors)):
        if player1 == pc_play:
            print("It's a tie!")
        else:
            if (player1 == rock) and (pc_play == paper):
                winner = 2
            elif (player1 == rock) and (pc_play == scissors):
                winner = 1
            elif (player1 == paper) and (pc_play == rock):
                winner = 1
            elif (player1 == paper) and (pc_play == scissors):
                winner = 2
            elif (player1 == scissors) and (pc_play == paper):
                winner = 1
            elif (player1 == scissors) and (pc_play == rock):
                winner = 2
            print(f"\nAAAANNNNDDD..... The WINNER is Player {winner}!!")
    else:
        print("Please enter a valid response!")
else:
    print("Please enter a response!")