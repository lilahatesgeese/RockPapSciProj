import random

PlayerInput = input("Rock, Paper, or Scissors?")
if PlayerInput == "rock" or PlayerInput == "Rock":
    PlayerInput = "Rock"
elif PlayerInput == "paper" or PlayerInput == "Paper":
    PlayerInput = "Paper"
elif PlayerInput == "scissors" or PlayerInput == "Scissors":
    PlayerInput = "Scissors"


ComputerChoice = ['Rock', 'Paper', 'Scissors']
ComputerPlay = random.choice(ComputerChoice)

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
    print("Player wins!")
elif PlayerInput == "Paper" and ComputerPlay == "Rock":
    print("Player wins!")
elif PlayerInput == "Scissors" and ComputerPlay == "Paper":
    print("Player wins!")

print("Thanks for playing")




