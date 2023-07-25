import random

sBoard = [0,1,2,3,4,5,6,7,8]

def displayBoard():
    
    for i in range(0, len(sBoard)):
        if(i%3) == 2:
            print(sBoard[i])
            
        else :
            print(sBoard[i], end = "")
            

     
def inputBoard(playerTurn) :
    if(playerTurn == "o") :
        zahyo = int(input("0-8の座標 ->"))
    else:
        zahyo = random.randint(0,8)

    if(sBoard[zahyo] == "o" or sBoard[zahyo] == "x"):
        inputBoard(playerTurn)

    else:
        sBoard[zahyo] = playerTurn

def winner():
    lines = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6],
    ]
    for i in range(0, len(lines)):
        [a,b,c] = lines[i]

        if sBoard[a] and sBoard[a] == sBoard[b] and sBoard[a] == sBoard[c]:
            return sBoard[a]
        

displayBoard()
for turn in range(0,8):
    if (turn%2 == 0) :
        print("Your Turn")
        inputBoard("o")
    else :
        print("CPU Turn")
        inputBoard("x")

    
    
    if winner():
        print(winner() + "の勝ち")
        break

    if turn == 8:
        print("引き分け")
        break

    displayBoard() 




