"""

https://leetcode.com/problems/excel-sheet-column-number/

Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

"""
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        n = 0
        for c in columnTitle:
            n = n * 26 + (ord(c) - ord('A') + 1)
        return n


sol = Solution()
print(sol.titleToNumber('AA'))