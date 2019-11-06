import random

rand = random.randint(0,2)

print("... rock ...")
print("... paper ...")
print("... scissors ...\n")

rock = "rock"
paper = "paper"
scissors = "scissors"

if rand == 0:
    pc_play = rock
elif rand == 1:
    pc_play = paper
elif rand == 2:
    pc_play = scissors

player = input("Enter Player's choice: ").lower()
print(f"Computer played: {pc_play}")
    
if player:
    if ((player == rock) or (player == paper) or (player == scissors)):
        if player == pc_play:
            print("It's a tie!")
        else:
            if (player == rock) and (pc_play == paper):
                winner = "computer"
            elif (player == rock) and (pc_play == scissors):
                winner = "player"
            elif (player == paper) and (pc_play == rock):
                winner = "player"
            elif (player == paper) and (pc_play == scissors):
                winner = "computer"
            elif (player == scissors) and (pc_play == paper):
                winner = "player"
            elif (player == scissors) and (pc_play == rock):
                winner = "computer"
            print(f"\nAAAANNNNDDD..... The WINNER is >>> {winner}!!")
    else:
        print("Please enter a valid response!")
else:
    print("Please enter a response!")