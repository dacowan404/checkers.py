#create a board
class board:
    def __init__(self):
        self.boardVar = []
        self.checkersDict = {}

        for i in range(8):
            self.boardVar.append([])
            if i == 3 or i == 4:
                for k in range(8):
                    self.boardVar[i].append(None)
            else:
                for j in range(8):
                    if (i+j)%2 == 0:
                        self.boardVar[i].append(None)
                    elif i < 4:
                        self.boardVar[i].append(checker([i,j], 1))
                    else:
                        self.boardVar[i].append(checker([i,j], -1))
    
    def printBoard(self):
        length =64
        print(" "*4 + "*"*length)
        print("\t A\t B\t C\t D\t E\t F\t G\t H\n")
        print(" " * 4 + "-"*length)
        for i in range(len(self.boardVar)):
            print(str(i) + "||", end="")
            for j in range(len(self.boardVar[i])):
                if self.boardVar[i][j] == None:
                    print("\t 0", end="") 
                elif self.boardVar[i][j].team == 1:
                    print("\t " + str(self.boardVar[i][j].team),end="")
                else:
                    print("\t" + str(self.boardVar[i][j].team), end="")
            print()
            print("\n" +" "* 4 + "-"*length)
        print(" " * 4 +"-"*length+"\n\n")
    


    def checkLocation(self, pieceLocation):
        newLocation = convertLocation(pieceLocation)
        if self.boardVar[col][row] == None:
            return 0
        else:
            return self.boardVar[col][row]

    def updateBoard(self):
        return 0

#creat checker class
class checker:
    def __init__(self, location, value):
        self.location = location
        self.alive = True
        self.team = value
    
    def checkMove(self, newLocation):
        if len(newLocation) != 2:
            return 1
        elif newLocation[0] < 0 or newLocation[0] > 7 or newLocation[1] < 0 or newLocation[1] > 7:
            return 2
        #elif value == 0 for no piece present
        elif self.team == 1 and newLocation[0] == self.location[0] + 1 and (newLocation[1] == self.location[1] - 1 or newLocation[1] ==self.location[1] + 1):
            self.location = newLocation
        elif self.team == -1 and newLocation[0] == self.location[0] - 1 and (newLocation[1] == self.location[1] -1 or newLocation[1] == self.location[1] + 1):
            self.location = newLocation
        
#create super checker class

#create game
newGame = board()
print("Starting new game. Team 1 goes first.")
team = 1
for i in range(5): #change to while both teams have at least one piece still alive and valid move eventually
    repeat = True
    newGame.printBoard()
    while (repeat):
        pieceLocation = input("Which piece would you like to move? ")
        checkerPiece = newGame.checkLocation(pieceLocation)
        if checkerPiece == False or checkerPiece == 0 or checkerPiece.team != team:
            print("Invalid location, try again")
            continue
        else:
            repeat = False
    repeat = True
    while (repeat):
        inputLocation = input("Where would you like to move to? ")
        movePosition = newGame.checkLocation(inputLocation)
        if movePosition == False or movePosition == type(checkerPiece):
            print("Invalid location, try again")
        elif movePosition

        
    #move self.board(newLocation) = self.board(oldLocation) then self.board(oldLocation) = None    

    team = team * -1

    #currentPiece = newGame.checkLocation(pieceLocation) #does entered location contain a valid piece

def convertLocation(location):
    col1 = location[0]
    if col1 == "A":
        col = 0
    elif col1 == "B":
        col = 1
    elif col1 == "C":
        col = 2
    elif col1 == "D":
        col = 3
    elif col1 == "E":
        col = 4
    elif col1 == "F":
        col = 5
    elif col1 == "G":
        col = 6
    elif col1 == "H":
        col = 7
    else:
        return [-1,-1]
    row = int(location[1])
    if row < 0 or row > 7:
        return [-1,-1]
    else:
        return [row, col]
