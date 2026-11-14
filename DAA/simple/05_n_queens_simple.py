"""Simple backtracking solution for the N-Queens problem."""

n = int(input("Enter board size: "))
board = [["."] * n for _ in range(n)]


def safe(row, column):
    for previous_row in range(row):
        previous_column = board[previous_row].index("Q") if "Q" in board[previous_row] else -1
        if previous_column == column or abs(previous_row - row) == abs(previous_column - column):
            return False
    return True


def place(row):
    if row == n:
        return True
    for column in range(n):
        if safe(row, column):
            board[row][column] = "Q"
            if place(row + 1):
                return True
            board[row][column] = "."
    return False


if place(0):
    for row in board:
        print(" ".join(row))
else:
    print("No solution exists.")
