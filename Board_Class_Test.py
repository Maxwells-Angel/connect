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
        self.noWin = True
        self.turns = 0
        
        for i in self.rangecolumns:
            for k in self.rangerows: 
                self.board.setdefault((i,k),' ')

    # Creates the board 
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

    def switchTurns(self):
        self.switch = self.switch*-1
        self.turns+=1 

    # Shows the board 
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
        print("The last move was ", self.history[-1][2], "by", self.history[-1][0],",",self.history[-1][1])     

    # Returns a list of all legal moves, in column order
    def show_legal_moves(self):
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
    
    # places move on the board if the move is legal 
    # returns false otherwise
    def placeMove(self, column, prnt = False):
        legal = False
        move = ()

        current_legal_moves = self.show_legal_moves()
        for moves in current_legal_moves: 
            if column == moves[0]:
                move = moves
                legal = True

        if legal:
            self.board[move] = self.checkTurn()[1]
            self.record(move)

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

        v_connect = 0
        for j in self.rangerows:

            if self.board[(last_column,j)]== marker:
                    v_connect+=1
            else: 
                    v_connect = 0
            
            if v_connect>=4:
                self.noWin = False

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

                elif i<=4:
                    if j>3:
                        # check negative diagonal
                        d_connect = 0
                        for step in range(0,4):
                            if self.board[(i-step,j-step)] == marker:
                                d_connect+=1
                            else:
                                d_connect = 0

                            if d_connect>=4:
                                self.noWin = False
        
        # do something if you detect a win
        if self.noWin == False:
            winner = self.history[-1][0]
            print("\n")
            print(winner," won, Game over!")
            print("\n")
            time.sleep(4)
            
    #This board returns a list of winning moves for the current game state
    def giveWinningMoves(self, x,y, marker):
        wins =[]
        #Checks all possible wins for (x,y) 
        #check right
        if x<= 4: 
            if self.board[(x+1,y)] ==  marker:
                if self.board[(x+2, y)] ==  marker:
                    if self.board[(x+3,y)] == marker:
                            if x not in wins: 
                                wins.append(x)
            if x == 2 or x ==3: 
                if self.board[(x-1,y)] ==  marker:
                    if self.board[(x+1, y)] ==  marker:
                        if self.board[(x+2,y)] == marker:
                           if x not in wins: 
                                wins.append(x)
            #then check up and right 
            if y <=3:
                    if self.board[(x+1,y+1)]  == marker:
                        if self.board[(x+2,y+2)] == marker:
                                if self.board[(x+3,y+3)] == marker:
                                    if x not in wins: 
                                        wins.append(x)
        #check just left
        if x>=4:
            if self.board[(x-1, y)] == marker:
                if self.board[(x-2, y)] == marker:
                    if self.board[(x-3,y)] == marker:
                        if x not in wins: 
                            wins.append(x)
            #then check up and left
            if y <=3:
                if self.board[(x-1,y+1)] == marker:
                    if self.board[(x-2,y+2)] == marker:
                        if self.board[(x-3,y+3)]== marker:
                            if x not in wins: 
                                wins.append(x) 
        #check down 
        if y >=4:
            if self.board[(x,y-1)] == marker:
                    if self.board[(x,y-2)] == marker:
                        if self.board[(x,y-3)] == marker:
                            if x not in wins: 
                                wins.append(x)
            #then check down and left
            if  x>= 4:
                if self.board[(x-1,y-1)] == marker:
                    if self.board[(x-2,y-2)] == marker:
                        if self.board[(x-3,y-3)] == marker:
                            if x not in wins: 
                                wins.append(x)
            #Lastly, check down and right
            if x<= 4:
                if self.board[(x+1,y-1)] == marker:
                    if self.board[(x+2,y-2)]  == marker:
                        if self.board[(x+3,y-3)] == marker:
                            if x not in wins: 
                                wins.append(x)
        #check midpoints for horizontal wins 
        if x>=3 and x<=5:
            if self.board[(x+1,y)] ==  marker:
                    if self.board[(x-1, y)] ==  marker:
                        if self.board[(x-2,y)] == marker:
                            if x not in wins: 
                                wins.append(x)
            if self.board[(x+2,y)] ==  marker:
                if self.board[(x+1, y)] ==  marker:
                    if self.board[(x-1,y)] == marker:
                            if x not in wins: 
                                wins.append(x)
        #Check midpoints for diagonal wins 
        if y>=2 and y<=4:
            #up and right with marker in second position 
            if x> 1 and x<6: 
                if self.board[(x-1,y-1)] ==  marker:
                    if self.board[(x+1, y+1)] ==  marker:
                        if self.board[(+2,y+2)] == marker:
                            if x not in wins: 
                                wins.append(x)
            if x> 2 and x<=6: 
                #up and left with marker in second position
                if self.board[(x+1,y-1)] ==  marker:
                    if self.board[(x-1, y+1)] ==  marker:
                        if self.board[(x-2,y+2)] == marker:
                            if x not in wins: 
                                wins.append(x)
        if y>=3 and y<=5:
            #up and right with marker in third position 
            if x>=3 and x<=6: 
                if self.board[(x-2,y-2)] ==  marker:
                    if self.board[(x-1, y-1)] ==  marker:
                        if self.board[(x+1,y+1)] == marker:
                            if x not in wins: 
                                wins.append(x)
            if x>=2 and x<=5: 
                #up and left with marker in third position
                if self.board[(x-1,y+1)] ==  marker:
                    if self.board[(x+1, y-1)] ==  marker:
                        if self.board[(x+2,y-2)] == marker:
                            if x not in wins: 
                                wins.append(x)
        if len(wins) == 0:
            return None 
        else:
            return wins

    #This board returns one winning move from a list of winning moves
    def giveWinningMoves2(self, x,y, marker):
        pass
        wins =[]
        #Checks all possible wins for (x,y) 
        #check right
        if x<= 4: 
            if self.board[(x+1,y)] ==  marker:
                if self.board[(x+2, y)] ==  marker:
                    if self.board[(x+3,y)] == marker:
                            if x not in wins: 
                                wins.append((x,y))
            if x == 2 or x ==3: 
                if self.board[(x-1,y)] ==  marker:
                    if self.board[(x+1, y)] ==  marker:
                        if self.board[(x+2,y)] == marker:
                           if x not in wins: 
                               wins.append((x,y))
            #then check up and right 
            if y <=3:
                    if self.board[(x+1,y+1)]  == marker:
                        if self.board[(x+2,y+2)] == marker:
                                if self.board[(x+3,y+3)] == marker:
                                    if x not in wins: 
                                        wins.append((x,y))
        #check just left
        if x>=4:
            if self.board[(x-1, y)] == marker:
                if self.board[(x-2, y)] == marker:
                    if self.board[(x-3,y)] == marker:
                        if x not in wins: 
                           wins.append((x,y))

            #then check up and left
            if y <=3:
                if self.board[(x-1,y+1)] == marker:
                    if self.board[(x-2,y+2)] == marker:
                        if self.board[(x-3,y+3)]== marker:
                            if x not in wins: 
                               wins.append((x,y))
        #check down 
        if y >=4:
            if self.board[(x,y-1)] == marker:
                    if self.board[(x,y-2)] == marker:
                        if self.board[(x,y-3)] == marker:
                            if x not in wins: 
                                wins.append((x,y))
            #then check down and left
            if  x>= 4:
                if self.board[(x-1,y-1)] == marker:
                    if self.board[(x-2,y-2)] == marker:
                        if self.board[(x-3,y-3)] == marker:
                            if x not in wins: 
                                wins.append((x,y))
            #Lastly, check down and right
            if x<= 4:
                if self.board[(x+1,y-1)] == marker:
                    if self.board[(x+2,y-2)]  == marker:
                        if self.board[(x+3,y-3)] == marker:
                            if x not in wins: 
                               wins.append((x,y))
        #check midpoints for horizontal wins 
        if x>=3 and x<=5:
            if self.board[(x+1,y)] ==  marker:
                    if self.board[(x-1, y)] ==  marker:
                        if self.board[(x-2,y)] == marker:
                            if x not in wins: 
                                wins.append((x,y))
            if self.board[(x+2,y)] ==  marker:
                if self.board[(x+1, y)] ==  marker:
                    if self.board[(x-1,y)] == marker:
                            if x not in wins: 
                                wins.append((x,y))
        #Check midpoints for diagonal wins 
        if y>=2 and y<=4:
            #up and right with marker in second position 
            if x> 1 and x<6: 
                if self.board[(x-1,y-1)] ==  marker:
                    if self.board[(x+1, y+1)] ==  marker:
                        if self.board[(+2,y+2)] == marker:
                            if x not in wins: 
                                wins.append((x,y))
            if x> 2 and x<=6: 
                #up and left with marker in second position
                if self.board[(x+1,y-1)] ==  marker:
                    if self.board[(x-1, y+1)] ==  marker:
                        if self.board[(x-2,y+2)] == marker:
                            if x not in wins: 
                               wins.append((x,y))
        if y>=3 and y<=5:
            #up and right with marker in third position 
            if x>=3 and x<=6: 
                if self.board[(x-2,y-2)] ==  marker:
                    if self.board[(x-1, y-1)] ==  marker:
                        if self.board[(x+1,y+1)] == marker:
                            if x not in wins: 
                                wins.append((x,y))
            if x>=2 and x<=5: 
                #up and left with marker in third position
                if self.board[(x-1,y+1)] ==  marker:
                    if self.board[(x+1, y-1)] ==  marker:
                        if self.board[(x+2,y-2)] == marker:
                            if x not in wins: 
                                wins.append((x,y))
        if len(wins) == 0:
            return None 
        else:
            return wins
   
if __name__ == '__main__': 
    
    #Initialize Board
    myBoard = Board()
    choices = [4,7,3,7,4,7,5,5,5,6,6,6,6]

    for i in range(50):
        
        chooser = random.randrange(1,8)
        myBoard.placeMove(chooser)
        #myBoard.placeMove(choices[i])
        myBoard.showBoard()
        myBoard.checkWins()

        if myBoard.noWin == True: 
            myBoard.switchTurns()
            time.sleep(0.3)
        else: 
            break

    #print(myBoard.history)
    print("complete")
