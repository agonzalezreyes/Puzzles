"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
    
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""

"""
Notes:
- Backtracking Algorithm problem
- DFS

Algorithm:
1. find empty space
2. attempt to place the digits 1-9 in that space
3. check if digit is valid in the current spot based on current board
4. if it is valid, recursively attempt to fill the board by repeating steps 1-3. if it is not valid, reset the square you filled and go to previous step.
5. once the board is full we have found a solution
"""
from typing import List

def find_empty_entry(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ".":
                return (i, j)
    return None

def solve(board: List[List[str]]):
    empty_sq = find_empty_entry(board)
    if empty_sq is None:
        return True
    else:
        r, c = empty_sq
    for i in range(1,10):
        if isValid(board, str(i), (r,c)):
            board[r][c] = str(i)
            if solve(board):
                return True
            board[r][c] = "."
    return False

def isValid(board: List[List[str]], num, position):
    y = position[0]
    x = position[1]
    # check row
    for i in range(len(board[0])):
        if board[y][i] == num and x != i:
            return False
    # check column
    for i in range(len(board)):
        if board[i][x] == num and y != i:
            return False
    #check subgrid
    grid_x = x // 3
    grid_y = y // 3
    for r in range(grid_y*3, grid_y*3 + 3):
        for c in range(grid_x*3, grid_x*3 + 3):
            if board[r][c] == num and (r, c) != position:
                return False
    return True

def solveSudoku(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    if board == None or len(board) == 0 or len(board[0]) == 0:
        return
    solve(board)
    return board

board = [["5","3",".",".","7",".",".",".","."], ["6",".",".","1","9","5",".",".","."], [".","9","8",".",".",".",".","6","."], ["8",".",".",".","6",".",".",".","3"], ["4",".",".","8",".","3",".",".","1"], ["7",".",".",".","2",".",".",".","6"], [".","6",".",".",".",".","2","8","."], [".",".",".","4","1","9",".",".","5"], [".",".",".",".","8",".",".","7","9"]]
output = [["5","3","4","6","7","8","9","1","2"], ["6","7","2","1","9","5","3","4","8"], ["1","9","8","3","4","2","5","6","7"], ["8","5","9","7","6","1","4","2","3"], ["4","2","6","8","5","3","7","9","1"], ["7","1","3","9","2","4","8","5","6"], ["9","6","1","5","3","7","2","8","4"], ["2","8","7","4","1","9","6","3","5"], ["3","4","5","2","8","6","1","7","9"]]

from util import Testing as t

tests = t.Testing("Sudoku Solver")

tests.addTest(output, solveSudoku, board)

tests.run()

#print(board)
#solveSudoku(board)
#print(board)
#print(board == output)
#print(output)
