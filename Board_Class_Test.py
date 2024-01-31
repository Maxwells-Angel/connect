import random 
import time

class Board:
    '''This is a class for a connect 4 board'''
    def __init__(self):
        self.board = {}
        self.switch = 1
        self.rangerows = range(1,7)
        self.rangecolumns = range(1,8)
        self.horizontalDivider = '___'*7
        self.history = []
        self.choices = []
        self.winner = ""
        self.noWin = True
        self.turns = 0
        self.winType = ""
        self.draw = False
        
        for i in self.rangecolumns:
            for k in self.rangerows: 
                self.board.setdefault((i,k),' ')

    def clearBoard(self):
        for i in self.rangecolumns:
            for k in self.rangerows: 
                self.board.setdefault((i,k),' ')
    
    def checkTurn(self):
        if self.switch == 1:
            return "Player 1", "x", 1
        elif self.switch == -1:
            return "Player 2", "o", -1
    
    def record(self, move):
        player,marker = self.checkTurn()[0],self.checkTurn()[1]
        self.history.append((player,marker, move))
        self.choices.append(move[0])

    def switchTurns(self):
        self.switch = self.switch*-1
        self.turns+=1 

    def showBoard(self):
        print("\n")
        print('''--------------------------------------CONNECT FOUR-----------------------------------------''')
        print("\n")
        print('| '+self.board[(1, 6)]+'| '+self.board[(2,6)]+'| '+self.board[(3,6)]+'| '+self.board[(4,6)]+'| '+self.board[(5, 6)]+'| '+self.board[(6,6)]+'| '+ self.board[(7,6)]+'|')  
        print("_"+ self.horizontalDivider)
        print('| '+self.board[(1,5)]+'| '+self.board[(2,5)]+'| '+self.board[(3,5)]+'| '+self.board[(4,5)]+'| '+self.board[(5, 5)]+'| '+self.board[(6,5)]+'| '+ self.board[(7,5)]+'|')     
        print("_"+ self.horizontalDivider)
        print('| '+self.board[(1,4)]+'| '+self.board[(2,4)]+'| '+self.board[(3,4)]+'| '+self.board[(4,4)]+'| '+self.board[(5, 4)]+'| '+self.board[(6,4)]+'| '+ self.board[(7,4)]+'|')
        print("_"+ self.horizontalDivider)
        print('| '+self.board[(1,3)]+'| '+self.board[(2,3)]+'| '+self.board[(3,3)]+'| '+self.board[(4,3)]+'| '+self.board[(5, 3)]+'| '+self.board[(6,3)]+'| '+ self.board[(7,3)]+'|')
        print("_"+ self.horizontalDivider)
        print('| '+self.board[(1,2)]+'| '+self.board[(2,2)]+'| '+self.board[(3,2)]+'| '+self.board[(4,2)]+'| '+self.board[(5, 2)]+'| '+self.board[(6,2)]+'| '+ self.board[(7,2)]+'|')
        print("_"+ self.horizontalDivider)
        print('| '+self.board[(1,1)]+'| '+self.board[(2,1)]+'| '+self.board[(3,1)]+'| '+self.board[(4,1)]+'| '+self.board[(5, 1)]+'| '+self.board[(6,1)]+'| '+ self.board[(7,1)]+'|')
        print("_"+ self.horizontalDivider)
        
        if self.turns > 0:
            print("TURN: ", self.turns)
            print("The last move was ", self.history[-1][2], "by", self.history[-1][0],",",self.history[-1][1])     

    def show_legal_moves(self):
        # Returns a list of all legal moves, in column order
        legalMoves = [] 
        for i in self.rangecolumns:
            if self.board[(i, 1)] == ' ':
                legalMoves.append((i,1))
            elif self.board[(i, 2)] == ' ':
                legalMoves.append((i,2))
            elif self.board[(i, 3)]== ' ':
                legalMoves.append((i,3))
            elif self.board[(i, 4)] == ' ':
                legalMoves.append((i,4))
            elif self.board[(i, 5)] == ' ':
                legalMoves.append((i,5))
            elif self.board[(i, 6)] == ' ':
                legalMoves.append((i,6))
        return legalMoves 
    
    def placeMove(self, column, prnt = False):
        # THIS function places a move on the board if the move is legal and returns True once placed
        # returns False otherwise
        legal = False
        move = ()
        
        if type(column) == str:
            column = column.strip()

        try: 
            column = int(column)
            if column < 1 or column >7:
                return False
        except: 
            return False

        current_legal_moves = self.show_legal_moves()
        for moves in current_legal_moves: 
            if column == moves[0]:
                move = moves
                legal = True

        if legal:
            self.board[move] = self.checkTurn()[1]
            self.record(move)
            return True

        else:
            if prnt:
                print("Column:",column," was specified. This move is not legal!")
            return False

    def checkWins(self):
        # turns noWins false if the game has been won and sets winner to player 1 or 2 
        # look at the history, what was the last move played 
        last = self.history[-1][2]
        last_column,last_row = last[0],last[1]
        
        # who played the last move 
        marker = self.history[-1][1]

        # check for a horizontal win
        h_connect = 0
        for i in self.rangecolumns:
            if self.board[(i,last_row)]== marker:
                    h_connect+=1
            else: 
                    h_connect = 0
            
            if h_connect>=4:
                self.noWin = False
                self.winType = "Horizontal"

        v_connect = 0
        for j in self.rangerows:

            if self.board[(last_column,j)]== marker:
                    v_connect+=1
            else: 
                    v_connect = 0
            
            if v_connect>=4:
                self.noWin = False
                self.winType = "Vertical"

        # check for a diagonal win
        for i in self.rangecolumns: 
            for j in self.rangerows:
                if i <=4:
                    if j<=3:
                        # check positive diagonal
                        d_connect = 0
                        for step in range(0,4):
                            if self.board[(i+step,j+step)] == marker:
                                d_connect+=1
                            else:
                                d_connect = 0
                            if d_connect>=4:
                                self.noWin = False
                                self.winType = "Positive Diagonal"
                    elif i<=4:
                        if j>3:
                            # check negative diagonal
                            d_connect = 0
                            for step in range(0,4):
                                if self.board[(i+step,j-step)] == marker:
                                    d_connect+=1
                                else:
                                    d_connect = 0

                                if d_connect>=4:
                                    self.noWin = False
                                    self.winType = "Negative Diagonal"
        
        # do something if you detect a win
        if self.noWin == False:
            self.winner = self.history[-1][0]
    
    def checkDraw(self): 
        if self.turns >=42:
            self.draw = True

