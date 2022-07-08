"""

https://leetcode.com/problems/sudoku-solver/

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

https://leetcode.com/problems/sudoku-solver/discuss/1761536/fastest-python-solution

"""

from collections import defaultdict
class Solution:

def solve(self, board, position, empty, rows, cols, boxes):
    if position == len(empty):
        return True
    r, c = empty[position]
    validValues = boxes[(r//3, c//3)].intersection(rows[r].intersection(cols[c]))
    for a_cell in validValues:
        board[r][c] = a_cell
        boxes[(r//3, c//3)].remove(a_cell)
        rows[r].remove(a_cell)
        cols[c].remove(a_cell)
        foundSolution = self.solve(board,position+1, empty, rows, cols, boxes)
        if foundSolution:
            return True
        else:
            boxes[(r//3, c//3)].add(a_cell)
            rows[r].add(a_cell)
            cols[c].add(a_cell)
    return False

def solveSudoku(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    rows = [set() for i in range(9)]
    cols = [set() for i in range(9)]
    boxes = defaultdict(set)
    empty = []
    for i in range(9):
        for j in range(9):
            cell = str(j+1)
            rows[i].add(cell)
            cols[i].add(cell)
    for i in range(3):
        for j in range(3):
            for k in range(1,10):
                boxes[(i,j)].add(str(k))
    for i in range(9):
        for j in range(9):
            cell = board[i][j]
            if cell != '.':
                rows[i].remove(cell)
                cols[j].remove(cell)
                boxes[(i//3, j//3)].remove(cell)
            else:
                empty.append((i,j))
    print(empty)
    self.solve(board, 0, empty, rows, cols, boxes)