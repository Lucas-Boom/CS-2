'''
Author: Lucas Boom 
Date: 4/6/26
Description: Analyzes titanic file and exports the results to an excel spreadsheet
List of completed functions: ai_bot, ai_bot_2, player_x_move, player_o_move, check_winner, check_draw, display_board, play_again, main 
Log: 1.0
'''
import random #imports random

       

def ai_bot(player_o_turn, board): 
    '''
    checks for best possible move bot as player 'O', if not found, picks random spot
    Args:
        player_o_turn(str): representation of player O 
        board(list of lists): a 3x3 tic tac toe board 
    Returns:
        None: Function changes the board by printing the ai's move
    '''
    
    print('Bot decides to go here: ')

    while True:



        #all possible rows for bot to win
        if board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == '-':
            board[0][2] = player_o_turn
            break
            
        elif board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == '-':
            board[1][2] = player_o_turn
            break

        elif board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == '-':
            board[2][2] = player_o_turn
            break



        elif board[0][0] == 'o' and board[0][1] == '-' and board[0][2] == 'o':
            board[0][1] = player_o_turn
            break

        elif board[1][0] == 'o' and board[1][1] == '-' and board[1][2] == 'o':
            board[1][1] = player_o_turn
            break

        elif board[2][0] == 'o' and board[2][1] == '-' and board[2][2] == 'o':
            board[2][1] = player_o_turn
            break


        
        elif board[0][0] == '-' and board[0][1] == 'o' and board[0][2] == 'o':
            board[0][0] = player_o_turn
            break

        elif board[1][0] == '-' and board[1][1] == 'o' and board[1][2] == 'o':
            board[1][0] = player_o_turn
            break

        elif board[2][0] == '-' and board[2][1] == 'o' and board[2][2] == 'o':
            board[2][0] = player_o_turn
            break
        

        #all possible columns for bot to win

        elif board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == '-':
            board[2][0] = player_o_turn
            break

        elif board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == '-':
            board[2][1] = player_o_turn
            break

        elif board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == '-':
            board[2][2] = player_o_turn
            break

        
        
        elif board[0][0] == 'o' and board[1][0] == '-' and board[2][0] == 'o':
            board[1][0] = player_o_turn
            break

        elif board[0][1] == 'o' and board[1][1] == '-' and board[2][1] == 'o':
            board[1][1] = player_o_turn
            break

        elif board[0][2] == 'o' and board[1][2] == '-' and board[2][2] == 'o':
            board[1][2] = player_o_turn
            break

        
    
        elif board[0][0] == '-' and board[1][0] == 'o' and board[2][0] == 'o':
            board[0][0] = player_o_turn
            break

        elif board[0][1] == '-' and board[1][1] == 'o' and board[2][1] == 'o':
            board[0][1] = player_o_turn
            break

        elif board[0][2] == '-' and board[1][2] == 'o' and board[2][2] == 'o':
            board[0][2] = player_o_turn
            break


        #all possible diagonals for bot to win

        elif board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == '-':
            board[2][2] = player_o_turn
            break

        elif board[0][0] == 'o' and board[1][1] == '-' and board[2][2] == 'o':
            board[1][1] = player_o_turn
            break

        elif board[0][0] == '-' and board[1][1] == 'o' and board[2][2] == 'o':
            board[0][0] = player_o_turn
            break

        
        
        elif board[2][0] == 'o' and board[1][1] == 'o' and board[0][2] == '-':
            board[0][2] = player_o_turn
            break

        elif board[2][0] == 'o' and board[1][1] == '-' and board[0][2] == 'o':
            board[1][1] = player_o_turn
            break

        elif board[2][0] == '-' and board[1][1] == 'o' and board[0][2] == 'o':
            board[2][0] = player_o_turn
            break
        
        ####
        ####
        ####
        ####

        #all possible rows to block
        if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == '-':
            board[0][2] = player_o_turn
            break
            
        elif board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == '-':
            board[1][2] = player_o_turn
            break

        elif board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == '-':
            board[2][2] = player_o_turn
            break



        elif board[0][0] == 'x' and board[0][1] == '-' and board[0][2] == 'x':
            board[0][1] = player_o_turn
            break

        elif board[1][0] == 'x' and board[1][1] == '-' and board[1][2] == 'x':
            board[1][1] = player_o_turn
            break

        elif board[2][0] == 'x' and board[2][1] == '-' and board[2][2] == 'x':
            board[2][1] = player_o_turn
            break


        
        elif board[0][0] == '-' and board[0][1] == 'x' and board[0][2] == 'x':
            board[0][0] = player_o_turn
            break

        elif board[1][0] == '-' and board[1][1] == 'x' and board[1][2] == 'x':
            board[1][0] = player_o_turn
            break

        elif board[2][0] == '-' and board[2][1] == 'x' and board[2][2] == 'x':
            board[2][0] = player_o_turn
            break
        

        #all possible columns to block

        elif board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == '-':
            board[2][0] = player_o_turn
            break

        elif board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == '-':
            board[2][1] = player_o_turn
            break

        elif board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == '-':
            board[2][2] = player_o_turn
            break

        
        
        elif board[0][0] == 'x' and board[1][0] == '-' and board[2][0] == 'x':
            board[1][0] = player_o_turn
            break

        elif board[0][1] == 'x' and board[1][1] == '-' and board[2][1] == 'x':
            board[1][1] = player_o_turn
            break

        elif board[0][2] == 'x' and board[1][2] == '-' and board[2][2] == 'x':
            board[1][2] = player_o_turn
            break

        
    
        elif board[0][0] == '-' and board[1][0] == 'x' and board[2][0] == 'x':
            board[0][0] = player_o_turn
            break

        elif board[0][1] == '-' and board[1][1] == 'x' and board[2][1] == 'x':
            board[0][1] = player_o_turn
            break

        elif board[0][2] == '-' and board[1][2] == 'x' and board[2][2] == 'x':
            board[0][2] = player_o_turn
            break


        #all possible diagonals to block

        elif board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == '-':
            board[2][2] = player_o_turn
            break

        elif board[0][0] == 'x' and board[1][1] == '-' and board[2][2] == 'x':
            board[1][1] = player_o_turn
            break

        elif board[0][0] == '-' and board[1][1] == 'x' and board[2][2] == 'x':
            board[0][0] = player_o_turn
            break

        
        
        elif board[2][0] == 'x' and board[1][1] == 'x' and board[0][2] == '-':
            board[0][2] = player_o_turn
            break

        elif board[2][0] == 'x' and board[1][1] == '-' and board[0][2] == 'x':
            board[1][1] = player_o_turn
            break

        elif board[2][0] == '-' and board[1][1] == 'x' and board[0][2] == 'x':
            board[2][0] = player_o_turn
            break


        ####
        ####
        ####
        ####


        else: #if not a good move, choose randomly
            
            column = ['1','2','3'] #possible column posibilites 
            column = random.choice(column) #choose randomly from column posibilities
            row = ['1','2','3'] #possible row posibilities
            row = random.choice(row) #choose randoms from row posibilities
    
            if board[int(row)-1][int(column)-1] == "-": #subracts 1 from row and column of user's inputed row and column and checks if it an empty space
                board[int(row)-1][int(column)-1] = player_o_turn # if in empty space, make it player o's turn
                break
            
            else: #else, choose another random spot
                continue 

