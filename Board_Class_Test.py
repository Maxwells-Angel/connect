import random 
import time

class Board:
    '''This is a class for a connect 4 board'''
    def __init__(self):
        self.board = {}
    switch = 1
    rangerows = range(1,7)
    rangecolumns = range(1,8)

    #Creates the board 
    def makeBoard(self):
        pass
        rangerows = range(1,7)
        rangecolumns = range(1,8)
        for i in rangecolumns:
            for k in rangerows: 
                self.board.setdefault((i,k),' ')

    # Shows the board 
    def showBoard(self):
        pass
        horizontalDivider = '___'*7
        print('''--------------------------------------CONNECT FOUR----------------------------------------''')
        print('| '+self.board[(1, 6)]+'| '+self.board[(2,6)]+'| '+self.board[(3,6)]+'| '+self.board[(4,6)]+'| '+self.board[(5, 6)]+'| '+self.board[(6,6)]+'| '+ self.board[(7,6)]+'|')  
        print("_"+ horizontalDivider)
        print('| '+self.board[(1,5)]+'| '+self.board[(2,5)]+'| '+self.board[(3,5)]+'| '+self.board[(4,5)]+'| '+self.board[(5, 5)]+'| '+self.board[(6,5)]+'| '+ self.board[(7,5)]+'|')     
        print("_"+ horizontalDivider)
        print('| '+self.board[(1,4)]+'| '+self.board[(2,4)]+'| '+self.board[(3,4)]+'| '+self.board[(4,4)]+'| '+self.board[(5, 4)]+'| '+self.board[(6,4)]+'| '+ self.board[(7,4)]+'|')
        print("_"+ horizontalDivider)
        print('| '+self.board[(1,3)]+'| '+self.board[(2,3)]+'| '+self.board[(3,3)]+'| '+self.board[(4,3)]+'| '+self.board[(5, 3)]+'| '+self.board[(6,3)]+'| '+ self.board[(7,3)]+'|')
        print("_"+ horizontalDivider)
        print('| '+self.board[(1,2)]+'| '+self.board[(2,2)]+'| '+self.board[(3,2)]+'| '+self.board[(4,2)]+'| '+self.board[(5, 2)]+'| '+self.board[(6,2)]+'| '+ self.board[(7,2)]+'|')
        print("_"+ horizontalDivider)
        print('| '+self.board[(1,1)]+'| '+self.board[(2,1)]+'| '+self.board[(3,1)]+'| '+self.board[(4,1)]+'| '+self.board[(5, 1)]+'| '+self.board[(6,1)]+'| '+ self.board[(7,1)]+'|')
        print("_"+ horizontalDivider)
        print('''--------------------------------------CONNECT FOUR----------------------------------------''')

    # Returns all legal moves 
    def legalMove(self):
        pass 
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
    
    #Returns false if the game has been won 
    def noWins(self):
        noWin = True
        rangerows = range(1,7)
        rangecolumns = range(1,8)
        columns = [1,2,3,4,5,6,7]
        rows = [1,2,3,4,5,6]
    
        #Check Horizontal wins
        for i in rows: 
            #for player 1 
            if self.board[(1, i)] == 'x':
                if self.board[(2,i)] == 'x':
                    if self.board[(3,i)] == 'x':
                        if self.board[(4,i)] == 'x':
                            print("Player 1 won! HORIZONTAL")
                            noWin = False
                            return False 
            if self.board[(2,i)] == 'x':
                if self.board[(3,i)] == 'x':
                    if self.board[(4,i)] == 'x':
                        if self.board[(5, i)] == 'x':
                            print("Player 1 won! HORIZONTAL")
                            noWin = False
                            return False 
            if self.board[(3,i)] == 'x':
                if self.board[(4,i)] == 'x':
                    if self.board[(5,i)] == 'x':
                        if self.board[(6, i)] == 'x':
                            print("Player 1 won! HORIZONTAL")
                            noWin = False
                            return False  
            if self.board[(4,i)] == 'x':
                if self.board[(5, i)] == 'x':
                    if self.board[(6,i)] == 'x':
                        if self.board[(7, i)] == 'x':
                            print("Player 1 won! HORIZONTAL")
                            noWin = False
                            return False
            #for player 2 
            if self.board[(1, i)] == 'o':
                if self.board[(2,i)] == 'o':
                    if self.board[(3,i)] == 'o':
                        if self.board[(4,i)] == 'o':
                            print("Player 2 won! HORIZONTAL")
                            noWin = False
                            return False 
            if self.board[(2,i)] == 'o':
                if self.board[(3,i)] == 'o':
                    if self.board[(4,i)] == 'o':
                        if self.board[(5, i)] == 'o':
                            print("Player 2 won! HORIZONTAL")
                            noWin = False
                            return False 
            if self.board[(3,i)] == 'o':
                if self.board[(4,i)] == 'o':
                    if self.board[(5,i)] == 'o':
                        if self.board[(6, i)] == 'o':
                            print("Player 2 won! HORIZONTAL")
                            noWin = False
                            return False  
            if self.board[(4,i)] == 'o':
                if self.board[(5, i)] == 'o':
                    if self.board[(6,i)] == 'o':
                        if self.board[(7, i)] == 'o':
                            print("Player 2 won! HORIZONTAL")
                            noWin = False
                            return  False

        # Next check for a vertical win 
        for placer in columns: 
            #player 1
            if self.board[(placer, 1)] == 'x':
                if self.board[(placer, 2)] =='x':
                    if self.board[(placer, 3)] =='x': 
                        if self.board[(placer, 4)] =='x':
                            print("Player 1 won! VERTICAL")
                            noWin = False
                            return False 
            if self.board[(placer, 2)] == 'x':
                if self.board[(placer, 3)] =='x':
                    if self.board[(placer, 4)] =='x': 
                        if self.board[(placer, 5)] =='x':
                            print("Player 1 won! VERTICAL")
                            noWin = False
                            return False 
            if self.board[(placer, 3)] == 'x':
                if self.board[(placer, 4)] =='x':
                    if self.board[(placer, 5)] =='x': 
                        if self.board[(placer, 6)] =='x':
                            print("Player 1 won! VERTICAL")
                            noWin = False
                            return False 
            #player 2 
            if self.board[(placer, 1)] == 'o':
                if self.board[(placer, 2)] =='o':
                    if self.board[(placer, 3)] =='o': 
                        if self.board[(placer, 4)] =='o':
                            print("Player 2 won! VERTICAL")
                            noWin = False
                            return False 
            if self.board[(placer, 2)] == 'o':
                if self.board[(placer, 3)] =='o':
                    if self.board[(placer, 4)] =='o': 
                        if self.board[(placer, 5)] =='o':
                            print("Player 2 won! VERTICAL")
                            noWin = False
                            return False 
            if self.board[(placer, 3)] == 'o':
                if self.board[(placer, 4)] =='o':
                    if self.board[(placer, 5)] =='o': 
                        if self.board[(placer, 6)] =='o':
                            print("Player 2 won! VERTICAL")
                            noWin = False
                            return False 
        #Last, check for diagonal wins   
        for y in rangerows: 
            for x in rangecolumns:
            #player 1 
                #check up and right 
                if y <=3 and x<= 4:
                    if self.board[(x,y)] == 'x':
                        if self.board[(x+1,y+1)] == 'x':
                            if self.board[(x+2,y+2)] == 'x':
                                if self.board[(x+3,y+3)] == 'x':
                                    print("Player 1 won! UP and RIGHT")
                                    noWin = False
                                    return False
                #check up and left
                if y <=3 and x>= 4:
                    if self.board[(x,y)] == 'x':
                        if self.board[(x-1,y+1)] == 'x':
                            if self.board[(x-2,y+2)] == 'x':
                                if self.board[(x-3,y+3)] == 'x':
                                    print("Player 1 won! UP and LEFT")
                                    noWin = False
                                    return False
                #check down and left
                if y >=4 and x>= 4:
                    if self.board[(x,y)] == 'x':
                        if self.board[(x-1,y-1)] == 'x':
                            if self.board[(x-2,y-2)] == 'x':
                                if self.board[(x-3,y-3)] == 'x':
                                    print("Player 1 won! DOWN and LEFT")
                                    noWin = False
                                    return False
                #check down and right
                if y >=4 and x<= 4:
                    if self.board[(x,y)] == 'x':
                        if self.board[(x+1,y-1)] == 'x':
                            if self.board[(x+2,y-2)] == 'x':
                                if self.board[(x+3,y-3)] == 'x':
                                    print("Player 1 won! DOWN and RIGHT")
                                    noWin = False
                                    return False
            #player 2 
                #check up and right 
                if y <=3 and x<= 4:
                    if self.board[(x,y)] == 'o':
                        if self.board[(x+1,y+1)] == 'o':
                            if self.board[(x+2,y+2)] == 'o':
                                if self.board[(x+3,y+3)] == 'o':
                                    print("Player 2 won! UP and RIGHT!")
                                    noWin = False
                                    return False
                #check up and left
                if y <=3 and x>= 4:
                    if self.board[(x,y)] == 'o':
                        if self.board[(x-1,y+1)] == 'o':
                            if self.board[(x-2,y+2)] == 'o':
                                if self.board[(x-3,y+3)] == 'o':
                                    print("Player 2 won! UP and LEFT")
                                    noWin = False
                                    return False
                #check down and left
                if y >=4 and x>= 4:
                    if self.board[(x,y)] == 'o':
                        if self.board[(x-1,y-1)] == 'o':
                            if self.board[(x-2,y-2)] == 'o':
                                if self.board[(x-3,y-3)] == 'o':
                                    print("Player 2 won! DOWN and LEFT")
                                    noWin = False
                                    return False
                #check down and right
                if y >=4 and x<= 4:
                    if self.board[(x,y)] == 'o':
                        if self.board[(x+1,y-1)] == 'o':
                            if self.board[(x+2,y-2)] == 'o':
                                if self.board[(x+3,y-3)] == 'o':
                                    print("Player 2 won! DOWN and RIGHT")
                                    noWin = False
                                    return False
        if noWin == True:
            return True     
            
    #This function checks to see if the game has been won and returns values 
    def checkWins2(self):
        rangerows = range(1,7)
        rangecolumns = range(1,8)
        columns = [1,2,3,4,5,6,7]
        rows = [1,2,3,4,5,6]
        Win = False
        #Check Horizontal wins
        for i in rows: 
            #for player 1 
            if self.board[(1, i)] == 'x':
                if self.board[(2,i)] == 'x':
                    if self.board[(3,i)] == 'x':
                        if self.board[(4,i)] == 'x':
                            #print("Player 1 won! HORIZONTAL")
                            Win  = True
                            return 1 
            if self.board[(2,i)] == 'x':
                if self.board[(3,i)] == 'x':
                    if self.board[(4,i)] == 'x':
                        if self.board[(5, i)] == 'x':
                            #print("Player 1 won! HORIZONTAL")
                            Win  = True
                            return 1
            if self.board[(3,i)] == 'x':
                if self.board[(4,i)] == 'x':
                    if self.board[(5,i)] == 'x':
                        if self.board[(6, i)] == 'x':
                            #print("Player 1 won! HORIZONTAL")
                            Win  = True
                            return 1 
            if self.board[(4,i)] == 'x':
                if self.board[(5, i)] == 'x':
                    if self.board[(6,i)] == 'x':
                        if self.board[(7, i)] == 'x':
                            #print("Player 1 won! HORIZONTAL")
                            Win  = True
                            return 1
            #for player 2 
            if self.board[(1, i)] == 'o':
                if self.board[(2,i)] == 'o':
                    if self.board[(3,i)] == 'o':
                        if self.board[(4,i)] == 'o':
                           # print("Player 2 won! HORIZONTAL")
                            Win  = True
                            return -1
            if self.board[(2,i)] == 'o':
                if self.board[(3,i)] == 'o':
                    if self.board[(4,i)] == 'o':
                        if self.board[(5, i)] == 'o':
                            #print("Player 2 won! HORIZONTAL")
                            Win  = True
                            return -1
            if self.board[(3,i)] == 'o':
                if self.board[(4,i)] == 'o':
                    if self.board[(5,i)] == 'o':
                        if self.board[(6, i)] == 'o':
                            #print("Player 2 won! HORIZONTAL")
                            Win  = True
                            return -1  
            if self.board[(4,i)] == 'o':
                if self.board[(5, i)] == 'o':
                    if self.board[(6,i)] == 'o':
                        if self.board[(7, i)] == 'o':
                            #print("Player 2 won! HORIZONTAL")
                            Win  = True
                            return  -1

        # Next check for a vertical win 
        for placer in columns: 
            #player 1
            if self.board[(placer, 1)] == 'x':
                if self.board[(placer, 2)] =='x':
                    if self.board[(placer, 3)] =='x': 
                        if self.board[(placer, 4)] =='x':
                           # print("Player 1 won! VERTICAL")
                            Win  = True
                            return 1 
            if self.board[(placer, 2)] == 'x':
                if self.board[(placer, 3)] =='x':
                    if self.board[(placer, 4)] =='x': 
                        if self.board[(placer, 5)] =='x':
                            #print("Player 1 won! VERTICAL")
                            Win  = True
                            return 1
            if self.board[(placer, 3)] == 'x':
                if self.board[(placer, 4)] =='x':
                    if self.board[(placer, 5)] =='x': 
                        if self.board[(placer, 6)] =='x':
                            #print("Player 1 won! VERTICAL")
                            Win  = True
                            return 1 
            #player 2 
            if self.board[(placer, 1)] == 'o':
                if self.board[(placer, 2)] =='o':
                    if self.board[(placer, 3)] =='o': 
                        if self.board[(placer, 4)] =='o':
                            #print("Player 2 won! VERTICAL")
                            Win  = True
                            return -1
            if self.board[(placer, 2)] == 'o':
                if self.board[(placer, 3)] =='o':
                    if self.board[(placer, 4)] =='o': 
                        if self.board[(placer, 5)] =='o':
                            #print("Player 2 won! VERTICAL")
                            Win  = True
                            return -1
            if self.board[(placer, 3)] == 'o':
                if self.board[(placer, 4)] =='o':
                    if self.board[(placer, 5)] =='o': 
                        if self.board[(placer, 6)] =='o':
                            #print("Player 2 won! VERTICAL")
                            Win  = True
                            return -1
        #Last, check for diagonal wins   
        for y in rangerows: 
            for x in rangecolumns:
            #player 1 
                #check up and right 
                if y <=3 and x<= 4:
                    if self.board[(x,y)] == 'x':
                        if self.board[(x+1,y+1)] == 'x':
                            if self.board[(x+2,y+2)] == 'x':
                                if self.board[(x+3,y+3)] == 'x':
                                    #print("Player 1 won! UP and RIGHT")
                                    Win  = True
                                    return 1
                #check up and left
                if y <=3 and x>= 4:
                    if self.board[(x,y)] == 'x':
                        if self.board[(x-1,y+1)] == 'x':
                            if self.board[(x-2,y+2)] == 'x':
                                if self.board[(x-3,y+3)] == 'x':
                                    #print("Player 1 won! UP and LEFT")
                                    Win  = True
                                    return 1
                #check down and left
                if y >=4 and x>= 4:
                    if self.board[(x,y)] == 'x':
                        if self.board[(x-1,y-1)] == 'x':
                            if self.board[(x-2,y-2)] == 'x':
                                if self.board[(x-3,y-3)] == 'x':
                                    #print("Player 1 won! DOWN and LEFT")
                                    Win  = True
                                    return 1
                #check down and right
                if y >=4 and x<= 4:
                    if self.board[(x,y)] == 'x':
                        if self.board[(x+1,y-1)] == 'x':
                            if self.board[(x+2,y-2)] == 'x':
                                if self.board[(x+3,y-3)] == 'x':
                                    #print("Player 1 won! DOWN and RIGHT")
                                    Win  = True
                                    return 1
            #player 2 
                #check up and right 
                if y <=3 and x<= 4:
                    if self.board[(x,y)] == 'o':
                        if self.board[(x+1,y+1)] == 'o':
                            if self.board[(x+2,y+2)] == 'o':
                                if self.board[(x+3,y+3)] == 'o':
                                    #print("Player 2 won! UP and RIGHT!")
                                    Win  = True
                                    return -1
                #check up and left
                if y <=3 and x>= 4:
                    if self.board[(x,y)] == 'o':
                        if self.board[(x-1,y+1)] == 'o':
                            if self.board[(x-2,y+2)] == 'o':
                                if self.board[(x-3,y+3)] == 'o':
                                    #print("Player 2 won! UP and LEFT")
                                    Win  = True
                                    return -1
                #check down and left
                if y >=4 and x>= 4:
                    if self.board[(x,y)] == 'o':
                        if self.board[(x-1,y-1)] == 'o':
                            if self.board[(x-2,y-2)] == 'o':
                                if self.board[(x-3,y-3)] == 'o':
                                    #print("Player 2 won! DOWN and LEFT")
                                    Win  = True
                                    return -1
                #check down and right
                if y >=4 and x<= 4:
                    if self.board[(x,y)] == 'o':
                        if self.board[(x+1,y-1)] == 'o':
                            if self.board[(x+2,y-2)] == 'o':
                                if self.board[(x+3,y-3)] == 'o':
                                    #print("Player 2 won! DOWN and RIGHT")
                                    Win  = True
                                    return -1
        if Win  != True:
            return 0    

    def clearBoard(self):
        pass
        rangerows = range(1,7)
        rangecolumns = range(1,8)
        for i in rangecolumns:
            for k in rangerows: 
                self.board[(i,k)] = " "
    
    def alignBoard(self, newBoard):
        pass 
        rangerows = range(1,7)
        rangecolumns = range(1,8)
        for i in rangecolumns:
            for k in rangerows: 
                self.board[(i,k)] = newBoard.board[(i,k)]
    
    #This board returns a list of winning moves for the current game state
    def giveWinningMoves(self, x,y, marker):
        pass
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

    #places move
    def placeMove(self, move):
        pass
        if self.switch == 1: 
            self.board[move] ='x'
        elif self.switch == -1:
            self.board[move] ='o'

    
if __name__ == '__main__': 
    #Initialize Board
    theBoard = Board()
    theBoard.makeBoard()
    theBoard.showBoard()
    gameOn = True
    counter = 0

    while gameOn == True: 
        chooser = random.randrange(1,8)
        theBoard.placeMove(chooser)
        theBoard.switch = theBoard.switch*-1
        theBoard.showBoard()
        rangerows = range(1,7)
        rangecolumns = range(1,8)
        gameOn = theBoard.noWins()
        time.sleep(0.2)
        counter+=1
        if counter >= 42: 
            print("I'm broken")
            theBoard.clearBoard()
            break 

    print("complete")
