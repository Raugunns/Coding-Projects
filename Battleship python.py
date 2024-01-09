import random

class Player:
    def __init__(self, name):
        self.name = name
        self.board = [[' '] * 10 for _ in range(10)]
        self.ships = {'carrier': 5, 'battleship': 4, 'cruiser': 3, 'submarine': 3, 'destroyer': 2}
        self.enemy_board = [[' '] * 10 for _ in range(10)]
        self.moves = set()

    def place_ships(self):
        for ship, size in self.ships.items():
            while True:
                self.print_board()
                print(f"{self.name}, place your {ship} ({size} cells)")
                start = input("Enter the starting coordinate (e.g., A1): ").upper()
                orientation = input("Enter orientation (H for horizontal, V for vertical): ").upper()

                row, col = ord(start[0]) - 65, int(start[1:]) - 1

                if self.is_valid_placement(row, col, size, orientation):
                    self.place_ship(ship, row, col, size, orientation)
                    break
                else:
                    print("Invalid placement. Try again.")

    def is_valid_placement(self, row, col, size, orientation):
        if orientation == 'H':
            return col + size <= 10 and all(self.board[row][c] == ' ' for c in range(col, col + size))
        elif orientation == 'V':
            return row + size <= 10 and all(self.board[r][col] == ' ' for r in range(row, row + size))
        return False

    def place_ship(self, ship, row, col, size, orientation):
        if orientation == 'H':
            for c in range(col, col + size):
                self.board[row][c] = ship[0]
        elif orientation == 'V':
            for r in range(row, row + size):
                self.board[r][col] = ship[0]

    def print_board(self):
        print(f"\n{self.name}'s Board:")
        print("   1 2 3 4 5 6 7 8 9 10")
        print("  ---------------------")
        for i in range(10):
            print(chr(65 + i), "|", " ".join(self.board[i]))
        print("\n")

    def print_enemy_board(self):
        print(f"\n{self.name}'s Enemy Board:")
        print("   1 2 3 4 5 6 7 8 9 10")
        print("  ---------------------")
        for i in range(10):
            print(chr(65 + i), "|", " ".join(self.enemy_board[i]))
        print("\n")

    def make_move(self, opponent):
        while True:
            move = input(f"{self.name}, enter your target (e.g., A1): ").upper()
            row, col = ord(move[0]) - 65, int(move[1:]) - 1

            if self.is_valid_move(row, col):
                self.moves.add((row, col))
                if opponent.receive_attack(row, col):
                    print("Hit!")
                else:
                    print("Miss!")
                break
            else:
                print("Invalid move. Try again.")

    def is_valid_move(self, row, col):
        return 0 <= row < 10 and 0 <= col < 10 and (row, col) not in self.moves

    def receive_attack(self, row, col):
        if self.board[row][col] != ' ':
            ship_hit = self.board[row][col]
            self.board[row][col] = 'X'
            self.print_board()
            print(f"{self.name}'s {ship_hit} has been hit!")
            if not any(ship_hit in row for row in self.board):
                print(f"{self.name}'s {ship_hit} has been sunk!")
                del self.ships[ship_hit.lower()]
            return True
        else:
            self.board[row][col] = 'O'
            self.print_board()
            print(f"{self.name}'s shot missed.")
            return False


class ComputerPlayer(Player):
    def place_ships(self):
        for ship, size in self.ships.items():
            while True:
                row, col = random.randint(0, 9), random.randint(0, 9)
                orientation = random.choice(['H', 'V'])

                if self.is_valid_placement(row, col, size, orientation):
                    self.place_ship(ship, row, col, size, orientation)
                    break

    def make_move(self, opponent):
        while True:
            row, col = random.randint(0, 9), random.randint(0, 9)

            if self.is_valid_move(row, col):
                self.moves.add((row, col))
                if opponent.receive_attack(row, col):
                    print("Hit!")
                else:
                    print("Miss!")
                break


def play_battleship():
    print("Welcome to Battleship!")
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name (or 'CPU' for computer opponent): ")

    player1 = Player(player1_name)
    if player2_name.upper() == 'CPU':
        player2 = ComputerPlayer("CPU")
    else:
        player2 = Player(player2_name)

    player1.place_ships()
    player2.place_ships()

    while any(player.ships for player in [player1, player2]):
        player1.print_board()
        player1.print_enemy_board()
        player1.make_move(player2)

        if not any(player.ships for player in [player1, player2]):
            break

        player2.print_board()
        player2.print_enemy_board()
        if player2_name.upper() == 'CPU':
            player2.make_move(player1)
        else:
            player2.make_move(player1)

    print("Game Over!")
    if not player1.ships:
        print(f"{player2.name} wins!")
    else:
        print(f"{player1.name} wins!")


if __name__ == "__main__":
    play_battleship()