def ai_bot_2(player_x_turn, board):

    '''
    checks for best possible move bot as player 'X', if not found, picks random spot
    Args:
        player_o_turn(str): representation of player X
        board(list of lists): a 3x3 tic tac toe board 
    Returns:
        None: Function changes the board by printing the ai's move
    '''

    print('Bot decides to go here: ')

    while True:



        #all possible rows for bot to win
        if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == '-':
            board[0][2] = player_x_turn
            break
            
        elif board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == '-':
            board[1][2] = player_x_turn
            break

        elif board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == '-':
            board[2][2] = player_x_turn
            break



        elif board[0][0] == 'x' and board[0][1] == '-' and board[0][2] == 'x':
            board[0][1] = player_x_turn
            break

        elif board[1][0] == 'x' and board[1][1] == '-' and board[1][2] == 'x':
            board[1][1] = player_x_turn
            break

        elif board[2][0] == 'x' and board[2][1] == '-' and board[2][2] == 'x':
            board[2][1] = player_x_turn
            break


        
        elif board[0][0] == '-' and board[0][1] == 'x' and board[0][2] == 'x':
            board[0][0] = player_x_turn
            break

        elif board[1][0] == '-' and board[1][1] == 'x' and board[1][2] == 'x':
            board[1][0] = player_x_turn
            break

        elif board[2][0] == '-' and board[2][1] == 'x' and board[2][2] == 'x':
            board[2][0] = player_x_turn
            break
        

        #all possible columns for bot to win

        elif board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == '-':
            board[2][0] = player_x_turn
            break

        elif board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == '-':
            board[2][1] = player_x_turn
            break

        elif board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == '-':
            board[2][2] = player_x_turn
            break

        
        
        elif board[0][0] == 'x' and board[1][0] == '-' and board[2][0] == 'x':
            board[1][0] = player_x_turn
            break

        elif board[0][1] == 'x' and board[1][1] == '-' and board[2][1] == 'x':
            board[1][1] = player_x_turn
            break

        elif board[0][2] == 'x' and board[1][2] == '-' and board[2][2] == 'x':
            board[1][2] = player_x_turn
            break

        
    
        elif board[0][0] == '-' and board[1][0] == 'x' and board[2][0] == 'x':
            board[0][0] = player_x_turn
            break

        elif board[0][1] == '-' and board[1][1] == 'x' and board[2][1] == 'x':
            board[0][1] = player_x_turn
            break

        elif board[0][2] == '-' and board[1][2] == 'x' and board[2][2] == 'x':
            board[0][2] = player_x_turn
            break


        #all possible diagonals for bot to win

        elif board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == '-':
            board[2][2] = player_x_turn
            break

        elif board[0][0] == 'x' and board[1][1] == '-' and board[2][2] == 'x':
            board[1][1] = player_x_turn
            break

        elif board[0][0] == '-' and board[1][1] == 'x' and board[2][2] == 'x':
            board[0][0] = player_x_turn
            break

        
        
        elif board[2][0] == 'x' and board[1][1] == 'x' and board[0][2] == '-':
            board[0][2] = player_x_turn
            break

        elif board[2][0] == 'x' and board[1][1] == '-' and board[0][2] == 'x':
            board[1][1] = player_x_turn
            break

        elif board[2][0] == '-' and board[1][1] == 'x' and board[0][2] == 'x':
            board[2][0] = player_x_turn
            break
        
        ####
        ####
        ####
        ####

        #all possible rows to block
        if board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == '-':
            board[0][2] = player_x_turn
            break
            
        elif board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == '-':
            board[1][2] = player_x_turn
            break

        elif board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == '-':
            board[2][2] = player_x_turn
            break



        elif board[0][0] == 'o' and board[0][1] == '-' and board[0][2] == 'o':
            board[0][1] = player_x_turn
            break

        elif board[1][0] == 'o' and board[1][1] == '-' and board[1][2] == 'o':
            board[1][1] = player_x_turn
            break

        elif board[2][0] == 'o' and board[2][1] == '-' and board[2][2] == 'o':
            board[2][1] = player_x_turn
            break


        
        elif board[0][0] == '-' and board[0][1] == 'o' and board[0][2] == 'o':
            board[0][0] = player_x_turn
            break

        elif board[1][0] == '-' and board[1][1] == 'o' and board[1][2] == 'o':
            board[1][0] = player_x_turn
            break

        elif board[2][0] == '-' and board[2][1] == 'o' and board[2][2] == 'o':
            board[2][0] = player_x_turn
            break
        

        #all possible columns to block

        elif board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == '-':
            board[2][0] = player_x_turn
            break

        elif board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == '-':
            board[2][1] = player_x_turn
            break

        elif board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == '-':
            board[2][2] = player_x_turn
            break

        
        
        elif board[0][0] == 'o' and board[1][0] == '-' and board[2][0] == 'o':
            board[1][0] = player_x_turn
            break

        elif board[0][1] == 'o' and board[1][1] == '-' and board[2][1] == 'o':
            board[1][1] = player_x_turn
            break

        elif board[0][2] == 'o' and board[1][2] == '-' and board[2][2] == 'o':
            board[1][2] = player_x_turn
            break

        
    
        elif board[0][0] == '-' and board[1][0] == 'o' and board[2][0] == 'o':
            board[0][0] = player_x_turn
            break

        elif board[0][1] == ' ' and board[1][1] == 'o' and board[2][1] == 'o':
            board[0][1] = player_x_turn
            break

        elif board[0][2] == '-' and board[1][2] == 'o' and board[2][2] == 'o':
            board[0][2] = player_x_turn
            break


        #all possible diagonals to block

        elif board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == '-':
            board[2][2] = player_x_turn
            break

        elif board[0][0] == 'o' and board[1][1] == '-' and board[2][2] == 'o':
            board[1][1] = player_x_turn
            break

        elif board[0][0] == '-' and board[1][1] == 'o' and board[2][2] == 'o':
            board[0][0] = player_x_turn
            break

        
        
        elif board[2][0] == 'o' and board[1][1] == 'o' and board[0][2] == '-':
            board[0][2] = player_x_turn
            break

        elif board[2][0] == 'o' and board[1][1] == '-' and board[0][2] == 'o':
            board[1][1] = player_x_turn
            break

        elif board[2][0] == '-' and board[1][1] == 'o' and board[0][2] == 'o':
            board[2][0] = player_x_turn
            break

        
        else: #if not good move, ai picks randomly
            
            column = ['1','2','3'] #possible column choices
            column = random.choice(column) #chooses randomly from possible column choices
            row = ['1','2','3'] #possible row choices
            row = random.choice(row) #ai chooses randoly from possible column choices
    
            if board[int(row)-1][int(column)-1] == '-': #if board of row -1 and column -1 is an empty space
                board[int(row)-1][int(column)-1] = player_x_turn #makes it player X's turn
                break
            
            else: #else, pick another spot 
                continue



