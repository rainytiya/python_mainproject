# wap for Tic tac toe

import random

board =["-","-","-",
        "-","-","-",
        "-","-","-"]
UserNumbers = [1,2,3,4,5,6,7,8,9]
current_player="X"
print()
print("---- TicTacToe ----")
print()
print("The current player is ",current_player)
print("the computer choice is O")
winner = None

# game board
def PrintBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def Playerinput(board):
    try:
     inputplayer=int(input("enter the numbers between 1 to 9 "))
     print("User input ",inputplayer)
     if(inputplayer in UserNumbers):
       if(board[inputplayer-1] =='-'):
        board[inputplayer-1]='X'
       else:
        print("Already player have input in it. Please select other number ")
        Playerinput(board)
     else:           # not in range of 1 to 9
       print("please enter correct input ")
       Playerinput(board)
    except ValueError:      # if input not numeric
      print("Input should be numeric ")
      Playerinput(board)
    except IndexError:     # if input negative numbers
       print("Input should be within 1 to 9 ")
       Playerinput(board)
    # finally:
    #   playerinput(board)


def Computerinput(board):       # computer choice
    inputcomp=random.randint(1,9)
    print("computer choice  ",inputcomp)
    if(board[inputcomp-1] =='-'):
        board[inputcomp-1]='O'
    else:
        print("Already player have input in it. selecting other input for computer")
        Computerinput(board)
   


def Checkwins(board):
    global winner
   # row wise
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        print("row wise ",winner," wins")
        return True
        
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        print("row wise ",winner," wins")
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        print("row wise ",winner," wins")
        return True
    
    # column wise
    elif board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        print("Column wise ",winner," wins")
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        print("Column wise ",winner," wins")
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        print("Column wise ",winner," wins")
        return True

    # diagonal wise
    elif board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        print("Diagonal wise ",winner, " wins")
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        print("Diagonal wise ",winner," wins")
        return True


while(True):
    PrintBoard(board)
    Playerinput(board)
    if(Checkwins(board)):
       PrintBoard(board)
       print(f"The winner is player {winner}!")
       break
    Computerinput(board)
    if(Checkwins(board)):
       PrintBoard(board)
       print(f"The winner is player {winner}!")
       break