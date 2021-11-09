import random
value = {"rock": ("scissors", "lizard"),
         "paper": ("rock", "spock"),
         "scissors": ("paper", "lizard"),
         "lizard": ("paper", "spock"),
         "spock": ("scissors", "rock")}

class stats:
    def __init__(self, wins, losses, ties):
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def stattrack(self):
        print("You've won", self.wins,
               "You've Lost", self.losses,
               "You've tied", self.ties)

    def addwins(self):
        self.wins += 1
        self.stattrack()
    def addlosses(self):
        self.losses += 1
        self.stattrack()
    def addties(self):
        self.ties += 1
        self.stattrack()
s1 = stats(0,0,0,)

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
            s1.addties()
        elif ComputerPlay in value[PlayerInput]:
            print("You win!")
            s1.addwins()
        else:
            print("Computer wins!")
            s1.addlosses()
    except:
        print("You can't do that you tin can of a man!")
        break

    PlayerStart = input("Would you like to play again?")

    if PlayerStart == "yes" or PlayerStart == "Yes" or PlayerStart == "y":
        PlayerStart = "Again"
    elif PlayerStart == "no" or PlayerStart == "No" or PlayerStart == "n":
        PlayerStart = "Stop"
    else:
        PlayerStart = "who"

    if PlayerStart == "Again":
        print("You have selected to play again!")
    elif PlayerStart == "Stop":
        print("Thanks for playing!")
        break
    elif PlayerStart == "who":
        print("wat")
        break
