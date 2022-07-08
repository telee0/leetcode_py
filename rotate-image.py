"""

https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                x = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = x
        for i in range(n):
            for j in range(n // 2):
                x = matrix[i][j]
                matrix[i][j] = matrix[i][n - j - 1]
                matrix[i][n - j - 1] = x
        print(matrix)


sol = Solution()
print(sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