def player_x_move(player1, player_x_turn, board):

    '''
    asks player x for row and column for their move, and assigns board values to that move
    Args:
        player1(str): player's inputed name for player X
        player_o_turn(str): representation of player X 
        board(list of lists): a 3x3 tic tac toe board 
    Returns:
        player's x's move for where they go on the tic tac toe board
    '''

    while True:

        row = input(f'{player1}, which row would you like? 1, 2, or 3?') #asks user for row
        if row == '1' or row == '2' or row == '3':
             pass
        else: 
            print('sorry, that is not a row') #else, print sorry that is not a row
            continue

        column = input(f'{player1}, which column would you like? 1, 2, or 3?') #ask user for column
        if column == '1' or column == '2' or column == '3':
            pass
        else:  
            print('sorry, that is not a column') #else, print sorry that is not a column
            continue

        

        
        if board[int(row)-1][int(column)-1] == "-": #if board of row -1 and column -1 is an empty space
            board[int(row)-1][int(column)-1] = player_x_turn #if empty, makes it player X's turn
            display_board(board) #print board
            break
        
        else:
            print('sorry, someone already went in that box') #else, tell user that they need to pick another box
            continue



def player_o_move(player2, player_o_turn, board):

    '''
    asks player O for row and column for their move, and assigns board values to that move
    Args:
        player2(str): player's inputed name for player O
        player_o_turn(str): representation of player O
        board(list of lists): a 3x3 tic tac toe board 
    Returns:
        player's O's move for where they go on the tic tac toe board
    '''

    while True:
        
        row = input(f'{player2}, which row would you like? 1, 2, or 3?')
        if row == '1' or row == '2' or row == '3':
             pass
        else: 
            print('sorry, that is not a row')
            continue

        column = input(f'{player2} which column would you like? 1, 2, or 3?')
        if column == '1' or column == '2' or column == '3':
            pass
        else:  
            print('sorry, that is not a column')
            continue
        
        if board[int(row)-1][int(column)-1] == "-": #if board of row -1 and column -1 is an empty space
            board[int(row)-1][int(column)-1] = player_o_turn #if empty, makes it player X's turn
            display_board(board) #print board
            break
        
        else:
            print('sorry, someone already went in that box') #else, tell user that they need to pick another box
            continue
        
        


