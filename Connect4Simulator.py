#This Program simulates Connect Four Game and tries to define a Optimal Strategy 
#! /usr/bin/env python3 

#Initializing variables
import pyglet
import random 
import time
from Board_Class_Test import Board 
from ChooseMove import simulateOnce
gameOn = True
one_player = False 
counter = 0
rangerows = range(1,7)
rangecolumns = range(1,8)

window = pyglet.window.Window() 

#Initialize the game board
theBoard = Board()
theBoard.makeBoard()
theBoard.showBoard()

#Maintenence of Entire Game State 
while gameOn == True: 
    # 1: Choosing Game Mode 
    if counter == 0:
        choice = '' 
        choice = input("Do you want to play against the computer? y/n")
        if choice == 'y':
            one_player = True
        else: 
            one_player = False

    # COMPUTER V. COMPUTER 
    if not one_player:              
        
        # 3a Beginning the turn 
        if theBoard.switch == 1:
            print("It's Player 1's turn")
        else: 
            print("It's Player 2's turn")

        # 4a Find legal moves
        currentLegalMoves = theBoard.legalMove()
       
        #Choose a random move from the legal moves
        try:
            r = random.randrange(0,len(currentLegalMoves))
            move = currentLegalMoves[r]

            #Place Move
            if theBoard.switch == 1: 
                theBoard.board[move] ='x'
            else:
                theBoard.board[move] ='o'
            
            theBoard.showBoard()
            gameOn = theBoard.noWins()
            counter+=1

            time.sleep(0.3)
            theBoard.switch = theBoard.switch*-1

        except:
            print("It's a draw!")
            gameOn = False

        #Play Again 
        if gameOn == False:
            counter = 0
            answer = input("Do you want to play again? y/n")
            if answer == 'y':
                theBoard.clearBoard()
                switch = 1
                gameOn = True
            else: 
                break

    # PLAYER VS. THE COMPUTER MODE         
    if one_player: 
        rng = random.random()
        if rng > 0.5: 
            player = {'Player':'Player 2', 'turn': -1}
            player_assigned = True
            computer = {'Player':'Player 1', 'turn': 1}
        if rng <= 0.5:
            player = {'Player':'Player 1', 'turn': 1}
            player_assigned = True 
            computer = {'Player':'Player 2', 'turn': -1}
        while player_assigned == True: 
            validMove = False
            if theBoard.switch == player['turn']:
                print("It's", player['Player'], "'s turn")
                while not validMove: 
                    player_move = input("choose your move")
                    try:
                        player_move = int(player_move)
                        theBoard.placeMove(player_move)
                        validMove = True
                    except:
                        validMove = False
            else: 
                print("It's ",computer['Player'], "'s turn")
                theBoard.placeMove(simulateOnce(theBoard)) # fix this for later, change the function back to fully aggregated one 
            
            theBoard.showBoard()
            gameOn = theBoard.noWins()

            time.sleep(0.3)
            counter+=1
            theBoard.switch = theBoard.switch*-1

            if counter >= 42: 
                print("You drew!")
                theBoard.clearBoard()
                gameOn = False
            
            #Play Again 
            if gameOn == False:
                answer = input("Do you want to play again? y/n")
                if answer == 'y':
                    theBoard.clearBoard()
                    switch = 1
                    counter = 0
                    one_player = False
                    player_assigned = False
                    gameOn = True
                else: 
                    break

print("complete")
