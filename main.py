"""
Tic-Tac-Toe Game
2021.06.14
https://gitlab.com/foxdata-io/tic-tac-toe

TODO: Implement computer player decision making
"""


def check_for_winner(board, player):
    # Using the provided player ("X" or "O"), determine if there is a winner.
    if board[0] == player:
        if board[3] == player:
            if board[6] == player:
                return 1
        elif board[4] == player:
            if board[8] == player:
                return 1
        elif board[1] == player:
            if board[2] == player:
                return 1
    if board[1] == player:
        if board[4] == player:
            if board[7] == player:
                return 1
    if board[2] == player:
        if board[5] == player:
            if board[8] == player:
                return 1
        elif board[4] == player:
            if board[6] == player:
                return 1
    if board[3] == player:
        if board[4] == player:
            if board[5] == player:
                return 1
    if board[6] == player:
        if board[7] == player:
            if board[8] == player:
                return 1
    return 0


def display_game_board(board):
    print(f'''
{board[0]}|{board[1]}|{board[2]}
-----
{board[3]}|{board[4]}|{board[5]}
-----
{board[6]}|{board[7]}|{board[8]}
    ''')


def show_help():
    print('''
    Use the digits 1-9 to select squares.
    1|2|3
    -----
    4|5|6
    -----
    7|8|9
    ''')


def show_menu():
    print('''
    [P]lay Game
    [H]elp
    [Q]uit
    ''')
    return input("Your choice: ").upper()


if __name__ == '__main__':

    # Flag for gameplay loop
    winner = 0
    user_move = 0
    menu_choice = ""

    # Show title
    print("Tic-Tac-Toe")

    # Show menu
    while menu_choice != "Q":
        menu_choice = show_menu()
        if menu_choice == "H":
            show_help()
        elif menu_choice == "Q":
            print("Goodbye!")
        elif menu_choice == "P":
            # Clear our game board and show the initial state.
            winner = 0
            game_board = list((" ", " ", " ", " ", " ", " ", " ", " ", " ",))
            display_game_board(game_board)

            # Main game loop. Runs until there is a winner.
            while not winner:
                # Loop until the user makes a valid move.
                valid_move = False
                while not valid_move:
                    # Get the user's move.
                    user_move = int(input("Enter your move: "))

                    # Check that the move submitted is valid.
                    # It must be between 1 and 9, as well as an empty space.
                    if user_move < 1 or user_move > 9:
                        print("Please choose a square between 1 and 9.")
                    else:
                        valid_move = game_board[user_move - 1] == " "
                        if not valid_move:
                            print("That square is already taken. Try again.")

                # We have a valid move at this point, so set the space to X and redisplay the game board
                game_board[user_move - 1] = "X"
                display_game_board(game_board)

                # Check to see if the move just made wins the game.
                # If X has won, winner == 1, if O has won, winner == 2
                # We only check for X win here. O wins are checked after the computer takes its turn.
                if check_for_winner(game_board, "X"):
                    winner = 1

                # Determine if the game has ended in a tie. If the board is full, and there is no
                # current winner, then the game is a tie and must end.
                if not winner and game_board.count(" ") == 0:
                    break

                # Only process computer move if user has not yet won.
                if not winner:
                    # Scan for open spot
                    for play_area in range(0, 8):
                        if game_board[play_area] == " ":
                            print(f"Computer plays {play_area + 1}.")
                            game_board[play_area] = "O"
                            display_game_board(game_board)
                            break

                    if check_for_winner(game_board, "O"):
                        winner = 2

                    # Determine if the game has ended in a tie. If the board is full, and there is no
                    # current winner, then the game is a tie and must end.
                    if not winner and game_board.count(" ") == 0:
                        break

            # Display the winner
            if winner == 1:
                print("You Win!")
            elif winner == 2:
                print("Computer Wins!")
            elif not winner:
                print("Tie Game!")

    # Done!
