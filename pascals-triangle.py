"""

https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = [[1]]
        for i in range(1, numRows):
            row_last = output[-1]
            output.append([1])
            row = output[-1]
            for j in range(1, len(row_last)):
                row.append(row_last[j - 1] + row_last[j])
            row.append(1)
        return output


sol = Solution()
print(sol.generate(5))
print(sol.generate(10))