def check_winner(player1, player2, board):

    '''
    checks all possible combinations for three in a row and win in tic tac toe for both parties
    Args:
        player1(str): player's inputed name for X
        player2(str): representation of player O 
        board(list of lists): a 3x3 tic tac toe board 
    Returns:
        None: prints congratulations and player name for whoever won 
    '''

    while True:
        if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x':
            print(f'congratulations, {player1} has won!')
            playagain()
        
        elif board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x':
            print(f'congratulations, {player1} has won!')
            playagain()
        
        elif board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x':
            print(f'congratulations, {player1} has won!')
            playagain()
        
        elif board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x':
            print(f'congratulations, {player1} has won!')
            playagain()
        
        elif board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x':
            print(f'congratulations, {player1} has won!')
            playagain()
        
        elif board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x':
            print(f'congratulations, {player1} has won!')
            playagain()
        
        elif board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
            print(f'congratulations, {player1} has won!')
            playagain()

        elif board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x':
            print(f'congratulations, {player1} has won!')
            playagain()

        elif board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == 'o':
            print(f'congratulations, {player2} has won!')
            playagain()
        
        elif board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == 'o':
            print(f'congratulations, {player2} has won!')
            playagain()
        
        elif board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == 'o':
            print(f'congratulations, {player2} has won!')
            playagain()
        
        elif board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == 'o':
            print(f'congratulations, {player2} has won!')
            playagain()
        
        elif board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == 'o':
            print(f'congratulations, {player2} has won!')
            playagain()
        
        elif board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == 'o':
            print(f'congratulations, {player2} has won!')
            playagain()
        
        elif board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
            print(f'congratulations, {player2} has won!')
            playagain()

        elif board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o':
            print(f'congratulations, {player2} has won!')
            playagain()
    
        else: 
            return False


    
