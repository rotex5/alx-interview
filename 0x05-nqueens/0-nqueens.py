#!/usr/bin/python3
"""
N Queens Solver Program
"""
import sys


class NQueensSolver:
    def __init__(self, N):
        """
        Initialize the NQueensSolver object.

        Args:
            N (int): Number of queens and the size of the chessboard.
        """
        self.N = N
        self.board = [[0 for _ in range(N)] for _ in range(N)]
        self.solutions = []

    def solve_nqueens(self):
        """
        Solve the N queens problem and return all solutions.

        Returns:
            list: List of solutions, where each solution is represented
            as a list of row and column indices of the queens.
        """
        self.solve_util(0)
        return self.solutions

    def solve_util(self, col):
        """
        Recursive helper function to solve the N queens problem.

        Args:
            col (int): Current column being processed.

        Returns:
            None
        """
        if col == self.N:
            queens = []
            for row in range(self.N):
                for col in range(self.N):
                    if self.board[row][col] == 1:
                        queens.append([row, col])
            self.solutions.append(queens)
            return

        for row in range(self.N):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.solve_util(col + 1)
                self.board[row][col] = 0

    def is_safe(self, row, col):
        """
        Check if a queen can be placed at the given position without attacking
        any other queens.

        Args:
            row (int): Row index of the position to check.
            col (int): Column index of the position to check.

        Returns:
            bool: True if the position is safe, False otherwise.
        """
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        i, j = row, col
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        i, j = row, col
        while i < self.N and j >= 0:
            if self.board[i][j] == 1:
                return False
            i += 1
            j -= 1

        return True


def main():
    """
    Main function that handles command line arguments and runs the program.
    """
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

    solver = NQueensSolver(N)
    solutions = solver.solve_nqueens()
    for solution in solutions:
        print(solution)


if __name__ == '__main__':
    main()