class Opponent(): 
    def __init__(self):
        self.player = ["x","o"]
        self.choice = 0
        self.challenge = [1,2,3,4]
        self.internalBoard = Board()
    
    def sync(self, board):
        #update representation of the board with newest changes
        self.internalBoard.board = board.board
        self.internalBoard.switch = board.switch 
        self.internalBoard.history = board.history

    def choose(self, board):
        # calculate the best move and return that choice 
        
        # level 1 - choose randomly 
        legal_moves = board.show_legal_moves()
        self.choice = random.randrange(len(legal_moves))
        return legal_moves[self.choice][1]
        
        # level 2 - try to win 
        # make a winning move when you see the opportunity 

        # level 3 - block 
        # block your opponent's potentially winning move 
    
        # level 4 - foresight
        # don't make a move that will lead to a forced loss, unless you have no other option
     
if __name__ == '__main__': 
    
    # Initialize Board and Opponent
    gameOn = True
    myBoard = Board()
    myBoard.showBoard()
    myOpp = Opponent()

    # RANDOMIZE PLAYER TO BE X OR O 
    order = random.randrange(101)
    if order%2 == 0: 
        player_turn = 1
    else: 
        player_turn = -1

    # WELCOME MESSAGE 
    print("HI, LET'S PLAY CONNECT FOUR!")

    # BEGIN GAMEPLAY 
    while gameOn:
        validMove = False 
        while validMove == False:
            if myBoard.switch == player_turn: 
                chooser = input("choose a column")
                #chooser = random.randrange(1,8) 
            else: 
                # random choice from AI
                chooser = myOpp.choose(myBoard)
                myOpp.sync(myBoard)

            validMove = myBoard.placeMove(chooser)

        myBoard.showBoard()
        myBoard.checkWins()

        if myBoard.noWin == True:
            myBoard.checkDraw()
            if myBoard.draw == False:  
                myBoard.switchTurns()
                time.sleep(0.5)
            else: 
                gameOn = False
        else: 
            gameOn = False
    
    if gameOn == False: 
        # Need to discriminate between winning and drawing
        if myBoard.draw == False:
            print(myBoard.winner," won. Game over!")
            print("Win type was: ", myBoard.winType)
        else: 
            print("The game ended in a DRAW!")

    #print(myBoard.history)
    print(myBoard.choices)
