"""A simple two-player Tic-Tac-Toe game for the terminal."""


def display_board(board):
    """Display the current game board."""
    print()
    for row in range(3):
        start = row * 3
        print(f" {board[start]} | {board[start + 1]} | {board[start + 2]} ")
        if row < 2:
            print("---+---+---")
    print()


def check_winner(board, player):
    """Return True if the player has three marks in a row."""
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6),              # Diagonals
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def play_game():
    """Play one round of Tic-Tac-Toe."""
    board = [str(number) for number in range(1, 10)]
    current_player = "X"

    print("\nWelcome to Tic-Tac-Toe!")
    print("Choose a position by entering a number from 1 to 9.")
    print("Player X goes first.")

    while True:
        display_board(board)
        choice = input(f"Player {current_player}, choose a position (1-9): ")

        # Check that the input is a number.
        if not choice.isdigit():
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        position = int(choice)

        # Check that the position is on the board.
        if position < 1 or position > 9:
            print("Invalid position. Choose a number from 1 to 9.")
            continue

        index = position - 1

        # Check that the position has not already been used.
        if board[index] in ("X", "O"):
            print("That position is already taken. Try again.")
            continue

        board[index] = current_player

        # Check whether the current player has won.
        if check_winner(board, current_player):
            display_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break

        # Check whether the board is full.
        if all(cell in ("X", "O") for cell in board):
            display_board(board)
            print("It's a draw!")
            break

        # Switch to the other player.
        current_player = "O" if current_player == "X" else "X"


def main():
    """Run games until the players choose to stop."""
    while True:
        play_game()
        again = input("\nWould you like to play again? (y/n): ").strip().lower()

        if again != "y":
            print("Thanks for playing Tic-Tac-Toe!")
            break


if __name__ == "__main__":
    main()
