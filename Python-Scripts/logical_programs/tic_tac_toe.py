import random

def print_board(board):
    print("\n" + "\n---------\n".join([" | ".join(row) for row in board]) + "\n")

def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def get_empty_cells(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                empty_cells.append((row, col))
    return empty_cells

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "O"
    empty_cells = get_empty_cells(board)

    while empty_cells:
        print_board(board)
        if current_player == "O":
            print("Player 2's turn. Enter row and column (0-2):")
            row = int(input("Row: "))
            col = int(input("Column: "))
            if (row, col) in empty_cells:
                board[row][col] = current_player
                empty_cells = get_empty_cells(board)
                if check_win(board, current_player):
                    print_board(board)
                    print("Player 2 wins!")
                    break
                current_player = "X"
            else:
                print("Invalid input. Try again.")
        else:
            print("Player 1's turn (computer).")
            row, col = random.choice(empty_cells)
            board[row][col] = current_player
            empty_cells = get_empty_cells(board)
            if check_win(board, current_player):
                print_board(board)
                print("Player 1 wins!")
                break
            current_player = "O"

    if not check_win(board, "O") and not check_win(board, "X"):
        print_board(board)
        print("It's a draw!")

if __name__ == "__main__":
    main()