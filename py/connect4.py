
PASTEBIN  |  #1 paste tool since 2002
create new pastetoolsapiarchivefaq
PASTEBIN
search...
Search...
 create new paste      trending pastes
sign uploginmy alertsmy settingsmy profile
 December SPECIAL! For a limited time only. Get 20% discount on a LIFETIME PRO account!Want more features on Pastebin? Sign Up, it's FREE!
Public Pastes
Untitled
2 sec ago
8782 Teleop
Java | 22 sec ago
Report Mạo Danh
27 sec ago
CrawJunk
40 sec ago
Untitled
47 sec ago
Untitled
55 sec ago
Untitled
C | 56 sec ago
Untitled
58 sec ago
0
tweet
Guest
Use_This!
BY: A GUEST ON DEC 4TH, 2015  |  SYNTAX: PYTHON  |  SIZE: 21.82 KB  |  VIEWS: 39  |  EXPIRES: NEVER
DOWNLOAD  |  RAW  |  EMBED  |  REPORT ABUSE  |  PRINT  |  QR CODE  |  CLONE
AD-BLOCK DETECTED - PLEASE SUPPORT PASTEBIN BY BUYING A PRO ACCOUNT
For only $2.95 you can unlock loads of extra features, and support Pastebin's development at the same time.
pastebin.com/pro

#Connect 4

#The objective of the game is for player or computer to try to get 4 in a row
#You can get win by achieving 4 colors in a row horizontally, vertically, or diagonally
#There will be a tie if the grid is filled and nobody wins.
#Win or lose, press space to start a new game
#Good luck!

import turtle
import random
import time

#GLOBAL CONSTANTS
ROW = 6
COLUMN = 7
NUM_CELLS = 42
#The X coordinate for the center of each cell.
CELL_CENTER = {'1': -210, '2': -140, '3': -70, '4': 0, '5': 70, '6': 140, '7': 210}
#Cell size.
CELL = 70
#Y coordinate of the center of the bottom row.
BOTTOM_ROW_CENTER = -160
DOT_SIZE = 60
#The number of tokens that need to be connected in order to win.
WINNING_DOT = 4
R = "R"
Y = "Y"
E = 'E'



LEFTBOUND = [-245, -175, -105, -35, 35, 105, 175]
RIGHTBOUND = [-175, -105, -35, 35, 105, 175, 245]



PMOVE = 1
CMOVE = 0
#The number of lines needed to create the cell box.
CELL_BOX = 4
LEFT_GRID = -245
BOTTOM_GRID = -195
#The grid's boundary for the left or right side of the board.
#It will be negative if used to describe the left boundary.
GRID_X_BOUNDARY = 245
GRID_TOP_BOUNDARY = 225
GRID_BOTTOM_BOUNDARY = -195
#Position for all in game messages.
INTERFACE_X_POS = -240
INTERFACE_Y_POS = -250

#Introduction constants used for position, font size and font type.
LARGE_SIZE = 35
MEDIUM_SIZE = 20
SMALL_SIZE = 15
LEFT_ALIGN = -240
FONT = "Times New Roman"

#GLOBAL NOT CONSTANTS
#Max Pieces per row
maxPieces = 6
class Pieces(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, min(value, maxPieces))