def check_draw(board):
    '''
    checks board for draws and returns false 
    Args: 
        board(list of lists): a 3x3 tic tac toe board 
    Returns:
        False: if game still has empty spots, returns false
        None: else, will print the game is a tie
    '''

    if board[0][0] == '-' or board[0][1] == '-' or board[0][2] == '-' or board[1][0] == '-' or board[1][1] == '-' or board[1][2] == '-' or board[2][0] == '-' or board[2][1] == '-' or board[2][2] == '-':
        return False
    else:
        print('The game is a tie!')
        playagain()



def display_board(board): 
    '''
    prints board using a 'for' loop to elimate parentesis and quotes around board moves
    Args: 
        board(list of lists): a 3x3 tic tac toe board 
    Returns:
        Printed board
    '''
    for row in board:
        for cell in row:     
            print(cell, end=' ')        
        print()

def main():

    option = input("Would you like to play against human or bot?") #asks user for game mode
    
    if option == 'human': #if option is to play human against human
        
        player1 = input("Player X, what is your name: ") #asks player 1 for name
        player2 = input("Player Y, what is your name: ") #asks player 2 for name
        
        turns = 1
        board = [['-', '-', '-'],  #board
                ['-', '-', '-'], 
                ['-', '-', '-']]
        while check_winner(player1, player2, board) == False and check_draw(board) == False: #if check winner and check draw are both false, keep playing
            if turns == 1 or turns == 3 or turns == 5 or turns == 7 or turns == 9:
                player_x_move(player1,'x', board)
                turns += 1
            else:
                player_o_move(player2,'o', board)
                turns += 1
    
    elif option == 'bot': #if option is to play against a bot

        while True:
            option = input('Would you like to play as X or O?') #asks user if they would like ot play as X or O
            
            if option == "X": #if user chooses X 
            
                player1 = input("Player X, what is your name: ") 
                player2 = 'bot'
                
                turns = 1
                board = [['-', '-', '-'], #board
                        ['-', '-', '-'], 
                        ['-', '-', '-']]
                while check_winner(player1, player2, board) == False and check_draw(board) == False: #if check winner and check draw are both false, keep playing
                    if turns == 1 or turns == 3 or turns == 5 or turns == 7 or turns == 9: #decides whether it is O or X's turn
                        player_x_move(player1, 'x', board)
                        turns += 1
                    else:
                        ai_bot('o', board) #ai_bot function
                        turns += 1
                        display_board(board) #display board function
                        
            elif option == "O": #if user chooses O
                
                player1 = 'bot'
                player2 = input("Player O, what is your name: ")
                
                turns = 1
                board = [['-', '-', '-'], #board
                        ['-', '-', '-'], 
                        ['-', '-', '-']]
                while check_winner(player1, player2, board) == False and check_draw(board) == False: #if check winner and check draw are both false, keep playing
                    if turns == 1 or turns == 3 or turns == 5 or turns == 7 or turns == 9:
                        ai_bot_2('x', board)
                        display_board(board) 
                        turns += 1
                    else:
                        player_o_move(player2, 'o', board)
                        turns += 1
                        

            else: 
                print("Please input X or O") #else, tell user to input X or O
                continue

    else:
        print('please input human or bot') #else, tell user to input human or bot

    

