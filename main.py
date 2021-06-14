# Tic-Tac-Toe Game
# 2021.06.14
# https://gitlab.com/foxdata-io/tic-tac-toe


# Store board as a list
empty_game_board = list((" ", " ", " ", " ", " ", " ", " ", " ", " "))


def check_for_winner(board):
    # TODO: Determine which player wins. Currently only looks for ANY winner.
    if board[0] != " " and board[0] == board[3] and board[0] == board[6]:
        return 1
    elif board[1] != " " and board[1] == board[4] and board[1] == board[7]:
        return 1
    elif board[2] != " " and board[2] == board[5] and board[2] == board[8]:
        return 1
    elif board[2] != " " and board[2] == board[4] and board[2] == board[6]:
        return 1
    elif board[0] != " " and board[0] == board[4] and board[0] == board[8]:
        return 1
    elif board[0] != " " and board[0] == board[1] and board[0] == board[2]:
        return 1
    elif board[3] != " " and board[3] == board[4] and board[3] == board[5]:
        return 1
    elif board[6] != " " and board[6] == board[7] and board[6] == board[8]:
        return 1
    return 0


def check_move(move, board):
    if board[move-1] == " ":
        return 1
    else:
        return 0


def display_game_board(board):
    print(f'''
{board[0]}|{board[1]}|{board[2]}
-----
{board[3]}|{board[4]}|{board[5]}
-----
{board[6]}|{board[7]}|{board[8]}
    ''')


if __name__ == '__main__':

    # Flag for gameplay loop
    winner = 0
    user_move = 0

    print("Tic-Tac-Toe")

    # TODO: Add menu

    # Clear our game board
    game_board = empty_game_board

    while winner == 0:
        print("Checking for winner")
        valid_move = 0
        while valid_move == 0:
            print("No winner yet")
            display_game_board(game_board)
            user_move = 0
            user_move = int(input("Enter your move: "))
            if user_move < 1 or user_move > 9:
                print("Please choose a square between 1 and 9.")
            else:
                print("Checking for valid move")
                valid_move = check_move(user_move, game_board)
                if valid_move == 0:
                    print("You cannot choose that square. Try again.")
        print("Setting user move to X")
        game_board[user_move - 1] = "X"
        winner = check_for_winner(game_board)
        # TODO: Add computer move
