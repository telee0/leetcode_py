"""

https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.

"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        output = []

        m, n = len(matrix), len(matrix[0])
        i_0, i_m, j_0, j_n = 1, m-1, 0, n-1
        i, j, count = 0, 0, 0
        di, dj = 0, 1

        while count < m * n:
            output.append(matrix[i][j])
            count += 1
            if dj > 0 and j == j_n:
                j_n -= 1
                di, dj = 1, 0
            elif di > 0 and i == i_m:
                i_m -= 1
                di, dj = 0, -1
            elif dj < 0 and j == j_0:
                j_0 += 1
                di, dj = -1, 0
            elif di < 0 and i == i_0:
                i_0 += 1
                di, dj = 0, 1
            i += di
            j += dj

        return output


sol = Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))