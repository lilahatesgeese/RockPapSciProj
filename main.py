import random
value = {"rock": ("scissors", "lizard"),
         "paper": ("rock", "spock"),
         "scissors": ("paper", "lizard"),
         "lizard": ("paper", "spock"),
         "spock": ("scissors", "rock")}

Fart = False
while Fart == False:


    PlayerInput = input("Rock, Paper, Scissors, Lizard, or Spock?").lower()

    ComputerChoice = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    ComputerPlay = random.choice(ComputerChoice)

    if PlayerInput == "rock" or PlayerInput == "paper" or PlayerInput == "scissors" or PlayerInput == "lizard" or PlayerInput == "spock":
        print(f"You picked {PlayerInput}, computer picked {ComputerPlay}.")

    try:
        if PlayerInput == ComputerPlay:
            print("Tie!")
        elif ComputerPlay in value[PlayerInput]:
            print("You win!")
        else:
            print("Computer wins!")
    except:
        print("You cant do that you tin can of a man!")
        break

    PlayerStart = input("Would you like to play again?")

    if PlayerStart == "yes" or PlayerStart == "Yes" or PlayerStart == "y":
        PlayerStart = "Again"
    elif PlayerStart == "no" or PlayerStart == "No" or PlayerStart == "n":
        PlayerStart = "Stop"

    if PlayerStart == "Again":
        print("You have selected to play again!")
    elif PlayerStart == "Stop":
        print("Thanks for playing!")
        break
