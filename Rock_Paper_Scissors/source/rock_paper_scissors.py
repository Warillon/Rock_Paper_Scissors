import os
import random

def game():

    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

    cls()

    def nobodyWin():
        cls()
        print("Nobody wins.")
        input("Press Enter to replay!")
        game()

    def playerWin():
        cls()
        print("You Win!")
        input("Press Enter to replay!")
        game()

    def botWin():
        cls()
        print("You lose..")
        input("Press Enter to replay!")
        game()

    def whoWin(playerChoice, botChoice):
        if botChoice == playerChoice:
            nobodyWin()
        elif (botChoice == "r" and playerChoice == "s") or \
             (botChoice == "s" and playerChoice == "p") or \
             (botChoice == "p" and playerChoice == "r"):
            botWin()
        else:
            playerWin()

    print("##########################################")
    print("Hello! and welcome to Rock-Paper-Scissors!")
    print("##########################################")
    input("Press Enter to continue...")
    cls()

    choice = ["r", "p", "s"]
    botChoice = random.choice(choice)

    def PLAYERCHOICE():
        playerChoice = input("Rock (r), Paper (p) or Scissors (s): ")
        if playerChoice in ("r", "p", "s"):
            whoWin(playerChoice, botChoice)
        else:
            cls()
            print("Please write a correct input")
            PLAYERCHOICE()

    PLAYERCHOICE()

game()
