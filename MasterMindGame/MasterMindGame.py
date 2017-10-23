#!/bin/python3
import random


possibleCodes = [('r', 'r', 'r'), ('r', 'r', 'w'), ('r', 'r', 'b'), ('r', 'r', 'o'), ('r', 'w', 'r'), ('r', 'w', 'w'), ('r', 'w', 'b'), ('r', 'w', 'o'), ('r', 'b', 'r'), ('r', 'b', 'w'), ('r', 'b', 'b'), ('r', 'b', 'o'), ('r', 'o', 'r'), ('r', 'o', 'w'), ('r', 'o', 'b'), ('r', 'o', 'o'), ('w', 'r', 'r'), ('w', 'r', 'w'), ('w', 'r', 'b'), ('w', 'r', 'o'), ('w', 'w', 'r'), ('w', 'w', 'w'), ('w', 'w', 'b'), ('w', 'w', 'o'), ('w', 'b', 'r'), ('w', 'b', 'w'), ('w', 'b', 'b'), ('w', 'b', 'o'), ('w', 'o', 'r'), ('w', 'o', 'w'), ('w', 'o', 'b'), ('w', 'o', 'o'), ('b', 'r', 'r'), ('b', 'r', 'w'), ('b', 'r', 'b'), ('b', 'r', 'o'), ('b', 'w', 'r'), ('b', 'w', 'w'), ('b', 'w', 'b'), ('b', 'w', 'o'), ('b', 'b', 'r'), ('b', 'b', 'w'), ('b', 'b', 'b'), ('b', 'b', 'o'), ('b', 'o', 'r'), ('b', 'o', 'w'), ('b', 'o', 'b'), ('b', 'o', 'o'), ('o', 'r', 'r'), ('o', 'r', 'w'), ('o', 'r', 'b'), ('o', 'r', 'o'), ('o', 'w', 'r'), ('o', 'w', 'w'), ('o', 'w', 'b'), ('o', 'w', 'o'), ('o', 'b', 'r'), ('o', 'b', 'w'), ('o', 'b', 'b'), ('o', 'b', 'o'), ('o', 'o', 'r'), ('o', 'o', 'w'), ('o', 'o', 'b'), ('o', 'o', 'o')]

def parseRes(res):
    numX = 0
    numO = 0
    print("In Parse")
    for item in res:
        if item == 'x' or item == 'X':
            numX = numX + 1
        elif item == 'O' or item == 'o':
            numO = numO + 1
    return(numX,numO)


def blank(code):
    print("Nothing Returned")
    ## Means none of the guessed was correct

def xRes(code,numX):
    print("In x responce")
    print(numX)

def oRes(code,numO):
    print("In o responce")
    print(numO)

def masterMind(currentCodes):
    numX = 0
    numO = 0
    code = "hello"
    ## Make Guess
    computerGuess = random.choice(currentCodes)

    ## Get User's Responce
    print("computer's guess")
    print(computerGuess)

    res = input("CodeMaters Responce: ")
    
    ## if nothing go to blank
    if(len(res) == 0):
        blank(code)
    else:
        numX, numO = parseRes(res)

    ## If Correct quit
    if(numX == 3):
        print("Found Solution!")
        return

    ## If X values
    if(numX > 0):
        xRes(code,numX)
    ## If O values
    if(numO > 0):
        oRes(code,numO)

    return masterMind(currentCodes)

## Start Game
Print("Starting Game")
masterMind(possibleCodes)

    
