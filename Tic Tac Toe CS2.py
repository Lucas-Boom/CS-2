import random

       

def ai_bot(player_o_turn, board):

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


        else:
            
            column = ['1','2','3']
            column = random.choice(column)
            row = ['1','2','3']
            row = random.choice(row)
    
            if board[int(row)-1][int(column)-1] == "-":
                board[int(row)-1][int(column)-1] = player_o_turn
                break
            
            else:
                continue

def ai_bot_2(player_x_turn, board):

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

        
        else:
            
            column = ['1','2','3']
            column = random.choice(column)
            row = ['1','2','3']
            row = random.choice(row)
    
            if board[int(row)-1][int(column)-1] == '-':
                board[int(row)-1][int(column)-1] = player_x_turn
                break
            
            else:
                continue



def player_x_move(player1, player_x_turn, board):

    while True:

        row = input(f'{player1}, which row would you like? 1, 2, or 3?')
        if row == '1' or row == '2' or row == '3':
             pass
        else: 
            print('sorry, that is not a row')
            continue

        column = input(f'{player1}, which column would you like? 1, 2, or 3?')
        if column == '1' or column == '2' or column == '3':
            pass
        else:  
            print('sorry, that is not a column')
            continue

        

        
        if board[int(row)-1][int(column)-1] == "-":
            board[int(row)-1][int(column)-1] = player_x_turn
            display_board(board)
            break
        
        else:
            print('sorry, someone already went in that box')
            continue



def player_o_move(player2, player_o_turn, board):

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
        
        if board[int(row)-1][int(column)-1] == "-":
            board[int(row)-1][int(column)-1] = player_o_turn
            display_board(board)
            break
        
        else:
            print('sorry, someone already went in that box')
            continue
        
        


def check_winner(player1, player2, board):

    while True:
        if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x':
            print(f'congratulations, {player1} has won!')
            exit()
        
        elif board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x':
            print(f'congratulations, {player1} has won!')
            exit()
        
        elif board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x':
            print(f'congratulations, {player1} has won!')
            exit()
        
        elif board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x':
            print(f'congratulations, {player1} has won!')
            exit()
        
        elif board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x':
            print(f'congratulations, {player1} has won!')
            exit()
        
        elif board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x':
            print(f'congratulations, {player1} has won!')
            exit()
        
        elif board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
            print(f'congratulations, {player1} has won!')
            exit()

        elif board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x':
            print(f'congratulations, {player1} has won!')
            exit()

        elif board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == 'o':
            print(f'congratulations, {player2} has won!')
            exit()
        
        elif board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == 'o':
            print(f'congratulations, {player2} has won!')
            exit()
        
        elif board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == 'o':
            print(f'congratulations, {player2} has won!')
            exit()
        
        elif board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == 'o':
            print(f'congratulations, {player2} has won!')
            exit()
        
        elif board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == 'o':
            print(f'congratulations, {player2} has won!')
            exit()
        
        elif board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == 'o':
            print(f'congratulations, {player2} has won!')
            exit()
        
        elif board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
            print(f'congratulations, {player2} has won!')
            exit()

        elif board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o':
            print(f'congratulations, {player2} has won!')
            exit()
    
        else: 
            return False


    
def check_draw(board):
    if board[0][0] == '-' or board[0][1] == '-' or board[0][2] == '-' or board[1][0] == '-' or board[1][1] == '-' or board[1][2] == '-' or board[2][0] == '-' or board[2][1] == '-' or board[2][2] == '-':
        return False
    else:
        print('The game is a tie!')
        exit()



def display_board(board): 
    for row in board:
        for cell in row:     
            print(cell, end=' ')        
        print()

def main():
    
    option = input("Would you like to play against human or bot?")
    
    if option == 'human':
        
        player1 = input("Player X, what is your name: ")
        player2 = input("Player Y, what is your name: ")
        
        turns = 1
        board = [['-', '-', '-'],
                ['-', '-', '-'], 
                ['-', '-', '-']]
        while check_winner(player1, player2, board) == False and check_draw(board) == False:
            if turns == 1 or turns == 3 or turns == 5 or turns == 7 or turns == 9:
                player_x_move(player1,'x', board)
                turns += 1
            else:
                player_o_move(player2,'o', board)
                turns += 1
    
    elif option == 'bot':

        option = input('Would you like to play as X or O?')
        
        if option == "X":
           
            player1 = input("Player X, what is your name: ")
            player2 = 'bot'
            
            turns = 1
            board = [['-', '-', '-'],
                    ['-', '-', '-'], 
                    ['-', '-', '-']]
            while check_winner(player1, player2, board) == False and check_draw(board) == False:
                if turns == 1 or turns == 3 or turns == 5 or turns == 7 or turns == 9:
                    player_x_move(player1, 'x', board)
                    turns += 1
                else:
                    ai_bot('o', board)
                    turns += 1
                    display_board(board)
                    
        elif option == "O":
            
            player1 = 'bot'
            player2 = input("Player O, what is your name: ")
            
            turns = 1
            board = [['-', '-', '-'],
                    ['-', '-', '-'], 
                    ['-', '-', '-']]
            while check_winner(player1, player2, board) == False and check_draw(board) == False:
                if turns == 1 or turns == 3 or turns == 5 or turns == 7 or turns == 9:
                    ai_bot_2('x', board)
                    display_board(board)
                    turns += 1
                else:
                    player_o_move(player2, 'o', board)
                    turns += 1
                    

        else: 
            print("Please input X or O")

    else:
        print('please input human or bot')

    

def playagain():

    while True:
        option = input("Would you like to play Tic Tac Toe? yes or no")
        if option == "yes":
            main()
        elif option == "no":
            exit()

        else: 
            print('Invalid response, please input yes or no')
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