#!/usr/bin/python3
"""
A module that contains functions solving the N queens challange
"""
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # check upper right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, N, solutions):
    """Utilize backtracking to place queens on the board"""
    if row == N:
        solutions.append([list(row) for row in board])
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(board, row + 1, N, solutions)
            board[row][col] = 0


def print_solutions(solutions, N):
    """Print all the solutions"""
    for solution in solutions:
        formatted_solution = []
        for row in range(N):
            for col in range(N):
                if solution[row][col] == 1:
                    formatted_solution.append([row, col])
        print(formatted_solution)


def main():
    """Main function to handle input and output"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, N, solutions)
    print_solutions(solutions, N)


if __name__ == "__main__":
    main()