def playagain(): 

    '''
    asks user is they would like to play again
    Args:
        None
    Returns:
        depending on user's decision, play again or exit
    '''

    while True:
        option = input("Would you like to play Tic Tac Toe? yes or no")
        if option == "yes":
            main()
        elif option == "no":
            exit()

        else: 
            print('Invalid response, please input just: yes or no')
            continue

playagain()




#not intelligent bot code
'''
def bot(player_o_turn, board):

    while True:

        print('Bot decides to go here: ')
        
        column = ['1','2','3']
        column = random.choice(column)
        row = ['1','2','3']
        row = random.choice(row)
 
        if board[int(row)-1][int(column)-1] == " ":
            board[int(row)-1][int(column)-1] = player_o_turn
            print(f"""
        {board[0]}
        {board[1]}
        {board[2]}
                  """)
            break
        
        else:
            continue
'''



'''
for row in board:
for cell in row:
    print(cell)
'''


'''
 #all possible rows for bot to win with empty space
        if board[0][0] == ' ' and board[0][1] == ' ' and board[0][2] == 'o':
            #now you have to change where the bot will go next. Just choose the space next to where the bot already has gone
            board[0][2] = player_x_turn #!!!!
            break
            
        elif board[1][0] == ' ' and board[1][1] == ' ' and board[1][2] == 'o':
            board[1][2] = player_x_turn
            break

        elif board[2][0] == ' ' and board[2][1] == ' ' and board[2][2] == 'o':
            board[2][2] = player_o_turn
            break



        elif board[0][0] == ' ' and board[0][1] == 'o' and board[0][2] == ' ':
            board[0][1] = player_o_turn
            break

        elif board[1][0] == ' ' and board[1][1] == 'o' and board[1][2] == ' ':
            board[1][1] = player_o_turn
            break

        elif board[2][0] == ' ' and board[2][1] == 'o' and board[2][2] == ' ':
            board[2][1] = player_o_turn
            break


        
        elif board[0][0] == 'o' and board[0][1] == ' ' and board[0][2] == ' ':
            board[0][0] = player_o_turn
            break

        elif board[1][0] == 'o' and board[1][1] == ' ' and board[1][2] == ' ':
            board[1][0] = player_o_turn
            break

        elif board[2][0] == 'o' and board[2][1] == ' ' and board[2][2] == ' ':
            board[2][0] = player_o_turn
            break
        

        #all possible columns for bot to win

        elif board[0][0] == ' ' and board[1][0] == ' ' and board[2][0] == 'o':
            board[2][0] = player_o_turn
            break

        elif board[0][1] == ' ' and board[1][1] == ' ' and board[2][1] == 'o':
            board[2][1] = player_o_turn
            break

        elif board[0][2] == ' ' and board[1][2] == ' ' and board[2][2] == 'o':
            board[2][2] = player_o_turn
            break

        
        
        elif board[0][0] == ' ' and board[1][0] == 'o' and board[2][0] == ' ':
            board[1][0] = player_o_turn
            break

        elif board[0][1] == ' ' and board[1][1] == 'o' and board[2][1] == ' ':
            board[1][1] = player_o_turn
            break

        elif board[0][2] == ' ' and board[1][2] == 'o' and board[2][2] == ' ':
            board[1][2] = player_o_turn
            break

        
    
        elif board[0][0] == 'o' and board[1][0] == ' ' and board[2][0] == ' ':
            board[0][0] = player_o_turn
            break

        elif board[0][1] == 'o' and board[1][1] == ' ' and board[2][1] == ' ':
            board[0][1] = player_o_turn
            break

        elif board[0][2] == 'o' and board[1][2] == ' ' and board[2][2] == ' ':
            board[0][2] = player_o_turn
            break


        #all possible diagonals for bot to win

        elif board[0][0] == ' ' and board[1][1] == ' ' and board[2][2] == 'o':
            board[2][2] = player_o_turn
            break

        elif board[0][0] == ' ' and board[1][1] == 'o' and board[2][2] == ' ':
            board[1][1] = player_o_turn
            break

        elif board[0][0] == 'o' and board[1][1] == ' ' and board[2][2] == ' ':
            board[0][0] = player_o_turn
            break

        
        
        elif board[2][0] == ' ' and board[1][1] == ' ' and board[0][2] == 'o':
            board[0][2] = player_o_turn
            break

        elif board[2][0] == ' ' and board[1][1] == 'o' and board[0][2] == ' ':
            board[1][1] = player_o_turn
            break

        elif board[2][0] == 'o' and board[1][1] == ' ' and board[0][2] == ' ':
            board[2][0] = player_o_turn
            break

        else:
            
            column = ['1','2','3']
            column = random.choice(column)
            row = ['1','2','3']
            row = random.choice(row)
    
            if board[int(row)-1][int(column)-1] == " ":
                board[int(row)-1][int(column)-1] = player_o_turn
                break
            
            else:
                continue



'''


