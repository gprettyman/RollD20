# RollForDamage - Easy Dice Roller for GMing
# For the night I forogt my dice. My bad.

import random

quitProgram = False
quitProgramInput = ""
random.seed()

def getUserInput():
    diceQuantity = int(input("How many dice/dice would you like to roll?"))
    global diceList 
    diceList = []
    for x in range(0, diceQuantity):
        print("Type the number of faces on die #", end = "")
        print((x+1))
        diceList.append(int(input()))
    print("The dice being rolled are:", end = " ")
    print(diceList)
    global modifier
    modifier = int(input("Is there any modifier? Don't forget a '-' if it is a penalty! Type '0' for no modifier."))

def rollDice():
    global diceList, modifier
    diceTotal = 0
    for x in diceList:
        diceCurrent = random.randint(1, x)
        print("Die #", end = "")
        print(x, end = " ")
        print("is a:", end = " ")
        print(diceCurrent)
        diceTotal += diceCurrent
    print("Dice Total:", end = " ")
    print(diceTotal, end = " ")
    if modifier > 0:
        print(" + ", end = " ")
        print(modifier, end = " modifier \n")
        print("Final Total = ")
        print(diceTotal + modifier)
    elif modifier < 0:
        print(modifier, end = " modifier \n")
        print("Final Total =", end = " ")
        print(diceTotal + modifier)
    print("")




while quitProgram != True:
    getUserInput()
    rollDice()
    quitProgramInput = ""
    while quitProgramInput == "":
        quitProgramInput = input("Reroll? Type 'Y' to continue or 'N' to quit")
        if quitProgramInput == "Y":
            print("The adventure continues!")
        elif quitProgramInput == "y":
            print("The adventure continues!")
        elif quitProgramInput == "N":
            print("Game over...for now")
            quitProgram = True
        elif quitProgramInput == "n":
            print("Game over...for now")
            quitProgram = True
        else:
            print("Invalid Input, please type either 'Y' or 'N'")
            quitProgramInput = ""