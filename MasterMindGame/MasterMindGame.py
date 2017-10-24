#!/bin/python3
import random


possibleCodes = [('r', 'r', 'r'), ('r', 'r', 'w'), ('r', 'r', 'b'), ('r', 'r', 'o'), ('r', 'w', 'r'), ('r', 'w', 'w'), ('r', 'w', 'b'), ('r', 'w', 'o'), ('r', 'b', 'r'), ('r', 'b', 'w'), ('r', 'b', 'b'), ('r', 'b', 'o'), ('r', 'o', 'r'), ('r', 'o', 'w'), ('r', 'o', 'b'), ('r', 'o', 'o'), ('w', 'r', 'r'), ('w', 'r', 'w'), ('w', 'r', 'b'), ('w', 'r', 'o'), ('w', 'w', 'r'), ('w', 'w', 'w'), ('w', 'w', 'b'), ('w', 'w', 'o'), ('w', 'b', 'r'), ('w', 'b', 'w'), ('w', 'b', 'b'), ('w', 'b', 'o'), ('w', 'o', 'r'), ('w', 'o', 'w'), ('w', 'o', 'b'), ('w', 'o', 'o'), ('b', 'r', 'r'), ('b', 'r', 'w'), ('b', 'r', 'b'), ('b', 'r', 'o'), ('b', 'w', 'r'), ('b', 'w', 'w'), ('b', 'w', 'b'), ('b', 'w', 'o'), ('b', 'b', 'r'), ('b', 'b', 'w'), ('b', 'b', 'b'), ('b', 'b', 'o'), ('b', 'o', 'r'), ('b', 'o', 'w'), ('b', 'o', 'b'), ('b', 'o', 'o'), ('o', 'r', 'r'), ('o', 'r', 'w'), ('o', 'r', 'b'), ('o', 'r', 'o'), ('o', 'w', 'r'), ('o', 'w', 'w'), ('o', 'w', 'b'), ('o', 'w', 'o'), ('o', 'b', 'r'), ('o', 'b', 'w'), ('o', 'b', 'b'), ('o', 'b', 'o'), ('o', 'o', 'r'), ('o', 'o', 'w'), ('o', 'o', 'b'), ('o', 'o', 'o')]

def parseRes(res):
    numX = 0
    numO = 0
    ## print("In Parse")
    for item in res:
        if item == 'x' or item == 'X':
            numX = numX + 1
        elif item == 'O' or item == 'o':
            numO = numO + 1
    return(numX,numO)


def blank(code,currentCodes):
    ## print("Nothing Returned")
    filterList = []
    pos1 = code[0]
    pos2 = code[1]
    pos3 = code[2]
    for items in currentCodes:
        if pos1 not in items and pos2 not in items and pos3 not in items:
            filterList.append(items)
    return filterList
    ## Means none of the guessed was correct
def xRes(code,numX,currentCodes):
    ## print("In x responce")
    filterList = []
    pos1 = code[0]
    pos2 = code[1]
    pos3 = code[2]
    if(numX == 2):
        for items in currentCodes:
            if (pos1 == items[0] and pos2 == items[1]) or (pos1 == items[0] and pos3 == items[2]) or (pos2 == items[1] and pos3 == items[2]):
                if items not in filterList:
                    filterList.append(items)
    else:
        for items in currentCodes:
            if (pos1 == items[0]) or (pos2 == items[1]) or (pos3 == items[2]):
                if items not in filterList:
                    filterList.append(items)
    return filterList

def oRes(code,numO,currentCodes):
    filterList = []
    pos1 = code[0]
    pos2 = code[1]
    pos3 = code[2]
    if(numO == 3):
        for items in currentCodes:
            if (pos2 == items[0] and pos3 == items[1] and pos1 == items[2]) or (pos3 == items[0] and pos1 == items[1] and pos2 == items[2]):
                if items not in filterList:
                    filterList.append(items)
    elif(numO == 2):
        ## random in first pos
        for items in currentCodes:
            if (pos3 == items[1] and pos2 == items[2]) or (pos1 == items[1] and pos2 == items[2]) or (pos3 == items[1] and pos1 == items[2]):
                if items not in filterList:
                    filterList.append(items)
        ## random in secound pos
        for items in currentCodes:
            if (pos3 == items[0] and pos1 == items[2]) or (pos2 == items[0] and pos1 == items[2]) or (pos3 == items[0] and pos2 == items[2]):
                if items not in filterList:
                    filterList.append(items)
        ## random in third pos
        for items in currentCodes:
            if (pos3 == items[0] and pos1 == items[1]) or (pos2 == items[0] and pos1 == items[1]) or (pos2 == items[0] and pos3 == items[1]):
                if items not in filterList:
                    filterList.append(items)
    else:
        ## first position correct color
        for items in currentCodes:
            if (pos1 == items[1]) or (pos1 == items[2]):
                if items not in filterList:
                    filterList.append(items)
        ## secound position correct color
        for items in currentCodes:
            if (pos2 == items[0]) or (pos2 == items[2]):
                if items not in filterList:
                    filterList.append(items)
        ## third position correct color
        for items in currentCodes:
            if (pos3 == items[0]) or (pos3 == items[1]):
                if items not in filterList:
                    filterList.append(items)
    return filterList

def masterMind(currentCodes):
    numX = 0
    numO = 0
    ## Make Guess
    computerGuess = random.choice(currentCodes)
    currentCodes.remove(computerGuess)

    ## Get User's Responce
    printOut = "Computer's Guess: " + repr(computerGuess)
    print(printOut)
    res = input("CodeMaster's Responce: ")
    
    ## if nothing go to blank
    if(len(res) == 0):
        currentCodes = list(blank(computerGuess,currentCodes))
        ## print(currentCodes)
    else:
        numX, numO = parseRes(res)

    ## If Correct quit
    if(numX == 3):
        print("Found Solution!")
        return

    ## If X values
    if(numX > 0):
        currentCodes = list(xRes(computerGuess,numX,currentCodes))
    ## If O values
    if(numO > 0):
        currentCodes = list(oRes(computerGuess,numO,currentCodes))
    ## print(currentCodes)

    return masterMind(currentCodes)

## Start Game
print("Starting Game")
masterMind(possibleCodes)