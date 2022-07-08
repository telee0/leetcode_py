"""

https://leetcode.com/problems/pascals-triangle-ii/submissions/

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        numRows = rowIndex + 1
        output = [[1]]
        for i in range(1, numRows):
            row_last = output[-1]
            output.append([1])
            row = output[-1]
            for j in range(1, len(row_last)):
                row.append(row_last[j - 1] + row_last[j])
            row.append(1)
        return output[rowIndex]


sol = Solution()
print(sol.getRow(3))
print(sol.getRow(10))