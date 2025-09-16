"""
N-Queens Problem Solver

This module implements a solution to the classic N-Queens problem using backtracking.
The N-Queens problem asks: "How can N chess queens be placed on an N×N chessboard 
so that no two queens attack each other?"

Author: Generated solution
"""

def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col].
    
    A queen can attack horizontally, vertically, and diagonally. This function
    checks if placing a queen at the given position would conflict with any
    previously placed queens.
    
    Args:
        board (list[list[int]]): 2D list representing the chessboard where 1 indicates a queen
        row (int): Row index where we want to place the queen
        col (int): Column index where we want to place the queen  
        n (int): Size of the chessboard (n x n)
        
    Returns:
        bool: True if it's safe to place a queen at the given position, False otherwise
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nq_util(board, col, n):
    """
    Utility function to solve N-Queens problem using backtracking.
    
    This is a recursive function that tries to place queens column by column.
    For each column, it tries placing a queen in each row and recursively
    attempts to place queens in subsequent columns.
    
    Args:
        board (list[list[int]]): 2D list representing the chessboard
        col (int): Current column index where we're trying to place a queen
        n (int): Size of the chessboard (n x n)
        
    Returns:
        bool: True if a solution is found, False if no solution exists for current configuration
    """
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_nq_util(board, col + 1, n):
                return True
            board[i][col] = 0
    return False

def solve_nq(n):
    """
    Solve the N-Queens problem and print the solution.
    
    Creates an empty n×n chessboard and attempts to find a valid arrangement
    of n queens such that none attack each other. If a solution is found,
    it prints the board with 'Q' representing queens and '.' representing empty squares.
    
    Args:
        n (int): Size of the chessboard and number of queens to place
        
    Returns:
        None: Prints the solution to stdout or "No solution exists" message
    """
    board = [[0] * n for _ in range(n)]
    if not solve_nq_util(board, 0, n):
        print("No solution exists")
        return
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))

if __name__ == "__main__":
    n = 8  # You can change this value to solve for different sizes
    solve_nq(n)