import random
print("Welcome to tic tac toe")
print("------------------------")
possibleNumbers=[1,2,3,4,5,6,7,8,9]
gameBoard=[[1,2,3],[4,5,6],[7,8,9]]
rows = 3
cols = 3
def printGameBoard():
    for x in range(rows):
        print("\n +---+---+---+")
        print(" |", end="")
        for y in range(cols):
            print("",gameBoard[x][y], end=" |")
    print("\n +---+---+---+")
printGameBoard()
def modifyArray(num,turn):
    num -= 1
    if (num==0):
        gameBoard[0][0]=turn
    elif (num==1):
        gameBoard[0][1]=turn
    elif (num==2):
        gameBoard[0][2]=turn
    elif (num==3):
        gameBoard[1][0]=turn
    elif (num==4):
        gameBoard[1][1]=turn
    elif (num==5):
        gameBoard[1][2]=turn
    elif (num==6):
        gameBoard[2][0]=turn
    elif (num==7):
        gameBoard[2][1]=turn
    elif (num==8):
        gameBoard[2][2]=turn
leaveLoop = False
turnCounter = 0
while (leaveLoop == False):
    if (turnCounter%2==1):
        printGameBoard()
        numberPicked=int(input("Enter a number from 1-9: "))
        if numberPicked >= 1 and numberPicked <= 9:
            modifyArray(numberPicked,'X')
            possibleNumbers.remove(numberPicked)
        else:
            print("Invalid number, please enter a number from 1-9")
        turnCounter += 1
    else:
        while (True):
            cpuChoice = random.choice(possibleNumbers)
            print("\n Cpu choice",cpuChoice)
            if (cpuChoice in possibleNumbers):
                modifyArray(cpuChoice,'O')
                possibleNumbers.remove(cpuChoice)
                turnCounter += 1
                break