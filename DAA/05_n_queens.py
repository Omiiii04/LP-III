"""N-Queens backtracking solver with an optional fixed first queen."""
from __future__ import annotations

import argparse


def solve(n: int, first_column: int | None = None) -> list[list[int]]:
    if n < 1 or (first_column is not None and not 0 <= first_column < n):
        raise ValueError("invalid board size or first queen column")
    board = [[0] * n for _ in range(n)]
    columns, diagonals, reverse_diagonals = set(), set(), set()

    def place(row: int) -> bool:
        if row == n:
            return True
        candidates = [first_column] if row == 0 and first_column is not None else range(n)
        for column in candidates:
            if column in columns or row - column in diagonals or row + column in reverse_diagonals:
                continue
            board[row][column] = 1
            columns.add(column); diagonals.add(row - column); reverse_diagonals.add(row + column)
            if place(row + 1):
                return True
            board[row][column] = 0
            columns.remove(column); diagonals.remove(row - column); reverse_diagonals.remove(row + column)
        return False

    if not place(0):
        raise ValueError("no solution exists for the requested first queen")
    return board


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, nargs="?", default=4)
    parser.add_argument("--first-column", type=int, help="1-based column for the first queen")
    args = parser.parse_args()
    board = solve(args.n, None if args.first_column is None else args.first_column - 1)
    print("\n".join(" ".join(map(str, row)) for row in board))


if __name__ == "__main__":
    main()
