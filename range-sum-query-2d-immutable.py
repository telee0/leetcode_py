"""

https://leetcode.com/problems/range-sum-query-2d-immutable/


Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

"""


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0]) if self.m > 0 else 0
        self.matrix = []
        for i in range(self.m):
            row = matrix[i].copy()
            self.matrix.append(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                sum += self.matrix[i][j]

        return sum




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
