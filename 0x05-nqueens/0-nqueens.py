#!/usr/bin/env python3
"""
N Queens Solver Program
"""
import sys


def is_safe(board, row, col, N):
    """Check if a queen can be placed at the given position
    without attacking any other queens on the board"""

    # Check row on the left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_nqueens(N):
    """Solve the N queens problem using backtracking"""

    def backtrack(board, col, N, solutions):
        """Base case: all queens are placed"""
        if col == N:
            # Append the solution to the list of solutions
            solution = []
            for row in range(N):
                for col in range(N):
                    if board[row][col] == 'Q':
                        solution.append([row, col])
            solutions.append(solution)
            return

        for row in range(N):
            if is_safe(board, row, col, N):
                # Place the queen at the current position
                board[row][col] = 'Q'

                # Recursively place the rest of the queens
                backtrack(board, col + 1, N, solutions)

                # Remove the queen from the current position
                board[row][col] = '.'

    # Create an empty NxN chessboard
    board = [['.' for _ in range(N)] for _ in range(N)]

    # List to store solutions
    solutions = []

    # Start backtracking from the first column
    backtrack(board, 0, N, solutions)

    return solutions


# Check the number of command-line arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Get the value of N from the command-line argument
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if N is at least 4
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Solve the N queens problem
solutions = solve_nqueens(N)

# Print the solutions
for solution in solutions:
    print([[pos[0], pos[1]] for pos in solution])
