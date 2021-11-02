import random
Fart = False
while Fart == False:

    PlayerInput = input("Rock, Paper, or Scissors?")

    if PlayerInput == "rock" or PlayerInput == "Rock":
        PlayerInput = "Rock"
    elif PlayerInput == "paper" or PlayerInput == "Paper":
        PlayerInput = "Paper"
    elif PlayerInput == "scissors" or PlayerInput == "Scissors":
        PlayerInput = "Scissors"
    else:
        print("You cant do that you tin can of a man!")

    ComputerChoice = ['Rock', 'Paper', 'Scissors']
    ComputerPlay = random.choice(ComputerChoice)

    if PlayerInput == "Rock" or PlayerInput == "Paper" or PlayerInput == "Scissors":
        print(f"You picked {PlayerInput}, computer picked {ComputerPlay}.")

    if PlayerInput == ComputerPlay:
        print("Tie!")

    elif PlayerInput == "Rock" and ComputerPlay == "Paper":
        print("Computer wins!")
    elif PlayerInput == "Paper" and ComputerPlay == "Scissors":
        print("Computer wins!")
    elif PlayerInput == "Scissors" and ComputerPlay == "Rock":
        print("Computer wins!")
    elif PlayerInput == "Rock" and ComputerPlay == "Scissors":
        print("You won!")
    elif PlayerInput == "Paper" and ComputerPlay == "Rock":
        print("You won!")
    elif PlayerInput == "Scissors" and ComputerPlay == "Paper":
        print("You won!")

    PlayerStart = input("Would you like to play again?")

    if PlayerStart == "yes" or PlayerStart == "Yes" or PlayerStart == "y":
        PlayerStart = "Again"
    elif PlayerStart == "no" or PlayerStart == "No" or PlayerStart == "n":
        PlayerStart = "Stop"

if PlayerStart == "Stop":
    print("Thanks for playing!")