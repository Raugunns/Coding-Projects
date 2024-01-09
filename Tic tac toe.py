import random

def print_board():
    print("-------------")
    for i in range(3):
        print("|", board[i * 3], "|", board[i * 3 + 1], "|", board[i * 3 + 2], "|")
        print("-------------")

def check_win(player):
    for i in range(3):
        if (board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == player):
            return True
    for i in range(3):
        if (board[i] == board[i + 3] == board[i + 6] == player):
            return True
    if (board[0] == board[4] == board[8] == player or
            board[2] == board[4] == board[6] == player):
        return True
    return False

def play_game():
    print("Welcome to Tic Tac Toe!")
    print("Select the mode:")
    print("1. 2 Players")
    print("2. Against Computer")
    mode = int(input("Enter your choice (1 or 2): "))

    if mode == 1:
        two_players_game()
    elif mode == 2:
        against_computer_game()
    else:
        print("Invalid choice. Exiting...")

def two_players_game():
    current_player = "X"
    while True:
        print_board()
        print("Player", current_player, "turn. Enter the position (1-9): ")
        position = int(input()) - 1

        if board[position] == " ":
            board[position] = current_player

            if check_win(current_player):
                print_board()
                print("Player", current_player, "wins!")
                break

            if " " not in board:
                print_board()
                print("It's a tie!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("Move is invalid. Try again.")

def against_computer_game():
    current_player = "X"
    while True:
        print_board()
        if current_player == "X":
            print("Player", current_player, "turn. Enter the position (1-9): ")
            position = int(input()) - 1
        else:
            position = random.choice([i for i in range(9) if board[i] == " "])

        if board[position] == " ":
            board[position] = current_player

            if check_win(current_player):
                print_board()
                if current_player == "X":
                    print("Player", current_player, "wins!")
                else:
                    print("Computer wins!")
                break

            if " " not in board:
                print_board()
                print("It's a tie!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("Move is invalid. Try again.")

board = [" " for _ in range(9)]
play_game()

