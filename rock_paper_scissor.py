print("... rock ...")
print("... paper ...")
print("... scissors ...")

player1 = input("Enter Player 1's choice: ")
player2 = input("Enter Player 2's choice: ")

winner = None
rock = "rock"
paper = "paper"
scissors = "scissors"

if player1 and player2:
    if ((player1 == rock) or (player1 == paper) or (player1 == scissors)) and ((player2 == rock) or (player2 == paper) or (player2 == scissors)):
        if player1 == player2:
            print("MATCHED!!")
        else:
            if (player1 == rock) and (player2 == paper):
                winner = 2
            elif (player1 == rock) and (player2 == scissors):
                winner = 1
            elif (player1 == paper) and (player2 == rock):
                winner = 1
            elif (player1 == paper) and (player2 == scissors):
                winner = 2
            elif (player1 == scissors) and (player2 == paper):
                winner = 1
            elif (player1 == scissors) and (player2 == rock):
                winner = 2
            print(f"\nAAAANNNNDDD..... The WINNER is Player {winner}!!")
    else:
        print("Please enter a valid response!")
else:
    print("Please enter a response!")