pieces = Pieces({'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0})
turn = 0
numMoves  = 0
gameList = [[E, E, E, E, E, E, E],
            [E, E, E, E, E, E, E],
            [E, E, E, E, E, E, E],
            [E, E, E, E, E, E, E],
            [E, E, E, E, E, E, E],
            [E, E, E, E, E, E, E]]

def leftBound():
    leftMargin = []
    for multiplier in range(COLUMN):
        margins = LEFT_GRID + (multiplier * CELL)
        leftMargin.append(margins)
    return leftMargin

def rightBound(leftbound):
    rightMargin = []
    for margins in range(leftbound):
        rightCell = int(margins) + CELL
        print(rightCell)

#margins = leftBound()
#rightBound(margins)


#Main will call intro screen, which will create "intro" turtle screen
def main():
    intro()
    grid()
    initialClick()
    clickSetup()

def intro():

    #Welcome turtle, dark orange background, welcome w/ rules
    welcome = turtle.Turtle()
    intro = turtle.Screen()
    intro.bgcolor('dark orange')
    welcome.ht()
    welcome.up()

    #Header
    welcome.goto(LEFT_ALIGN, 100)
    welcome.write ("Welcome to Connect 4!",
                   font = (FONT, LARGE_SIZE, "bold"))

    #Rules
    welcome.goto(LEFT_ALIGN, 70)
    welcome.write("Rules:",
                  font = (FONT, MEDIUM_SIZE))
    welcome.goto(LEFT_ALIGN, 40)
    welcome.write("Players take turn to slide a token to the first available row in clicked column",
                  font = (FONT, SMALL_SIZE))
    welcome.goto(LEFT_ALIGN, 20)
    welcome.write("Goal is to get 4 in a row horizontally, vertically, or diagonally.",
                  font = (FONT, SMALL_SIZE))
    welcome.goto(LEFT_ALIGN, 0)
    welcome.write("If there are no more moves and nobody wins, the game is a tie",
                  font = (FONT, SMALL_SIZE))
    welcome.goto(LEFT_ALIGN, -20)
    welcome.write("Click anywhere on the screen to start the game.",
                  font = (FONT, SMALL_SIZE))
    welcome.goto(LEFT_ALIGN, -40)
    welcome.write("Press space to exit when you're done!",
                  font = (FONT, SMALL_SIZE))
    intro.exitonclick()

def grid():
    #Setting up our pretty screen with a light blue background.
    pretty = turtle.Screen()
    pretty.bgcolor('lightblue')
    #Setting up the turtle that draws the grid lines.
    grid = turtle.Turtle()
    grid.ht()
    speed = turtle.Screen()
    #Increases the speed of the grid.
    speed.tracer(20)
    #Loops every time a single row is drawn.
    for row in range(ROW):
        #Sets up the position for the next cell to be created.
        for col in range(COLUMN):
            grid.up()
            grid.setpos((col * CELL) + LEFT_GRID, (row * CELL) + BOTTOM_GRID)
            grid.pd()
            #This is where each individual cell is drawn.
            for i in range(CELL_BOX):
                grid.fd(CELL)
                grid.lt(90)

def clickSetup():
    #Sets up for any onkey commands and the click.
    clickGrid = turtle.Screen()
    clickGrid.bgcolor('lightblue')
    #Onclick command which will be executed once a click has gone through.
    #Calls the function clickMove once the player clicks.
    clickGrid.onclick(clickMove)
    #Onkey commands.
    clickGrid.onkey(clickGrid.bye, "space")
    clickGrid.onkey(save,"s")
    clickGrid.onkey(load,"l")
    #Listen is required in order to use any onkey commands.
    #It waits and listens until one of onkey command are used,
    #which will than call the corresponding function.
    clickGrid.listen()
    #Creats a infinite loop which basically always listens for a click.
    clickGrid.mainloop()

def clickMove(x, y):
    global numMoves, gameList, turn, INTERFACE
    interface = turtle.Turtle()
    interface.ht()
    #Checks to see if the click is within the y-axis of the grid.
    if y >= GRID_BOTTOM_BOUNDARY and y <= GRID_TOP_BOUNDARY:

        #Checks to see if the click is within the x-axis of the grid.
        if x >= - GRID_X_BOUNDARY and x <= GRID_X_BOUNDARY:
            #Calls the function gameOver to check if any player has won.
            winState = gameOver()

            #Checks if there are any empty cells and no one has won the game.
            if numMoves != NUM_CELLS and winState == False:

                #Checks to see if the computer had the previous turn and no one has won the game.
                if turn == CMOVE and winState == False:
                    #Updates gameList and also calls move.
                    #Executes player turn.
                    gameList = move(x)
                    #Updates winState to check if the player has won.
                    winState = gameOver()

                #Checks to see if the player and the previous turn and no one has won the game.
                if turn == PMOVE and winState == False:
                    #Choses a random number between 1-7,
                    #which will be where the cpu will play their token.
                    cpu = str(random.randrange(1, 8))
                    #Updates gameList and also calls move.
                    #Executes the computers turn.
                    gameList = compMove(cpu)
                    #Updates winState to check if the computer has won.
                    winState = gameOver()

                #Checks to see if someone has won this will be executed.
                if winState == True:
                    #Allows user to exit the screen on click.
                    exit = turtle.Screen()
                    exit.exitonclick()
            else:
                #If all 42 cells are occupied this will be executed.
                #This prints a message in the game screen,
                # telling the user it is a stalemate.
                interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
                interface.write("The game has resulted in a stalemate.",
                                font = (FONT, LARGE_SIZE))
                #Allows user to exit the screen on click.
                exit = turtle.Screen()
                exit.exitonclick()
        else:
            #This combined with the next else statement,
            #print an error message if the user has clicked outside the grid,
            #in either direction.
            #This will be executed if the user clicks outside of the grid in the x-axis.
            #Prints an error message in the game screen,
            # telling the user to click inside the grid.
            interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
            interface.write("Please click inside the grid.",
                            font = (FONT, MEDIUM_SIZE))
            #time.sleep is used to keep the text there for two seconds,
            # it does this by pausing for the two seconds.
            time.sleep(2)
            #This will than clear the turtle.
            interface.clear()
    else:
        #Prints an error message in the game screen,
        # telling the user to click inside the grid,
        #only if the user clicks above or below the board.
        interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
        interface.write("Please click inside the grid.",
                        font = (FONT, MEDIUM_SIZE))
        #time.sleep is used to keep the text there for two seconds,
        # it does this by pausing for the two seconds.
        time.sleep(2)
        #This will than clear the turtle.
        interface.clear()

def move(column):
    global gameList
    index = 0
    #for each left-bound cell
    for cell in range(len(LEFTBOUND)):
        #Parameters for clicking - It must be within the grid
        if column >= LEFTBOUND[cell] and column <= RIGHTBOUND[cell]:
            #Column will be cell converted into a string, +1
            #This is because the range starts from 0 and dictionary starts at 1
            index = cell
            red(str(index + 1))
            break

    if turn == PMOVE:
        #Passes new gameList to updateState
        gameList = updateState(index + 1)
    return gameList

def updateState(column):
    global gameList
    col = int(column)
    #Generates the list that will be returned
    #Takes the index given by move and updates the gameList to reflect recent move.
    gameList[(pieces[str(col)] -1 )][col -1] = R
    print(gameList, 'UPDATING "R" STATE')
    return gameList

def initialClick():
    global gameList, turn, numMoves
    #Randomizes if computer will go first or player first
    #If firstMove == 1, computer goes first.
    firstMove = random.randrange(1, 3)
    if firstMove == 1:
        turn = PMOVE
        cpu = str(random.randrange(1, COLUMN + 1))
        gameList = compMove(cpu)
        numMoves += 1

### PLAYER PIECE ###

def red(column):
    global pieces, gameList, turn, numMoves
    interface = turtle.Turtle()
    interface.ht()
    red = turtle.Turtle()
    red.ht()
    red.up()
    #Pieces * Cell length for Y value
    #Conditions for red to move are pieces in each column must be less than the rows
    #CPU also must have moved beforehand
    #if conditions are met, pieces[column] and numMoves incremented by 1, turn reflects player
    if pieces[column] < ROW and turn == CMOVE:
        red.goto(CELL_CENTER[column], BOTTOM_ROW_CENTER + (pieces[column] * CELL))
        red.dot(DOT_SIZE, 'red')
        pieces[column] += 1
        turn = PMOVE
        numMoves += 1
    else:
        interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
        interface.write("Please chose a column that is not filled.",
                        font = (FONT, MEDIUM_SIZE))
        time.sleep(2)
        interface.clear()


### WIN CONDITIONS ###

def gameOver():
    return False #horizontalCheck(), verticalCheck(), diagonalCheck()

def horizontalCheck():
    global gameList
    countR = 0
    countY = 0
    SubListDifference = 0
    for i in range(1, NUM_CELLS):
        SubList = int(i / (COLUMN + .1))
        if SubList != SubListDifference:
            countR = 0
        if SubList != SubListDifference:
            countY = 0
        placeInSubList = (i % COLUMN) - 1
        accessToSubList = gameList[SubList]
        if R in accessToSubList[placeInSubList]:
            countR += 1
        else:
            countR = 0
        if countR == WINNING_DOT:
            print("Red Wins horizontally!")
            return True
        if Y in accessToSubList[placeInSubList]:
            countY += 1
        else:
            countY = 0
        if countY == WINNING_DOT:
            print("Yellow Wins horizontally!")
            return True
        SubListDifference = SubList
    return False

def verticalCheck(row, col):

    win = False
    consec = 0

    for cell in range (row, col):
        if gameList[cell][col] == gameList[row][col]:
            consec += 1
        else:
            break

    if consec >= 4:
        win = True

    return win

def diagonalCheck():
    global gameList
    #The r in the variables stand for right.
    #Which is used for any of the diagonal checks,
    # that are stacked towards the right side.
    #The l in the variables stand for left.
    #Which is used for any of the diagonal checks,
    # that are stacked towards the left side.
    #Any variable with "second" in it, is used for diagonal check,
    # that doesn't begin in the first subList in gameList.
    #All the counts, are used to keep track of the amount of R or Y in a row.
    rCount = 0
    rCountYellow = 0
    secondRCount = 0
    secondRCountYellow = 0
    #All subLists's are used to isolate a single position in the 2D list.
    rSubList = []
    secondRSubList = []
    positionInRSubList = 0
    #numOfSubList is used to get the correct subList that is being tested.
    numOfSubList = 0
    #Loops 3 times because there are 6 possible diagonal checks from the left.
    #We split up the 6 checks into two categories, which is why it loops 3 times.
    for i in range (3):
        for variablePosition in range(ROW):
            #Used to make sure nothing is out of the boards range.
            if positionInRSubList < ROW and numOfSubList < ROW:
                secondRSubList = gameList[numOfSubList][variablePosition]
                rSubList = gameList[variablePosition][positionInRSubList + 1]
                #Accumulating each time it loops.
                positionInRSubList += 1
                numOfSubList += 1
            #Checks if R is in that specific position
            if R in rSubList:
                #Count increases by 1 if R is in the position.
                rCount += 1
            else:
                #If R is not in the position that count is reset to 0.
                rCount = 0
            #once count is 4, it prints who won.
            if rCount == WINNING_DOT:
                print("Red Wins diagonally!!")
                return True
            #Checks if Y is in that specific position
            if Y in rSubList:
                #Count increases by 1 if Y is in the position.
                rCountYellow += 1
            else:
                #If Y is not in the position that count is reset to 0.
                rCountYellow = 0
            #once count is 4, it prints who won.
            if rCountYellow == WINNING_DOT:
                print("Yellow Wins diagonally!")
                return True
            if R in secondRSubList:
                secondRCount += 1
            else:
                secondRCount = 0
            if secondRCount == WINNING_DOT:
                print("Red Wins diagonally!")
                return True
            if Y in secondRSubList:
                secondRCountYellow += 1
            else:
                secondRCountYellow = 0
            if secondRCountYellow == WINNING_DOT:
                print("Yellow Wins diagonally!")
                return True
        #Each time the 6 loops are done, it resets the sublists.
        rSubList = []
        #Each time the 6 loops are done,
        # it resets the positionInSubList and numOfSubList,
        # but it also increase by 1,
        # from the previous loop (first Loop in the nested Loop).
        positionInRSubList = i + 1
        numOfSubList = i + 1
        rCount = 0
        rCountYellow = 0
        secondRCount = 0
        secondRCountYellow = 0
    return False


### COMPUTER FUNCTIONS ###
def compDot(column):
    global turn, numMoves
    interface = turtle.Turtle()
    interface.ht()
    #Computer turtle
    yellow = turtle.Turtle()
    yellow.ht()
    yellow.up()

    #It will only create a piece if these conditionals are met.
    #That means player must have moved first and also,
    #the specific position in the gameList must be empty and the column cannot be filled
    #It will the change turn to reflect computer moved.
    #Pieces[column] and numMoves get incremented.
    if pieces[column] < ROW and turn == PMOVE:
        yellow.goto(CELL_CENTER[column], BOTTOM_ROW_CENTER + (pieces[column] * CELL))
        yellow.dot(DOT_SIZE, 'yellow')
        turn = CMOVE
        pieces[column] += 1
        numMoves += 1
    else:
        interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
        interface.write("Yellow tried to make an illegal move, please click again.",
                        font = (FONT, MEDIUM_SIZE))
        time.sleep(1.5)
        interface.clear()


def compMove(column):
    global gameList
    compDot(str(column))
    #If turn == Computer, update the gameList
    if turn == CMOVE:
        gameList = cUpdateState(column)
    return gameList

def cUpdateState(column):
    global gameList
    col = int(column)
    #Replaces the proper index that was passed from comp -> cMove -> cUpdate to be Y.
    #Reflects in the gameList
    gameList[(pieces[str(col)] -1 )][col -1] = 'Y'
    print(gameList, 'UPDATING THROUGH CUPDATESTATE')
    return gameList


def save():
    interface = turtle.Turtle()
    interface.ht()
    # put the gameList into a txt file
    # end result just letter
    interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
    interface.write("The game has been successfully saved.",
                        font = (FONT, MEDIUM_SIZE))
    time.sleep(1.5)
    interface.clear()
    with open("tempGameState.txt", "w") as f:
        for row in gameList:
            rowStr = ''
            for cell in row:
                rowStr += cell + ''
            f.write(rowStr + '\n')


# method to load the game
# parameters: nothing
# goes back to grid
def load():
    global pieces
    interface = turtle.Turtle()
    interface.ht()
    interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
    interface.write("Please click on the screen to open your loaded game!",
                        font = (FONT, MEDIUM_SIZE))
    time.sleep(1.5)
    interface.clear()
    savedFile = open("tempGameState.txt","r")
    reading = savedFile.read()
    reading = reading.replace('\n',"")
    reading = reading.strip("")

    # method is to close the old grid, making a new grid
    def closeScreen():
        global turn
        #resets turn
        turn = 0
        closewn = turtle.Screen()
        closewn.exitonclick()
        grid()

    # reset the dictionary
    # params: the dictionary and the value we want it to reset to
    # return the original dictionary
    def newValue(dict,reset_to):
        global numMoves
        #resets numMoves
        numMoves = 0
        for keys in dict:
            # look at the whatever keys is and makes it = 0
            dict[keys] = reset_to
        return dict


    # convert to file into a list
    #param: the saved file
    # return the saved file as a nested list
    def to2dList(saveFile):
        converter = []
        row = []
        # loops it 42 times
        for cell in range(len(saveFile)):
            # if row has 7 letters inside the list
            # it will go to the converter
            if len(row) == 7:
                converter.append(row)
                row = [saveFile[cell]]
            # keeps adding the letters to row
            else:
                row.append(saveFile[cell])
        converter.append(row)
        return converter


    # method to find where red and yellow where made on the board
    # param: the saved filed as a nested list
    # returns: nothing
    def reDot(savedList):
        global gameList
        gameList = savedList
        #look at the sublist
        for sublist in range(len(savedList)):
            #looks at the sublist index
            for sublistIndex in range(len(savedList[sublist])):
                letter = savedList[sublist][sublistIndex]
                # if  there is a "R" then it will take that index
                # and go to the red function and stamp it on that col
                if letter == "R":
                    # add a 1 because the index can equal zero and our col doesn't
                    # start from 0
                    savedRed(sublistIndex + 1)
                # if  there is a "Y" then it will take that index
                # and go to the comp function and stamp it on that col
                if letter == "Y":
                    # add a 1 because the index can equal zero and our col doesn't
                    # start from 0
                    savedComp(sublistIndex + 1)


    # re-dots all the red dots from the saved file
    def savedRed(column):
        global pieces, turn, numMoves
        red = turtle.Turtle()
        red.ht()
        red.up()
        column = str(column)
        #Pieces * Cell length for Y value
        #listIndex = column
        red.goto(CELL_CENTER[column], BOTTOM_ROW_CENTER + (pieces[column] * CELL))
        red.dot(DOT_SIZE, 'red')
        pieces[column] += 1
        turn = PMOVE
        numMoves += 1

    # re-dot all the yellow dots from the saved file
    def savedComp(column):
        global pieces, turn, numMoves
        yellow = turtle.Turtle()
        yellow.ht()
        yellow.up()
        column = str(column)
        yellow.goto(CELL_CENTER[column], BOTTOM_ROW_CENTER + (pieces[column] * CELL))
        yellow.dot(DOT_SIZE, 'yellow')
        turn = CMOVE
        pieces[column] += 1
        numMoves += 1

    closeScreen()
    pieces = newValue(pieces, 0)
    ToList = to2dList(reading)
    reDot(ToList)
    clickSetup()

main()
clone this paste RAW Paste Data

#Connect 4

#The objective of the game is for player or computer to try to get 4 in a row
#You can get win by achieving 4 colors in a row horizontally, vertically, or diagonally
#There will be a tie if the grid is filled and nobody wins.
#Win or lose, press space to start a new game
#Good luck!

import turtle
import random
import time

#GLOBAL CONSTANTS
ROW = 6
COLUMN = 7
NUM_CELLS = 42
#The X coordinate for the center of each cell.
CELL_CENTER = {'1': -210, '2': -140, '3': -70, '4': 0, '5': 70, '6': 140, '7': 210}
#Cell size.
CELL = 70
#Y coordinate of the center of the bottom row.
BOTTOM_ROW_CENTER = -160
DOT_SIZE = 60
#The number of tokens that need to be connected in order to win.
WINNING_DOT = 4
R = "R"
Y = "Y"
E = 'E'



LEFTBOUND = [-245, -175, -105, -35, 35, 105, 175]
RIGHTBOUND = [-175, -105, -35, 35, 105, 175, 245]



PMOVE = 1
CMOVE = 0
#The number of lines needed to create the cell box.
CELL_BOX = 4
LEFT_GRID = -245
BOTTOM_GRID = -195
#The grid's boundary for the left or right side of the board.
#It will be negative if used to describe the left boundary.
GRID_X_BOUNDARY = 245
GRID_TOP_BOUNDARY = 225
GRID_BOTTOM_BOUNDARY = -195
#Position for all in game messages.
INTERFACE_X_POS = -240
INTERFACE_Y_POS = -250

#Introduction constants used for position, font size and font type.
LARGE_SIZE = 35
MEDIUM_SIZE = 20
SMALL_SIZE = 15
LEFT_ALIGN = -240
FONT = "Times New Roman"

#GLOBAL NOT CONSTANTS
#Max Pieces per row
maxPieces = 6
class Pieces(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, min(value, maxPieces))

pieces = Pieces({'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0})
turn = 0
numMoves  = 0
gameList = [[E, E, E, E, E, E, E],
            [E, E, E, E, E, E, E],
            [E, E, E, E, E, E, E],
            [E, E, E, E, E, E, E],
            [E, E, E, E, E, E, E],
            [E, E, E, E, E, E, E]]

def leftBound():
    leftMargin = []
    for multiplier in range(COLUMN):
        margins = LEFT_GRID + (multiplier * CELL)
        leftMargin.append(margins)
    return leftMargin

def rightBound(leftbound):
    rightMargin = []
    for margins in range(leftbound):
        rightCell = int(margins) + CELL
        print(rightCell)

#margins = leftBound()
#rightBound(margins)


#Main will call intro screen, which will create "intro" turtle screen
def main():
    intro()
    grid()
    initialClick()
    clickSetup()

def intro():

    #Welcome turtle, dark orange background, welcome w/ rules
    welcome = turtle.Turtle()
    intro = turtle.Screen()
    intro.bgcolor('dark orange')
    welcome.ht()
    welcome.up()

    #Header
    welcome.goto(LEFT_ALIGN, 100)
    welcome.write ("Welcome to Connect 4!",
                   font = (FONT, LARGE_SIZE, "bold"))

    #Rules
    welcome.goto(LEFT_ALIGN, 70)
    welcome.write("Rules:",
                  font = (FONT, MEDIUM_SIZE))
    welcome.goto(LEFT_ALIGN, 40)
    welcome.write("Players take turn to slide a token to the first available row in clicked column",
                  font = (FONT, SMALL_SIZE))
    welcome.goto(LEFT_ALIGN, 20)
    welcome.write("Goal is to get 4 in a row horizontally, vertically, or diagonally.",
                  font = (FONT, SMALL_SIZE))
    welcome.goto(LEFT_ALIGN, 0)
    welcome.write("If there are no more moves and nobody wins, the game is a tie",
                  font = (FONT, SMALL_SIZE))
    welcome.goto(LEFT_ALIGN, -20)
    welcome.write("Click anywhere on the screen to start the game.",
                  font = (FONT, SMALL_SIZE))
    welcome.goto(LEFT_ALIGN, -40)
    welcome.write("Press space to exit when you're done!",
                  font = (FONT, SMALL_SIZE))
    intro.exitonclick()

def grid():
    #Setting up our pretty screen with a light blue background.
    pretty = turtle.Screen()
    pretty.bgcolor('lightblue')
    #Setting up the turtle that draws the grid lines.
    grid = turtle.Turtle()
    grid.ht()
    speed = turtle.Screen()
    #Increases the speed of the grid.
    speed.tracer(20)
    #Loops every time a single row is drawn.
    for row in range(ROW):
        #Sets up the position for the next cell to be created.
        for col in range(COLUMN):
            grid.up()
            grid.setpos((col * CELL) + LEFT_GRID, (row * CELL) + BOTTOM_GRID)
            grid.pd()
            #This is where each individual cell is drawn.
            for i in range(CELL_BOX):
                grid.fd(CELL)
                grid.lt(90)

def clickSetup():
    #Sets up for any onkey commands and the click.
    clickGrid = turtle.Screen()
    clickGrid.bgcolor('lightblue')
    #Onclick command which will be executed once a click has gone through.
    #Calls the function clickMove once the player clicks.
    clickGrid.onclick(clickMove)
    #Onkey commands.
    clickGrid.onkey(clickGrid.bye, "space")
    clickGrid.onkey(save,"s")
    clickGrid.onkey(load,"l")
    #Listen is required in order to use any onkey commands.
    #It waits and listens until one of onkey command are used,
    #which will than call the corresponding function.
    clickGrid.listen()
    #Creats a infinite loop which basically always listens for a click.
    clickGrid.mainloop()

def clickMove(x, y):
    global numMoves, gameList, turn, INTERFACE
    interface = turtle.Turtle()
    interface.ht()
    #Checks to see if the click is within the y-axis of the grid.
    if y >= GRID_BOTTOM_BOUNDARY and y <= GRID_TOP_BOUNDARY:

        #Checks to see if the click is within the x-axis of the grid.
        if x >= - GRID_X_BOUNDARY and x <= GRID_X_BOUNDARY:
            #Calls the function gameOver to check if any player has won.
            winState = gameOver()

            #Checks if there are any empty cells and no one has won the game.
            if numMoves != NUM_CELLS and winState == False:

                #Checks to see if the computer had the previous turn and no one has won the game.
                if turn == CMOVE and winState == False:
                    #Updates gameList and also calls move.
                    #Executes player turn.
                    gameList = move(x)
                    #Updates winState to check if the player has won.
                    winState = gameOver()

                #Checks to see if the player and the previous turn and no one has won the game.
                if turn == PMOVE and winState == False:
                    #Choses a random number between 1-7,
                    #which will be where the cpu will play their token.
                    cpu = str(random.randrange(1, 8))
                    #Updates gameList and also calls move.
                    #Executes the computers turn.
                    gameList = compMove(cpu)
                    #Updates winState to check if the computer has won.
                    winState = gameOver()

                #Checks to see if someone has won this will be executed.
                if winState == True:
                    #Allows user to exit the screen on click.
                    exit = turtle.Screen()
                    exit.exitonclick()
            else:
                #If all 42 cells are occupied this will be executed.
                #This prints a message in the game screen,
                # telling the user it is a stalemate.
                interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
                interface.write("The game has resulted in a stalemate.",
                                font = (FONT, LARGE_SIZE))
                #Allows user to exit the screen on click.
                exit = turtle.Screen()
                exit.exitonclick()
        else:
            #This combined with the next else statement,
            #print an error message if the user has clicked outside the grid,
            #in either direction.
            #This will be executed if the user clicks outside of the grid in the x-axis.
            #Prints an error message in the game screen,
            # telling the user to click inside the grid.
            interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
            interface.write("Please click inside the grid.",
                            font = (FONT, MEDIUM_SIZE))
            #time.sleep is used to keep the text there for two seconds,
            # it does this by pausing for the two seconds.
            time.sleep(2)
            #This will than clear the turtle.
            interface.clear()
    else:
        #Prints an error message in the game screen,
        # telling the user to click inside the grid,
        #only if the user clicks above or below the board.
        interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
        interface.write("Please click inside the grid.",
                        font = (FONT, MEDIUM_SIZE))
        #time.sleep is used to keep the text there for two seconds,
        # it does this by pausing for the two seconds.
        time.sleep(2)
        #This will than clear the turtle.
        interface.clear()

def move(column):
    global gameList
    index = 0
    #for each left-bound cell
    for cell in range(len(LEFTBOUND)):
        #Parameters for clicking - It must be within the grid
        if column >= LEFTBOUND[cell] and column <= RIGHTBOUND[cell]:
            #Column will be cell converted into a string, +1
            #This is because the range starts from 0 and dictionary starts at 1
            index = cell
            red(str(index + 1))
            break

    if turn == PMOVE:
        #Passes new gameList to updateState
        gameList = updateState(index + 1)
    return gameList

def updateState(column):
    global gameList
    col = int(column)
    #Generates the list that will be returned
    #Takes the index given by move and updates the gameList to reflect recent move.
    gameList[(pieces[str(col)] -1 )][col -1] = R
    print(gameList, 'UPDATING "R" STATE')
    return gameList

def initialClick():
    global gameList, turn, numMoves
    #Randomizes if computer will go first or player first
    #If firstMove == 1, computer goes first.
    firstMove = random.randrange(1, 3)
    if firstMove == 1:
        turn = PMOVE
        cpu = str(random.randrange(1, COLUMN + 1))
        gameList = compMove(cpu)
        numMoves += 1

### PLAYER PIECE ###

def red(column):
    global pieces, gameList, turn, numMoves
    interface = turtle.Turtle()
    interface.ht()
    red = turtle.Turtle()
    red.ht()
    red.up()
    #Pieces * Cell length for Y value
    #Conditions for red to move are pieces in each column must be less than the rows
    #CPU also must have moved beforehand
    #if conditions are met, pieces[column] and numMoves incremented by 1, turn reflects player
    if pieces[column] < ROW and turn == CMOVE:
        red.goto(CELL_CENTER[column], BOTTOM_ROW_CENTER + (pieces[column] * CELL))
        red.dot(DOT_SIZE, 'red')
        pieces[column] += 1
        turn = PMOVE
        numMoves += 1
    else:
        interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
        interface.write("Please chose a column that is not filled.",
                        font = (FONT, MEDIUM_SIZE))
        time.sleep(2)
        interface.clear()


### WIN CONDITIONS ###

def gameOver():
    return False #horizontalCheck(), verticalCheck(), diagonalCheck()

def horizontalCheck():
    global gameList
    countR = 0
    countY = 0
    SubListDifference = 0
    for i in range(1, NUM_CELLS):
        SubList = int(i / (COLUMN + .1))
        if SubList != SubListDifference:
            countR = 0
        if SubList != SubListDifference:
            countY = 0
        placeInSubList = (i % COLUMN) - 1
        accessToSubList = gameList[SubList]
        if R in accessToSubList[placeInSubList]:
            countR += 1
        else:
            countR = 0
        if countR == WINNING_DOT:
            print("Red Wins horizontally!")
            return True
        if Y in accessToSubList[placeInSubList]:
            countY += 1
        else:
            countY = 0
        if countY == WINNING_DOT:
            print("Yellow Wins horizontally!")
            return True
        SubListDifference = SubList
    return False

def verticalCheck(row, col):

    win = False
    consec = 0

    for cell in range (row, col):
        if gameList[cell][col] == gameList[row][col]:
            consec += 1
        else:
            break

    if consec >= 4:
        win = True

    return win

def diagonalCheck():
    global gameList
    #The r in the variables stand for right.
    #Which is used for any of the diagonal checks,
    # that are stacked towards the right side.
    #The l in the variables stand for left.
    #Which is used for any of the diagonal checks,
    # that are stacked towards the left side.
    #Any variable with "second" in it, is used for diagonal check,
    # that doesn't begin in the first subList in gameList.
    #All the counts, are used to keep track of the amount of R or Y in a row.
    rCount = 0
    rCountYellow = 0
    secondRCount = 0
    secondRCountYellow = 0
    #All subLists's are used to isolate a single position in the 2D list.
    rSubList = []
    secondRSubList = []
    positionInRSubList = 0
    #numOfSubList is used to get the correct subList that is being tested.
    numOfSubList = 0
    #Loops 3 times because there are 6 possible diagonal checks from the left.
    #We split up the 6 checks into two categories, which is why it loops 3 times.
    for i in range (3):
        for variablePosition in range(ROW):
            #Used to make sure nothing is out of the boards range.
            if positionInRSubList < ROW and numOfSubList < ROW:
                secondRSubList = gameList[numOfSubList][variablePosition]
                rSubList = gameList[variablePosition][positionInRSubList + 1]
                #Accumulating each time it loops.
                positionInRSubList += 1
                numOfSubList += 1
            #Checks if R is in that specific position
            if R in rSubList:
                #Count increases by 1 if R is in the position.
                rCount += 1
            else:
                #If R is not in the position that count is reset to 0.
                rCount = 0
            #once count is 4, it prints who won.
            if rCount == WINNING_DOT:
                print("Red Wins diagonally!!")
                return True
            #Checks if Y is in that specific position
            if Y in rSubList:
                #Count increases by 1 if Y is in the position.
                rCountYellow += 1
            else:
                #If Y is not in the position that count is reset to 0.
                rCountYellow = 0
            #once count is 4, it prints who won.
            if rCountYellow == WINNING_DOT:
                print("Yellow Wins diagonally!")
                return True
            if R in secondRSubList:
                secondRCount += 1
            else:
                secondRCount = 0
            if secondRCount == WINNING_DOT:
                print("Red Wins diagonally!")
                return True
            if Y in secondRSubList:
                secondRCountYellow += 1
            else:
                secondRCountYellow = 0
            if secondRCountYellow == WINNING_DOT:
                print("Yellow Wins diagonally!")
                return True
        #Each time the 6 loops are done, it resets the sublists.
        rSubList = []
        #Each time the 6 loops are done,
        # it resets the positionInSubList and numOfSubList,
        # but it also increase by 1,
        # from the previous loop (first Loop in the nested Loop).
        positionInRSubList = i + 1
        numOfSubList = i + 1
        rCount = 0
        rCountYellow = 0
        secondRCount = 0
        secondRCountYellow = 0
    return False


### COMPUTER FUNCTIONS ###
def compDot(column):
    global turn, numMoves
    interface = turtle.Turtle()
    interface.ht()
    #Computer turtle
    yellow = turtle.Turtle()
    yellow.ht()
    yellow.up()

    #It will only create a piece if these conditionals are met.
    #That means player must have moved first and also,
    #the specific position in the gameList must be empty and the column cannot be filled
    #It will the change turn to reflect computer moved.
    #Pieces[column] and numMoves get incremented.
    if pieces[column] < ROW and turn == PMOVE:
        yellow.goto(CELL_CENTER[column], BOTTOM_ROW_CENTER + (pieces[column] * CELL))
        yellow.dot(DOT_SIZE, 'yellow')
        turn = CMOVE
        pieces[column] += 1
        numMoves += 1
    else:
        interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
        interface.write("Yellow tried to make an illegal move, please click again.",
                        font = (FONT, MEDIUM_SIZE))
        time.sleep(1.5)
        interface.clear()


def compMove(column):
    global gameList
    compDot(str(column))
    #If turn == Computer, update the gameList
    if turn == CMOVE:
        gameList = cUpdateState(column)
    return gameList

def cUpdateState(column):
    global gameList
    col = int(column)
    #Replaces the proper index that was passed from comp -> cMove -> cUpdate to be Y.
    #Reflects in the gameList
    gameList[(pieces[str(col)] -1 )][col -1] = 'Y'
    print(gameList, 'UPDATING THROUGH CUPDATESTATE')
    return gameList


def save():
    interface = turtle.Turtle()
    interface.ht()
    # put the gameList into a txt file
    # end result just letter
    interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
    interface.write("The game has been successfully saved.",
                        font = (FONT, MEDIUM_SIZE))
    time.sleep(1.5)
    interface.clear()
    with open("tempGameState.txt", "w") as f:
        for row in gameList:
            rowStr = ''
            for cell in row:
                rowStr += cell + ''
            f.write(rowStr + '\n')


# method to load the game
# parameters: nothing
# goes back to grid
def load():
    global pieces
    interface = turtle.Turtle()
    interface.ht()
    interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
    interface.write("Please click on the screen to open your loaded game!",
                        font = (FONT, MEDIUM_SIZE))
    time.sleep(1.5)
    interface.clear()
    savedFile = open("tempGameState.txt","r")
    reading = savedFile.read()
    reading = reading.replace('\n',"")
    reading = reading.strip("")

    # method is to close the old grid, making a new grid
    def closeScreen():
        global turn
        #resets turn
        turn = 0
        closewn = turtle.Screen()
        closewn.exitonclick()
        grid()

    # reset the dictionary
    # params: the dictionary and the value we want it to reset to
    # return the original dictionary
    def newValue(dict,reset_to):
        global numMoves
        #resets numMoves
        numMoves = 0
        for keys in dict:
            # look at the whatever keys is and makes it = 0
            dict[keys] = reset_to
        return dict


    # convert to file into a list
    #param: the saved file
    # return the saved file as a nested list
    def to2dList(saveFile):
        converter = []
        row = []
        # loops it 42 times
        for cell in range(len(saveFile)):
            # if row has 7 letters inside the list
            # it will go to the converter
            if len(row) == 7:
                converter.append(row)
                row = [saveFile[cell]]
            # keeps adding the letters to row
            else:
                row.append(saveFile[cell])
        converter.append(row)
        return converter


    # method to find where red and yellow where made on the board
    # param: the saved filed as a nested list
    # returns: nothing
    def reDot(savedList):
        global gameList
        gameList = savedList
        #look at the sublist
        for sublist in range(len(savedList)):
            #looks at the sublist index
            for sublistIndex in range(len(savedList[sublist])):
                letter = savedList[sublist][sublistIndex]
                # if  there is a "R" then it will take that index
                # and go to the red function and stamp it on that col
                if letter == "R":
                    # add a 1 because the index can equal zero and our col doesn't
                    # start from 0
                    savedRed(sublistIndex + 1)
                # if  there is a "Y" then it will take that index
                # and go to the comp function and stamp it on that col
                if letter == "Y":
                    # add a 1 because the index can equal zero and our col doesn't
                    # start from 0
                    savedComp(sublistIndex + 1)


    # re-dots all the red dots from the saved file
    def savedRed(column):
        global pieces, turn, numMoves
        red = turtle.Turtle()
        red.ht()
        red.up()
        column = str(column)
        #Pieces * Cell length for Y value
        #listIndex = column
        red.goto(CELL_CENTER[column], BOTTOM_ROW_CENTER + (pieces[column] * CELL))
        red.dot(DOT_SIZE, 'red')
        pieces[column] += 1
        turn = PMOVE
        numMoves += 1

    # re-dot all the yellow dots from the saved file
    def savedComp(column):
        global pieces, turn, numMoves
        yellow = turtle.Turtle()
        yellow.ht()
        yellow.up()
        column = str(column)
        yellow.goto(CELL_CENTER[column], BOTTOM_ROW_CENTER + (pieces[column] * CELL))
        yellow.dot(DOT_SIZE, 'yellow')
        turn = CMOVE
        pieces[column] += 1
        numMoves += 1

    closeScreen()
    pieces = newValue(pieces, 0)
    ToList = to2dList(reading)
    reDot(ToList)
    clickSetup()

main()
Pastebin.com Tools & Applications
iPhone/iPad  Windows  Firefox  Chrome  WebOS  Android  Mac  Opera  Click.to  UNIX  WinPhone
create new paste  |  api  |  trends  |  syntax languages  |  faq  |  tools  |  privacy  |  cookies  |  contact  |  dmca  |  advertise on pastebin  |  scraping  |  go PRO
Follow us: pastebin on facebook  |  pastebin on twitter  |  pastebin in the news
Dedicated Server Hosting by Steadfast
Pastebin v3.11 rendered in: 0.006 seconds
Site design & logo © 2015 Pastebin; user contributions (pastes) licensed under cc by-sa 3.0  Top
#Connect 4

#The objective of the game is for player or computer to try to get 4 in a row
#You can get win by achieving 4 colors in a row horizontally, vertically, or diagonally
#There will be a tie if the grid is filled and nobody wins.
#Win or lose, press space to start a new game
#Good luck!

import turtle
import random
import time

#GLOBAL CONSTANTS
ROW = 6
COLUMN = 7
NUM_CELLS = 42
#The X coordinate for the center of each cell.
CELL_CENTER = {'1': -210, '2': -140, '3': -70, '4': 0, '5': 70, '6': 140, '7': 210}
#Cell size.
CELL = 70
#Y coordinate of the center of the bottom row.
BOTTOM_ROW_CENTER = -160
DOT_SIZE = 60
#The number of tokens that need to be connected in order to win.
WINNING_DOT = 4
R = "R"
Y = "Y"
E = 'E'



LEFTBOUND = [-245, -175, -105, -35, 35, 105, 175]
RIGHTBOUND = [-175, -105, -35, 35, 105, 175, 245]



PMOVE = 1
CMOVE = 0
#The number of lines needed to create the cell box.
CELL_BOX = 4
LEFT_GRID = -245
BOTTOM_GRID = -195
#The grid's boundary for the left or right side of the board.
#It will be negative if used to describe the left boundary.
GRID_X_BOUNDARY = 245
GRID_TOP_BOUNDARY = 225
GRID_BOTTOM_BOUNDARY = -195
#Position for all in game messages.
INTERFACE_X_POS = -240
INTERFACE_Y_POS = -250

#Introduction constants used for position, font size and font type.
LARGE_SIZE = 35
MEDIUM_SIZE = 20
SMALL_SIZE = 15
LEFT_ALIGN = -240
FONT = "Times New Roman"

#GLOBAL NOT CONSTANTS
#Max Pieces per row
maxPieces = 6
class Pieces(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, min(value, maxPieces))

pieces = Pieces({'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0})
turn = 0
numMoves  = 0
gameList = [[E, E, E, E, E, E, E],
            [E, E, E, E, E, E, E],
            [E, E, E, E, E, E, E],
            [E, E, E, E, E, E, E],
            [E, E, E, E, E, E, E],
            [E, E, E, E, E, E, E]]

def leftBound():
    leftMargin = []
    for multiplier in range(COLUMN):
        margins = LEFT_GRID + (multiplier * CELL)
        leftMargin.append(margins)
    return leftMargin

def rightBound(leftbound):
    rightMargin = []
    for margins in range(leftbound):
        rightCell = int(margins) + CELL
        print(rightCell)

#margins = leftBound()
#rightBound(margins)


#Main will call intro screen, which will create "intro" turtle screen
def main():
    intro()
    grid()
    initialClick()
    clickSetup()

def intro():

    #Welcome turtle, dark orange background, welcome w/ rules
    welcome = turtle.Turtle()
    intro = turtle.Screen()
    intro.bgcolor('dark orange')
    welcome.ht()
    welcome.up()

    #Header
    welcome.goto(LEFT_ALIGN, 100)
    welcome.write ("Welcome to Connect 4!",
                   font = (FONT, LARGE_SIZE, "bold"))

    #Rules
    welcome.goto(LEFT_ALIGN, 70)
    welcome.write("Rules:",
                  font = (FONT, MEDIUM_SIZE))
    welcome.goto(LEFT_ALIGN, 40)
    welcome.write("Players take turn to slide a token to the first available row in clicked column",
                  font = (FONT, SMALL_SIZE))
    welcome.goto(LEFT_ALIGN, 20)
    welcome.write("Goal is to get 4 in a row horizontally, vertically, or diagonally.",
                  font = (FONT, SMALL_SIZE))
    welcome.goto(LEFT_ALIGN, 0)
    welcome.write("If there are no more moves and nobody wins, the game is a tie",
                  font = (FONT, SMALL_SIZE))
    welcome.goto(LEFT_ALIGN, -20)
    welcome.write("Click anywhere on the screen to start the game.",
                  font = (FONT, SMALL_SIZE))
    welcome.goto(LEFT_ALIGN, -40)
    welcome.write("Press space to exit when you're done!",
                  font = (FONT, SMALL_SIZE))
    intro.exitonclick()

def grid():
    #Setting up our pretty screen with a light blue background.
    pretty = turtle.Screen()
    pretty.bgcolor('lightblue')
    #Setting up the turtle that draws the grid lines.
    grid = turtle.Turtle()
    grid.ht()
    speed = turtle.Screen()
    #Increases the speed of the grid.
    speed.tracer(20)
    #Loops every time a single row is drawn.
    for row in range(ROW):
        #Sets up the position for the next cell to be created.
        for col in range(COLUMN):
            grid.up()
            grid.setpos((col * CELL) + LEFT_GRID, (row * CELL) + BOTTOM_GRID)
            grid.pd()
            #This is where each individual cell is drawn.
            for i in range(CELL_BOX):
                grid.fd(CELL)
                grid.lt(90)

def clickSetup():
    #Sets up for any onkey commands and the click.
    clickGrid = turtle.Screen()
    clickGrid.bgcolor('lightblue')
    #Onclick command which will be executed once a click has gone through.
    #Calls the function clickMove once the player clicks.
    clickGrid.onclick(clickMove)
    #Onkey commands.
    clickGrid.onkey(clickGrid.bye, "space")
    clickGrid.onkey(save,"s")
    clickGrid.onkey(load,"l")
    #Listen is required in order to use any onkey commands.
    #It waits and listens until one of onkey command are used,
    #which will than call the corresponding function.
    clickGrid.listen()
    #Creats a infinite loop which basically always listens for a click.
    clickGrid.mainloop()

def clickMove(x, y):
    global numMoves, gameList, turn, INTERFACE
    interface = turtle.Turtle()
    interface.ht()
    #Checks to see if the click is within the y-axis of the grid.
    if y >= GRID_BOTTOM_BOUNDARY and y <= GRID_TOP_BOUNDARY:

        #Checks to see if the click is within the x-axis of the grid.
        if x >= - GRID_X_BOUNDARY and x <= GRID_X_BOUNDARY:
            #Calls the function gameOver to check if any player has won.
            winState = gameOver()

            #Checks if there are any empty cells and no one has won the game.
            if numMoves != NUM_CELLS and winState == False:

                #Checks to see if the computer had the previous turn and no one has won the game.
                if turn == CMOVE and winState == False:
                    #Updates gameList and also calls move.
                    #Executes player turn.
                    gameList = move(x)
                    #Updates winState to check if the player has won.
                    winState = gameOver()

                #Checks to see if the player and the previous turn and no one has won the game.
                if turn == PMOVE and winState == False:
                    #Choses a random number between 1-7,
                    #which will be where the cpu will play their token.
                    cpu = str(random.randrange(1, 8))
                    #Updates gameList and also calls move.
                    #Executes the computers turn.
                    gameList = compMove(cpu)
                    #Updates winState to check if the computer has won.
                    winState = gameOver()

                #Checks to see if someone has won this will be executed.
                if winState == True:
                    #Allows user to exit the screen on click.
                    exit = turtle.Screen()
                    exit.exitonclick()
            else:
                #If all 42 cells are occupied this will be executed.
                #This prints a message in the game screen,
                # telling the user it is a stalemate.
                interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
                interface.write("The game has resulted in a stalemate.",
                                font = (FONT, LARGE_SIZE))
                #Allows user to exit the screen on click.
                exit = turtle.Screen()
                exit.exitonclick()
        else:
            #This combined with the next else statement,
            #print an error message if the user has clicked outside the grid,
            #in either direction.
            #This will be executed if the user clicks outside of the grid in the x-axis.
            #Prints an error message in the game screen,
            # telling the user to click inside the grid.
            interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
            interface.write("Please click inside the grid.",
                            font = (FONT, MEDIUM_SIZE))
            #time.sleep is used to keep the text there for two seconds,
            # it does this by pausing for the two seconds.
            time.sleep(2)
            #This will than clear the turtle.
            interface.clear()
    else:
        #Prints an error message in the game screen,
        # telling the user to click inside the grid,
        #only if the user clicks above or below the board.
        interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
        interface.write("Please click inside the grid.",
                        font = (FONT, MEDIUM_SIZE))
        #time.sleep is used to keep the text there for two seconds,
        # it does this by pausing for the two seconds.
        time.sleep(2)
        #This will than clear the turtle.
        interface.clear()

def move(column):
    global gameList
    index = 0
    #for each left-bound cell
    for cell in range(len(LEFTBOUND)):
        #Parameters for clicking - It must be within the grid
        if column >= LEFTBOUND[cell] and column <= RIGHTBOUND[cell]:
            #Column will be cell converted into a string, +1
            #This is because the range starts from 0 and dictionary starts at 1
            index = cell
            red(str(index + 1))
            break

    if turn == PMOVE:
        #Passes new gameList to updateState
        gameList = updateState(index + 1)
    return gameList

def updateState(column):
    global gameList
    col = int(column)
    #Generates the list that will be returned
    #Takes the index given by move and updates the gameList to reflect recent move.
    gameList[(pieces[str(col)] -1 )][col -1] = R
    print(gameList, 'UPDATING "R" STATE')
    return gameList

def initialClick():
    global gameList, turn, numMoves
    #Randomizes if computer will go first or player first
    #If firstMove == 1, computer goes first.
    firstMove = random.randrange(1, 3)
    if firstMove == 1:
        turn = PMOVE
        cpu = str(random.randrange(1, COLUMN + 1))
        gameList = compMove(cpu)
        numMoves += 1

### PLAYER PIECE ###

def red(column):
    global pieces, gameList, turn, numMoves
    interface = turtle.Turtle()
    interface.ht()
    red = turtle.Turtle()
    red.ht()
    red.up()
    #Pieces * Cell length for Y value
    #Conditions for red to move are pieces in each column must be less than the rows
    #CPU also must have moved beforehand
    #if conditions are met, pieces[column] and numMoves incremented by 1, turn reflects player
    if pieces[column] < ROW and turn == CMOVE:
        red.goto(CELL_CENTER[column], BOTTOM_ROW_CENTER + (pieces[column] * CELL))
        red.dot(DOT_SIZE, 'red')
        pieces[column] += 1
        turn = PMOVE
        numMoves += 1
    else:
        interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
        interface.write("Please chose a column that is not filled.",
                        font = (FONT, MEDIUM_SIZE))
        time.sleep(2)
        interface.clear()


### WIN CONDITIONS ###

def gameOver():
    return False #horizontalCheck(), verticalCheck(), diagonalCheck()

def horizontalCheck():
    global gameList
    countR = 0
    countY = 0
    SubListDifference = 0
    for i in range(1, NUM_CELLS):
        SubList = int(i / (COLUMN + .1))
        if SubList != SubListDifference:
            countR = 0
        if SubList != SubListDifference:
            countY = 0
        placeInSubList = (i % COLUMN) - 1
        accessToSubList = gameList[SubList]
        if R in accessToSubList[placeInSubList]:
            countR += 1
        else:
            countR = 0
        if countR == WINNING_DOT:
            print("Red Wins horizontally!")
            return True
        if Y in accessToSubList[placeInSubList]:
            countY += 1
        else:
            countY = 0
        if countY == WINNING_DOT:
            print("Yellow Wins horizontally!")
            return True
        SubListDifference = SubList
    return False

def verticalCheck(row, col):

    win = False
    consec = 0

    for cell in range (row, col):
        if gameList[cell][col] == gameList[row][col]:
            consec += 1
        else:
            break

    if consec >= 4:
        win = True

    return win

def diagonalCheck():
    global gameList
    #The r in the variables stand for right.
    #Which is used for any of the diagonal checks,
    # that are stacked towards the right side.
    #The l in the variables stand for left.
    #Which is used for any of the diagonal checks,
    # that are stacked towards the left side.
    #Any variable with "second" in it, is used for diagonal check,
    # that doesn't begin in the first subList in gameList.
    #All the counts, are used to keep track of the amount of R or Y in a row.
    rCount = 0
    rCountYellow = 0
    secondRCount = 0
    secondRCountYellow = 0
    #All subLists's are used to isolate a single position in the 2D list.
    rSubList = []
    secondRSubList = []
    positionInRSubList = 0
    #numOfSubList is used to get the correct subList that is being tested.
    numOfSubList = 0
    #Loops 3 times because there are 6 possible diagonal checks from the left.
    #We split up the 6 checks into two categories, which is why it loops 3 times.
    for i in range (3):
        for variablePosition in range(ROW):
            #Used to make sure nothing is out of the boards range.
            if positionInRSubList < ROW and numOfSubList < ROW:
                secondRSubList = gameList[numOfSubList][variablePosition]
                rSubList = gameList[variablePosition][positionInRSubList + 1]
                #Accumulating each time it loops.
                positionInRSubList += 1
                numOfSubList += 1
            #Checks if R is in that specific position
            if R in rSubList:
                #Count increases by 1 if R is in the position.
                rCount += 1
            else:
                #If R is not in the position that count is reset to 0.
                rCount = 0
            #once count is 4, it prints who won.
            if rCount == WINNING_DOT:
                print("Red Wins diagonally!!")
                return True
            #Checks if Y is in that specific position
            if Y in rSubList:
                #Count increases by 1 if Y is in the position.
                rCountYellow += 1
            else:
                #If Y is not in the position that count is reset to 0.
                rCountYellow = 0
            #once count is 4, it prints who won.
            if rCountYellow == WINNING_DOT:
                print("Yellow Wins diagonally!")
                return True
            if R in secondRSubList:
                secondRCount += 1
            else:
                secondRCount = 0
            if secondRCount == WINNING_DOT:
                print("Red Wins diagonally!")
                return True
            if Y in secondRSubList:
                secondRCountYellow += 1
            else:
                secondRCountYellow = 0
            if secondRCountYellow == WINNING_DOT:
                print("Yellow Wins diagonally!")
                return True
        #Each time the 6 loops are done, it resets the sublists.
        rSubList = []
        #Each time the 6 loops are done,
        # it resets the positionInSubList and numOfSubList,
        # but it also increase by 1,
        # from the previous loop (first Loop in the nested Loop).
        positionInRSubList = i + 1
        numOfSubList = i + 1
        rCount = 0
        rCountYellow = 0
        secondRCount = 0
        secondRCountYellow = 0
    return False


### COMPUTER FUNCTIONS ###
def compDot(column):
    global turn, numMoves
    interface = turtle.Turtle()
    interface.ht()
    #Computer turtle
    yellow = turtle.Turtle()
    yellow.ht()
    yellow.up()

    #It will only create a piece if these conditionals are met.
    #That means player must have moved first and also,
    #the specific position in the gameList must be empty and the column cannot be filled
    #It will the change turn to reflect computer moved.
    #Pieces[column] and numMoves get incremented.
    if pieces[column] < ROW and turn == PMOVE:
        yellow.goto(CELL_CENTER[column], BOTTOM_ROW_CENTER + (pieces[column] * CELL))
        yellow.dot(DOT_SIZE, 'yellow')
        turn = CMOVE
        pieces[column] += 1
        numMoves += 1
    else:
        interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
        interface.write("Yellow tried to make an illegal move, please click again.",
                        font = (FONT, MEDIUM_SIZE))
        time.sleep(1.5)
        interface.clear()


def compMove(column):
    global gameList
    compDot(str(column))
    #If turn == Computer, update the gameList
    if turn == CMOVE:
        gameList = cUpdateState(column)
    return gameList

def cUpdateState(column):
    global gameList
    col = int(column)
    #Replaces the proper index that was passed from comp -> cMove -> cUpdate to be Y.
    #Reflects in the gameList
    gameList[(pieces[str(col)] -1 )][col -1] = 'Y'
    print(gameList, 'UPDATING THROUGH CUPDATESTATE')
    return gameList


def save():
    interface = turtle.Turtle()
    interface.ht()
    # put the gameList into a txt file
    # end result just letter
    interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
    interface.write("The game has been successfully saved.",
                        font = (FONT, MEDIUM_SIZE))
    time.sleep(1.5)
    interface.clear()
    with open("tempGameState.txt", "w") as f:
        for row in gameList:
            rowStr = ''
            for cell in row:
                rowStr += cell + ''
            f.write(rowStr + '\n')


# method to load the game
# parameters: nothing
# goes back to grid
def load():
    global pieces
    interface = turtle.Turtle()
    interface.ht()
    interface.goto(INTERFACE_X_POS, INTERFACE_Y_POS)
    interface.write("Please click on the screen to open your loaded game!",
                        font = (FONT, MEDIUM_SIZE))
    time.sleep(1.5)
    interface.clear()
    savedFile = open("tempGameState.txt","r")
    reading = savedFile.read()
    reading = reading.replace('\n',"")
    reading = reading.strip("")

    # method is to close the old grid, making a new grid
    def closeScreen():
        global turn
        #resets turn
        turn = 0
        closewn = turtle.Screen()
        closewn.exitonclick()
        grid()

    # reset the dictionary
    # params: the dictionary and the value we want it to reset to
    # return the original dictionary
    def newValue(dict,reset_to):
        global numMoves
        #resets numMoves
        numMoves = 0
        for keys in dict:
            # look at the whatever keys is and makes it = 0
            dict[keys] = reset_to
        return dict


    # convert to file into a list
    #param: the saved file
    # return the saved file as a nested list
    def to2dList(saveFile):
        converter = []
        row = []
        # loops it 42 times
        for cell in range(len(saveFile)):
            # if row has 7 letters inside the list
            # it will go to the converter
            if len(row) == 7:
                converter.append(row)
                row = [saveFile[cell]]
            # keeps adding the letters to row
            else:
                row.append(saveFile[cell])
        converter.append(row)
        return converter


    # method to find where red and yellow where made on the board
    # param: the saved filed as a nested list
    # returns: nothing
    def reDot(savedList):
        global gameList
        gameList = savedList
        #look at the sublist
        for sublist in range(len(savedList)):
            #looks at the sublist index
            for sublistIndex in range(len(savedList[sublist])):
                letter = savedList[sublist][sublistIndex]
                # if  there is a "R" then it will take that index
                # and go to the red function and stamp it on that col
                if letter == "R":
                    # add a 1 because the index can equal zero and our col doesn't
                    # start from 0
                    savedRed(sublistIndex + 1)
                # if  there is a "Y" then it will take that index
                # and go to the comp function and stamp it on that col
                if letter == "Y":
                    # add a 1 because the index can equal zero and our col doesn't
                    # start from 0
                    savedComp(sublistIndex + 1)


    # re-dots all the red dots from the saved file
    def savedRed(column):
        global pieces, turn, numMoves
        red = turtle.Turtle()
        red.ht()
        red.up()
        column = str(column)
        #Pieces * Cell length for Y value
        #listIndex = column
        red.goto(CELL_CENTER[column], BOTTOM_ROW_CENTER + (pieces[column] * CELL))
        red.dot(DOT_SIZE, 'red')
        pieces[column] += 1
        turn = PMOVE
        numMoves += 1

    # re-dot all the yellow dots from the saved file
    def savedComp(column):
        global pieces, turn, numMoves
        yellow = turtle.Turtle()
        yellow.ht()
        yellow.up()
        column = str(column)
        yellow.goto(CELL_CENTER[column], BOTTOM_ROW_CENTER + (pieces[column] * CELL))
        yellow.dot(DOT_SIZE, 'yellow')
        turn = CMOVE
        pieces[column] += 1
        numMoves += 1

    closeScreen()
    pieces = newValue(pieces, 0)
    ToList = to2dList(reading)
    reDot(ToList)
    clickSetup()

main()
