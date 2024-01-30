# This is a strategy function for the connect four simulator 
#It plots a course towards an interesting/forced win 

#Initializing variables
from Board_Class_Test import Board 
import random
import time

def simulateOnce(realBoard): 
    thinking = True
    practice = Board()
    practice.makeBoard()
    practice.alignBoard(realBoard)
    practice.showBoard()
    draw = False 
    turn_elapsed = 0

    #Check whose turn it is on initializing 
    if realBoard.switch == -1: 
        turn_seq = ['o','x']*2000
    else: 
        turn_seq = ['x','o']*2000

    # PLACE INITIAL MOVE DOWN    
    #Get a list of legal moves 
    c_list = practice.legalMove()
    r = random.randrange(0,len(c_list))
    move = c_list[r]

    #Check for draws, aka, no more legal moves 
    if len(c_list) == 0:
        thinking = False
        draw = True  
        
    #remember initial marker 
    initial_marker = turn_seq[0]
    
    #place initial move if there is a legal move 
    if draw != True:    
        if turn_seq[turn_elapsed] == 'x': 
            practice.board[move] ='x'
        else:
            practice.board[move] ='o'
        
    practice.showBoard()

    #Check for a win after your initial move 
    if draw != True:  
        thinking = practice.noWins()

    if thinking == False: 
        print("Initial move was ",c_list[r], "for player:", turn_seq[0], " A win was found on the first move ") 
    
    while thinking:

        #Initialize variables 
        randomize = False
        turn_elapsed += 1 
        blunder_counter = 0
        blunder = True  

        #Get all the legal moves 
        legal_moves = practice.legalMove()

        #Check for draw 
        if len(legal_moves) == 0: 
            #for later, restart thinking 
            print("A draw was found")
            break

        try:
            marker = turn_seq[turn_elapsed]
            o_marker = turn_seq[turn_elapsed+1]
        except IndexError:
           print("Bad loop")
           break 

        for move in legal_moves:
            #Check for an immediate win 
            if practice.giveWinningMoves2(move[0], move[1], marker) != None:
                if turn_seq[turn_elapsed] == 'x': 
                    practice.board[move] ='x'
                else:
                    practice.board[move] ='o'

                if marker == initial_marker: 
                    print("Initial move was ",c_list[r], "for player:", turn_seq[0], " and an interesting win was found") #for some reason a prior block is sometimes causing this to be wrongfully activated
                else: 
                    print("Initial move was ",c_list[r], "for player:", turn_seq[0], " and a forced loss was found") 
                randomize = False
                thinking = False
                break
            #Block an opponent's win 
            elif practice.giveWinningMoves2(move[0], move[1], o_marker) != None:
                 #place move 
                print(move)
                if turn_seq[turn_elapsed] == 'x': 
                    practice.board[move] ='x'
                else:
                    practice.board[move] ='o'
                randomize = False
                break
            else: 
                randomize  = True 
        
        trip = 0 
        #Start randomizing
        if randomize:
            while blunder == True: 
                trip += 1
                blunder_counter = 0
                if trip <=1:
                    print('''CURRENT STRATEGY: random choice''')
                s = random.randrange(0, len(legal_moves))
                move = legal_moves[s]

                if turn_seq[turn_elapsed] == 'x': 
                    practice.board[move] ='x'
                else:
                    practice.board[move] ='o'

                #Check to see if the move will let the opponent win
                for new_moves in practice.legalMove():
                    if practice.giveWinningMoves2(new_moves[0], new_moves[1], o_marker) != None:
                        blunder_counter+=1

                if blunder_counter > 0:
                    #print("Avoiding a blunder", trip)
                    blunder = True
                    practice.board[move] = ' '
                else: 
                    blunder = False
                    print(move)
                    break

                if trip>=10:
                    blunder = False
                    print( "I bite the bullet", move)
                    if turn_seq[turn_elapsed] == 'x': 
                        practice.board[move] ='x'
                    else:
                        practice.board[move] ='o'
                
        thinking = practice.noWins()
        #time.sleep(.3)
        practice.showBoard()

    #Ask it to save what it knows in a form that is usable to it. 

    #After you've placed the initial move, start simulating possibilities 
        #Suppose win for an opponent     
        #If it's your turn 
        # Try to win 
        # Block chances for your opponent to win 
        # else, place a random move 
        # keep going until you find an interesting win 
        #if you get to completion, revert to initial and try again 
        #if you get to a loss, revert to initial and try again (maybe mark in memory for avoidance?)
        #later on we will want to save all interesting wins and discriminate based on number of paths and length of paths

if __name__ == "__main__":       
    #Making the board 
    real = Board() 
    real.makeBoard()
    simulator =0
    #putting down markers to test 
    #real.board[(4,1)] = 'x' #1
    #real.switch *=-1 
    
    #real.board[(4,2)] = 'o' #-1
    #real.switch *=-1 

    #real.board[(4,3)] = 'x' #1
    #real.switch *=-1 

    #real.board[(6,1)] = 'o' #-1
    #real.switch *=-1 
    
    #real.board[(3,1)] = 'x' # 1
    #real.switch *=-1 
    
    #real.board[(7,1)] = 'o' # -1
    #real.switch *=-1 

    #real.placeMove(6)# -1 
    #real.switch *=-1 
    #real.showBoard()
    #real.showBoard()
    while simulator <10:
        print('''       ------------------------------------NEW VERSION SIMULATED--------------------------------- 
                                                        %s  
        ------------------------------------NEW VERSION SIMULATED--------------------------------- '''%simulator)
        simulateOnce(real)
        simulator+=1 
    
    print('Complete')

   