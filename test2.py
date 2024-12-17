connect4= [["6","_","_","_","_","_","_","_","_"],["5","_", "_","_","_","_","_","_","_"],
            ["4","_","_","_","_","_","_","_","_"],["3","_", "_","_","_","_","_","_","_"],
            ["2","_","_","_","_","_","_","_","_"],["1","_", "_","_","_","_","_","_","_"], 
            ["0","1","2","3","4","5","6","7","8"]]


invalidmove = True
win = False
Ocountx=0
Xcountx=0

for index in connect4:
    print(index)


def correction(movey):
    if movey == 1:
        movey =5
    elif movey == 2:
        movey = 4
    elif movey == 4:
        movey = 2
    elif movey == 5:
        movey = 1 
    elif movey== 6:
        movey = 0  
    return movey

#player x and o moves, checks if the space is available and if the piece is not floating
def playerX(movex, movey):
    movey = correction(movey)
    
    if movey<5 and connect4[movey+1][movex] == "_":
        print("You cannot place a piece here as it would be floating")
        invalidmove = True 
        return invalidmove

    elif connect4[movey][movex] != "_":
        print("There is a piece there already")
        invalidmove = True
        return invalidmove
    connect4[movey][movex]= "x"
    invalidmove= False

    print("Player X moved")

    for index in connect4:
        print(index)
    return invalidmove

def playerO(movex,movey):
    movey= correction(movey)
    if movey < 5 and connect4[movey+1][movex] == "_":
        print("You cannot place a piece here as it would be floating")
        invalidmove = True
        return invalidmove
    elif connect4[movey][movex] != "_":
        print("There is a piece there already")
        invalidmove = True
        return invalidmove
    connect4[movey][movex]= "o"
    invalidmove = False
    print("Player O moved")

    for index in connect4:
        print(index)
    return invalidmove

#Gameplay:
while win == False:

    while invalidmove == True:
        print("Player 1 to move:")
        invalidmove = playerX(int(input("Move in x: ")), int(input("Move in y: ")))
        
        for searchx in connect4:   
            for searchy in searchx:
                if searchy == ("x"):
                    Xcountx += 1
                else:
                    Xcountx = 0
                if Xcountx == 4:
                    print("Player 1 wins!")
                    win = True
                    break
    if win == True:
        break

    invalidmove = True

    while invalidmove == True:
        print("Player 2 to move:")
        invalidmove = playerO(int(input("Move in x: ")), int(input("Move in y: ")))

        for searchx in connect4:   
            for searchy in searchx:
                if searchy == ("o"):
                    Ocountx += 1
                else:
                    Ocountx = 0
                if Ocountx == 4:
                    print("Player 2 wins!")
                    win = True 
                    break
    invalidmove = True 