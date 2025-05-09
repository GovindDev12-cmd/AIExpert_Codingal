import random
from colorama import init, Fore, style
init(autoreset=True)


def display_board(board):
    print()
    def colored(cell):
        if cell =='X':
            return Fore.RED + cell + style.RESET_ALL
        elif cell == '0':
            return Fore.RED + cell + style.RESET_ALL
        else:
            return Fore.YELLOW + cell+ Style.RESET_ALL
        

    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))


def player_choice():
    symbol = ""
    while symbol not in ['X','0']:
     try:
         move = int(input("Enter you move (1-9):"))
         if move not in range(1, 10) or not board[move - 1].isdigit():
             print("Invalid move. please try again")
        except ValueError:
          print("Please enter number between 1 and 9")
        board[move-1] = symbol
     

def ai_move(board, ai_symbol,player_symbol):
    for i in range(9):
        if board[i].indisgit():
            board_copy = board
            board_copy