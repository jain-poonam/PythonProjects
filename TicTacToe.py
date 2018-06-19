'''
Created on Jun 18, 2018

@author: pyjain
'''
from IPython.display import clear_output
import random

def display_board(board):
    """print out a board. 
        Set up your board as a list, where each index 1-9 corresponds 
        with a number on a number pad."""
    
    clear_output()
    print(" "+"|"+" "+"|")
    print(board[7]+"|"+board[8]+"|"+board[9])
    print("-----")
    print(" "+"|"+" "+"|")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-----")
    print(" "+"|"+" "+"|")
    print(board[1]+"|"+board[2]+"|"+board[3])
    
def player_input():
    """Take in a player input and assign their marker as 'X' or 'O'"""
    
    marker='' 
    while marker != "O" and marker != "X":
        marker = input("Player1 choose X or O : ")
    player1=marker
    if player1== "X":
        player2="O"
    else:
        player2="X"
    return (player1,player2)


def place_marker(board, marker, position):
        """assigns Marker to the board"""
        
        board[position]= marker
        return board
    

def win_check(board, mark):
    """checks to see if A mark has won"""
    
    if board[1]==board[2]==board[3]==mark:
        return True
    elif board[1]==board[5]==board[9]==mark:
        return True
    elif board[1]==board[4]==board[7]==mark:
        return True
    elif board[7]==board[5]==board[3]==mark:
        return True
    elif board[8]==board[5]==board[2]==mark:
        return True
    elif board[9]==board[6]==board[3]==mark:
        return True
    elif board[9]==board[7]==board[8]==mark:
        return True
    elif board[4]==board[5]==board[6]==mark:
        return True
    
    else:
        
        return False 
    

def choose_first():
    """random module to randomly decide which player goes first"""
    player=random.randint(1,2)
    return player
choose_first()


def space_check(board, position):
    """Check if a space on the board is freely available"""
    a= board[position]
    if a==" ":
        return True
    else:
        return False

def full_board_check(board):
    """Check if the board is full"""
    for i in range(1,10):
        if board[i]== " ":
            return False
      
    return True

def player_choice(board):
    """ asks for a player's next position"""
    
    position=int(input("Choose a new position: "))
    value1=space_check(board, position)
    if value1:
        return position
    else:
        return 0

def replay():
    """asks the player if they want to play again"""
    
    play_again=input("Do you want to play: YES/NO: ")
    if play_again.upper()=="YES":
        return True
    else:
        return False

print('Welcome to Tic Tac Toe!')
ask=replay()
while ask:
    
    board=[" "," "," "," "," "," "," "," "," "," "]

    display_board(board)

    player1_marker,player2_marker=player_input()
    player_first=choose_first()
    print("Player "+ str(player_first)+ " goes first.")
    
    if player_first==1:
        marker1=player1_marker
        marker2=player2_marker
       
    else:
        marker1=player2_marker
        marker2=player1_marker
    
    while  (full_board_check(board)==False):
    
        index1=player_choice(board)
        
        if index1 != 0:
            
            board=place_marker(board,marker1,index1)
            display_board(board)
        else:
            print("Position already occupied")
            
        if win_check(board, marker1)==True or full_board_check(board)==True: 
            break
          
        index2=player_choice(board)
        
        if index2 != 0:
                
            board=place_marker(board,marker2,index2)
            display_board(board)
                
        else:
            print("Position already occupied")
        if win_check(board, marker2)==True or full_board_check(board)==True:
            break
      
    if full_board_check(board)== True:    
        print("Board is full, try again!!")
        
    elif win_check(board, marker1):
        print("Congratulations!! Player1 wins")
            
    elif win_check(board, marker2):
        print("Congratulations!! Player2 wins")            
    ask=replay()
    if not ask:
        break  


