import random
from colorama import init, Fore, Style

init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    
    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))

def player_choice(board, symbol):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move not in range(1, 10):
                print("Please enter a number between 1 and 9")
            elif not board[move - 1].isdigit():
                print("Invalid move. Cell already taken, please try again")
            else:
                board[move - 1] = symbol
                break
        except ValueError:
            print("Please enter a number between 1 and 9")
    return board

def ai_move(board, ai_symbol, player_symbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol
            if check_winner(board_copy, ai_symbol):
                board[i] = ai_symbol
                return board
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol
            if check_winner(board_copy, player_symbol):
                board[i] = ai_symbol
                return board
    available = [i for i in range(9) if board[i].isdigit()]
    if available:
        move = random.choice(available)
        board[move] = ai_symbol
    return board

def check_winner(board, symbol):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == symbol:
            return True
    return False

def is_board_full(board):
    return all(not cell.isdigit() for cell in board)

def play_game():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    player_symbol = ''
    while player_symbol not in ['X', 'O']:
        player_symbol = input("Choose your symbol (X or O): ").upper()
    ai_symbol = 'O' if player_symbol == 'X' else 'X'
    
    while True:
        display_board(board)
        board = player_choice(board, player_symbol)
        if check_winner(board, player_symbol):
            display_board(board)
            print("Congratulations! You win!")
            break
        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break
        board = ai_move(board, ai_symbol, player_symbol)
        if check_winner(board, ai_symbol):
            display_board(board)
            print("AI wins!")
            break
        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()