'''
#all possible rows for bot to win with empty space
        if board[0][0] == ' ' and board[0][1] == ' ' and board[0][2] == 'o':
            #now you have to change where the bot will go next. Just choose the space next to where the bot already has gone
            board[0][2] = player_o_turn #!!!!
            break
            
        elif board[1][0] == ' ' and board[1][1] == ' ' and board[1][2] == 'o':
            board[1][2] = player_o_turn
            break

        elif board[2][0] == ' ' and board[2][1] == ' ' and board[2][2] == 'o':
            board[2][2] = player_o_turn
            break



        elif board[0][0] == ' ' and board[0][1] == 'o' and board[0][2] == ' ':
            board[0][1] = player_o_turn
            break

        elif board[1][0] == ' ' and board[1][1] == 'o' and board[1][2] == ' ':
            board[1][1] = player_o_turn
            break

        elif board[2][0] == ' ' and board[2][1] == 'o' and board[2][2] == ' ':
            board[2][1] = player_o_turn
            break


        
        elif board[0][0] == 'o' and board[0][1] == ' ' and board[0][2] == ' ':
            board[0][0] = player_o_turn
            break

        elif board[1][0] == 'o' and board[1][1] == ' ' and board[1][2] == ' ':
            board[1][0] = player_o_turn
            break

        elif board[2][0] == 'o' and board[2][1] == ' ' and board[2][2] == ' ':
            board[2][0] = player_o_turn
            break
        

        #all possible columns for bot to win

        elif board[0][0] == ' ' and board[1][0] == ' ' and board[2][0] == 'o':
            board[2][0] = player_o_turn
            break

        elif board[0][1] == ' ' and board[1][1] == ' ' and board[2][1] == 'o':
            board[2][1] = player_o_turn
            break

        elif board[0][2] == ' ' and board[1][2] == ' ' and board[2][2] == 'o':
            board[2][2] = player_o_turn
            break

        
        
        elif board[0][0] == ' ' and board[1][0] == 'o' and board[2][0] == ' ':
            board[1][0] = player_o_turn
            break

        elif board[0][1] == ' ' and board[1][1] == 'o' and board[2][1] == ' ':
            board[1][1] = player_o_turn
            break

        elif board[0][2] == ' ' and board[1][2] == 'o' and board[2][2] == ' ':
            board[1][2] = player_o_turn
            break

        
    
        elif board[0][0] == 'o' and board[1][0] == ' ' and board[2][0] == ' ':
            board[0][0] = player_o_turn
            break

        elif board[0][1] == 'o' and board[1][1] == ' ' and board[2][1] == ' ':
            board[0][1] = player_o_turn
            break

        elif board[0][2] == 'o' and board[1][2] == ' ' and board[2][2] == ' ':
            board[0][2] = player_o_turn
            break


        #all possible diagonals for bot to win

        elif board[0][0] == ' ' and board[1][1] == ' ' and board[2][2] == 'o':
            board[2][2] = player_o_turn
            break

        elif board[0][0] == ' ' and board[1][1] == 'o' and board[2][2] == ' ':
            board[1][1] = player_o_turn
            break

        elif board[0][0] == 'o' and board[1][1] == ' ' and board[2][2] == ' ':
            board[0][0] = player_o_turn
            break

        
        
        elif board[2][0] == ' ' and board[1][1] == ' ' and board[0][2] == 'o':
            board[0][2] = player_o_turn
            break

        elif board[2][0] == ' ' and board[1][1] == 'o' and board[0][2] == ' ':
            board[1][1] = player_o_turn
            break

        elif board[2][0] == 'o' and board[1][1] == ' ' and board[0][2] == ' ':
            board[2][0] = player_o_turn
            break
'''